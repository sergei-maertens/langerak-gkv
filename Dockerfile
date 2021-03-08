# Stage 1 - Compile needed python dependencies
FROM python:3.6-slim-buster AS build

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./requirements /app/requirements
RUN pip install pip setuptools -U \
    && pip install -r requirements/production.txt

# Stage 2 - build frontend
FROM mhart/alpine-node:10 AS frontend-build

WORKDIR /app

COPY ./*.json /app/
RUN npm ci

COPY ./build/ /app/build/
COPY ./gulpfile.js ./webpack.config.js ./.babelrc /app/

COPY src/langerak_gkv/js/ /app/src/langerak_gkv/js/
COPY src/langerak_gkv/sass/ /app/src/langerak_gkv/sass/
RUN npm run build --production

# Stage 3 - Build docker image suitable for execution and deployment
FROM python:3.6-slim-buster AS production

# Stage 3.1 - Set up the needed production dependencies
# install all the dependencies for GeoDjango
RUN apt-get update && apt-get install -y --no-install-recommends \
        procps \
        vim \
        mime-support \
        postgresql-client \
        gettext \
    && rm -rf /var/lib/apt/lists/*

COPY --from=build /usr/local/lib/python3.6 /usr/local/lib/python3.6
COPY --from=build /usr/local/bin/uwsgi /usr/local/bin/uwsgi
COPY --from=frontend-build /app/node_modules/normalize.css /app/node_modules/normalize.css

# Stage 3.2 - Copy source code
WORKDIR /app
COPY ./bin/uwsgi.sh /uwsgi.sh
RUN mkdir /app/log

COPY ./src /app/src

COPY --from=frontend-build /app/src/langerak_gkv/static/css /app/src/langerak_gkv/static/css
COPY --from=frontend-build /app/src/langerak_gkv/static/js /app/src/langerak_gkv/static/js

RUN groupadd -g 1000 app-user \
    && useradd -M -u 1000 -g 1000 app-user \
    && chown -R app-user /app

# drop privileges
USER app-user

ENV DJANGO_SETTINGS_MODULE=langerak_gkv.conf.production

ARG SECRET_KEY=dummy
ARG DOCKER_BUILD=1

# Run collectstatic, so the result is already included in the image
RUN python src/manage.py collectstatic --noinput \
    && python src/manage.py compilemessages \
    && chmod ugo+rwx -R /app/log

EXPOSE 8000
CMD ["/uwsgi.sh"]

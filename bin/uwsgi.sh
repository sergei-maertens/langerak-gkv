#!/bin/bash

set -e

# Wait for the database (container)
# See: https://docs.docker.com/compose/startup-order/
PGHOST=${DB_HOST:-db}
PGPORT=${DB_PORT:-5432}

until pg_isready ; do
  >&2 echo "Waiting for database connection..."
  sleep 3
done

>&2 echo "Database is up."

# Apply database migrations
>&2 echo "Apply database migrations"
python src/manage.py migrate

>&2 echo "Ensure apphooks are installed"
python src/manage.py ensure_apphooks

>&2 echo "Deal with possible CMS upgrades"
python src/manage.py cms fix-tree

# Start server
>&2 echo "Starting server"
uwsgi \
    --http :${UWSGI_PORT:-8000} \
    --module wsgi \
    --static-map /static=/app/static \
    --static-map /media=/app/media  \
    --chdir src \
    --processes 2 \
    --threads 2 \
    --buffer-size=32768
    # processes & threads are needed for concurrency without nginx sitting inbetween

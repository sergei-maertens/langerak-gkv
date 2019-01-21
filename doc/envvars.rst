===============================
Supported environment variables
===============================

**Required:**

* ``SECRET_KEY``: the Django secret key
* ``ALLOWED_HOSTS``: comma-separated list of domain names
* ``DB_NAME``: name of the database to connect to
* ``DB_USER``: username of the database user to connect as
* ``DB_PASSWORD``: password of the database user to connect as
* ``GOOGLE_API_KEY``: Google (maps?) API key
* ``DEFAULT_FROM_EMAIL``: the default sender of e-mails

**Optional:**

* ``SITE_ID``: pk of the site to run with
* ``DB_HOST``: host of the database to connect to. Defaults to ``localhost``.
* ``DB_PORT``: port-number of the datbase to connect to. Defaults to 5432.
* ``SENTRY_DSN``: the DSN for the Sentry project

Kerkwebsite
===========

CMS project/codebase for "Gereformeerde Kerk Langerak en omstreken".

Getting started
---------------

**Requirements**

* Python 3.11
* PostgreSQL
* ElasticSearch 7.x
* Redis 6

**Docker**

You can bring up all the services with ``docker-compose up --build``.

**Local environment**

.. code-block:: bash

    mkvirtualenv kerkwebsite -p python3.11
    pip install -r requirements/dev.txt

    # initialize database
    createuser langerak_gkv
    createdb langerak_gkv -O langerak_gkv

    # initialize frontend tooling
    nvm use
    npm i
    npm run build

    # migrate DB & kick off dev server
    src/manage.py migrate
    src/manage.py runserver

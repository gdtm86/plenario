[![Join the chat at https://gitter.im/UrbanCCD-UChicago/plenario](https://badges.gitter.im/UrbanCCD-UChicago/plenario.svg)](https://gitter.im/UrbanCCD-UChicago/plenario?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Code Climate](https://codeclimate.com/github/UrbanCCD-UChicago/plenario/badges/gpa.svg)](https://codeclimate.com/github/UrbanCCD-UChicago/plenario)
[![Build Status](https://travis-ci.org/UrbanCCD-UChicago/plenario.svg?branch=master)](https://travis-ci.org/UrbanCCD-UChicago/plenario)

# Plenar.io

API for geospatial and time aggregation across multiple open datasets.

This project is funded by the [NSF Computer and Information Science and Engineering (CISE) Directorate](http://www.nsf.gov/dir/index.jsp?org=CISE)
through a grant to the [Urban Center for Computation and Data](https://urbanccd.org/) (UrbanCCD)
at the [Computation Institute](http://ci.uchicago.edu)
of the [University of Chicago](http://uchicago.edu) and [Argonne National Laboratory](http://www.anl.gov).
It is maintained by UrbanCCD and was prototyped by [DataMade](http://datamade.us).

## Running locally

* Get the Plenario source:

``` bash
git clone git@github.com:UrbanCCD-UChicago/plenario.git
```

Install support libraries for Python:

``` bash
cd plenario
pip install -r requirements.txt
```

Create a PostgreSQL database for Plenario. (If you aren't already running
[PostgreSQL](http://www.postgresql.org/), we recommend installing version 9.3 or
later.) The following command creates the default database, `plenario_test`.
This corresponds with the `DB_NAME` setting in your `plenario/settings.py` file
and can be modified.

```
createdb plenario_test
```

Make sure your local database has the [PostGIS](http://postgis.net/) extension:

```
psql plenario_test
plenario_test=# CREATE EXTENSION postgis;
```

You'll need the ogr2ogr utility; it's part of the gdal package (we use it toimport and export shape datasets)

OSX
```
brew install gdal --with-postgresql
```

Ubuntu/Debian

```
sudo apt-get install gdal-bin
```

Create your own `settings.py` files:
=======


```
cp plenario/settings.py.example plenario/settings.py
cp plenario/celery_settings.py.example plenario/celery_settings.py
```

You will want to change, at the minimum, the following `settings.py` fields:

* `DATABASE_CONN`: edit this field to reflect your PostgreSQL
  username, server hostname, port, and database name.

* `DEFAULT_USER`: change the username, email and password on the administrator account you will use on Plenario locally.


Additionally, create your own `celery_settings.py` file:

```
cp plenario/celery_settings.py.example plenario/celery_settings.py
```

You probably do not need to change any values in `celery_settings.py`,
unless you are running redis remotely (see `BROKER_URL`).

Before running the server, [Redis](http://redis.io/) and
[Celery](http://www.celeryproject.org/) also need to be running.

* To start Redis locally (in the background):
```
redis-server &
```

* To start Celery locally (in the background):
```
celery -A plenario.celery_app worker --loglevel=info &
```

Initialize the plenario database by running `python init_db.py`.

Finally, run the server:

```
python runserver.py
```

Once the server is running, navigate to http://localhost:5001/ . From
the homepage, click 'Login' to log in with the username and password
from `settings.py`. Once logged in, go to 'Add a dataset' under the
'Admin' menu to add your own datasets.

# Open source tools:

### Application Dependencies

* [PostgreSQL](http://www.postgresql.org/) - database version 9.3 or greater
* [PostGIS](http://postgis.net/) - spatial database for PostgreSQL
* [Flask](http://flask.pocoo.org/) - a microframework for Python web applications
* [SQL Alchemy](http://www.sqlalchemy.org/) - Python SQL toolkit and Object Relational Mapper
* [psycopg2](http://initd.org/psycopg/) - PostgreSQL adapter for the Python
* [GeoAlchemy 2](http://geoalchemy-2.readthedocs.org/en/0.2.4/) - provides extensions to SQLAlchemy for working with spatial databases
* [GDAL](http://www.gdal.org/) - geospatial data mungeing
* [Celery](http://www.celeryproject.org/) - asynchronous task queue
* [Redis](http://redis.io/) - key-value cache
* [Gunicorn](http://gunicorn.org/) - WSGI server

### Production Support

Many thanks for the following hosted services that have given us free academic/open source accounts.

* [Sentry](https://getsentry.com/welcome/) - exception and task monitoring
* [Code Climate](https://codeclimate.com/) - static analysis


## Team

* Charlie Catlett
* Brett Goldstein
* Will Engler

## Join Our Community

Join us on Gitter for technical help with the Plenario API,

[![Join the chat at https://gitter.im/UrbanCCD-UChicago/plenario](https://badges.gitter.im/UrbanCCD-UChicago/plenario.svg)](https://gitter.im/UrbanCCD-UChicago/plenario?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

## Testing

The plenario/tests folder includes a suite of API tests split across the /points and /shapes directories. To run the tests using with nose, use the command 'nosetests tests' from the /plenario directory

## Errors / Bugs

If something is not behaving intuitively, it is a bug, and should be reported.
Report it here: https://github.com/UrbanCCD-UChicago/plenario/issues

## Note on Patches/Pull Requests

Pull requests make us very happy.
If you're interested in contributing, come chat with us on Gitter
to discuss what you'd like to do.
Then follow [common best practices](http://www.contribution-guide.org/)
to send us a PR.

## Copyright

Copyright (c) 2014 University of Chicago and DataMade.
Released under the [MIT License](https://github.com/UrbanCCD-UChicago/plenario/blob/master/LICENSE).

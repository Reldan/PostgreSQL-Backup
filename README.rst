PostgreSQL continues backup
==============================================

Project structure
----------------------------------------------
::

    archive - directory for WAL
    src  - code directory
    src/run.py - runner
    src/settings.py - settings for user, password, host and database name

Setup postgresql.conf
-----------------------------------------------
::

    wal_level = hot_standby
    archive_mode = on
    archive_command = 'cp -i %p /Developer/myprogs/python/tutorials/PostgreSQL-Backup/archive/%f </dev/null'

Import test database
-----------------------------------------------
::

    psql mydb < dellstore2-normal-1.0.sql

Restart postgresql
-----------------------------------------------
::

    pg_ctl -D /usr/local/var/postgres/ -l logfile restart

Install psycopg2
-----------------------------------------------
::

    pip install psycopg2

Run src/run.py
-----------------------------------------------
::

    python ./src/run.py
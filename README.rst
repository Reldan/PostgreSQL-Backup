PostgreSQL continues backup
===================

archive - directory for WAL
src  - code directory
src/run.py - runner
src/settings.py - settings for user, password, host and database name

====================
1) Setup postgresql.conf

'
wal_level = hot_standby
archive_mode = on
archive_command = 'cp -i %p /Developer/myprogs/python/tutorials/test-psycopg2/archive/%f </dev/null'
'

2) Restart postgresql

pg_ctl -D /usr/local/var/postgres/ -l logfile restart
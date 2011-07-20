#!/bin/bash
#
#
PGDATA=/usr/local/var/postgres
BACKUPNAME=mybackup
ARCHIVE=/Developer/myprogs/python/tutorials/PostgreSQL-Backup
DBNAME=mydb

rm ./archive/BACKUPNAME
rm ./archive/00*
psql -s mydb -c "SELECT pg_start_backup('mybackup')"
tar -cv --exclude {$PGDATA}/pg_xlog -f ARCHIVE/$BACKUPNAME $PGDATA
python ./src/run.py
PID=`head -1 /usr/local/var/postgres/postmaster.pid`

kill -9 $PID
sleep 9
pg_ctl -D $PGDATA -l logfile start

#restore
#mv ../standalone/archive/ archive/
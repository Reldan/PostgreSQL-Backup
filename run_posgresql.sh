#!/bin/bash
#
#
PGDATA=/usr/local/var/postgres
pg_ctl -D $PGDATA -l logfile status
pg_ctl -D $PGDATA -l logfile start
tail /usr/local/var/postgres/logfile -1
pg_ctl -D $PGDATA -l logfile status
FROM postgres

COPY ./backup.sql ./var/lib/backup.sql

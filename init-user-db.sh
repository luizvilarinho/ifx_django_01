#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER sccp_db;
    CREATE DATABASE dbSCCP;
    GRANT ALL PRIVILEGES ON DATABASE dbSCCP TO sccp_db;
EOSQL
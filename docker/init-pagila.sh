#!/bin/bash
set -e

# 1. Crear base de datos pagila
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
  CREATE DATABASE pagila;
EOSQL

# 2. Cargar primero el schema
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" -d pagila -f /docker-entrypoint-initdb.d/pagila-schema.sql

# 3. Luego los datos
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" -d pagila -f /docker-entrypoint-initdb.d/pagila-data.sql

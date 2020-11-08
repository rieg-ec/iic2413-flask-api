#!/bin/bash
set -e

echo ">>>>>>> trying to create database and users"
if [ -n "${MONGO_INITDB_ROOT_USERNAME:-}" ] && [ -n "${MONGO_INITDB_ROOT_PASSWORD:-}" ] && [ -n "${MONGO_USER:-}" ] && [ -n "${MONGO_PASSWORD:-}" ]; then
mongo -u $MONGO_INITDB_ROOT_USERNAME -p $MONGO_INITDB_ROOT_PASSWORD<<EOF
use admin;
db.createUser({
  user:  '$MONGO_USER',
  pwd: '$MONGO_PASSWORD',
  roles: [{
    role: 'readWrite',
    db: '$MONGO_DB'
  }]
});
EOF
mongoimport -c usuarios -d $MONGO_DB --mode upsert --type json --jsonArray --file data/usuarios.json
mongoimport -c mensajes -d $MONGO_DB --mode upsert --type json --jsonArray --file data/mensajes.json
else
    echo "env variables not provided"
    exit 403
fi

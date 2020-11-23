#!/bin/bash
set -e

echo ">>>>>>> trying to create database and users"
if [ -n "${MONGO_INITDB_ROOT_USERNAME:-}" ] && [ -n "${MONGO_INITDB_ROOT_PASSWORD:-}" ]\
 && [ -n "${MONGO_USER:-}" ] && [ -n "${MONGO_PASSWORD:-}" ] && [ -n "${MONGO_URI:-}" ]\
 && [ -n "${MONGO_DB:-}" ]; then
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
mongoimport -c users -d $MONGO_DB --mode upsert --type json --jsonArray --file data/files/usuarios.json
mongoimport -c messages -d $MONGO_DB --mode upsert --type json --jsonArray --file data/files/mensajes.json
mongo -u $MONGO_USER -p $MONGO_PASSWORD<<EOF
use grupo42;
db.messages.createIndex({ message: "text" });
EOF
else
    echo "env variables not provided"
    exit 403
fi

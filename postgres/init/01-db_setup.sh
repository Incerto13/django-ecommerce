#!/bin/sh

export PGUSER=$POSTGRES_USER
export PGDATABASE=$POSTGRES_DB
export PGPASSWORD=$POSTGRES_PASSWORD

psql -U postgres -c "CREATE USER $PGUSER PASSWORD '$PGPASSWORD'"
psql -U postgres -c "CREATE DATABASE $PGDATABASE OWNER $PGUSER"
psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE $PGDATABASE TO $PGUSER"


##### None of this BELOW should be here, just for reference, datadump isn't even in this directory
# and this containder doesn't have python

# import initial data to database
# echo "Importing initial dbase data"
# docker-compose exec web python3 manage.py loaddata datadump.json

# Apply data migrations
# echo "Apply data migrations"
# docker-compose exec web python3 manage.py migrate

# Collect static files in /static/ directory
# docker-compose exec web python3 manage.py collectstatic --noinput && chmod 775 -R /static
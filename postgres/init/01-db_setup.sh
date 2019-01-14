#!/bin/sh

psql -U postgres -c "CREATE USER django PASSWORD 'pwordyaezz'"
psql -U postgres -c "CREATE DATABASE ecommerce OWNER django"
psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE ecommerce TO django"

##### None of this below should be here, just for reference

# import initial data to database
# echo "Importing initial dbase data"
# docker-compose exec web python3 manage.py loaddata datadump.json

# Apply data migrations
# echo "Apply data migrations"
# docker-compose exec web python3 manage.py migrate

# Collect static files in /static/ directory
# docker-compose exec web python3 manage.py collectstatic --noinput && chmod 775 -R /static

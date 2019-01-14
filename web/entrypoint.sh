#!/bin/sh

docker-compose exec web python3 manage.py migrate --run-syncdb --noinput
docker-compose exec web python3 manage.py loaddata datadump.json
docker-compose exec web python3 manage.py collectstatic --noinput && chmod 775 -R /static

# Run this script from test_site root after pulling from git
# You might have to change this file's permissions, e.g.:
# $> chmod 777 build.sh

# Get Python and dependencies
yes | sudo apt-get update
yes | sudo apt-get install python3.6
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 10

yes | sudo apt install python3-pip
pip3 install Flask

yes | sudo apt-get install postgresql
yes | sudo apt-get install postgresql-server-dev-10
pip3 install psycopg2

# Build database
echo "starting postgres"
sudo service postgresql start
echo "creating db user"
sudo -u postgres psql -c "ALTER ROLE postgres WITH PASSWORD 'postgres';"
echo "creating database"
sudo -u postgres psql -c "CREATE DATABASE musicstore;"
echo "running db scripts"
sudo -u postgres psql -d musicstore -a -f ./seed_data/create.sql
sudo -u postgres psql -d musicstore -a -f ./seed_data/helper_functions.sql
sudo -u postgres psql -d musicstore -a -f ./seed_data/make_views.sql
sudo -u postgres psql -d musicstore -a -f ./seed_data/initial_seeds.sql
sudo -u postgres psql -d musicstore -a -f ./seed_data/sales.sql

# Run api.py if in dev environment
# Run prod.py if in prod
sudo python api.py
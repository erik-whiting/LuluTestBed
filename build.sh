cd ~

# Get Python and dependencies
sudo apt-get update
sudo apt-get install python3.6
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 10
sudo apt install python3-pip
pip3 install Flask

sudo apt-get install postgresql
sudo apt-get install postgresql-server-dev-10
pip3 install psycopg2 # Must install postgres first

# Clone project
git clone https://github.com/erik-whiting/test_site.git

cd test_site

# Build database
sudo service postgresql start
psql -U postgres -h 127.0.0.1 -f ./seed_data/create.sql
psql -U postgres -h 127.0.0.1 -f ./seed_data/helper_functions.sql
psql -U postgres -h 127.0.0.1 -f ./seed_data/make_views.sql
psql -U postgres -h 127.0.0.1 -f ./seed_data/initial_seeds.sql
psql -U postgres -h 127.0.0.1 -f ./seed_data/sales.sql

python api.py
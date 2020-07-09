cd ~

# Get Python and dependencies
sudo apt-get update
sudo apt-get install python3.6
pip install Flask
pip install psycopg2

# Install database
sudo apt-get install postgresql

# Clone project
git clone https://github.com/erik-whiting/test_site.git

# Build project
cd test_site
sudo service postgresql start
psql -U postgres -h 127.0.0.1 -f ./seed_data/create.sql
psql -U postgres -h 127.0.0.1 -f ./seed_data/helper_functions.sql
psql -U postgres -h 127.0.0.1 -f ./seed_data/make_views.sql
psql -U postgres -h 127.0.0.1 -f ./seed_data/initial_seeds.sql
psql -U postgres -h 127.0.0.1 -f ./seed_data/sales.sql

python api.py
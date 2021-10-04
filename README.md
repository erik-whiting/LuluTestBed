# LuluTestBed

LuluTestBed is a simple web application built with Python and Flask. It simulates a
record store inventory and online shopping application. The application is meant to
provide an environment for teams to evaluate testing frameworks, tools, and techniques
against a realistic, but inconsequential application. It also aims to provide all
these things to individual users who are trying to learn how to use these tools.

The application aims to provide the following features:
* Wide variety of web components to evaluate browser automation tools.
* Different groups of users and a variety of use-cases to evaluate performance testing tools
* REST endpoints to evaluate integration testing tools
* Multiple UIs written in different JS frameworks

As of writing this, LuluTestBed is in its early stages of development, and many of
these features do no yet exist. This repository is open for all to use, modify, and
distribute. Contributors are encouraged and welcome.

# Set up

The web application is built with Python, Flask, and Postgres. At this time,
Postgres is a hard requirement due to Python packaging requirements (and really 
to help us keep things simple). We wish to add the ability to allow users to
use whatever database system they want.

## Docker
To run using docker-compose ```docker-compose up -d```.  
.env file contains host to docker container. Without docker-compose 
testing set ```localhost```.

## Linux

In this repository's root, you will find a file called `build.sh`. Execute
this script to build the web application in a Linux environment. Additionally,
at the bottom of this script, you will find commented-out commands to start
the application. Uncommenting these will run LuluTestBed once the build has
completed. This is helpful for remote environments like clouds and CI servers
where each run typically requires a fresh installation.

## Windows

We do not currently have a PowerSheel script to automate Windows setup, but
the application can be set up quite easily (and a PS script contribution
would be wildly appreciated).

First, install Python3; we reommend 3.8 but teh application was originally
built in Python 3.6 and should work with that version and any later. Do
be advised though, Python 3.6 end-of-life is coming very soon.

You can find the latest Python release for Windows [here](https://www.python.org/downloads/windows/).

Next, you need to install PostgreSQL, a relational database management system
(RDBMS). You can find Windows specific installation guidance [here](https://www.postgresql.org/download/windows/).

The next step is to install Python dependencies. This repository
comes with a `requirements.txt` file, so this part is pretty easy. We **strongly**
suggest using Python virtual environments for this. The general steps
for this are as follows:

From a command line, make sure you're in the project root and run:

`python -m venv .env`

You can name your environment whatever you want, I'm .env as an example.
However, this repository's `.gitignore` file is already configured to ignore
any folder named `.env`, so if you stick with that name, you can be sure
the contents are local only (as it should be).

To activate the environment, run

`.env\Scripts\activate.bat`
or possibly
`.env/bin/activate`

That will activate your virtual environment and you should see `(.env)`
in front of your command prompt.

Now, install the requirements. If you've opted out of using virtualenv,
you still need to do this part

`pip install -r requirements.txt`

Wit this part done, you've got all the dependencies set up and it's time
to build and run the application. First thing's first, you need build the
database. When you installed Postgres, it should've come with an application
called pgAdmin. Find this application on your computer and run it, it'll
open in a browser.

If you're prompted for a user name and password, it's most likely "postgres"
for both. Once you've logged in, we need to create the database. Use the UI
to create a database called `musicstore`.

Once you've done this, we need to *seed* the databse (put data in it). The
first step is to open the SQL terminal and copy and paste the contents
of `seed_data/create.sql` into it, and run the script. Once that's done,
repeat the same process for the following scripts in this order:
`seed_data/helper_functions.sql`
`seed_data/make_views.sql`
`seed_data/initial_seeds.sql`
`seed_data/sales.sql`

We're almost done! With all that out of the way, it's now time to
run the application. From a terminal (cmd, PowerShell, etc) get to
this project's root and run:
`python api.py`
And that's it! Your application will most likely be running on
port 5000, [click here](localhost:5000) to see it locally. Let us
know if we missed any steps or if you've run into any problems by
raising an issue [here](https://github.com/erik-whiting/LuluTestBed/issues/new/choose). Thanks!
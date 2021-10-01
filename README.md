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

## Linux

In this repository's root, you will find a file called `build.sh`. Execute
this script to build the web application in a Linux environment. Additionally,
at the bottom of this script, you will find commented-out commands to start
the application. Uncommenting these will run LuluTestBed once the build has
completed. This is helpful for remote environments like clouds and CI servers
where each run typically requires a fresh installation.

## Windows

TODO: Create PowerShell script to build and launc application in Windows
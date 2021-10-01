# Contribution Guide

Welcome to LuluTestBed! We're really excited that you're interested in contributing.
The Lulu family of software quality tools is built on open source contributors and
we're always thankful for new talent coming our way.

# Project Philosophy and Goals

LuluTestBed, or LTB, is basically a playground web application. Specifically, it's
built to allow people to practice test automation skills or evaluate test automation
tools. However, there are no rules saying that it can't be used for other things!
Some other reasons someone might want to run LTB:
* Learn about and practice web scraping
* Learn about web development
* Experiment with different JavaScript frameworks
* Practice web app security skills

LTB is freely distributed and users are allowed to do whatever they want with it.

## Variety and Customizability

On top of providing an as-realistic-as-possible web application, LuluTestBed
strives to provide variety and customizability so users can choose from many
different configurations.

### Variety

One goal of LTB is to have multiple front ends built in a variety of JavaScript
frameworks. This allows users to explore the features and nuances of the many
frameworks they will encounter in the "real world."

Other features showcasing our dedication to **variety** haven't yet revealed
themselves, but as a potential contributor, you now know what we're *going for*
when we say "variety," you are empowered to make those kinds of decisions.

If you have an idea for a feature or something similar , please don't hesitate
to [report it as an issue](https://github.com/erik-whiting/LuluTestBed/issues/new/choose).

### Customizability

Another goal of LTB is to let users customize the web application. At this time,
we only support building the application with Postgres, but adding the ability to
run this web application with a MySQL, SQL Server, or even Mongo DB backend is
an example of what we mean by customizable. We are desperately seeking assistance
in this area!

Another area that needs customizability work is in web server software. Currently,
there is only a Linux build script provided, and the application only runs the
built-in flask web server. We'd like to add customizability for both operating systems
and server software.

# Contributing

We do not require you to discuss features or bug fixes prior to making a pull request
for LTB. At this time, all pull-requests, no matter how minor, frivolous, or ambitious
will be considered.

That said, if you'd like to discuss a feature or want to ask some general areas where
help is most appreciated, drop Erik an email: erik [at] erikwhiting [dot] com.

## Getting Started

If you would like to contribute to development, please pull the latest version of
`main`, create a local branch with a descriptive name, write your code, and push
the branch to the repository. After this, create a pull request for your feature
branch to the `main` branch.

### An example workflow

After you've followed setup steps in the README, think of a meaningful
name for the branch you're about to make and run these commands:

`git checkout -b my-cool-branch-name`

Write your code and try to make meaningful commits. Here's an example:

```cmd
# Write some code
$> git commit -am "Add new class to a module"
# Make some more changes
$> git commit -am "Add test for new class"
 ```

Once you've committed everything, run:

`git push origin my-cool-branch-name`

Then, head over to the [repository on Github](https://github.com/erik-whiting/LuluTestBed)
and create your pull request against the main branch. That's it!

Erik (or someone) will look over the PR and make comments or accept it outright.
Either way, you will get notified based on your GitHub notification settings, so
keep an eye on your email (or whatever you use).

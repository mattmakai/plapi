# Programming Languages API (PLAPI)
Plapi is a web API for programming languages. There are endpoints for
common paradigms, programming languages, libraries and tutorials.

This repository contains the source code for the web API. You don't
need anything from here to get started with the API, just check out
the next section.


## Quickstart
Let's pull up some basic information about the Python programming 
language using the programming-language endpoint (see the next section
for a list of all endpoints). 

Try a GET request on the following URL:

    GET http://api.plapi.io/programming-language/python

You'll receive back JSON corresponding to the Python programming language.


## Endpoints
Currently there are 3 endpoints:

1. Language paradigms
1. Programming languages
1. Libraries


### Paradigms

    /paradigms/


### Programming Languages

    /programming-languages/


### Libraries

    /programming-language/<language-slug>/libraries


## Adding new data
Issue a POST request to an endpoint with the required data. There's a
quick manual approval process, to make sure the data is correct and
has all of the proper fields. After the data is approved it'll be live
for all Plapi requests.


## Editing existing data
TBD.


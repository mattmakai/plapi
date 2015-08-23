# Programming Languages API (PLAPI)
Plapi is a web API for programming languages. There are endpoints for
common paradigms, programming languages, libraries and tutorials.

This repository contains the source code for the web API. You don't
need anything from here to get started with the API, just check out
the next section.


## Examples
### Languages, Ecosystems, Concepts and Implementation
Return a list of all imperative paradigm programming languages that are 
dynamically-typed.

    https://api.plapi.io/paradigms/imperative/?typing=dynamic


What concepts should I know about in Ada?


    https://api.plapi.io/concepts/ada


Show me all the task queue implementations written in Go, Python or Java.

    
    https://api.plapi.io/implementations/task-queues/?language=go&language2=python&language3=java


List all the programming languages that first appeared starting in 2001.

    https://api.plapi.io/programming-languages/?year-gte=2001


How many major and minor versions (x.x) of Go have been released?

    TBD


What languages were influenced by COBOL?

    TBD


What license is the Python programming language released under?

    https://api.plapi.io/programming-languages/python


### Learning
Give me a random Python with Django tutorial that shows how to implement 
WebSockets.

    GET https://api.plapi.io/tutorials/python/django/?tags=websockets&id=-1


Gimme another random tutorial on the same topic.

    GET https://api.plapi.io/tutorials/python/django/?tags=websockets&id=-1


Return all Ruby books published or updated since January 2014.

    GET https://api.plapi.io/books/ruby/?last_updated=01-01-2014


List 50 language-agnostic relational database articles and tutorials.

    GET https://api.plapi.io/tutorials/?tags=relational-database&limit=50


Give me 3 articles each on why I should use Java, Python and Go.


### Services
What companies are currently hiring for remote Ruby jobs?


Are there any government agencies using Go?





### Meta
Who created this API?
[Matt Makai](http://www.mattmakai.com/)


Is this API open source?
[Yup](https://github.com/makaimc/plapi)


If I use another API besides this one, which one should I use?
[Twilio](https://twilio.com/docs) :)


## Quickstart
Let's pull up some basic information about the Python programming 
language using the programming-language endpoint (see the next section
for a list of all endpoints). 

Try a GET request on the following URL:

    GET http://api.plapi.io/programming-language/python

You'll receive back JSON corresponding to the Python programming language.


## Endpoints
There are several endpoints:

Language ecosystems
1. Concepts
1. Code implementations
1. Paradigms
1. Programming languages

Learning materials
1. Tutorials
1. Books
1. Courses


Services
1. Helper libraries
1. Consultants and contractors
1. Gigs


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



# Programming Languages API (PLAPI)
Plapi is a web API for programming languages, code libraries and tutorials. 

This repository contains the source code for the web API. You don't
need any code from here to get started using the API, but this README does
provide a reference for getting started.

There are currently two endpoints:

1. [/programming-languages/](http://api.plapi.io/programming-languages/)

1. [/tutorials/](http://api.plapi.io/tutorials/)


You can use these endpoints as an unauthenticated user at a rate of 5 
requests per minute, or grab an API key to bump the limit up to 20 requests 
per minute.


## Examples
### Programming Languages
TBD


### Potential Future Improvements 
Return a list of all imperative paradigm programming languages that are 
dynamically-typed.

    https://api.plapi.io/paradigms/imperative/?typing=dynamic
Show me all the task queue implementations written in Go, Python or Java.
    
    https://api.plapi.io/implementations/task-queues/?language=go&language2=python&language3=java


List all the programming languages that first appeared starting in 2001.

    https://api.plapi.io/programming-languages/?year-gte=2001


How many major and minor versions (x.x) of Go have been released?

What languages were influenced by COBOL?

What license is the Python programming language released under?

    https://api.plapi.io/programming-languages/python


### Tutorials
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


### Meta
Who created this API?
[Matt Makai](http://www.mattmakai.com/)


Is this API open source?
[Yup](https://github.com/makaimc/plapi/LICENSE)


If I use another API besides this one, which one should I use?
[Twilio](https://twilio.com/api) :)


## Quickstart
Let's pull up some basic information about the Python programming 
language using the programming-language endpoint (see the next section
for a list of all endpoints). 

Try a GET request on the following URL:

    GET http://api.plapi.io/programming-language/python

You'll receive back JSON corresponding to the Python programming language.


## Adding new data
Issue a POST request to an endpoint with the required data. There's a
quick manual approval process, to make sure the data is correct and
has all of the proper fields. After the data is approved it'll be live
for all Plapi requests.


## Editing existing data
TBD



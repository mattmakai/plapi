# Programming Languages Web API
Plapi is a web application programming interface (API) for obtaining 
curated data about programming languages, code libraries and tutorials. 

This repository contains the source code for the web API. You don't
need any code from here to use the API, but this README does provide a 
reference for learning about what the API contains.


## Endpoints
There are currently three endpoints:

1. [/libraries](http://api.plapi.io/libraries/) - a package of code,
   such as a web framework or data analysis tool

1. [/programming-languages](http://api.plapi.io/programming-languages/) -
   the anchor concept for the web API, a named programming language such
   as Python or Elixir

1. [/tutorials](http://api.plapi.io/tutorials/) - an article or blog post
   that helps the reader learn about a programming language and/or code
   library


You can use these endpoints as an unauthenticated user at a rate of 5 
requests per minute, or grab an API key (coming soon) to bump the limit up 
to 20 requests per minute.


## Searching
The data will soon be searchable with querystring parameters such as the
following examples.

* List all the programming languages that first appeared starting in 2001.

  GET [http://api.plapi.io/programming-languages/?year-gte=2001](http://api.plapi.io/programming-languages/?year-gte=2001)


List all the programming languages that first appeared starting in 2001
but no later than 2010.

    http://api.plapi.io/programming-languages/?year-gte=2001&year-lte=2010


What languages are open sourced under the MIT license?

    http://api.plapi.io/programming-languages/?license=MIT


What code libraries are useful for deploying code?

    http://api.plapi.io/libraries/?tags=deployment


List all the code libraries for either django OR flask.

    http://api.plapi.io/libraries/?tags=django,flask


## Adding new data
Issue a POST request to an endpoint with the required data. There is a
quick manual approval process before the data is made visible. After the 
data is approved it'll be live for all Plapi requests.


### FAQ / Meta
1. **Who created this API?**

    [Matt Makai](http://www.mattmakai.com/), currently a 
    [Developer Evangelist @ Twilio](https://www.twilio.com/blog/2014/02/introducing-developer-evangelist-matt-makai.html).


1. **Is this API open source?**

    [Yup, MIT license](https://github.com/makaimc/plapi/LICENSE). Fork and 
    hack away. Submit a 
    [pull request](https://github.com/makaimc/plapi/pulls) when you improve
    the code.


1. **I'm learning about web APIs. What's another one I should use?**

    [Twilio](https://twilio.com/api) :)


1. **Where can I learn more about building web apps and APIs with Python?**

    [Full Stack Python](https://www.fullstackpython.com), especially the
    [Best Python Resources](https://www.fullstackpython.com/best-python-resources.html)
    page.


### Future Work & Ideas
1. A /change-log/ endpoint whenever something new is added.
1. Retrieve random libraries and tutorials on specific tags.
1. Edit existing data through POST requests.


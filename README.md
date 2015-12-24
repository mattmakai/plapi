# Programming Languages Web API
Plapi is a web application programming interface (API) for obtaining 
curated data about programming languages, code libraries and tutorials. 

This repository contains the source code for the web API. You don't
need any code from here to use the API, but this README does provide a 
reference for learning about what the API contains.


## Endpoints
There are currently three endpoints:

1. [/libraries](http://api.plapi.io/libraries/) - 

1. [/programming-languages](http://api.plapi.io/programming-languages/)

1. [/tutorials](http://api.plapi.io/tutorials/)


You can use these endpoints as an unauthenticated user at a rate of 5 
requests per minute, or grab an API key (coming soon) to bump the limit up 
to 20 requests per minute.


## Searching
The data will soon be searchable with querystring parameters such as the
following examples.

List all the programming languages that first appeared starting in 2001.

    https://api.plapi.io/programming-languages/?year-gte=2001


What languages are open sourced under the MIT license?

    https://api.plapi.io/programming-languages/?license=MIT


## Adding new data
Issue a POST request to an endpoint with the required data. There is a
quick manual approval process before the data is made visible. After the 
data is approved it'll be live for all Plapi requests.


### Meta
Who created this API?
[Matt Makai](http://www.mattmakai.com/)


Is this API open source?
[Yup](https://github.com/makaimc/plapi/LICENSE)


If I use another API besides this one, which one should I use?
[Twilio](https://twilio.com/api) :)


### Future Ideas
1. A /change-log/ endpoint whenever something new is added.
1. Retrieve random tutorials on specific tags.
1. Edit existing data through POST requests.

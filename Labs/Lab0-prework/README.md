# The Coffee Bar App 
The demo application instrumented by [OpenTelemetry] framework.

![The Coffee Bar](/images/tcb.png)
Format: ![Alt Text](url)

## Content
* `deployments` directory contains specific deployments templates files
* `applications` directory contains sources of the application
    * `aws-lambdas` - contains sources of the CheckSweets and Sweets AWS lambda functions
    * `dotnet-core-calculator-svc` - contains sources of the `calculator-svc` application
    * `js-the-coffee-bar-ui-clicker` - contains sources of the [puppeteer] which clicks on the frontend application
    * `python-the-coffee-bar-apps` - contains sources of `the-coffee-lover, the-coffee-bar, the-coffee-machine` and 
    `the-cashdesk` applications
    * `ruby-the-coffee-bar-apps` - contains sources of `machine-svc, coffee-svc and water-svc` applications
    * `the-coffee-bar-frontend` - contains sources of the web UI application
* `scripts` - directory contains build scripts

## Prerequisities
* Installed [docker]
* Installed [docker-compose]

## How to build?
Execute the build script `build_local_all.sh` from `scripts` directory. The script is going to build all of the 
applications in the docker images.  To run the application execute `docker-compose up` command in the `dockerization` directory.

## Application Overview
The Coffee Bar is an application designed to test instrumentation possibilities using the [OpenTelemetry] framework. 
The application consists of several small services written in various languages, including Python, Ruby and 
ASP .NET Core.

### Application flow
Like in the real italian coffee bar there is espresso and his fans. The coffee enthusiast role goes to `the-coffee-bar-frontend` 
web application or `the-coffee-lover` app (traffic simulator). `the-coffee-bar` is a small italian bar where `the-coffee-machine` 
and `the-cashdesk` are located. `the-coffee-machine` with her parts: `machine-svc` responsible for coffee preparation, `coffee-svc` responsible for 
providing coffee beans and `water-svc` responsible for water provision. The espresso coffee is not for free. 
Payment is handled by `the-cashdesk`. To be sure that the sum to be paid is correct, `calculator-svc` is present.

1. `the-coffee-bar-frontend` - The Coffee Bar user interface
2. `the-coffee-lover` is asking for espresso coffee by HTTP POST request with specific JSON to `the-coffee-bar` service.  
3. `the-coffee-bar` is sending the HTTP POST request to `the-coffee-machine` which sends a request to `machine-svc`.  
4. `machine-svc` calls `coffee-svc` and `water-svc` for ingredients and then prepares coffee.  
5. When coffee is done `the-coffee-bar` is sending the payment request to `the-cashdesk`.  
6. `the-cashdesk` application is querying `postgres` to get a coffee price and then sends a request to `calculator-svc`  
7. `calculator-svc` is doing some simple mathematical operations.

* `the-coffee-bar-frontend` - NodeJS
* `the-coffee-lover` - Python
    * `the-coffee-bar` - Python
        * `lambdas` - Python
        * `the-coffee-machine` - Python
            * `machine-svc` - Ruby
                * `coffee-svc` - Ruby
                * `machine-svc` - Ruby
        * `the-cashdesk` - Python
            * `calculator-svc` - ASP .NET Core
            * `postgres`

## Lab 0 - Pre-Work
From this directory, run `docker-compose up`

# Contact
In case of any issues please contact Mateusz 'mat' Rumian @ mrumian@sumologic.com


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [pipenv]: <https://pypi.org/project/pipenv/>
   [jaeger]: <https://www.jaegertracing.io/docs/1.18/getting-started/#all-in-one>
   [docker]: <https://docs.docker.com/get-docker/>
   [docker-compose]: <https://docs.docker.com/compose/install/>
   [OpenTelemetry-Python]: <https://opentelemetry-python.readthedocs.io/en/stable/examples/auto-instrumentation/README.html>
   [OpenTelemetry]: <https://opentelemetry.io/>
   [puppeteer]: <https://github.com/puppeteer/puppeteer>

# weather
Python app that exposes via web server on port 8080 Cape Town weather data that it got from a web service.

"Host" refers to the machine from which the container image is built and run.

## Build image
In the host, in the `weather` directory:
Build a docker image named repeater from the Dockerfile.

`docker build -f Dockerfile -t repeater .`

## Run the container
In the host, in the `weather` directory:
Run a container using the repeater image in interactive mode with a pseudo-TTY (-it) in host network (--network host), removing container when it exits (--rm).

`docker run --rm -it --network host repeater`

Container will exit on CTL+C. To run it in daemon mode, use the -d switch with docker run.

## To use
From inside the host, go with browser to `localhost:8080`.
It should display temperature, wind and a summary for today's weather for Cape Town.
If the hostName variable in repeater.py is changed from localhost to the IP address of the host and the image is built, then running the container in the same way will allow computers access to port 8080 from outside the host.

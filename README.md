# weather
Python app that exposes via web server Cape Town weather data that it got from a web service.

From inside the weather directory...

## Build image
Build a docker image named repeater from the Dockerfile.

`docker build -f Dockerfile -t repeater .`

## Run the container
Run a container using the repeater image in interactive mode with a pseudo-TTY (-it) in host network (--network host), removing container when it exits (--rm).

`docker run --rm -it --network host repeater`

Container will exit on CTL+C. To run it in daemon mode, use the -d switch with docker run.

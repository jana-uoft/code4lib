# Demo 1: Images and Containers

## Building an image
`docker image build [OPTIONS] {context}`

The docker build command builds Docker images from a Dockerfile and a “context”.
A build’s context is the set of files located in the specified PATH or URL.
The build process can refer to any of the files in the context.

Image Build options: https://docs.docker.com/engine/reference/commandline/build/#options

```
docker image build --tag jokes .
```

## Spinning up a new container from an image
`docker container run [OPTIONS] IMAGE[:TAG|@DIGEST] [COMMAND] [ARG...]`

Container Run options: https://docs.docker.com/engine/reference/commandline/run/#options

<em>this python script will print out a random joke into the terminal.</em>

```
docker container run --name joker1 jokes
```
`docker container ls --all`
```
docker container run --name joker1 jokes
```
```
docker container run --name joker1 --rm jokes
```

## Re-starting a stopped container
`docker container start [OPTIONS] CONTAINER [CONTAINER...]`

Container Start options: https://docs.docker.com/engine/reference/commandline/start/#options

```
docker container start --attach joker
```

## Deleting a container
`docker container rm [OPTIONS] CONTAINER [CONTAINER...]`

```
docker container rm joker1
```

```
docker container prune
```

## Deleting an image
`docker image rm [OPTIONS] IMAGE [IMAGE...]`

```
docker image rm jokes1
```

```
docker image prune
```
Image prune options: https://docs.docker.com/engine/reference/commandline/image_prune/#options

## Overriding the container run CMD
```
docker container run --name joker1 --rm jokes python --version
```

# Demo 2: Exposing Ports

## Building an image
```
docker build --tag mysite .
```

## Spinning up a new container from an image
`docker container run [OPTIONS] IMAGE[:TAG|@DIGEST] [COMMAND] [ARG...]`

Container Run options: https://docs.docker.com/engine/reference/commandline/run/#options

```
docker container run --name site1 -p 8000:8000 mysite
```

Go to http://localhost:8000 to see your web page

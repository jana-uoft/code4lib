# Demo 1: Running a basic Python app

The Python app will print out a randomly generated joke to the terminal.

## Build image:
```
docker build -t jokes1 .
```

## Spin up container from the image:
```
docker container run --name joker jokes1
```

## Delete container:
```
docker container rm joker
```

## Delete image:
```
docker image rm jokes1
```
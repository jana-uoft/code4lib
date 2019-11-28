# Demo 2: Running a basic Python app

The Python app writes a random joke to text file.

## Build image:
```
docker build -t jokes2 .
```

## Spin up container from the image:
```
docker container run --name joker2 jokes2
```

## Delete container:
```
docker container rm joker2
```

## Delete image:
```
docker image rm jokes2
```
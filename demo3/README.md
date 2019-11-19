# Demo 3: Running a basic web site

## Build image:
```
docker build -t mysite1 .
```

## Spin up container from the image:
```
docker container run --name site1 mysite1 -p 8000:8000
```

## Access the website

Go to the URL http://localhost:8000 to see your web page

## Stop the container

Press CTRL C in the terminal window where you did `docker container run`

## Delete container:
```
docker container rm site1
```

## Delete image:
```
docker image rm mysite1
```
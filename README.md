# splunk

## Stand alone
```bash
docker run --rm --name=splunk -p 8000:8000 -e 'SPLUNK_START_ARGS=--accept-license' -e 'SPLUNK_PASSWORD=12345678' splunk/splunk:latest
```

## Setup
```bash
docker-compose up -d
```

## Logs
```bash
docker-compose logs --tail=10 -f splunk
```

## Delete
```bash
docker-compose down --volumes
```

## Build [App Inspector](https://dev.splunk.com/enterprise/docs/releaseapps/appinspect/) Docker
```bash
docker build --tag appinspect:latest --file=appinspect.Dockerfile .
docker run --rm -ti --volume $PWD/app:/app appinspect:latest sh
docker run --rm -ti --volume $PWD/app.tgz:/app.tgz appinspect:latest splunk-appinspect inspect app.tgz
```


## Build [Slim](https://dev.splunk.com/enterprise/docs/releaseapps/packagingtoolkit/) Docker
```bash
docker build --tag slim:latest --file=slim.Dockerfile .
docker run --rm -ti --volume $PWD/app:/app slim:latest sh
```

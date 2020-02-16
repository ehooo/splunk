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

# Tools
## [App Inspector](https://dev.splunk.com/enterprise/docs/releaseapps/appinspect/) Docker
```bash
docker build --tag appinspect:latest --file=appinspect.Dockerfile .
docker run --rm -ti --volume $PWD:/app appinspect:latest sh
docker run --rm -ti --volume $PWD/app.tgz:/app.tgz appinspect:latest splunk-appinspect inspect app.tgz
```


## [Slim](https://dev.splunk.com/enterprise/docs/releaseapps/packagingtoolkit/) Docker
```bash
docker build --tag slim:latest --file=slim.Dockerfile .
docker run --rm -ti --volume $PWD:/app slim:latest sh
```


## [Python SDK](https://github.com/splunk/splunk-sdk-python) Docker
```bash
docker build --tag splunk_sdk:latest --file=splunk_sdk.Dockerfile .
docker run --rm -ti --volume $PWD:/app splunk_sdk:latest sh
```

# Related doc:
* [Refresh apps entrypoint](http://localhost:8000/en-GB/debug/refresh)
* [Custom Search Commands](https://dev.splunk.com/enterprise/docs/developapps/customsearchcommands/)
* [App.conf doc](https://docs.splunk.com/Documentation/Splunk/8.0.1/Admin/Appconf)
* [Develop Apps](https://dev.splunk.com/enterprise/docs/developapps/)
* [Python Splunk SDK](https://github.com/splunk/splunk-sdk-python)

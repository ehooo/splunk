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

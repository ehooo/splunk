FROM python:3.7-alpine

ENV PYTHONWARNINGS="ignore"

# Install Splunk App Inspector
RUN apk --update --no-cache add gcc libc-dev libxslt-dev jpeg-dev libmagic && \
    wget https://download.splunk.com/misc/appinspect/splunk-appinspect-latest.tar.gz --output-document splunk-appinspect.tgz && \
    tar -zxvf splunk-appinspect.tgz && \
    cd splunk-appinspect-* && \
    python setup.py install && \
    cd .. && rm -fr splunk-appinspect*

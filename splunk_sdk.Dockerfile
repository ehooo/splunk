FROM python:3.7-alpine

ENV PYTHONWARNINGS="ignore"

# Install Splunk App Lib
RUN apk --update --no-cache add git && \
    git clone https://github.com/splunk/splunk-sdk-python.git && \
    cd splunk-sdk-python && \
    python setup.py install

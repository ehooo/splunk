FROM python:2.7-alpine

ENV PYTHONWARNINGS="ignore"

# Install Splunk Packaging Toolkit
RUN wget http://download.splunk.com/misc/packaging-toolkit/splunk-packaging-toolkit-1.0.0.tar.gz  --output-document splunk-packaging-toolkit.tgz && \
    pip install semantic_version && \
    pip install splunk-packaging-toolkit.tgz
    rm splunk-packaging-toolkit.tgz

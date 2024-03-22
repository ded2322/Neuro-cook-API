FROM docker.elastic.co/beats/filebeat-oss:8.12.2-arm64

COPY filebeat.yml ./filebeat/filebeat.yml
USER root
RUN chown -R root ./filebeat/
RUN chmod -R go-w ./filebeat/
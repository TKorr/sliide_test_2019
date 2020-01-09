FROM google/cloud-sdk:slim

LABEL maintainer="data-engineering@energyaspects.com"

COPY dist/__name__-0.1.0.tar.gz __name__-0.1.0.tar.gz

COPY dist/gcloud-service-key.json gcloud-service-key.json

ARG GCP_PROJECT

RUN gcloud --quiet config set project $GCP_PROJECT
RUN gcloud --quiet config set compute/zone europe-west1
RUN gcloud auth activate-service-account --key-file gcloud-service-key.json

RUN apt-get update -y
RUN apt-get install python3-pip --upgrade -y

RUN pip3 install pip __name__-0.1.0.tar.gz --upgrade

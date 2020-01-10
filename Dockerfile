FROM python:3.6-slim
LABEL maintainer="Thomas Korrison"

COPY dist/sliide_test-0.1.0.tar.gz sliide_test-0.1.0.tar.gz

RUN apt-get update -y
RUN apt-get install python3-pip --upgrade -y

RUN pip3 install pip sliide_test-0.1.0.tar.gz --upgrade

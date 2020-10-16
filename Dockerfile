FROM python:3.8-slim

RUN apt update && apt install -y curl

WORKDIR /appconftest

RUN curl -sL https://get.helm.sh/helm-v3.3.4-linux-amd64.tar.gz | tar -xvz; mv linux-amd64/helm /usr/local/bin && rm -Rf linux-amd64

COPY --from=instrumenta/conftest:v0.21.0 /usr/local/bin/conftest /usr/local/bin

ADD run.py .
ADD policy /appconftest/policy

CMD python run.py

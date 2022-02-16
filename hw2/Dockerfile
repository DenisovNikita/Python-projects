FROM ubuntu:20.04

ARG  DEBIAN_FRONTEND=noninteractive
ENV  TZ=Europe/Moscow

RUN  apt-get update && apt-get -y install \
     texlive-latex-recommended \
     latexmk \
     python3-pip

RUN apt-get update && apt-get -y install \
    libgraphviz-dev

RUN pip install pygraphviz
RUN pip install -i \
    https://test.pypi.org/simple/ ast-builder-package-DenisovNikita==0.1.0

COPY artefacts /root/artefacts
COPY resources /root/resources
COPY src       /root/src
WORKDIR /root/src/
RUN ./run_medium_task.sh
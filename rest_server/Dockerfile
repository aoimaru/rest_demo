FROM python:3.7.5

ARG app_dir=/src/

ADD requirements.txt $app_dir

WORKDIR $app_dir

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

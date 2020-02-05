FROM python:2.7.17-stretch
RUN apt update && apt install -y ffmpeg
ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
ADD . /code
WORKDIR /code

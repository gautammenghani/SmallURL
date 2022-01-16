FROM ubuntu:20.04
RUN apt update && apt install -y memcached
RUN apt install -y python3.8 python3-pip

EXPOSE 5000
EXPOSE 11211

RUN mkdir /SmallURL
WORKDIR /SmallURL

ADD . /SmallURL
RUN pip3 install -r requirements.txt
ENV FLASK_ENV=development

ENTRYPOINT service memcached start && flask run --host 0.0.0.0

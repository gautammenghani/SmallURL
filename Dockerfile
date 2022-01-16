FROM ubuntu:20.04
RUN apt update && apt install -y memcached
RUN apt install -y python3.8 python3-pip

# RUN useradd -d /home/user/ -m -p user -s /bin/bash user
# RUN echo "user:user" | chpasswd

EXPOSE 5000
EXPOSE 11211

RUN mkdir /SmallURL
WORKDIR /SmallURL

ADD . /SmallURL
RUN pip3 install -r requirements.txt
ENV FLASK_ENV=development


# CMD ["/usr/bin/memcached","-d", "-l", "0.0.0.0", "-p", "11211", "-u", "root","-m","64"]
# RUN /usr/bin/memcached -l 0.0.0.0 -p 11211 -u root &
# CMD ["flask", "run","--host=0.0.0.0"]
ENTRYPOINT service memcached start && flask run --host 0.0.0.0

# Ubuntu Linux as the base image
FROM ubuntu:latest

# Install packages 
RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get -y install python3-pip python3-dev
	
ADD . /webApp

RUN pip3 install flask
RUN pip3 install requests

ENV HOME /webApp
WORKDIR /webApp

EXPOSE 6000

CMD ["python3 pyService.py && tail -f /dev/null"]

ENTRYPOINT ["/bin/bash", "-c"]	

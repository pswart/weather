FROM python:3

WORKDIR /usr/src/app

COPY . .

CMD [ "python", "./repeater.py" ]

RUN pip install --upgrade pip
RUN pip install requests==2.22.0
RUN pip install requests-unixsocket==0.2.0
RUN pip install httplib2==0.14.0
RUN pip install simplejson==3.16.0

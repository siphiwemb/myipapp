FROM python:3.9.6-alpine

ENV PYTHONUNBUFFERED 1

RUN addgroup -S admin && adduser -S admin -G admin

# install uwsgi dependencies
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers python3-dev musl-dev openssl-dev \
    && apk add libffi-dev nano \
    && rm -rf /var/lib/apt/lists/* 

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/
COPY .env /app/

RUN python manage.py collectstatic --noinput

# create uwsgi logs file 
RUN mkdir -p /var/log/uwsgi/ && touch /var/log/uwsgi/myip.log && chown admin:admin -R /var/log/uwsgi/

CMD ["uwsgi", "--ini", "uwsgi.ini"]
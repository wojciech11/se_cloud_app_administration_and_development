from python:3

RUN mkdir -p /tmp
ADD requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

RUN mkdir -p /srv

ADD main.py /srv
ADD wsgi.py /srv

WORKDIR /srv

ENV GUNICORN_WORKERS=4

CMD rm -rf multiproc-tmp && \
	mkdir multiproc-tmp && \
	gunicorn --bind 0.0.0.0:8080 -w $GUNICORN_WORKERS wsgi:app

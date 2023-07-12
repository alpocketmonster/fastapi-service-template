FROM python:3.9-slim

ARG APP_HOME=/code

WORKDIR ${APP_HOME}

ENV PYTHONPATH=$HOME
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PIP_NO_CACHE_DIR=1

COPY constraints.txt requirements.txt /etc/

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libldap2-dev libc-dev libsasl2-dev \
    && pip install -c /etc/constraints.txt -r /etc/requirements.txt \
    && apt-get purge -y --auto-remove gcc libc-dev

COPY app ${APP_HOME}/app
RUN chown -R :root ${APP_HOME}/

CMD python -m app
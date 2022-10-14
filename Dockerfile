ARG PYTHON_VERSION=3.8.13
FROM python:${PYTHON_VERSION}

RUN apt-get update && \
    apt-get install -y cron make gettext-base libpq-dev

ENV PROJECT_DIR /opt/app/
WORKDIR ${PROJECT_DIR}
RUN mkdir -p ${PROJECT_DIR}
ADD requirements.txt ${PROJECT_DIR}/
RUN pip3 install -r ${PROJECT_DIR}/requirements.txt

ADD . ${PROJECT_DIR}

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]

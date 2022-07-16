ARG PYTHON_VERSION
FROM python:${PYTHON_VERSION}

RUN apt-get update && \
    apt-get install -y cron make gettext-base libpq-dev

WORKDIR /opt/app
RUN mkdir -p ${WORKDIR}
ADD requirements.txt ${WORKDIR}/
RUN pip3 install -r ${WORKDIR}/requirements.txt

ADD . ${WORKDIR}

EXPOSE 8000

ENTRYPOINT ["/opt/app/entrypoint.sh"]

FROM python:3.13.2-slim

ENV PYTHONUNBUFFERED 1

ADD requirements* /

RUN pip install --upgrade pip setuptools \
    && pip install -r /requirements.txt -r /requirements-dev.txt

EXPOSE 8000
# ENTRYPOINT [ "executable" ]
WORKDIR /apps/app
CMD ["python", "manage.py", "runserver_plus", "0.0.0.0:8000"]

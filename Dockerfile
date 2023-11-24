FROM python:3.11.6-slim

ENV PYTHONUNBUFFERED 1

RUN apt update && apt upgrade -y && apt -y install curl vim && pip install --upgrade pip setuptools

ADD requirements* /

RUN pip install -r /requirements.txt -r /requirements-dev.txt

EXPOSE 8000
# ENTRYPOINT [ "executable" ]
WORKDIR /apps/app
CMD ["python", "manage.py", "runserver_plus", "0.0.0.0:8000"]

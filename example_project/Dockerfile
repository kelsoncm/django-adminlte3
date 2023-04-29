FROM python:3.9.16-slim-bullseye

ENV PYTHONUNBUFFERED 1

RUN apt update && apt upgrade -y && apt -y install curl vim && pip install --upgrade pip setuptools

ADD requirements_example.txt /

RUN pip install -r /requirements_example.txt 

COPY --from=lib . /app/lib

ADD . /apps/app

EXPOSE 8000
# ENTRYPOINT [ "executable" ]
WORKDIR /apps/app
CMD ["python", "manage.py", "runserver_plus", "0.0.0.0:8000"]

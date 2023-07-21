FROM python:3.12.0b3-slim-bullseye

ENV PYTHONUNBUFFERED 1

RUN apt update && apt upgrade -y && apt -y install curl vim && pip install --upgrade pip setuptools

COPY --from=app /requirements.txt /
COPY --from=app /requirements-dev.txt /
RUN pip install -r requirements.txt -r requirements-dev.txt

COPY --from=app / /app/lib/
RUN pip install -r /app/lib/example_project/requirements_example.txt

ADD . /app/example_project/

EXPOSE 8000
# ENTRYPOINT [ "executable" ]
WORKDIR /app/example_project/
CMD ["python", "manage.py", "runserver_plus", "0.0.0.0:8000"]

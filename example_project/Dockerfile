FROM python:3.13.2-slim

ENV PYTHONUNBUFFERED 1

COPY --from=app /requirements.txt /
COPY --from=app /requirements-dev.txt /
COPY --from=app / /app/lib/
RUN pip install --upgrade pip setuptools \
    && pip install -r requirements.txt -r requirements-dev.txt \
    && pip install -r /app/lib/example_project/requirements_example.txt

ADD . /app/example_project/

EXPOSE 8000
# ENTRYPOINT [ "executable" ]
WORKDIR /app/example_project/
CMD ["python", "manage.py", "runserver_plus", "0.0.0.0:8000"]

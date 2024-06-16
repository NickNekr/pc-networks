FROM python:3.11

WORKDIR /web

COPY ./pyproject.toml  /web/pyproject.toml 
COPY ./solution.py  /web/solution.py

RUN pip install poetry
RUN poetry install --no-root --verbose

FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /src/
COPY poetry.lock pyproject.toml /src/

RUN pip install -U pip
RUN pip install poetry
RUN poetry config virtualenvs.create false && \
  poetry config virtualenvs.in-project true && \
  poetry install --no-root

COPY . /src/

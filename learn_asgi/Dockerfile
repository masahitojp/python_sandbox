FROM python:3.9-slim

RUN pip install starlette hypercorn

RUN useradd -m heroku_user
USER heroku_user

COPY ./app /app

CMD hypercorn app.main:app --bind 0.0.0.0:$PORT
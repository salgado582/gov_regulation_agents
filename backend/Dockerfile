FROM ubuntu:22.04
FROM python:3.11-slim

RUN mkdir /app

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=13

ENV PYTHONBUFFERED=13

RUN pip install --upgrade pip

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

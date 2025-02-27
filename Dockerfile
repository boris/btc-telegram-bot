FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY main.py /app
CMD ["python", "main.py"]

# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim

EXPOSE 8081

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1


WORKDIR /app
COPY . /app

RUN python -m pip install -r requirements.txt


RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

CMD ["gunicorn", "--bind", "0.0.0.0:8081", "-k", "uvicorn.workers.UvicornWorker", "app.main:app"]

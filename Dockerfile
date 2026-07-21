FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN addgroup --system tasklite \
    && adduser --system --ingroup tasklite tasklite

COPY requirements.txt requirements-dev.txt ./
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements-dev.txt

COPY --chown=tasklite:tasklite app ./app
COPY --chown=tasklite:tasklite tests ./tests
COPY --chown=tasklite:tasklite wsgi.py ./wsgi.py

EXPOSE 8000

USER tasklite

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "1", "--threads", "2", "--timeout", "30", "wsgi:app"]

FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1

CMD ["python", "backend/manage.py", "runserver", "127.0.0.1:8000"]
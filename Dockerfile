FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "backend/manage.py", "runserver", "0.0.0.0:8000"]
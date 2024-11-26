FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app

CMD ["gunicorn", "todo.wsgi:application", "--bind", "0.0.0.0:8000"]
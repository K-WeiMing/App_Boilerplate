FROM python:3.11.8

WORKDIR /app

COPY ./backend .

RUN pip install --no-cache-dir -r requirements.txt --verbose

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
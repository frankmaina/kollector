FROM python:3.11
EXPOSE 8050/tcp
WORKDIR /app

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /app

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8050"]
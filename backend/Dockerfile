FROM python:3.10-alpine

WORKDIR /app

ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "./start_dev.sh" ]

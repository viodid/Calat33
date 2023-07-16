FROM python:3.11-slim

ARG EMAIL_SENDER
ARG EMAIL_PASSWORD

ENV EMAIL_SENDER ${EMAIL_SENDER}
ENV EMAIL_PASSWORD ${EMAIL_PASSWORD}

RUN env | grep EMAIL

WORKDIR /calat33

COPY requirements.txt .

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8888/tcp

CMD ["gunicorn", "--bind", "0.0.0.0:8888", "run:app"]

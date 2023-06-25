FROM python:3.10-slim

ENV EMAIL_SENDER ${EMAIL_SENDER}
ENV EMAIL_PASSWORD ${EMAIL_PASSWORD}

WORKDIR /calat33

COPY requirements.txt .

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8888/tcp

CMD ["gunicorn", "--bind", "0.0.0.0:8888", "run:app"]

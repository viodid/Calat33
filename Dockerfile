FROM python:3.10-slim


WORKDIR /calat33

COPY requirements.txt .

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt
    
# Provide the config file to the container by command line
# docker run --secret=your_secret_name ...
COPY ./config.json /etc/calat33/

COPY . .

EXPOSE 8888/tcp

CMD ["gunicorn", "--bind", "0.0.0.0:8888", "run:app"]

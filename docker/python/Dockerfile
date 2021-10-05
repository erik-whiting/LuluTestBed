FROM python:3.8

WORKDIR /usr/src/app

RUN apt-get update -y && \
    apt-get install -y postgresql

COPY requirements.txt ./

RUN pip install psycopg2

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "api.py" ]
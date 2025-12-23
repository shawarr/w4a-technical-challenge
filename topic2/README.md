# Bugs

app.py:

The following imports have no uses.
should also import os for reading .env

```
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
```

---

TZ is not a valid variable, should be switched to os.getenv('TZ') to pull TZ from environment variables.

```
cet = pytz.timezone(TZ)
```

---

some_string is not valid JSON format

fixed version:

```
some_string = """
{ "ids"     : ["1", "2", "3"],
 "key"     : "eval{23W5865}",
  "context" : "restore" }
"""
```

---

No usage for POST in endpoint /ip

```
@app.route('/ip', methods=['GET', 'POST'])
to
@app.route('/ip', methods=['GET'])

```

def cet() name clashes with cet variable defined above also, it doesn't use cet variable defined above.

also: returns datetime object, which flask does not accept, therefore should be cast to string

changes:

```
@app.route('/cet', methods=['POST'])
def get_cet():
    return str(datetime.now(cet))
```

---

get_turtle endpoint should start with '/', also need to add imports for json and jsonify

changes:

```
from flask import Flask, request, send_file, jsonify
import json
@app.route("/get_turtle", methods=['GET'])
```

---

no global variable API_KEY, should pull api key from env

changes:

```
@app.route("/super_secret", methods=['GET'])
def super_secret():
    if os.getenv('API_KEY'):
        return "access granted", 200
    else:
        return "access denied", 403
```

---

Dockerfile

```
FROM alpine:latest

RUN useradd -m capybara

RUN apt-get update && apt-get install -y \
   curl \
   ca-certificates \
   apt-transport-https \
   gnupg \
   bash

RUN apt-get update

RUN apt-get update && apt-get install -y jq apt-utils cron curl nmap vim

WORKDIR /app

COPY app.py /app/app.py

RUN pip install Flask flask_cors pytz requests pyjwt

ENV FLASK_APP app.py

CMD ["flask", "run", "--host=0.0.0.0"]
```

Bugs listed:
using alpine image (which uses package manager apk, and adduser), and the below commands are apt-get and useradd

required dependencies for pip install are: flask pytz, based on the app.py file.

fixed Dockerfile:

```
FROM python:3.13-slim
WORKDIR /app
RUN pip install flask, pytz
COPY ./api/app.py .
COPY var.env .
ENV FLASK_APP app.py
EXPOSE 30307
CMD ["flask", "run", "--host=0.0.0.0", "-p", "30307"]
```

---

compose.yaml

buggy file:

```
services:
  buggy-api:
    container_name: buggy-api
    build:
      context: ./buggy-api/
      dockerfile: Dockerfile
    env_file:
      - var.env
    ports:
        - "80:80"
    networks:
      - buggy-api_network
  networks:
    buggy-api_network:
      name: buggy-api_network
```

fixes:
i've adjusted build context to be . (relative to compose.yaml), whereas my app.py and Dockerfile are in ./api/

ports: have mapped ports from 80:80 to 30307:30307

services.networks does not exist, fix indentation.

fixed naming for api since its not buggy anymore :)

```
services:
  awesome-api:
    container_name: awesome-api
    build:
      context: .
      dockerfile: ./api/Dockerfile
    env_file:
      - var.env
    ports:
      - "30307:30307"
    networks:
      - awesome-api_network
networks:
  awesome-api_network:
    name: awesome-api_network
```

---

runs perfectly with docker compose up --build :D

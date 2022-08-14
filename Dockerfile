FROM python:3.8.10

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . /app

WORKDIR /app

ENV PYTHONDONTWRITEBYCODE 1

ENV PYHTONUNBUFFRED 1

COPY ./docker.sh /
ENTRYPOINT ["sh","docker.sh"]








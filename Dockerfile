FROM python:3.6-slim

ENV PYTHONUNBUFFERED=1

RUN apt-get -qq update

RUN apt-get install --yes libgomp1

RUN mkdir /code

WORKDIR /code

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /code/

RUN python -m nltk.downloader punkt

EXPOSE 12346

CMD python nmt.py models/translation models/preprocessing/truecasing.model models/preprocessing/sentencepiece.model

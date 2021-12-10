FROM python:3.9-slim-buster

USER poop

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip3 install -f requirememts.txt

COPY . .

CMD [ "python3", "bot.py"]
FROM python:3.9-slim-buster

RUN useradd -ms /bin/bash  poop

USER poop

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "bot.py"]
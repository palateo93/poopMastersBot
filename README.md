# poopMastersBot

#### This bot is used for a very important purpose: to see which person is pooping the most :) 
---
## How to run the application in your local environment:
* `pip3 intsall python-telegram-bot`
* `pip3 intsall prettytable`
* `export TELEGRAM_TOKEN=xxxxx`
* `python3 bot.py`

## How to run the application in Docker:
* `docker run -d -e TELEGRAM_TOKEN=${token} ${image}:${tag}` 

## Available commands:
* `/start` : Start the poop competition
* `/poop` : Increase your poop count
* `/score` : Show the ranking

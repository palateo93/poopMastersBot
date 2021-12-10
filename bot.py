#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)
poopScore = {}

def stupid(score: dict):
    print(score)

# Define a few command handlers. These usually take the two arguments update and
# context.
def start(score: dict, update: Update) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    print("user: ",user.first_name)
    if user.first_name in score:
      msg = 'You have already started the competition! Keep pooping!'
    else:
      score[user.first_name] = 0
      msg = f'{user.first_name} started the poop competition, good luck!\n\n Your current score is: 0\n\n Use /poop to start counting how many times you poop!'
    update.message.reply_text(msg)


def updatePoopCount(score, update: Update) -> None:
    """Update poop counter"""
    user = update.effective_user
    if user.first_name in score:
      score[user.first_name] += 1
      msg = f"{user.first_name}'s score: {score[user.first_name]}"
    else:
      msg = "You haven't started the competition, start it with /start."
    update.message.reply_text(msg)

def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("5075306465:AAHHZ6w-XfPUJ4vKHSAqRKSC8fc7UI5KKSo")
        
    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", lambda update, context: start(poopScore, update)))
    dispatcher.add_handler(CommandHandler("poop", lambda update, context: updatePoopCount(poopScore, update)))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()

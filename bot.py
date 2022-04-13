import logging

from telegram import Update, ForceReply, Message, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет. Я Камаси-бот! Скинь своего Камасика, ведь ты здесь именно за этим.")


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    # forward user message to group
    # note: group ID with the negative sign
    channel_chat_id = YOUR_CHAT_ID
    context.bot.forward_message(chat_id=channel_chat_id,
                        from_chat_id=update.message.chat_id,
                        message_id=update.message.message_id)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Ваш Камаси отправлен. Скоро он появится в канале.")


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("BOT_TOKEN")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()

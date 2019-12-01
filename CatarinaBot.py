from firebase import Firebase
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler, CallbackQueryHandler)
import logging
from MachineLearning import MachineLearning
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

config = {
    "apiKey": "AIzaSyCZlfxzBAz4i1sUjrQw8ka8CTVoxeFl660",
    "authDomain": "catarina-agkdsc.firebaseapp.com",
    "databaseURL": "https://catarina-agkdsc.firebaseio.com",
    "projectId": "catarina-agkdsc",
    "storageBucket": "catarina-agkdsc.appspot.com",
    "messagingSenderId": "90816412114",
    "appId": "1:90816412114:web:bb54468e4e647263bc300b",
    "measurementId": "G-8D1H4674TW"
}

firebase = Firebase(config)
db = firebase.database()
# data = {"name": "Joe Tilsed"}
# db.child("users").push(data)
ml = MachineLearning()

def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu

def bot(bot, update):
    user = update.message.from_user
    logger.info("Usuário %s iniciou o bot.", user.id)
    text = update.message.text
    message = ml.getResposta(text)
    bot.sendMessage(chat_id=update.message.chat_id,
                    text=message)
    data = ml.getData(user.id)
    if data:
        print(data)
        db.child("new_messenger").push(data)
        ml.clearData()

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    updater = Updater("1061605622:AAENxYFS2CmPB1gcl-KzmR7DsWI8nbJtz7E")
    dp = updater.dispatcher

    bot_machine = MessageHandler(Filters.text, bot)

    dp.add_handler(bot_machine)
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

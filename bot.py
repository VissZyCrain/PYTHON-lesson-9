from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

bot = Bot(token='5921049610:AAG_QdtK3-Kw5K-vpVRYS-OX-10trFlTLW4')
updater = Updater(token='5921049610:AAG_QdtK3-Kw5K-vpVRYS-OX-10trFlTLW4')
dispatcher = updater.dispatcher

def del_abv(update, context):
    text = update.message.text.split()
    list1= []
    for i in text:
        if "абв" in i:
            list1.append(i)
    context.bot.send_message(update.effective_chat.id, " ".join(list1))

def del_abvV2(update, context):
    text = update.message.text.split()
    list1 = []
    for i in text:
        if "абв" in i:
            list1.append(i)
    context.bot.send_message(update.effective_chat.id, " ".join(list1[1:]))

hand_com = CommandHandler("filter", del_abvV2)
del_handler = MessageHandler(Filters.text, del_abv)
dispatcher.add_handler(del_handler)
dispatcher.add_handler(hand_com)

updater.start_polling()
updater.idle()
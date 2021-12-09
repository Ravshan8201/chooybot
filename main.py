
from telegram.ext import Updater, Dispatcher, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from func import *
from telegram.ext import callbackqueryhandler
upd = Updater(token=TOKEN, workers=4)
dis = upd.dispatcher

dis.add_handler(CommandHandler(command='start', callback=start))
dis.add_handler(CommandHandler(command='users_list', callback= users_list))
dis.add_handler(CallbackQueryHandler(pattern='ru_change', callback=ru_change))
dis.add_handler(CallbackQueryHandler(pattern='uz_change', callback=uz_change))
dis.add_handler(CallbackQueryHandler(pattern='ru', callback=ru))
dis.add_handler(CallbackQueryHandler(pattern='uz', callback=uz))
dis.add_handler(CallbackQueryHandler(pattern='STREET', callback=STREET))
dis.add_handler(CallbackQueryHandler(pattern='FLASH', callback=FLASH))
dis.add_handler(CallbackQueryHandler(pattern='ROYAL', callback=ROYAL))
dis.add_handler(MessageHandler(Filters.photo, adm))
dis.add_handler(MessageHandler(Filters.video, adm_v))
dis.add_handler(MessageHandler(Filters.text, next_func))
dis.add_handler(MessageHandler(Filters.contact, get_contac))

upd.start_polling(drop_pending_updates=True)

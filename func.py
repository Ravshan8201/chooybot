
from logger import logger
from telegram.error import BadRequest
from telegram.ext import updater

from cons import *
from cons import dct
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
from time import sleep
from sql_cons import *
import sqlite3
def start(update, context):
    user_id = update.message.chat_id
    f_name =update.message.from_user.first_name

    context.bot.send_message(chat_id= user_id, text='{} 👋🙃'.format(f_name))
    sleep(1)
    connect = sqlite3.connect('table_0f_tables.sqlite')
    cur = connect.cursor()
    TG_ID = cur.execute(get_id.format(user_id)).fetchall()
    try:
        TG_ID = TG_ID[0][0]

    except Exception:
        pass
    if TG_ID== 95753147:
            id = 957531477
            context.bot.send_message(chat_id=id, text='Админу')


    if TG_ID == user_id:
            lang_ = cur.execute(lang_select.format(user_id)).fetchall()
            connect.commit()

            lang_ = lang_[0][0]

            cur.execute(stagee.format('{}', user_id).format(5))    #!!!!!!!!!!!!!!!!!!!!!!!!!!!! v baze dannix
            connect.commit()
            home_button = [KeyboardButton(text=newdct[lang_][4])]
            context.bot.send_message(chat_id=user_id, text=newdct[lang_][2],
                                 reply_markup=ReplyKeyboardMarkup([home_button], resize_keyboard=True))

    if user_id != TG_ID:                  #!!!!!!!!!!!!!!!! eto bez dannix
            cur.execute(first_insert.format(user_id,1))
            connect.commit()
            sleep(1)
            knopka_lang = [
                InlineKeyboardButton(text='RU🇷🇺', callback_data='ru'),
                InlineKeyboardButton(text='UZ🇺🇿', callback_data='uz')
            ]
            context.bot.send_message(chat_id=user_id, text='Выберите язык:\nTilni tanglang:',
                                  reply_markup=InlineKeyboardMarkup([knopka_lang]))









def next_func(update, context):
    connect = sqlite3.connect('table_0f_tables.sqlite')
    cur = connect.cursor()
    user_id = update.message.chat_id
    f_name = update.message.from_user.first_name
    stage_ = cur.execute(stage.format(user_id)).fetchall()
    lang_= cur.execute(lang_select.format(user_id)).fetchall()
    connect.commit()
    message = update.message.text
    message = str(message)
    stage_ = stage_[0][0]
    lang_ = lang_[0][0]


    if message.lower() == 'davom etish>>>' and stage_ == 2 or message.lower() == 'далее>>>' and stage_ == 2:
            context.bot.send_message(chat_id=user_id, text=dct[lang_][0])
            sleep(1)
            _but = [KeyboardButton(text='далее>>>')]
            context.bot.send_message(text=dct[lang_][1], chat_id=user_id,
                                     reply_markup=ReplyKeyboardRemove([_but], resize_keyboard=True,
                                                                      one_time_keyboard=True))

            cur.execute(stagee.format('{}', user_id).format(3))
            connect.commit()
    if stage_ == 3:
        message1 = update.message.text
        cur.execute(upd_name.format(message1, user_id))
        connect.commit()

        cur.execute(stagee.format('{}', user_id).format(4))
        connect.commit()

    stag_ = cur.execute(stage.format(user_id)).fetchall()
    stag_ = stag_[0][0]
    if stag_ == 4 :
        name = cur.execute(select_name.format(user_id)).fetchall()
        name = name[0][0]
        b = [KeyboardButton(text=dct[lang_][4], request_contact=True)]

        context.bot.send_message(chat_id=user_id, text=dct[lang_][2].format(name),
                                 reply_markup=ReplyKeyboardMarkup([b], resize_keyboard=True,  one_time_keyboard=True))
        sleep(1)
        cur.execute(stagee.format('{}', user_id).format(5))
        connect.commit()
#!!!!!!!!!!!!!!!!! MAIN MENU
    if stage_ == 5 or message == newdct[lang_][1] and stage_==5.1 or message == newdct[lang_][4] and stage_==5.1 or message == newdct[lang_][4] and stage_==5 or message == newdct[lang_][1] and stage_==5.8:
        main_button = [KeyboardButton(text=Main_dct[lang_][0]),
                       KeyboardButton(text=Main_dct[lang_][1]),
                       KeyboardButton(text=Main_dct[lang_][2])]
        main_button1 = [KeyboardButton(text=Main_dct[lang_][3]),
                        KeyboardButton(text=Main_dct[lang_][4])]
        main_button2 = [KeyboardButton(text=newdct[lang_][9])]
        context.bot.send_message(chat_id=user_id, text=newdct[lang_][2],
                                 reply_markup=ReplyKeyboardMarkup([main_button,
                                                                   main_button1 ,
                                                                   main_button2], resize_keyboard=True))

#!!!!!!!!!!!!!!!!!!!!!!!! SMMMMMMMMMMMMM
    if message == Main_dct[lang_][0] or stage_ == 5.11:
        cur.execute(stagee.format('{}', user_id).format(5.1))
        connect.commit()
        cur.execute(get_Usluga.format('{}', user_id).format('SMM'))
        connect.commit()
        knopka_lang = [
            InlineKeyboardButton(text='🚏STREET', callback_data='STREET'),
            InlineKeyboardButton(text='⚡️FLASH', callback_data='FLASH'),
            InlineKeyboardButton(text='👑ROYAL', callback_data='ROYAL')]
        if lang_ ==2:
             context.bot.send_photo(chat_id=user_id, photo=open('Photo_base/smmru.jpg', 'rb'), reply_markup=InlineKeyboardMarkup([knopka_lang]))
        if lang_ ==1:
            context.bot.send_photo(chat_id=user_id, photo=open('Photo_base/rusmm.jpg', 'rb'),
                                   reply_markup=InlineKeyboardMarkup([knopka_lang]))
        main_button1 = [KeyboardButton(text=newdct[lang_][1])]
        context.bot.send_message(chat_id=user_id, text=newdct[lang_][0],
                                 reply_markup=ReplyKeyboardMarkup([main_button1], resize_keyboard=True))
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!WEEEEEEEEEEEEbbbbb
    if message == Main_dct[lang_][1] or stage_ == 5.2:
        cur.execute(stagee.format('{}', user_id).format(5.1))
        cur.execute(get_Usluga.format('{}', user_id).format('WEB'))
        connect.commit()
        connect.commit()
        knopka_lang = [
            InlineKeyboardButton(text=dct[lang_][12], callback_data='STREET')]
        if lang_ ==2:
             context.bot.send_photo(chat_id=user_id, photo=open('Photo_base/saytuz.jpg', 'rb'), reply_markup=InlineKeyboardMarkup([knopka_lang]))
        if lang_ ==1:
            context.bot.send_photo(chat_id=user_id, photo=open('Photo_base/saytru.jpg', 'rb'),
                                   reply_markup=InlineKeyboardMarkup([knopka_lang]))

        main_button1 = [KeyboardButton(text=newdct[lang_][1])]
        context.bot.send_message(chat_id=user_id, text=newdct[lang_][0].format(f_name),
                                 reply_markup=ReplyKeyboardMarkup([main_button1], resize_keyboard=True))
#GIVEAWAY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    if message == Main_dct[lang_][2] or stage_ == 5.3:
        cur.execute(stagee.format('{}', user_id).format(5.1))
        cur.execute(get_Usluga.format('{}', user_id).format('GIVEAWAY'))
        connect.commit()
        connect.commit()
        knopka_lang = [
            InlineKeyboardButton(text=dct[lang_][12], callback_data='STREET')]
        if lang_ == 2:
            context.bot.send_photo(chat_id=user_id, photo=open('Photo_base/givuz.jpg', 'rb'),
                                   reply_markup=InlineKeyboardMarkup([knopka_lang]))
        if lang_ == 1:
            context.bot.send_photo(chat_id=user_id, photo=open('Photo_base/givru.jpg', 'rb'),
                                   reply_markup=InlineKeyboardMarkup([knopka_lang]))

        main_button1 = [KeyboardButton(text=newdct[lang_][1])]
        context.bot.send_message(chat_id=user_id, text=newdct[lang_][0].format(f_name),
                                 reply_markup=ReplyKeyboardMarkup([main_button1], resize_keyboard=True))

#!!!!!!!!!!!!!!!!!!!!!!!! ONLINEEEEEEEEEEEE KURS
    if message == Main_dct[lang_][3] or stage_ == 5.9 and message == newdct[lang_][1]:
        cur.execute(stagee.format('{}', user_id).format(5.8))
        connect.commit()
        main_button = [KeyboardButton(text=course[lang_][0]),
                       KeyboardButton(text=course[lang_][1])]
        main_button1 = [KeyboardButton(text=course[lang_][2]),
                        KeyboardButton(text=course[lang_][3])]
        main_button2 = [KeyboardButton(text=newdct[lang_][1])]
        context.bot.send_message(chat_id=user_id, text=newdct[lang_][0].format(f_name),
                                 reply_markup=ReplyKeyboardMarkup([main_button,main_button1, main_button2], resize_keyboard=True))
       ####Course
    if message == course[lang_][0] or stage_ == 5.2:
        cur.execute(stagee.format('{}', user_id).format(5.9))
        cur.execute(get_Usluga.format('{}', user_id).format('math'))
        connect.commit()
        connect.commit()
        knopka_lang = [
            InlineKeyboardButton(text=dct[lang_][13], callback_data='STREET')]
        if lang_ ==2:
             context.bot.send_photo(chat_id=user_id, photo=open('Photo_base/matuz.jpg', 'rb'), reply_markup=InlineKeyboardMarkup([knopka_lang]))
        if lang_ ==1:
            context.bot.send_photo(chat_id=user_id, photo=open('Photo_base/matru.jpg', 'rb'),
                                   reply_markup=InlineKeyboardMarkup([knopka_lang]))

        main_button1 = [KeyboardButton(text=newdct[lang_][1])]
        context.bot.send_message(chat_id=user_id, text=newdct[lang_][0].format(f_name),
                                 reply_markup=ReplyKeyboardMarkup([main_button1], resize_keyboard=True))

    if message == course[lang_][1] or stage_ == 5.2:
        cur.execute(stagee.format('{}', user_id).format(5.9))
        cur.execute(get_Usluga.format('{}', user_id).format('smmkurs'))
        connect.commit()
        connect.commit()
        knopka_lang = [
            InlineKeyboardButton(text=dct[lang_][13], callback_data='STREET')]
        if lang_ ==2:
             context.bot.send_photo(chat_id=user_id, photo=open('Photo_base/smuz.jpg', 'rb'), reply_markup=InlineKeyboardMarkup([knopka_lang]))
        if lang_ ==1:
            context.bot.send_photo(chat_id=user_id, photo=open('Photo_base/smru.jpg', 'rb'),
                                   reply_markup=InlineKeyboardMarkup([knopka_lang]))

        main_button1 = [KeyboardButton(text=newdct[lang_][1])]
        context.bot.send_message(chat_id=user_id, text=newdct[lang_][0].format(f_name),
                                 reply_markup=ReplyKeyboardMarkup([main_button1], resize_keyboard=True))

    if message == course[lang_][2] or stage_ == 5.2:
        cur.execute(stagee.format('{}', user_id).format(5.9))
        cur.execute(get_Usluga.format('{}', user_id).format('diz'))
        connect.commit()
        connect.commit()
        knopka_lang = [
            InlineKeyboardButton(text=dct[lang_][13], callback_data='STREET')]
        if lang_ ==2:
             context.bot.send_photo(chat_id=user_id, photo=open('Photo_base/dizuz.jpg', 'rb'), reply_markup=InlineKeyboardMarkup([knopka_lang]))
        if lang_ ==1:
            context.bot.send_photo(chat_id=user_id, photo=open('Photo_base/dizru.jpg', 'rb'),
                                   reply_markup=InlineKeyboardMarkup([knopka_lang]))

        main_button1 = [KeyboardButton(text=newdct[lang_][1])]
        context.bot.send_message(chat_id=user_id, text=newdct[lang_][0].format(f_name),
                                 reply_markup=ReplyKeyboardMarkup([main_button1], resize_keyboard=True))

    if message == course[lang_][3] or stage_ == 5.2:
        cur.execute(stagee.format('{}', user_id).format(5.9))
        cur.execute(get_Usluga.format('{}', user_id).format('eng'))
        connect.commit()
        connect.commit()
        knopka_lang = [
            InlineKeyboardButton(text=dct[lang_][13], callback_data='STREET')]
        if lang_ ==2:
             context.bot.send_photo(chat_id=user_id, photo=open('Photo_base/enguz.jpg', 'rb'), reply_markup=InlineKeyboardMarkup([knopka_lang]))
        if lang_ ==1:
            context.bot.send_photo(chat_id=user_id, photo=open('Photo_base/engru.jpg', 'rb'),
                                   reply_markup=InlineKeyboardMarkup([knopka_lang]))

        main_button1 = [KeyboardButton(text=newdct[lang_][1])]
        context.bot.send_message(chat_id=user_id, text=newdct[lang_][0].format(f_name),
                                 reply_markup=ReplyKeyboardMarkup([main_button1], resize_keyboard=True))
#!!!!!!!!!!!!!!!!!!!!!!!! INFORMATIOOOOOOOOON
    if message == Main_dct[lang_][4] or stage_ == 5.3:
        cur.execute(stagee.format('{}', user_id).format(5.1))
        connect.commit()
        main_button1 = [KeyboardButton(text=dct[lang_][11]),
                        KeyboardButton(text=dct[lang_][8])]#insta
        main_button2 = [KeyboardButton(text=newdct[lang_][1])]#назад
        context.bot.send_message(chat_id=user_id, text=newdct[lang_][0].format(f_name),
                                 reply_markup=ReplyKeyboardMarkup([main_button1, main_button2], resize_keyboard=True))
#!!!!!!!!!info
    if message == dct[lang_][8] and stage_ == 5.1:
        context.bot.send_location(chat_id=user_id, latitude=41.293979, longitude=69.214407 )
        context.bot.send_message(chat_id=user_id, text=dct[lang_][7])
#!!!!!!!location
    if message == dct[lang_][11] and stage_ == 5.1:
        if lang_ ==1:
          insta = [InlineKeyboardButton(text=' 📷Instagram', url='http://Instagram.com/choymedia'),
                   InlineKeyboardButton(text='🚀Telegram', url='http://t.me/choymedia'),
                   InlineKeyboardButton(text='Сайт', url='http://Choymedia.uz')]
          if lang_==1:
              context.bot.send_document(chat_id=user_id, document=open('Photo_base/rukp.pdf','rb'), caption=dct[lang_][5], reply_markup=InlineKeyboardMarkup([insta]))

        if lang_ ==2:
          insta = [InlineKeyboardButton(text=' 📷Instagram', url='http://Instagram.com/choymedia'),
                   InlineKeyboardButton(text='🚀Telegram', url='http://t.me/choymedia'),
                   InlineKeyboardButton(text='Sayt', url='http://Choymedia.uz')]

          context.bot.send_document(chat_id=user_id, document=open('Photo_base/uzkp.pdf','rb'), caption=dct[lang_][5], reply_markup=InlineKeyboardMarkup([insta]))

    if message == '⚙️Настройки'  or message == '⚙️Sozlamalr' :

           lang_but = [KeyboardButton(text=newdct[lang_][7]),
                       KeyboardButton(text=newdct[lang_][8])]
           back_but  = [KeyboardButton(text=newdct[lang_][1])]
           context.bot.send_message(chat_id=user_id, text=newdct[lang_][0],
                                    reply_markup=ReplyKeyboardMarkup([lang_but,back_but], resize_keyboard=True))
           cur.execute(stagee.format('{}', user_id).format(5.1))
           connect.commit()
    if message == 'Til🇺🇿🇷🇺' and stage_ == 5.1 or message == 'Язык🇷🇺🇺🇿' and stage_ == 5.1:
           knopka_lang = [
               InlineKeyboardButton(text='Русский язык🇷🇺', callback_data='ru_change')
           ]
           knopka_lang1 = [
               InlineKeyboardButton(text='''O'zbek tili🇺🇿''', callback_data='uz_change')
           ]
           context.bot.send_message(chat_id=user_id, text='Выберите язык:\nTilni tagnlang:',
                                    reply_markup=InlineKeyboardMarkup([knopka_lang, knopka_lang1]))

    if message == 'Номер телефона☎️' and stage_ == 5.1 or message == 'Telefon nomer☎️' and stage_ == 5.1:
           num_ = cur.execute(select_num.format(user_id)).fetchall()
           num_ = num_[0][0]
           cur.execute(stagee.format('{}', user_id).format(5.1))
           connect.commit()
           stage_41 = cur.execute(stage.format(user_id)).fetchall()
           stage_41 = stage_41[0][0]
           # cur.execute(update_phone_num.format(num, user_id))
           # conn.commit()

           if stage_41 == 5.1:
               b = [KeyboardButton(text=newdct[lang_][6], request_contact=True)]

               context.bot.send_message(chat_id=user_id, text=newdct[lang_][6].format(f_name),
                                        reply_markup=ReplyKeyboardMarkup([b], resize_keyboard=True))




def get_contac(update, context):
        user_id = update.message.chat_id

        num = update.message.contact.phone_number
        name = update.message.from_user.first_name
        num = str(num)
        conn = sqlite3.connect('table_0f_tables.sqlite')
        cur = conn.cursor()
        cur.execute(update_phone_num.format(num, user_id))
        conn.commit()
        cur.execute(stagee.format('{}', user_id).format(5))
        conn.commit()

        stage_ = cur.execute(stage.format(user_id)).fetchall()
        lang_ = cur.execute(lang_select.format(user_id)).fetchall()
        conn.commit()
        stage_ = stage_[0][0]
        lang_ = lang_[0][0]
        main_button = [KeyboardButton(text=Main_dct[lang_][0]),
                       KeyboardButton(text=Main_dct[lang_][1]),
                       KeyboardButton(text=Main_dct[lang_][2])]
        main_button1 =[KeyboardButton(text=Main_dct[lang_][3]),
                       KeyboardButton(text=Main_dct[lang_][4])]
        main_button2 =[KeyboardButton(text=newdct[lang_][9])]
        context.bot.send_message(chat_id=user_id, text=newdct[lang_][2],
                                     reply_markup=ReplyKeyboardMarkup([main_button,
                                                                       main_button1,
                                                                       main_button2], resize_keyboard=True))
def STREET(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('table_0f_tables.sqlite')
    cur = connect.cursor()
    stage_ = cur.execute(stage.format(user_id)).fetchall()
    lang_ = cur.execute(lang_select.format(user_id)).fetchall()
    usluga = cur.execute(select_Usluga.format(user_id)).fetchall()
    num = cur.execute(select_num.format(user_id)).fetchall()
    name = cur.execute(select_name.format(user_id)).fetchall()
    connect.commit()

    stage_ = stage_[0][0]
    lang_ = lang_[0][0]
    usluga = usluga[0][0]
    name = name[0][0]
    num = num[0][0]


    if stage_ == 5.1 and usluga== 'SMM':
        context.bot.send_message(chat_id=-621470895, text='⚒Услуга: {}\n⚖️Тариф: {}\n👤Имя: {}\n📞Номер телефона: {} '.format('SMM','STREET',name,num ))

        home_button = [KeyboardButton(text=newdct[lang_][4])]
        context.bot.send_message(chat_id=user_id, text=newdct[lang_][3],
                                 reply_markup=ReplyKeyboardMarkup([home_button], resize_keyboard=True))
    if stage_ == 5.1 and usluga== 'WEB':
        context.bot.send_message(chat_id=-621470895, text='⚒Услуга: {}\n👤Имя: {}\n📞Номер телефона: {} '.format('WEB',name,num ))

        home_button = [KeyboardButton(text=newdct[lang_][4])]
        context.bot.send_message(chat_id=user_id, text=newdct[lang_][3],
                                 reply_markup=ReplyKeyboardMarkup([home_button], resize_keyboard=True))
    if stage_ == 5.1 and usluga== 'GIVEAWAY':
        context.bot.send_message(chat_id=-621470895, text='⚒Услуга: {}\n👤Имя: {}\n📞Номер телефона: {} '.format('GIVEAWAY',name,num ))

        home_button = [KeyboardButton(text=newdct[lang_][4])]
        context.bot.send_message(chat_id=user_id, text=newdct[lang_][3],
                                 reply_markup=ReplyKeyboardMarkup([home_button], resize_keyboard=True))


    #kkkkkkuuuuuuuurrrrrrsssss

    if stage_ == 5.9 and usluga== 'math':
        context.bot.send_message(chat_id=-621470895, text='К У Р С \n\nKурс: {}\n⚖️Язык: {}\n👤Имя: {}\n📞Номер телефона: {} '.format('Математика',lang_,name,num ))

        home_button = [KeyboardButton(text=newdct[lang_][4])]
        context.bot.send_message(chat_id=user_id, text=newdct[lang_][3],
                                 reply_markup=ReplyKeyboardMarkup([home_button], resize_keyboard=True))
        cur.execute(stagee.format('{}', user_id).format(5.1))
        connect.commit()
    if stage_ == 5.9 and usluga== 'smmkurs':
        context.bot.send_message(chat_id=-621470895, text='К У Р С \n\nKурс: {}\n⚖️Язык: {}\n👤Имя: {}\n📞Номер телефона: {} '.format('Smm',lang_,name,num ))

        home_button = [KeyboardButton(text=newdct[lang_][4])]
        context.bot.send_message(chat_id=user_id, text=newdct[lang_][3],
                                 reply_markup=ReplyKeyboardMarkup([home_button], resize_keyboard=True))
        cur.execute(stagee.format('{}', user_id).format(5.1))
        connect.commit()
    if stage_ == 5.9 and usluga== 'diz':
        context.bot.send_message(chat_id=-621470895, text='К У Р С \n\nKурс: {}\n⚖️Язык: {}\n👤Имя: {}\n📞Номер телефона: {} '.format('Графический дизайн',lang_,name,num ))

        home_button = [KeyboardButton(text=newdct[lang_][4])]
        context.bot.send_message(chat_id=user_id, text=newdct[lang_][3],
                                 reply_markup=ReplyKeyboardMarkup([home_button], resize_keyboard=True))
        cur.execute(stagee.format('{}', user_id).format(5.1))
        connect.commit()
    if stage_ == 5.9 and usluga== 'eng':
        context.bot.send_message(chat_id=-621470895, text='К У Р С \n\nKурс: {}\n⚖️Язык: {}\n👤Имя: {}\n📞Номер телефона: {} '.format('Английский язык',lang_,name,num ))

        home_button = [KeyboardButton(text=newdct[lang_][4])]
        context.bot.send_message(chat_id=user_id, text=newdct[lang_][3],
                                 reply_markup=ReplyKeyboardMarkup([home_button], resize_keyboard=True))
    cur.execute(stagee.format('{}', user_id).format(5.1))
    connect.commit()

def FLASH(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('table_0f_tables.sqlite')
    cur = connect.cursor()
    stage_ = cur.execute(stage.format(user_id)).fetchall()
    lang_ = cur.execute(lang_select.format(user_id)).fetchall()
    usluga = cur.execute(select_Usluga.format(user_id)).fetchall()
    num = cur.execute(select_num.format(user_id)).fetchall()
    name = cur.execute(select_name.format(user_id)).fetchall()
    connect.commit()

    stage_ = stage_[0][0]
    lang_ = lang_[0][0]
    usluga = usluga[0][0]
    name = name[0][0]
    num = num[0][0]


    if stage_ == 5.1 and usluga== 'SMM':
        context.bot.send_message(chat_id=-621470895, text='⚒Услуга: {}\n⚖️Тариф: {}\n👤Имя: {}\n📞Номер телефона: {} '.format('SMM','FLASH',name,num ))

        home_button = [KeyboardButton(text=newdct[lang_][4])]
        context.bot.send_message(chat_id=user_id, text=newdct[lang_][3],
                                 reply_markup=ReplyKeyboardMarkup([home_button], resize_keyboard=True))
    if stage_ == 5.1 and usluga== 'WEB':
        context.bot.send_message(chat_id=-621470895, text='⚒Услуга: {}\n⚖️Тариф: {}\n👤Имя: {}\n📞Номер телефона: {} '.format('WEB','FLASH',name,num ))

        home_button = [KeyboardButton(text=newdct[lang_][4])]
        context.bot.send_message(chat_id=user_id, text=newdct[lang_][3],
                                 reply_markup=ReplyKeyboardMarkup([home_button], resize_keyboard=True))
    if stage_ == 5.1 and usluga== 'GIVEAWAY':
        context.bot.send_message(chat_id=-621470895, text='⚒Услуга: {}\n⚖️Тариф: {}\n👤Имя: {}\n📞Номер телефона: {} '.format('GIVEAWAY','FLASH',name,num ))

        home_button = [KeyboardButton(text=newdct[lang_][4])]
        context.bot.send_message(chat_id=user_id, text=newdct[lang_][3],
                                 reply_markup=ReplyKeyboardMarkup([home_button], resize_keyboard=True))
def ROYAL(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('table_0f_tables.sqlite')
    cur = connect.cursor()
    stage_ = cur.execute(stage.format(user_id)).fetchall()
    lang_ = cur.execute(lang_select.format(user_id)).fetchall()
    usluga = cur.execute(select_Usluga.format(user_id)).fetchall()
    num = cur.execute(select_num.format(user_id)).fetchall()
    name = cur.execute(select_name.format(user_id)).fetchall()
    connect.commit()

    stage_ = stage_[0][0]
    lang_ = lang_[0][0]
    usluga = usluga[0][0]
    name = name[0][0]
    num = num[0][0]


    if stage_ == 5.1 and usluga== 'SMM':
        context.bot.send_message(chat_id=-621470895, text='⚒Услуга: {}\n⚖️Тариф: {}\n👤Имя: {}\n📞Номер телефона: {} '.format('SMM','ROYAL',name,num ))

        home_button = [KeyboardButton(text=newdct[lang_][4])]
        context.bot.send_message(chat_id=user_id, text=newdct[lang_][3],
                                 reply_markup=ReplyKeyboardMarkup([home_button], resize_keyboard=True))
    if stage_ == 5.1 and usluga== 'WEB':
        context.bot.send_message(chat_id=-621470895, text='⚒Услуга: {}\n⚖️Тариф: {}\n👤Имя: {}\n📞Номер телефона: {} '.format('WEB','ROYAL',name,num ))

        home_button = [KeyboardButton(text=newdct[lang_][4])]
        context.bot.send_message(chat_id=user_id, text=newdct[lang_][3],
                                 reply_markup=ReplyKeyboardMarkup([home_button], resize_keyboard=True))
    if stage_ == 5.1 and usluga== 'GIVEAWAY':
        context.bot.send_message(chat_id=-621470895, text='⚒Услуга: {}\n⚖️Тариф: {}\n👤Имя: {}\n📞Номер телефона: {} '.format('GIVEAWAY','ROYAL',name,num ))

        home_button = [KeyboardButton(text=newdct[lang_][4])]
        context.bot.send_message(chat_id=user_id, text=newdct[lang_][3],
                                 reply_markup=ReplyKeyboardMarkup([home_button], resize_keyboard=True))


def ru(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('table_0f_tables.sqlite')
    cur = connect.cursor()
    lang_choose = cur.execute(lang.format('{}', user_id).format(1)).fetchall()
    connect.commit()
    cur.execute(stagee.format('{}', user_id).format(2))
    connect.commit()
    k_but = [KeyboardButton(text='далее>>>')]
    context.bot.send_message(text='нажмите на кнопку далее...' , chat_id=user_id,  reply_markup=ReplyKeyboardMarkup([k_but], resize_keyboard=True, one_time_keyboard=True))
    sleep(1)
def uz(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('table_0f_tables.sqlite')
    cur = connect.cursor()
    cur.execute(lang.format('{}', user_id).format(2))
    connect.commit()
    cur.execute(stagee.format('{}', user_id).format(2))
    connect.commit()
    k_but = [KeyboardButton(text='davom etish>>>')]
    context.bot.send_message(chat_id=user_id, text='davom etamish tugmasini bosing...',  reply_markup= ReplyKeyboardMarkup([k_but], resize_keyboard=True, one_time_keyboard=True))
    sleep(1)
def adm(update,context):
    user_id = update.message.chat_id
    for e in admindct[1]:
     if user_id == e:
        text = update.message.caption
        photo_id = update.message.photo[-1].file_id
        file = context.bot.getFile(photo_id)
        file.download('Picture.jpeg')
        if text == None:
            pass
        else:
            try:
                connect = sqlite3.connect('table_0f_tables.sqlite')
                cur = connect.cursor()
                id = cur.execute('''
                SELECT TG_ID
                FROM Users
                WHERE TG_ID !=0
                ''').fetchall()
                for e in id:
                      e = e[0]
                      context.bot.send_photo(photo= open('Picture.jpeg','rb'), chat_id=e, caption=text)
                      sleep(1.5)
            except Exception:
                    continue
def adm_v(update,context):
    user_id = update.message.chat_id
    for e in admindct[1]:
     if user_id == e:
        text = update.message.caption
        photo_id = update.message.video.file_id
        file = context.bot.getFile(photo_id)
        file.download('Video_base/Picture.mp4')
        if text == None:
            pass
        else:
            try:
                connect = sqlite3.connect('table_0f_tables.sqlite')
                cur = connect.cursor()
                id =  cur.execute('''
                SELECT TG_ID
                FROM Users
                WHERE TG_ID !=0
                ''').fetchall()
                for e in id:
                      e = e[0]
                      context.bot.send_video(video= open('Video_base/Picture.mp4','rb'), chat_id=e, caption=text)
                      sleep(1.5)
            except Exception:
                    continue
def ru_change(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('table_0f_tables.sqlite')
    cur = connect.cursor()
    lang_choose = cur.execute(lang.format('{}', user_id).format(1)).fetchall()
    connect.commit()
    cur.execute(stagee.format('{}', user_id).format(5))
    connect.commit()
    k2_but = [KeyboardButton(text='🏠Главное меню')]
    context.bot.send_message(chat_id=user_id, text='🏠Asosiy menyu tugmasini bosing...',
                             reply_markup=ReplyKeyboardMarkup([k2_but], resize_keyboard=True))
    sleep(1)
def uz_change(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('table_0f_tables.sqlite')
    cur = connect.cursor()
    cur.execute(lang.format('{}', user_id).format(2))
    connect.commit()
    cur.execute(stagee.format('{}', user_id).format(5))
    connect.commit()
    k1_but = [KeyboardButton(text='🏠Asosiy menyu')]
    context.bot.send_message(chat_id=user_id, text='🏠Asosiy menyu tugmasini bosing...',  reply_markup= ReplyKeyboardMarkup([k1_but], resize_keyboard=True))
    sleep(1)

def users_list(update, context):
    user_id = update.message.chat_id
    connect = sqlite3.connect('table_0f_tables.sqlite')
    cur = connect.cursor()
    TG_ID = cur.execute(get_id.format(user_id)).fetchall()
    stage_update = cur.execute(stage.format(user_id)).fetchall()

    try:
            ids = cur.execute('''
            SELECT TG_ID
            FROM Users
            WHERE TG_ID !=0
            ''').fetchall()
            x = 0
            for e in ids:
                x+=1
            context.bot.send_message(chat_id=user_id, text='{} аккаунтов пользуются ботом'.format(x))

    except Exception:
        pass



def error_callback(bot, update, error):
    try:
        raise error
    except BadRequest:
        # handle malformed requests - read more below!
        print('Same message')



def error(bot, update, error):
    if not (error.message == "Message is not modified"):
        logger.warning('Update "%s" caused error "%s"' % (update, error))

    updater.dispatcher.logger.addFilter(
        (lambda s: not s.msg.endswith('A TelegramError was raised while processing the Update')))

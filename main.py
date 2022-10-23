import telebot
from telebot import types
from datetime import datetime

bot = telebot.TeleBot('5337991832:AAHS--96TNmRDWD2MTwbnU6uG-odUm4LbVI')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f"Привет, {message.from_user.first_name} {message.from_user.last_name}\n" \
           f"Я бот-помощник Зайнаба :)\n" \
           f"Она велела мне направить и помочь тебе с оформлением заказа\n\n"
    bot.send_message(message.chat.id, mess, parse_mode='html')

    day = datetime(2022, 9, 3, 12)
    data = f"До начало продажи SHOPPING MAP осталось дней: {(day - datetime.now()).days}"

    bot.send_message(message.chat.id, data, parse_mode='html')
    if message.from_user.username == 'SHEDRYn':
        bot.send_message(message.chat.id, message)
    markup_inline = types.InlineKeyboardMarkup()
    shopping_map_btn = types.InlineKeyboardButton(text='Shopping map', callback_data='shopping map')
    markup_inline.add(shopping_map_btn)

    bot.send_message(message.chat.id, "<b>Выберети желаемый продукт</b>", reply_markup=markup_inline, parse_mode='html')

    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    # start = types.KeyboardButton("Начало")
    # status = types.KeyboardButton("Статус")
    # markup.add(start, status)
    # bot.send_message(message.chat.id, f"<b>Выберети желаемый продукт</b>", reply_markup=markup, parse_mode='html')


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.message:
        if call.data == 'shopping map':
            mess = f"<b><u>SHOPPING MAP</u></b>\n" \
                   f"<b>Цена: 4000₽</b>\n" \
                   f"<b>Срок подписки: 3 месяца</b>\n" \
                   f"<b>Описание:</b> Документ в котором содержиться множество разных и уникальных наборов стилей одежды.\n\n" \
                   f"<i>После оплаты вам будет доступно ссылка на этот документ</i>"

            markup_inline = types.InlineKeyboardMarkup()
            pay_btn = types.InlineKeyboardButton(text='💳Оплатить', callback_data='pay')
            back_btn = types.InlineKeyboardButton(text='🔙Назад', callback_data='back')
            markup_inline.add(pay_btn, back_btn)

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=mess,
                                  reply_markup=markup_inline, parse_mode='html')
        elif call.data == 'back':
            mess = "<b>Выберети желаемый продукт</b>"

            markup_inline = types.InlineKeyboardMarkup()
            shopping_map_btn = types.InlineKeyboardButton(text='Shopping map', callback_data='shopping map')
            markup_inline.add(shopping_map_btn)

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=mess,
                                  reply_markup=markup_inline, parse_mode='html')


@bot.message_handler(content_types=['text'])
def echo(message):
    if message.from_user.username == 'SHEDRYn':
        bot.send_message()

@bot.message_handler()
def get_user_text(message):
    if message.text == "Начало":
        mess = f"Итак, оплатить <u>shopping map</u> можно по следующем реквизитам:\n\n" \
               f"📌Сбербанк\n4276620027812274\nZAINAB IBRAGIMOVA\n\n" \
               f"📌TINKOFF\n5536914113695542\nZAINAB IBRAGIMOVA\n\n" \
               f"После оплаты вам нужно будет выслать мне квитанцию об оплате, а также:" \
               f"\n•ФИО\n•эл.почту\n•номер телефона"
        bot.send_message(message.chat.id, mess, parse_mode='html')
    elif message.text == "m":
        bot.send_message(message.chat.id, message.chat.id)
    else:
        bot.send_message(message.chat.id, "Я не понимать тебя", parse_mode='html')


bot.polling(none_stop=True)

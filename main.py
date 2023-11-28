import telebot

bot = telebot.TeleBot('6976487615:AAGQ7o6Zl8MF9JxYIOPnCn6aMSEBvzS-jbc')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,
                     'Напиши свой знак зодиака в формате /знак_зодиака_по-английски и получи персональное послание')


@bot.message_handler(commands=['capricorn'])
def main(message):
    bot.send_message(message.chat.id,
                     'Ты всегда уверен в себе и готов помочь \nЕсли хочешь больше приятностей, пиши /more')


@bot.message_handler(commands=['aquarus'])
def main(message):
    bot.send_message(message.chat.id, 'Ты такой чуткий и понимающий \nЕсли хочешь больше приятностей, пиши /more')


@bot.message_handler(commands=['pisces'])
def main(message):
    bot.send_message(message.chat.id,
                     'У тебя незаурядный ум и большое сердце \nЕсли хочешь больше приятностей, пиши /more')


@bot.message_handler(commands=['aries'])
def main(message):
    bot.send_message(message.chat.id, 'Хочу быть, как ты \nЕсли хочешь больше приятностей, пиши /more')


@bot.message_handler(commands=['taurus'])
def main(message):
    bot.send_message(message.chat.id, 'Ты – сама надежность \nЕсли хочешь больше приятностей, пиши /more')


@bot.message_handler(commands=['gemini'])
def main(message):
    bot.send_message(message.chat.id,
                     'Быть с тобой – это постоянный праздник \nЕсли хочешь больше приятностей, пиши /more')


@bot.message_handler(commands=['cancer'])
def main(message):
    bot.send_message(message.chat.id, 'С тобой хорошо и комфортно \nЕсли хочешь больше приятностей, пиши /more')


@bot.message_handler(commands=['leo'])
def main(message):
    bot.send_message(message.chat.id, 'Твоя уверенность восхищает \nЕсли хочешь больше приятностей, пиши /more')


@bot.message_handler(commands=['virgo'])
def main(message):
    bot.send_message(message.chat.id,
                     'Ты прекрасно разбираешься в людях и жизни \nЕсли хочешь больше приятностей, пиши /more')


@bot.message_handler(commands=['libra'])
def main(message):
    bot.send_message(message.chat.id,
                     'Благодаря тебе мне хочется меняться к лучшему \nЕсли хочешь больше приятностей, пиши /more')


@bot.message_handler(commands=['scorpio'])
def main(message):
    bot.send_message(message.chat.id, 'Ты необычайно умен и прозорлив \nЕсли хочешь больше приятностей, пиши /more')


@bot.message_handler(commands=['sagittarius'])
def main(message):
    bot.send_message(message.chat.id,
                     'Я ценю твою щедрость и чувство юмора \nЕсли хочешь больше приятностей, пиши /more')


@bot.message_handler(commands=['more'])
def main(message):
    bot.send_message(message.chat.id, '[ДЛЯ ХОРОШЕГО НАСТРОЕНИЯ](https://generatom.com/compliment)')


bot.infinity_polling()


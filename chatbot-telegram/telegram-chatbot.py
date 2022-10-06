import telebot
api = '5646881602:AAG7P31Qd5m7bpazeW9MP1HDV9dCqvv044M'
bot = telebot.TeleBot(api)


@bot.message_handler(commands=['start'])
def action_start(message):
    print(message)
    nama = message.from_user.first_name
    nama_akhir = message.from_user.last_name
    bot.reply_to(
        message, 'halo apa kabar {} {} ??' . format(nama, nama_akhir))


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, 'apa yang bisa saya bantu??')


@bot.message_handler(commands=['id'])
def send_welcome(message):
    nomor_id = message.from_user.id
    nama = message.from_user.first_name
    nama_akhir = message.from_user.last_name
    bot.reply_to(message, '''
    HI ID kamu
ID = {}
Nama = {} {}
    ''' . format(nomor_id, nama, nama_akhir))


user = '1305798998 Firman'


@bot.message_handler(commands=['start-private'])
def action_start(message):
    no_id = str(message.from_user.id)
    if no_id in user:
        bot.reply_to(message, 'halo apa kabar?')
    else:
        bot.reply_to(message, 'Hanya user tertentu')


print('bot start running')
bot.polling()

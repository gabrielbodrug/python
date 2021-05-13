import telebot

bot = telebot.TeleBot('1734529045:AAFpvhUr2W2xH8o-tMyMjAjI25v7YgH-w1k')

bot.send_message('365913711', 'Bot start')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Welcom to Gabriel Bot 🍄 {message.chat.username}\n{message.chat.id}')
    bot.delete_message(message.chat.id, message.id)

@bot.message_handler(commands=['message'])
def _message(message):
    bot.send_message(message.chat.id, 'Send some message')

@bot.message_handler(commands=['reply'])
def reply(message):
    bot.reply_to(message, 'Что-нибудь')

@bot.message_handler(commands=['edit'])
def edit(message):
    bot.edit_message_text('новый текст сообщения ✨✨', message.chat.id, 78)

@bot.message_handler(commands=['send_to'])
def send_to(message):
    bot.forward_message('131463619', message.chat.id, message.id)

@bot.message_handler(commands=['photo'])
def photo(message):
    photo = open('./photo.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)

@bot.message_handler(commands=['poop'])
def send_poop(message):
    poop = open('./poop.mp3', 'rb')
    bot.send_audio(message.chat.id, poop)

@bot.message_handler(commands=['send_me_doc'])
def send_me_doc(message):
    doc = open('./doc.docx', 'rb')
    bot.send_document(message.chat.id, doc)

@bot.message_handler(commands=['clear'])
def clear(message):
    i = message.id
    while i != i - 10:
        try: 
            bot.delete_message(message.chat.id, i)
            print(i)
        except:
            i -= 1
bot.polling()
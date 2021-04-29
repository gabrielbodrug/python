import telebot

bot = telebot.TeleBot('1734529045:AAFpvhUr2W2xH8o-tMyMjAjI25v7YgH-w1k')

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, f'Welcom to Gabriel Bot 🍄 {message.chat.username}')

@bot.message_handler(commands=['culc'])
def startCulc(message):
    SplitMessage = message.text.split(' ')  
    a = int(SplitMessage[1])
    b = int(SplitMessage[3])
    action = SplitMessage[2]
    if action == '+': 
        answer = a + b
    elif action == '-': 
        answer = a - b
    elif action == '*': 
        answer = a * b
    elif action == '/': 
        answer = a / b
    bot.send_message(message.chat.id, f'{a} {action} {b} = {answer}')



bot.polling()
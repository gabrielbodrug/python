import telebot
import json

with open('config.json', 'r') as f:
    data = json.load(f)

bot = telebot.TeleBot(data["TOKEN"])

culc = {
    "a": 0,
    "b": 0 
}

def add_table_message_id(message_id, data):
    data["message_id"] = message_id
    with open('config.json', 'w') as f:
        json.dump(data, f)

def take_table_message_id():
    with open('config.json', 'r') as f:
        data = json.load(f)
    return data["message_id"]

@bot.message_handler(commands=['start'])
def send_start_message(message):
    add_table_message_id(message.id + 1, data)
    bot.send_message(message.chat.id, 'Приветик, в нашем первом боте ! 🍄\n\n /culc - запустит калькулятор')
    bot.delete_message(message.chat.id, message.id)

@bot.message_handler(commands=['say_my_name'])
def say_my_name(message):
    bot.edit_message_text(message.from_user.username, message.chat.id, take_table_message_id())
    bot.delete_message(message.chat.id, message.id)

@bot.message_handler(commands=['culc'])
def start_culc(message):
    bot.edit_message_text('a:', message.chat.id, take_table_message_id())
    bot.delete_message(message.chat.id, message.id)

@bot.message_handler(content_types=['text'])
def lisener(message):
    if message.chat.type == 'private':
        if 'хуй' in message.text: 
            bot.send_message(message.chat.id, 'маленький')
        else:
            if culc["a"] == 0:
                culc["a"] = int(message.text)
                bot.edit_message_text(f'a = {culc["a"]}\n b:', message.chat.id, take_table_message_id())
                bot.delete_message(message.chat.id, message.id)
            else: 
                culc["b"] = int(message.text)
                bot.edit_message_text(f'{culc["a"]} + {culc["b"]} = {culc["a"] + culc["b"]}', message.chat.id, take_table_message_id())
                bot.delete_message(message.chat.id, message.id)

        

bot.polling()
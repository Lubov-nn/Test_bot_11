import telebot
from telebot import types
from pprint import pprint

file_name = "C:\Python_project\Creds\Key_My_love_11.txt"

with open(file_name) as f:
    print(f)

    pprint(vars(f))

    bot_key = f.read()

botTimeWeb = telebot.TeleBot(bot_key)

if __name__ == '__main__':
    print("START")

    @botTimeWeb.message_handler()
    def print_msg(message):
        print(message)
    @botTimeWeb.message_handler(commands=['start'])
    def startBot(message):
        first_mess = f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>, привет!\nХочешь расскажу немного о нашей компании?"
        markup = types.InlineKeyboardMarkup()
        button_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
        markup.add(button_yes)
        botTimeWeb.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)


    @botTimeWeb.callback_query_handler(func=lambda call: True)
    def response(function_call):
        if function_call.message:
            if function_call.data == "yes":
                second_mess = "Мы облачная платформа для разработчиков и бизнеса. Более детально можешь ознакомиться с нами на нашем сайте!"
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://timeweb.cloud/"))
                botTimeWeb.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
                botTimeWeb.answer_callback_query(function_call.id)


    botTimeWeb.infinity_polling()
    print("END")

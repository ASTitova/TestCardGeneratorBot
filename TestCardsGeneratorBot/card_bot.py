# подключение библиотек
# В google colab добавить: !pip install pyTelegramBotAPI
# В google colab добавить: !pip install Faker
# для установки необходимо в файл requirements.text добавить строки
# 'PyTelegramBotApi'
# 'faker'

from telebot import TeleBot, types
from faker import Faker


bot = TeleBot(token='', parse_mode='html') # создание бота

faker = Faker() 

# объект клавиаутры
card_type_keybaord = types.ReplyKeyboardMarkup(resize_keyboard=True)
# первый ряд кнопок
card_type_keybaord.row(
    types.KeyboardButton(text='💳 VISA'),
    types.KeyboardButton(text='💳 Mastercard'),
    types.KeyboardButton(text='💳 Maestro')
)

# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('cat.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(
        chat_id=message.chat.id, # id чата, в который необходимо направить сообщение
        text='Готов генерировать тестовые номера 😎\n\nВыбери тип карты:', # текст сообщения
        reply_markup=card_type_keybaord,
    )

# обработчик всех остальных сообщений
@bot.message_handler()
def message_handler(message: types.Message):
   
    if message.text == '💳 VISA':
        card_type = 'visa'
    elif message.text == '💳 Mastercard':
        card_type = 'mastercard'
    elif message.text == '💳 Maestro':
        card_type = 'maestro'
   
    else:
        # если текст не совпал ни с одной из кнопок 
        # выводим ошибку
        bot.send_message(
            chat_id=message.chat.id,
            text='Не понимаю тебя 😢',
        )
        return

    # получаем номер тестовой карты выбранного типа
    card_number = faker.credit_card_number(card_type)
    
    # и выводим пользователю
    bot.send_message(
        chat_id=message.chat.id,
        text=f'Тестовая карта {card_type}:\n<code>{card_number}</code>'
    )


# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()

if __name__ == '__main__':
    main()

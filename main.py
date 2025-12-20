import telebot 
from config import token

from logic import Pokemon

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    username = message.from_user.username

    if username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(username)

        # Отправляем информацию о покемоне
        bot.send_message(message.chat.id, pokemon.info())

        # Отправляем картинку покемона
        bot.send_photo(message.chat.id, pokemon.show_img())

        # Отправляем возможности
        abilities_text = (
            "Вот что ты можешь сделать со своим покемоном:\n\n"
            "/heal - подлечить покемона (+10 HP)\n"
            "/powerup - увеличить силу атаки (+5)\n"
            "/levelup - прокачать покемона (+5 HP, +3 Атака, +2 Защита)\n"
            "/info - посмотреть текущие характеристики покемона\n"
        )
        bot.send_message(message.chat.id, abilities_text)

    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['heal'])
def heal_pokemon(message):
    username = message.from_user.username
    if username in Pokemon.pokemons:
        Pokemon.pokemons[username].heal()
        bot.reply_to(message, f"Твой покемон подлечен! ❤️ HP теперь: {Pokemon.pokemons[username].hp}")
    else:
        bot.reply_to(message, "Сначала создай покемона командой /go")


# Прокачиваем атаку
@bot.message_handler(commands=['powerup'])
def powerup_pokemon(message):
    username = message.from_user.username
    if username in Pokemon.pokemons:
        Pokemon.pokemons[username].power_up()
        bot.reply_to(message, f"Сила атаки покемона увеличена! ⚔️ Атака теперь: {Pokemon.pokemons[username].attack}")
    else:
        bot.reply_to(message, "Сначала создай покемона командой /go")


# Уровень выше (апгрейд всех характеристик)
@bot.message_handler(commands=['levelup'])
def levelup_pokemon(message):
    username = message.from_user.username
    if username in Pokemon.pokemons:
        Pokemon.pokemons[username].level_up()
        p = Pokemon.pokemons[username]
        bot.reply_to(message, f"Покемон прокачан! ❤️ HP: {p.hp}, ⚔️ Атака: {p.attack}, 🛡️ Защита: {p.defense}")
    else:
        bot.reply_to(message, "Сначала создай покемона командой /go")




bot.infinity_polling(none_stop=True)


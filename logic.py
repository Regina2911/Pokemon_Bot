from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()

        self.hp = self.get_hp()
        self.attack = self.get_attack()
        self.defense = self.get_defense()
        self.type = self.get_type()
        

        Pokemon.pokemons[pokemon_trainer] = self


    def heal(self):
            self.hp += 10

    def power_up(self):
        self.attack += 5

    def level_up(self):
        self.hp += 5
        self.attack += 3
        self.defense += 2

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['home']['front_shiny'])
        else:
            return "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/25.png"
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"


    def get_hp(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['stats'][0]['base_stat']
        return 50


    def get_attack(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['stats'][1]['base_stat']
        return 50


    def get_defense(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['stats'][2]['base_stat']
        return 50


    def get_type(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['types'][0]['type']['name']
        return "normal"


    def info(self):
        return (
             f"🐾 Имя покемона: {self.name}\n"
        f"🔥 Тип покемона: {self.type}\n"
        f"❤️ Здоровье (HP): {self.hp}\n"
        f"⚔️ Сила атаки: {self.attack}\n"
        f"🛡️ Защита: {self.defense}"
        )

    def show_img(self):
        return self.img



   



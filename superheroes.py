import random

class Hero:
    def __init__(self, name):
        self.abilities = list()
        self.name = name

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        attack_value = 0
        for a in self.abilities:
            attack_value += a.attack()
        return attack_value



class Ability:
    def __init__(self, name, attack_strength):
        if __name__ == "__main__":
            self.name = name
            self.attack_strength = attack_strength


    def attack(self):
        return random.randint((self.attack_strength // 2), self.attack_strength)


    def update_attack(self, attack_strength):
        self.attack_strength = attack_strength



class Weapon(Ability):
    def attack(self):
        return random.randint(0, self.attack_strength)



class Team:
    def init(self, team_name):
        self.name = team_name
        self.heroes = list()

    def add_hero(self, Hero):
        self.heroes.append(Hero)

    def remove_hero(self, name):
        for x in self.heroes:
            if x == name:
                self.heroes.pop()
            else:
                return 0

    def find_hero(self, name):
        for x in self.heroes:
            if x == name:
                return self.heroes[x]
            else:
                return 0

    def view_all_heroes(self):
        print(self.heroes)



# test code
# if __name__ == "__main__":
#     hero = Hero("Wonder Woman")
#     print(hero.attack())
#     ability = Ability("Divine Speed", 300)
#     hero.add_ability(ability)
#     print(hero.attack())
#     new_ability = Ability("Super Human Strength", 800)
#     hero.add_ability(new_ability)
#     print(hero.attack())

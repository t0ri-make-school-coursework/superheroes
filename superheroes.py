import random

class Hero:
    def __init__(self, name, health=100):
        self.abilities = list()
        self.name = name
        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        self.abilities.append(ability)


    def add_armor(self, armor):
        self.armors.append(armor)


    def attack(self):
        attack_value = 0
        for a in self.abilities:
            attack_value += a.attack()
        return attack_value


    def defend(self):
        defense_total = 0

        if self.health > 0:
            for x in self.armors:
                defense_total += x.defend()
        else:
            defense_total = 0
        return defense_total


    def take_damage(self, damage_amt):
        self.health -= damage_amt

        if self.health < 1:
            self.deaths += 1

        return self.deaths

    def add_kill(self, num_kills):
        self.kills += num_kills

class Ability:
    def __init__(self, name, attack_strength):
        # if __name__ == "__main__":
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
    def __init__(self, team_name):
        self.name = team_name
        self.heroes = list()

        team_kills = 0


    def add_hero(self, Hero):
        self.heroes.append(Hero)


    def remove_hero(self, name):
        n = 0

        for x in self.heroes:
            if x.name == name:
                del self.heroes[n]
                return

            n += 1

        return 0


    def find_hero(self, name):
        n = 0

        for x in self.heroes:
            if x.name == name:
                return self.heroes[n]

            n += 1

        return 0


    def view_all_heroes(self):
        for x in self.heroes:
            print(x.name)


    def attack(self, other_team):
        team_attack = 0

        for x in self.heroes:
            team_attack += x.attack()

        num_kills = other_team.defend(team_attack)

        for x in self.heroes:
            x.add_kill(num_kills)

        return num_kills


    def defend(self, damage_amt):
        team_defense = 0
        team_deaths = 0

        for x in self.heroes:
            team_defense += x.defend()

        if damage_amt > team_defense:
            return self.deal_damage(damage_amt - team_defense)

        for x in self.heroes:
            team_deaths = x.deaths

        return team_deaths


    def deal_damage(self, damage):
        total_deaths = 0

        for x in self.heroes:
            total_deaths += x.take_damage(damage/len(self.heroes))

        return total_deaths


    def revive_heroes(self, health=100):
        for x in self.heroes:
            x.health = x.start_health


    def stats(self):
        for x in self.heroes:
            print("HERO: {} KILLS: {} DEATHS: {}".format(x.name, x.kills, x.deaths))


    def update_kills(self):
        self.team_kills += 1

class Armor:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense

    def defend(self):
        return random.randint(0, self.defense)


class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None
        self.size = 0

    def hero_creation_input(self, team):
        name = input("Name your hero: ")
        ability = input("Hero's ability: ")
        ability_strength = int(input("{} strength: ".format(ability)))
        weapon = input("Hero's weapon: ")
        weapon_strength = int(input("{} strength: ".format(weapon)))
        armor = input("Hero's armor type: ")
        armor_strength = int(input("{} strength: ".format(armor)))

        new_hero = Hero(name, 100)
        new_hero.add_ability(Ability(ability, ability_strength))
        new_hero.add_ability(Weapon(weapon, weapon_strength))
        new_hero.add_armor(Armor(armor, armor_strength))

        team.add_hero(new_hero)

    def build_team_one(self):
        team_one_name = input("Name your first team: ")
        self.team_one = Team(team_one_name)
        should_exit = False

        while should_exit == False:
            response = input("Do you have a hero you'd like to create for {}? y/n: ".format(team_one_name))
            if response in ("y", "Y"):
                self.hero_creation_input(self.team_one)
            elif response in ("n", "N"):
                should_exit = True
                print(self.team_one.heroes)


    def build_team_two(self):
        team_two_name = input("Name your second team: ")
        self.team_two = Team(team_two_name)
        should_exit = False

        while should_exit == False:
            response = input("Do you have a hero you'd like to create for {}? y/n: ".format(team_two_name))
            if response in ("y", "Y"):
                self.hero_creation_input(self.team_two)
            elif response in ("n", "N"):
                should_exit = True


    def team_battle(self):
        team_one_dead_heroes = 0
        team_two_dead_heroes = 0
        while team_one_dead_heroes < 6 and team_two_dead_heroes < 6:
            team_two_dead_heroes += self.team_one.attack(self.team_two)
            team_one_dead_heroes += self.team_two.attack(self.team_one)

    def show_stats(self):
        print("{} Stats: ".format(self.team_one.name))
        self.team_one.stats()
        print("{} Stats: ".format(self.team_two.name))
        self.team_two.stats()

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()

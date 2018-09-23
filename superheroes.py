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


    def defend(self, damage_amt):
        team_defense = 0
        team_deaths = 0

        for x in self.heroes:
            team_defense += x.defend()

        if damage_amt > team_defense:
            return self.deal_damage(damage_amt - team_defense)

        for x in self.heroes:
            team_deaths = x.self.deaths

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
            print("HERO: {} KILLS: {} DEATHS: {}".format(self.name, self.kills, self.deaths))


    def update_kills(self):


class Armor:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense

    def defend(self):
        return random.randint(0, self.defense)
        # return 5

class Arena:
    def __init__(self, team_one_name, team_two_name):
        self.team_one = Team(team_one_name)
        self.team_two = Team(team_two_name)

    def hero_creation_input(y, x):
        name = input("Name your hero: ")
        ability = input("Hero's ability: ")
        ability_strength = int(input("{} strength: ").format(ability))
        weapon = input("Hero's weapon: ")
        weapon_strength = int(input("{} strength: ").format(weapon))
        armor = input("Hero's armor type: ")
        armor_strength = int(input("{} strength: ").format(armor))
        create_hero(y, x, name, ability, ability_strength, weapon, weapon_strength, armor, armor_strength)

    def create_hero(y, x, name, ability, ability_strength, weapon, weapon_strength, armor, armor_strength):
        self.y.add_hero(Hero(name))
        self.y.heroes[x].add_ability(Ability(ability, ability_strength))
        self.y.heroes[x].add_weapon(Weapon(weapon, weapon_strength))
        self.y.heroes[x].add_armor(Armor(armor, armor_strength))


    def build_team_one(self):
        response = input("Do you have heroes you'd like to create for {}"? y/n).format(team_one_name).lower()
        if response == "y":
            hero_creation_input(team_one_name, x)
        elif response == "n":
            build_team_two()

    def build_team_two(self):
        response = input("Do you have heroes you'd like to create for {}"? y/n).format(team_two_name).lower()
        if response == "y":
            hero_creation_input(team_two_name, x)
        elif response == "n":
            team_battle()


    def team_battle(self):
        """
        This method should continue to battle teams until
        one or both teams are dead.
        """

    def show_stats(self):
        print("{} Stats: ".format(team_one_name) + team_one.stats())
        print("{} Stats: ".format(team_two_name) + team_two.stats())

# test code
if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())

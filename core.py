import random, colored
from colored import stylize, fg


class Game():
    '''current state of the game'''

    def set_up(self, Gladiator_1, Gladiator_2, turn, choose_name1,
               choose_name2):
        self.Gladiator_1 = Gladiator_1
        self.Gladiator_2 = Gladiator_2
        self.turn = turn
        self.choose_name1 = choose_name1
        self.choose_name2 = choose_name2


class Player():
    """ Whoever is currently playing. """

    def __init__(self, health, damage_low, damage_high):
        """Creates a new player with health, rage, damage_low,
        and damage_high. """

    def getName(self):
        return self.__class__.__name__

    def inventory_harm(self, defender):
        random_bag_harm = {
            'a Banana Cream Pie': 5,
            'a tangle of Bolas': 30,
            'a vial of Viper Poison': 35,
            'a Joker Bomb': 40,
            'a Torque Candle': 32,
            'a loaded .45': 45,
        }
        if self.rage < 20:
            return '\nYou do not have enough Rage to use anything in your Pain Pack.\nRage Needed: 20\n'
        else:
            harming_item, harming_power = random.choice(
                list(random_bag_harm.items()))
            defender.health = min(100, defender.health)
            defender.health -= harming_power
            self.rage = max(0, self.rage)
            self.rage -= 20
            return '\nYou look into your inventory to find {}. The opponent\'s health decreases {} points.\n'.format(
                harming_item, harming_power)

    def is_dead(self):
        """
        - Returns True if gladiator has no health
        """
        if self.health <= 0:
            self.health = 0
            return True
        else:
            return False


class ClosePlayer(Player):
    """A subclass of Player, that is specific to classes that do not use magic. """

    def __init__(self, health, damage_low, damage_high, rage):

        self.health = health
        self.rage = rage
        self.damage_low = damage_low
        self.damage_high = damage_high

    def heal(self, choose_name):
        random_bag_heal = {
            'Bad Juju': 1,
            'Noku Noir': 5,
            'Recaii Red': 10,
            'Saita Seauti': 25,
            'Fanoctic Fain': 28,
            'Kaiju Blue': 30
        }
        if self.health == 100:
            print('\nCannot heal over 100 health!\n')
        else:
            if self.rage < 10:
                return '\nYou do not have enough Rage to use anything in your Apothecary\'s Satchel.\nRage Needed: 5\n'
            else:
                healing_item, healing_power = random.choice(
                    list(random_bag_heal.items()))
                self.health = min(100, healing_power + self.health)
                self.rage = max(0, self.rage)
                self.rage -= 10
                return '\n{} looks into the inventory to find {}.{} heals {} point(s).\n'.format(
                    choose_name, healing_item, choose_name, healing_power)

    def attack(self, defender, choose_name, choose_name2):
        """
        - Each attack can hit normally or crit
        - Crit chance is the same as the attacker's rage (50 rage == 50% crit chance)
        - Damage dealt is a random integer between the attacker's damage\_low and damage\_high
        - Critting doubles damage dealt
        - If a gladiator crits, their rage is reset to 0
        - If the gladiator hits normally, their rage is increased by 15
        """
        #randint 0-100 #If a random number is less than the attacker's rage it is a critical (double damage *2)
        number = self.rage
        low = self.damage_low
        high = self.damage_high
        if number < random.randint(0, 100):
            lost = random.randint(low, high)
            defender.health -= lost
            self.rage += 15
            return '\n{} lost {} health!\n'.format(choose_name, lost)
        else:
            super_lost = random.randint(low, high) * 2
            defender.health -= super_lost
            self.rage = 0
            return '\nIT\'S SUPER EFFECTIVE!\n{} lost {} health!\n'.format(
                choose_name, super_lost)


class FarPlayer(Player):
    """A subclass of Player that is specific to classes that can only use magic. """

    def __init__(self, health, damage_low, damage_high, rage):

        self.health = health
        self.rage = rage
        self.damage_low = damage_low
        self.damage_high = damage_high

    def attack(self, defender, choose_name, choose_name2):
        number = self.rage
        magic_dictionary = {
            'Kaiju Blue Bath': -15,
            'Fire Storm': 12,
            'Wind-Waker': 15,
            'Ground Pound': 11,
            'Water Cannon': 14,
            'Undead Underground': 16,
            'Vine Whip': 10,
            'Sunshine\'s Rays': 20,
            'Bad Luck Bang': 5,
            'Good Fortune': 20,
            'Gastly Grimoire': 17,
            'Blessed Brigamine': 18
        }
        critical_magic_dictionary = {
            'Kaiju Blue Spa': -30,
            'Bring About The Fire Rain': 30,
            'Wasting Winds Of The Waker': 33,
            'Shifting Pangea Peril': 29,
            'Hurricane Of TerrorTears': 32,
            'Paralyzing AkaiEyes': 34,
            'Poison Ivy Grave': 28,
            'Scorching Sunburst': 48,
            'Unlucky Eulogy': 14,
            'Luck Of The Chinese New Year': 49,
            'Murderous Matoia': 35,
            'Holy Water Spring': 36
        }

        if number < random.randint(0, 100):
            random_magic_attack = random.choice(list(magic_dictionary))
            v = magic_dictionary[random_magic_attack]
            defender.health -= v
            self.rage += 15
            return '\n{} has cast {}! {} lost {} health!\n'.format(
                choose_name2, random_magic_attack, choose_name, v)
        else:
            random_magic_attack = random.choice(
                list(critical_magic_dictionary))
            lost = critical_magic_dictionary[random_magic_attack]
            super_lost = lost * 2
            defender.health -= super_lost
            self.rage += 15
            return '\n{} has cast {}!\nIT\'S SUPER EFFECTIVE!\n{} lost {} health!\n'.format(
                choose_name2, random_magic_attack, choose_name, super_lost)

    def heal(self, choose_name):
        """

        - Spends 10 rage to heal 5 health
        - Cannot heal above max health of 100

        """
        if self.health == 100:
            return '\nCannot heal over 100 health!\n'
        else:
            if self.rage < 10:
                return '\nYou do not have enough Rage to heal.\n'
            else:
                self.rage = max(0, self.rage)
                self.rage -= 10
                self.health = min(100, 20 + self.health)
                return '\n' + choose_name + ' has healed 20 points!\n'


class Barbarian(ClosePlayer):
    """A barbarian of the wastes. (A certain sub-class
    of Player.) """

    def __init__(self, health, rage, damage_low, damage_high):

        super().__init__(health, rage, damage_low, damage_high)
        self.health = health
        self.rage = rage

        self.damage_low = damage_low
        self.damage_high = damage_high

    def special(self, defender, choose_name):
        """If the Barbarian's health is under 30, damage_low += 10 and damage_high += 15."""
        if self.health <= 30:
            self.damage_low += 10
            # min(self.damage_low + 10, self.damage_high)
            self.damage_high += 15
            return '\n-' + choose_name + ': "I\'m not done yet!"\n\nWarrior\'s Spirit Activates! Ghosts of past Barbarian\'s rise from the ground and bless Killer Axe!\nLow Atk raised 10 points and High Atk raised 15 points!\n'
        else:
            return ''


class Wizard(FarPlayer):
    """A certain sub-class of Player who uses ancient magic. """

    def __init__(self, health, rage, damage_low, damage_high):
        super().__init__(health, rage, damage_low, damage_high)
        self.health = health
        self.rage = rage
        self.damage_low = damage_low
        self.damage_high = damage_high

    def special(self, defender, choose_name):
        """If the Wizard's health is under 20, opponent is hurt 15 points."""
        if self.health <= 20:
            defender.health -= 15
            return '\n-' + choose_name + ': "The skies have aligned!"\n\nAligned Skies is activated!\n' + choose_name + '\'s Wand naturally protects it\'s master!\n\nThe opponent lost 15 health!\n'
        else:
            return ''


class Bishop(FarPlayer):
    """A certain sub-class of Player who uses magic and healing. """

    def __init__(self, health, rage, damage_low, damage_high):

        super().__init__(health, rage, damage_low, damage_high)
        self.health = health
        self.rage = rage
        self.damage_low = damage_low
        self.damage_high = damage_high

    def special(self, defender, choose_name):
        """If the Bishop's health is under 35, heal 15 points."""
        if self.health <= 35:
            self.health += 30
            return '\n-' + choose_name + ': "God truly watches over me!"\n\nHoly Ground has activated!\n' + choose_name + ' healed 15 points!\n'
        else:
            return ''


class Noble(ClosePlayer):
    """A certain sub-class of Player who uses swords and naginatas."""

    def __init__(self, health, rage, damage_low, damage_high):

        super().__init__(health, rage, damage_low, damage_high)
        self.health = health
        self.rage = rage
        self.damage_low = damage_low
        self.damage_high = damage_high

    def special(self, defender, choose_name):
        """If the Noble's health is under 25, rage is raised 5 points and opponent is dealt 10 damage."""
        if self.health <= 25:
            self.rage += 5
            defender.health -= 10
            return '\n-' + choose_name + ': "Heroes Never Die!"\n\nHigh Birth has activated!\n' + choose_name + '\'s retainer charges in and attacks!\n' + choose_name + '\'s Rage raised 5 points!\nThe opponent was dealt 10 damage!\n'
        else:
            return ''


class Cavalier(ClosePlayer):
    """A certain sub-class of Player who uses swords, lances, and rides atop a horse. """

    def __init__(self, health, rage, damage_low, damage_high):

        super().__init__(health, rage, damage_low, damage_high)
        self.health = health
        self.rage = rage
        self.damage_low = damage_low
        self.damage_high = damage_high

    def special(self, defender, choose_name):
        """If the Cavalier's health is under 30, use an item and heal 10 points, and rage is increased by 10."""
        if self.health <= 30:
            self.health += 10
            self.rage += 10
            return '\n-' + choose_name + ': "Lucky for me, I came prepared!"\n\nLucky Habits has activated!\n' + choose_name + ' looked into a first aid kit and healed 10 points, rage is increased by 10!\n'
        else:
            return ''


class General(ClosePlayer):
    """A certain sub-class of Player who defends well and uses axes and lances. """

    def __init__(self, health, rage, damage_low, damage_high):

        super().__init__(health, rage, damage_low, damage_high)
        self.health = health
        self.rage = rage
        self.damage_low = damage_low
        self.damage_high = damage_high

    def special(self, defender, choose_name):
        """If the General's health is under 20, damage_high += 10 and opponent is dealt 10 damage."""
        if self.health <= 20:
            self.damage_high += 10
            defender.health -= 10
            return '\n-' + choose_name + ': "I\'m through playing around!"\n\nPiercing Blows has activated!\n' + choose_name + ' reveals a hidden mace and swings it with deadly precision!\n' + choose_name + '\'s High Atk raised 10 points!\nThe opponent lost 10 health!\n'
        else:
            return ''


class Valkyrie(ClosePlayer):
    """A certain sub-class of Player who uses lances and swords. """

    def __init__(self, health, rage, damage_low, damage_high):

        super().__init__(health, rage, damage_low, damage_high)
        self.health = health
        self.rage = rage
        self.damage_low = damage_low
        self.damage_high = damage_high

    def special(self, defender, choose_name):
        """If the Valkyrie's health is under 30, rage is increased by 10 points and harms the opponent by 5 points."""
        if self.health <= 30:
            self.rage += 10
            defender.health -= 5
            return '\n-' + choose_name + ': "Now I\'m angry!"\n\nShrieking War Cry is activated!\n' + choose_name + '\'s Rage is raised 10 points!\nThe opponent lost 5 health!\n'
        else:
            return ''


class Assassin(ClosePlayer):
    """A certain sub-class of Player who uses swords, with deadly blows. """

    def __init__(self, health, rage, damage_low, damage_high):

        super().__init__(health, rage, damage_low, damage_high)
        self.health = health
        self.rage = rage
        self.damage_low = damage_low
        self.damage_high = damage_high

    def special(self, defender, choose_name):
        """If the Assassin's health is under 10, opponent is hurt by 20."""
        if self.health <= 10:
            defender.health -= 20
            return '\n-' + choose_name + ': "Accept your fate."\n\nSwift Kill is activated!\n' + choose_name + '\'s Killing Edge shines brightly in the shadows!\nThe opponent lost 20 health!\n'
        else:
            return ''


class Troubadour(FarPlayer):
    """A certain sub-class of Player who uses magic and rides atop a horse. """

    def __init__(self, health, rage, damage_low, damage_high):

        super().__init__(health, rage, damage_low, damage_high)
        self.health = health
        self.rage = rage
        self.damage_low = damage_low
        self.damage_high = damage_high

    def special(self, defender, choose_name):
        """If the Troubadour's health is under 25, opponent is dealt 10 damage and damage_high += 10."""
        if self.health <= 25:
            self.damage_high += 10
            defender.health -= 10
            return '\n-' + choose_name + ': "I\'m tired of being pushed around! This ends now!"\n\nSick Of It has activated!\n' + choose_name + '\'s High Atk raised 10 points!\nThe opponent lost 10 health!\n'
        else:
            return ''


class Dragonmaster(ClosePlayer):
    """A certain sub-class of Player who rides a dragon, and uses spears and javalins. """

    def __init__(self, health, rage, damage_low, damage_high):

        super().__init__(health, rage, damage_low, damage_high)
        self.health = health
        self.rage = rage
        self.damage_low = damage_low
        self.damage_high = damage_high

    def special(self, defender, choose_name):
        """If the Dragonmaster's health is under 20, Rage += 5 and opponent is dealt 15 damage."""
        if self.health <= 20:
            self.rage += 5
            defender.health -= 15
            return '\n-' + choose_name + ': "No retreat! No surrender!"\n\nSearing Spear is activated!\n' + choose_name + '\'s dragon sets fire to the spear!\n' + choose_name + '\'s Rage is raised 5 points!\nThe opponent lost 15 health!\n'
        else:
            return ''

import random
from random import randint
import time

class Character(object):
    def __init__(self):
        self.name = '<undefined>'
        self.health = 10
        self.power = 5
        self.coins = 20

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.alive():
            return
        print "%s attacks %s" % (self.name, enemy.name)
        enemy.receive_damage(self.power)
        time.sleep(1.5)

    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name

    def print_status(self):
        print "%s has %d health and %d power." % (self.name, self.health, self.power)

class Hero(Character):
    def __init__(self):
        self.name = 'hero'
        self.health = 10
        self.power = 5
        self.coins = 20
        self.armor = 0
        self.evade = 0
        self.crit_chance = 20
        self.critpower = self.power * 2
        self.inventory = []
        self.tonic = 0
        self.supertonic = 0

    def restore(self):
        self.health = 10
        print "Hero's heath is restored to %d!" % self.health
        time.sleep(1)

    def buy(self, item):
        if self.coins >= item.cost:
            self.coins -= item.cost
            item.apply(hero)
        else:
            print "You can't afford that!"

    def attack(self, enemy):
        if not self.alive():
            return
        rand_int = randint(1, 100)
        if rand_int <= self.crit_chance:
            print "%s attacks %s for double damage!" % (self.name, enemy.name)
            enemy.receive_damage(self.critpower)
        else:
            print "%s attacks %s." % (self.name, enemy.name)
            enemy.receive_damage(self.power)
        time.sleep(1.5)

    def receive_damage(self, points):
        rand_int = randint(1, 20)
        if self.evade >= rand_int:
            print "%s evades! No damage received."
        else:
            if (points - self.armor > 0):
                self.health -= (points - self.armor)
                print "%s received %d damage." % (self.name, points)
            elif (points - self.armor < 0):
                print "%s received no damage!" % self.name
            if self.health <= 0:
                print "%s is dead." % self.name

class Goblin(Character):
    def __init__(self):
        self.name = 'goblin'
        self.health = 6
        self.power = 2
        self.coins = 5

class Wizard(Character):
    def __init__(self):
        self.name = 'wizard'
        self.health = 8
        self.power = 1
        self.coins = 6

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print "%s swaps power with %s during attack" % (self.name, enemy.name)
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power

class Medic(Character):
    def __init__(self):
        self.name = 'medic'
        self.heal = 2
        self.heal_chance = 20
        self.coins = 6

    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name
        rand_int = randint(1,100)
        if rand_int <= heal_chance:
            self.health += self.heal
            print "%s regenerates %d health points!" % (self.name, self.heal)

class Zombie(Character):
    def __init__(self):
        self.name = 'zombie'
        self.coins = 10

    def alive(self):
        return True

    def receive_damage(self, points):
        self.health -= points
        print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s cannot die. %s is a zombie!" % (self.name, self.name)

class Shadow(Character):
    def __init__(self):
        self.name = 'shadow'
        self.health = 1
        self.vanish = 90
        self.coins = 10

    def receive_damage(self, points):
        rand_int = randint(1,100)
        if rand_int <= self.vanish:
            print "%s vanished! %s received no damage." % (self.name, self.name)
        elif rand_int > self.vanish:
            self.health -= points
            print "%s received %d damage." % (self.name, points)
        if self.health <= 0:
            print "%s is dead." % self.name

class Dragon(Character):
    def __init__(self):
        self.name = 'DRAGON'
        self.health = 20
        self.power = 4
        self.coins = 30
        self.fireball_chance = 10
        self.fireball_power = 20

    def attack(self, enemy):
        if not self.alive():
            return
        rand_int = randint(1,100)
        if self.fireball_chance >= rand_int:
            print "%s launches a fireball at %s!" % (self.name, enemy.name)
            enemy.receive_damage(fireball_power)
        elif self.fireball_chance < rand_int:
            print "%s attacks %s" % (self.name, enemy.name)
            enemy.receive_damage(self.power)
        time.sleep(1.5)    

class Troll(Character):
    def __init__(self):
        self.name = 'troll'
        self.power = 9
        self.health = 10
        self.hit_chance = 30
        self.coins = 15

    def attack(self, enemy):
        if not self.alive():
            return
        rand_int = randint(1, 100)
        if self.hit_chance >= rand_int:
            print "%s attacks %s. It's a bone-crushing blow!" % (self.name, enemy.name)
            enemy.receive_damage(self.power)
        elif self.hit_chance < rand_int:
            print "%s swings wildy with his club and misses!" % (self.name)
        time.sleep(1.5)

class Battle(object):
    def do_battle(self, hero, enemy):
        print "====================="
        print "Hero faces the %s" % enemy.name
        print "====================="
        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()
            time.sleep(1.5)
            print "-----------------------"
            print "What do you want to do?"
            print "1. Fight %s." % enemy.name
            print "2. Do nothing."
            print "3. Flee."
            print "> "
            input = int(raw_input())
            if input == 1:
                hero.attack(enemy)
            elif input == 2:
                pass
            elif input == 3:
                print "Goodbye."
                exit(0)
            else:
                print "Invalid input %r" % input
                continue
            enemy.attack(hero)
        if hero.alive():
            hero.coins += enemy.coins
            print "You defeated the %s! You collect a bounty of %d coins." % (enemy.name, enemy.coins)
            return True
        else:
            print "YOU LOSE!"
            return False

class Tonic(object):
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print "%s's health increased to %d." % (character.name, character.health)

class SuperTonic(object):
    cost = 10
    name = 'supertonic'
    def apply(self, character):
        character.health = 10
        print "%'s health increased to %d." % (character.name, character.health)

class Sword(object):
    cost = 10
    name = 'sword'
    def apply(self, hero):
        hero.power += 2
        print "%s's power increased to %d." % (hero.name, hero.power)

class JestersClub(object):
    cost = 10
    name = "jester's club"
    def apply (self, hero):
        rand_int = randint(-2, 4)
        if rand_int > 0:
            hero.power += rand_int
            print "%s's power increased by %d!" % (hero.name, rand_int)
        elif rand_int < 0:
            hero.power += rand_int
            if hero.power < 1:
                hero.power = 1
            print "%s's power decreased by %d!" % (hero.name, rand_int)
        else:
            print "The jester's club vanishes in a puff of smoke!"

class Armor(object):
    cost = 10
    name = 'armor'
    def apply(self, hero):
        hero.armor += 2
        print "%s's armor increased to %d." % (hero.name, hero.armor)

class Evade(object):
    cost = 10
    name = 'evade'
    def apply(self, hero):
        if hero.evade < 18:
            hero.evade += 2
            print "%s's evasion increased to %d." % (hero.name, hero.evade)
        else:
            print "%s has already reached maximum evasion!" % hero.name

class BrassKnuckles(object):
    cost = 10
    name = 'brass knuckles'
    def apply(self, hero):
        if hero.crit_chance < 100:
            hero.crit_chance += 10
            if hero.crit_chance > 100:
                hero.crit_chance = 100
            # print "%s's critical strike chance increased to %d%." % (hero.name, hero.crit_chance)
        elif hero.crit_chance == 100:
            print "%s has already reached maximum critical strike chance!" % hero.name        



class Shopping(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Shopping.items => [Tonic, Sword]
    items = [Tonic, SuperTonic, Sword, JestersClub, BrassKnuckles, Armor, Evade]
    def do_shopping(self, hero):
        while True:
            print "====================="
            print "Welcome to the store!"
            print "====================="
            print "You have %d coins." % hero.coins
            print "What do you want to do?"
            for i in xrange(len(Shopping.items)):
                item = Shopping.items[i]
                print "%d. buy %s (%d coins)" % (i + 1, item.name, item.cost)
            print "10. back to the goblins"
            input = int(raw_input("> "))
            if input == 10:
                break
            else:
                ItemToBuy = Shopping.items[input - 1]
                item = ItemToBuy()
                hero.buy(item)

hero = Hero()
monsters = [Goblin(), Wizard()]
battle_engine = Battle()
shopping_engine = Shopping()

for monster in monsters:
    hero_won = battle_engine.do_battle(hero, monster)
    if not hero_won:
        print "YOU LOSE!"
        exit(0)
    shopping_engine.do_shopping(hero)

print "YOU WIN!"
from collections import namedtuple



from game_items import Food_Items
from game_items import Crafting_Items
from game_items import Weapon_Items


class Hero:
    """Your typical starting hero.
    """

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon_Items[0]
        self.inventory = []
        self.inventory.append(self.weapon)



    def damage_handle(self, hp_modifier: int):
        """Subtract HP if modifier is negative,
        Heal HP up to cap (100) when modifier is positive.
        """
        health = self.health
        health += hp_modifier
        if health > 100:
            health -= (health - 100)
        elif health == 0:
            print("Oh no! You have died!")


    def item_pickup(self, item):
        self.item = item
        self.inventory.append(item)

    def item_drop(self, item):
        self.item = item
        self.inventory.remove(item)



class Monster:
    """For now the only monster in the game shall be a slime.
    """

    def __init__(self, name):
        self.name = name
        self.health = 6
        self.damage = 15

    def damage_handle(self, hp_modifier: int):      #For now monsters do not have the capability to heal themselves.
        health = self.health
        health -= hp_modifier

# SlimeA = Monster("Slime")
#
# Bob = Hero("Bob")
#
# print(Bob.weapon)
# Bob.damage_handle(-50)
# print(Bob.health)
# Bob.damage_handle(+100)
# print(Bob.health)
# print(Bob.inventory)
# Bob.item_pickup('Mayonnaise')
# print(Bob.inventory)







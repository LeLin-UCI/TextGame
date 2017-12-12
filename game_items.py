from collections import namedtuple

Food_Item = namedtuple('Common', 'name description recover price')
Crafting_Item = namedtuple('Common', 'name description price')
Weapon_Item = namedtuple('Common', 'name description sharpness durability price')



Bread = Food_Item('Bread', "You can eat this to recover some health.", 10, 5)


Broken_Hilt = Crafting_Item('Broken Hilt', "Maybe you could salvage this.", 11)


Sword = Weapon_Item('Copper Sword', "A reliable sword made from copper", 4, 10.0, 1)



Food_Items = [Bread,
                ]

Crafting_Items = [Broken_Hilt,
                  ]

Weapon_Items = [Sword,
                ]

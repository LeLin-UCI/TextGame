from random import randrange


from game_characters import Hero
from game_spawn import Monster


def game():
    """Main Program
    """
    print("Welcome to my Text Game v1.6!")
    print("As you can tell by the version #, I've been through a lot of trials already.")
    print("Still working on a lot of things such as being able to customize your starting character.")
    print("No dropping or looting mechanics exist yet either.")
    our_chars = character_list_new()
    our_chars = handle_commands(our_chars)


CONTROLS = """
Little Text Game --- Here are the controls:
    w: Move FORWARD 
    a: Move LEFT
    s: Move BACKWARD
    d: Move RIGHT
    i: Access your inventory
    f: Attack!
    v: Run!
"""


def handle_commands(C: list):


    while True:
        response = input(CONTROLS)
        if response == 'w':
            action = input(travel_up())
            if action == 'f':


        elif response == 'a':
            action = input(travel_left())

        elif response == 's':
            action = input(travel_back())

        elif response == 'd':
            action = input(travel_right())


        else:
            invalid_command(response)

def invalid_command(response):
    print("Sorry; '" + response + "' isn't a valid command. Please try again.")


def travel_up():
    possibilities = ["You travel up the road ahead of you and you run into a slime! Attack or Run?",
                     "You travel up the road ahead of you and you see nothing.",
                     "You travel up the road ahead of you and you see a bag. Loot?",
                     "There is no road ahead of you"
    ]
    return possibilities[randrange(len(possibilities))]

def travel_left():
    possibilities = ["You travel down the road you see to your left and run into a slime! Attack or Run?",
                     "You travel down the road you see to your left and you see nothing."
                     "You travel down the road you see to your left and you see a torn bag. Loot?",
                     "There is no road to the left of you"
    ]
    return possibilities[randrange(len(possibilities))]

def travel_right():
    possibilities = ["You travel down the road you see to your right and you run into a slime! Attack or Run?",
                     "You travel down the road you see to your right and you see nothing."
                     "You travel down the road you see to your right and you see a dirty bag. Loot?",
                     "There is no road to the left of you"
    ]
    return possibilities[randrange(len(possibilities))]

def travel_back():
    possibilities = ["You travel back the way you came and you run into a slime! You don't question why the road behind you has changed. Attack or Run?",
                     "You travel back the way you came and you see nothing. You don't question why the road behind you has changed."
                     "You travel back the way you came and you see a dirty bag. You don't question why the road behind you has changed. Loot?",
                     "You turn around, ready to walk back from where you came from, but are surprised to see that the path has disappeared. You don't question it."
    ]
    return possibilities[randrange(len(possibilities))]


def attack_scenario():
    


def character_list_new():
    return Hero



game()
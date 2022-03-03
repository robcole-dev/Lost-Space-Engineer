from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit import prompt

inv_slots = []

NAVIGATION = False
POWER = False
LIFE_SUPPORT = False
LIGHT_SPEED_DRIVE = False
aval_tools = ["Ductape", "Spanner", "Hammer", "Screwdriver", "String",
              "Super Glue"]


class DirectionValidator(Validator):
    """Direction validator"""
    def validate(self, document):
        text = document.text
        words = ["left", "right", "forward", "backwards"]
        if text not in words:
            raise ValidationError(message="This is not a correct direction!")


class SubSystem:
    """Sub Systems"""
    def __init__(self, system, power, fixed):
        self.system = system
        self.power = power
        self.fixed = fixed
    
    def power_change(self, system, power):
        if power is True:
            print(f"{system} is currently online")
        else:
            print(f"{system} is currently offline")


class Tools:
    """Class for tools"""
    def __init__(self, name, durability):
        """Properties for tools"""
        self.name = name
        self.durability = durability


class Inventory:
    """Class for storing Inventory"""
    def __init__(self):
        self.tools = {}

    def add_item(self, tool):
        self.tools[tool.name] = tool

    def print_inv(self):
        print('\t'.join(['Name', 'Dur']))
        for tool in self.tools.values():
            print('\t'.join([str(x) for x in [tool.name, tool.durability]]))


def directions(values):
    """directions function"""
    count = len(values)
    print(f"You have {count} directions to go...")
    print("Please choose one of the following")
    print(f"{values}")
    direction = prompt("Which way do you want to go??\n", validator=DirectionValidator())

    return direction


def tools():
    """Function to collect a random tool"""
    print("Congratulations you have found a room containing tools")
    print("You look around and find a box that looks hopefull")
    

def start_game():
    """looks for input from player to begin the adventure"""
    print("Welcome to the text adventure game Lost Space Engineer\n")
    print("The aim of the game is to explore the ship and "
          "fix any broken sub-systems")
    print("While exploring the ship you may find tools "
          "to help fix any broken systems\n")
    while True:
        play = input("Are you ready? if so type 'play'\n")

        if play_check(play):
            print("Good Luck and have fun!!")
            first_steps()


def play_check(value):
    """Checks to see if the player has enter play and it's valid"""
    try:
        if value != "play":
            raise ValueError(
                "Please type 'play' in all lowercase"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def first_steps():
    """First Steps scenario"""
    print("You have woken from stasis. However, something doesn't seem right.")
    print("After gathering your senses you stumble out the room to find lights"
          " flickering everywhere and nobody in sight.\n")
    ways = ["left", "forward", "right", "backwards"]
    direction = directions(ways)
    if direction == "left":
        print("left")
    elif direction == "forward":
        print("forward")
    elif direction == "right":
        print("right")
    elif direction == "backwards":
        print("backwards")


def main():
    start_game()


main()

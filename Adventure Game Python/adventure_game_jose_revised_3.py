# calling modules for time and random phrases
import time
import random


# defining the message timing. Every 2 seconds.
def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


# defning intro with random characters to fight with.
#         1         2         3         4         5         6         7       *
# 34567890123456789012345678901234567890123456789012345678901234567890123456789
def intro(item, character):
    print_pause("You find yourself standing in an open field, filled with "
                "grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + character + " is somewhere around "
                "here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To you right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) "
                "dagger.")


# defining the field to to go. including a condition for wrong field selection.
#         1         2         3         4         5         6         7       *
# 34567890123456789012345678901234567890123456789012345678901234567890123456789
def field(item, character):
    print_pause("\nEnter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    location = input("(Please enter 1 or 2.)\n")
    if location == '1':
        house(item, character)
    elif location == '2':
        cave(item, character)
    else:
        field(item, character)


# defining the house actions. calling a function named "fight".
#         1         2         3         4         5         6         7       *
# 34567890123456789012345678901234567890123456789012345678901234567890123456789
def house(item, character):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out"
                "steps a " + character + ".")
    print_pause("Eep! This is the " + character + "'s house!")
    print_pause("The " + character + " attacks you!")
    if "sword" in item:
        fight(item, character)
    else:
        print_pause("You feel a bit under-prepared for this, what with "
                    "only having a tiny dagger.")
        fight(item, character)


# defining the cave actions.
# if/else added to do actions if sword is on item ornot.
# appending the sword to item.
# calling a function named "field" to go gack to field,
# calles sword is on items.
#         1         2         3         4         5         6         7       *
# 34567890123456789012345678901234567890123456789012345678901234567890123456789
def cave(item, character):
    if "sword" in item:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all the good stuff."
                    "It's just an empty cave now.")
        print_pause("You walk back to the field.")
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take the sword"
                    "with you.")
        print_pause("You walk back out to the field.")
        item.append("sword")
    field(item, character)


# defining the fight scenarios, fight or escape.
# Including a condition for wrong field selection.
#         1         2         3         4         5         6         7       *
# 34567890123456789012345678901234567890123456789012345678901234567890123456789
def fight(item, character):
    fight_action = input("Would you like to (1) fight or (2) "
                         "run away?\n")
    if fight_action == '1':
        win_lose(item, character)
    elif fight_action == '2':
        print_pause("You run back into the field. Luckily, you"
                    "don't seem to have been followed.")
        field(item, character)
    else:
        play_again()


# defining the win or lose scenario.
# Verifying if sword is on items to select win or defect.
# ask to player if playing again.
#         1         2         3         4         5         6         7       *
# 34567890123456789012345678901234567890123456789012345678901234567890123456789
def win_lose(item, character):
    if "sword" in item:
        print_pause("As the " + character + " moves to attack, "
                    "you unsheath your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in "
                    "your hand as you brace yourself for the attack.")
        print_pause("But the " + character + " takes one look at "
                    "your shiny new toy and runs away!")
        print_pause("You have rid the town of the " + character + ". You "
                    "are victorious!")
        play_again()
    else:
        print_pause("You do your best...")
        print_pause("but your dagger is no match for the " + character + ".")
        print_pause("You have been defeated!")
        play_again()


# defining the function fro playing again.
# Including option for wrong selection.
#         1         2         3         4         5         6         7       *
# 34567890123456789012345678901234567890123456789012345678901234567890123456789
def play_again():
    playagain = input("Would you like to play again? (y/n)\n").lower()
    if playagain == "y":
        print_pause("Excellent! Restarting the game ...\n")
        play_game()
    elif playagain == "n":
        print_pause("Thanks for playing! See you next time.")
    else:
        play_again()


# Game by defining the main functions to be called.
# randon characters listed.
#         1         2         3         4         5         6         7       *
# 34567890123456789012345678901234567890123456789012345678901234567890123456789
def play_game():
    item = []
    character = random.choice(["dragon", "gorgon", "pirate", "troll",
                               "wicked fairie", "Udacity Instructor"])
    intro(item, character)
    field(item, character)


# Playing the game
play_game()

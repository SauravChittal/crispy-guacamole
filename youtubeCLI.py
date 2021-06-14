from numpy.random import rand
from plumbum import cli 
from pyfiglet import Figlet
import questionary as q
from questionary.prompts.text import text
from questionary import Validator, ValidationError

import termplotlib as tpl
import numpy

import random

class NameValidator(Validator):
    def validate(self, document):
        some = open("all_pokemon.txt", "r")
        all_str = some.read().replace(" ", "-").upper().split(",")
        pokemon_name = str(document.text.upper())

        if pokemon_name.__contains__("-"):
            till = pokemon_name.find("-")
            print(pokemon_name[till:])
            if pokemon_name[till + 1:].upper() == "GALAR" or pokemon_name[till + 1:].upper() == "ALOLA":
                something = ""
                if pokemon_name[till + 1:].upper() == "GALAR":
                    something = "IAN"
                else:
                    something = "N"
                one, two = pokemon_name[till + 1:], pokemon_name[:till]
                pokemon_name = one + something + "-" + two
                print("The pokemon name is " + pokemon_name)

        if pokemon_name not in all_str:
            raise ValidationError(message="Please enter an Actual Pokemon", cursor_position=len(document.text))

def print_banner(text):
    print(Figlet(font='smslant').renderText(text))

def not_pokemon_function():
    # Ironic I'm using random inside seen
    numpy.random.seed(random.randint(1, 1000))
    sample = numpy.random.normal(size=1000)
    counts, bin_edges = numpy.histogram(sample, bins=39)
    fig = tpl.figure()
    fig.hist(counts, bin_edges, grid=[15, 25], force_ascii=False)
    fig.show()
    print("Hopefully this random histogram(because I couldn't generate plot graphs) which is generated cheers you up")

def validate_pokemon(text):
    some = open("all_pokemon.txt", "r")
    all_str = some.read().replace(" ", "-").upper().split(",")
    pokemon_name = str(text.upper())

    if pokemon_name.__contains__("-"):
        till = pokemon_name.find("-")
        print(pokemon_name[till:])
        if pokemon_name[till + 1:].upper() == "GALAR" or pokemon_name[till + 1:].upper() == "ALOLA":
            something = ""
            if pokemon_name[till + 1:].upper() == "GALAR":
                something = "IAN"
            else:
                something = "N"
            one, two = pokemon_name[till + 1:], pokemon_name[:till]
            pokemon_name = one + something + "-" + two
            print("The pokemon name is " + pokemon_name)

        if pokemon_name not in all_str:
            raise ValidationError(message="Please enter an Actual Pokemon", cursor_position=len(document.text))


def pokemon_function(pokemon, oppo_pokemon, uhp=100, ohp=100):
    print(Figlet(font='barbwire', width=200).renderText("HP : " + str(ohp) + "/100"))
    print(Figlet(font='banner3', width=200).renderText(oppo_pokemon))

    print(Figlet(font='barbwire', width=200).renderText("HP : " + str(uhp) + "/100"))
    print(Figlet(font='colossal', width=200).renderText(pokemon))

    answer = q.select("Select a move", choices=["Metronome", "Metronome", "Metronome", "Metronome"]).ask()

    urandom = random.randint(10, 20)
    orandom = random.randint(10, 20)

    print("You did " + str(orandom) + " damage, however, the opponent did " + str(urandom) + " damage")

    ohp -= orandom
    if ohp < 0:
        print("You have Won. Yaaay")
        return
    uhp -= urandom
    if uhp < 0:
        print("You have lost :(")
        return
    pokemon_function(pokemon, oppo_pokemon, uhp, ohp)

def rps_function():
    randNumber = random.randint(1,3)
    companswer = "Scissor"
    if randNumber == 1:
        companswer = "Rock"
    elif randNumber == 2:
        companswer = "Paper"

    answer = q.select("Select Rock, Paper or Scissors", choices=["Rock", "Paper", "Scissor"]).ask()

    print(answer, companswer, sep=" and ")

    if answer == companswer:
        print(Figlet(font='3x5', width=1000).renderText("It was a draw unfortunately"))
    elif (answer == "Rock" and companswer == "Paper") or (answer == "Paper" and companswer == "Scissor") or (answer == "Scissor" and companswer == "Rock"):
        print(Figlet(font='3x5', width=100).renderText("Unfortunately you lost"))
    else:
        print(Figlet(font='3x5').renderText("You won yay"))
    pass

class RandomBoredThings(cli.Application):
    VERSION = "1.3"
    r_p_s = cli.Flag(['p', 'play'], help="Allows you to play Rock Paper Scissors with the computer")

    def main(self):
        print_banner("Bored Eh?")
        if self.r_p_s:
            rps_function()
            return
        answer = q.select("What would you like to do?", choices=["Play some Pokemon", "Not Play Some Pokemon"], qmark="",use_shortcuts= True, use_arrow_keys=True).ask()
        print("Oh so you want to " + answer)

        if answer == "Not Play Some Pokemon":
            not_pokemon_function()
        elif answer == "Play some Pokemon":
            pokemon = q.text("What is your favourite pokemon?", validate=NameValidator).ask()
            oppo_pokemon = q.text("What Pokemon would you like to battle against?", validate=NameValidator).ask()
            pokemon_function(pokemon, oppo_pokemon)

if __name__ == "__main__":
    RandomBoredThings()

def test_pokemon_validation():
    try:
        validate_pokemon("Hydreigon")
        validate_pokemon("hydreigon")
        validate_pokemon("HYDREIGON")
        assert True
    except:
        assert False

    try:
        validate_pokemon("Moltres-Galar")
        validate_pokemon("moltres-Galar")
        validate_pokemon("MOLTRES-GALAR")
        assert True
    except:
        assert False

    try:
        validate_pokemon("Test")
        validate_pokemon("test")
        validate_pokemon("TEST")
        assert False
    except:
        assert True

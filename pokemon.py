# project 38: Pokemon Simulation App
import random


class Pokemon:
    """Parent class of Fire, Water, Grass classes"""

    def __init__(self, name, element, health, speed):
        self.name = name.title()
        self.element = element
        self.current_health = health
        self.max_health = health
        self.speed = speed
        self.is_alive = True

    def light_attack(self, enemy):
        """The light attack will be guaranteed to do minimal damage to the enemy pokemon.
        This light attack will have a different name, depending on the elemental type of pokemon.
        However, all light attacks will appear in a list called moves."""
        damage = random.randint(15, 25)
        print(f"Pokemon {self.name} used {self.moves[0]}.")
        print(f"it dealt {damage} damage.")
        enemy.current_health -= damage

    def heavy_attack(self, enemy):
        """The heavy attack has the potential to deal massive damage"""
        damage = random.randint(0, 50)
        print(f"Pokemon {self.name} used {self.moves[1]}.")
        if damage < 10:
            print("The attack missed!!!")
        else:
            print(f"it dealt {damage} damage.")
            enemy.current_health -= damage

    def restore(self):
        """The restore move doesn't deal any damage at all but instead restores a small portion of health"""
        heal = random.randint(15, 25)
        print(f"pokemon {self.name} used {self.moves[2]}")
        print(f"it healed {heal} points")
        self.current_health += heal
        if self.current_health > self.max_health:
            self.current_health = self.max_health

    def faint(self):
        """If the pokemon health is less than or equal to zero"""
        if self.current_health <= 0:
            self.is_alive = False
            print(f"{self.name} has fainted.")
            input("PRESS 'ENTER' TO CONTINUE.")

    def show_stats(self):
        print(f"\nName of The Pokemon: {self.name}")
        print(f"Element Type: {self.element}")
        print(f"Current Health: {self.current_health}")
        print(f"Maximum Health: {self.max_health}")
        print(f"Speed: {self.speed}")


class Fire(Pokemon):
    def __init__(self, name, element, health, speed):
        super().__init__(name, element, health, speed)
        self.moves = ["Scratch", "Ember", "Light", "Fire Blast"]

    def special_attack(self, enemy):
        """This special attack deals massive damage to grass type Pokemon."""
        print(f"Pokemon {self.name} used {self.moves[3]}")
        if enemy.element == "GRASS":
            print("It's SUPER effective!")
            damage = random.randint(35, 50)
        elif enemy.element == "WATER":
            print("It's NOT VERY effective.")
            damage = random.randint(5, 10)
        else:
            damage = random.randint(10, 30)
        print(f"It dealt {damage} damage.")
        enemy.current_health -= damage

    def move_info(self):
        """Display pokemon move info"""
        print(f"\n{self.name} Moves: ")

        # Light attack
        print(f"__{self.moves[0]}__")
        print("\tAn efficient attack...")
        print("\tGuaranteed to do damage within a range of 15 to 25 damage points.")

        # Heavy attack
        print(f"__{self.moves[1]}__")
        print("\tAn risky attack...")
        print("\tCould deal damage up to 50 points or as little as 0 damage points.")

        # Restore move
        print(f"__{self.moves[2]}__")
        print("\tA restorative move...")
        print("\tGuaranteed to heal your pokemon 15 to 25 damage points.")

        # Special attack
        print(f"__{self.moves[3]}__")
        print("\tA powerful FIRE based attack...")
        print("\tGuaranteed to deal MASSIVE damage to GRASS type pokemon")


class Water(Pokemon):
    """A Water based pokemon"""
    def __init__(self, name, element, health, speed):
        super().__init__(name, element, health, speed)
        self.moves = ["Bite", "Splash", "Dive", "Water Cannon"]

    def special_attack(self, enemy):
        print(f"Pokemon {self.name} used {self.moves[3]}")
        if enemy.element == "FIRE":
            print("It's SUPER effective!")
            damage = random.randint(35, 50)
        elif enemy.element == "GRASS":
            print("It's NOT VERY effective")
            damage = random.randint(5, 10)
        else:
            damage = random.randint(10, 20)
        print(f"it dealt {damage} damage.")
        enemy.current_health -= damage

    def move_info(self):
        """Display pokemon move info"""
        print(f"\n{self.name} Moves: ")

        # Light attack
        print(f"__{self.moves[0]}__")
        print("\tAn efficient attack...")
        print("\tGuaranteed to do damage within a range of 15 to 25 damage points.")

        # Heavy attack
        print(f"__{self.moves[1]}__")
        print("\tAn risky attack...")
        print("\tCould deal damage up to 50 points or as little as 0 damage points.")

        # Restore move
        print(f"__{self.moves[2]}__")
        print("\tA restorative move...")
        print("\tGuaranteed to heal your pokemon 15 to 25 damage points.")

        # Special attack
        print(f"__{self.moves[3]}__")
        print("\tA powerful WATER based attack...")
        print("\tGuaranteed to deal MASSIVE damage to FIRE type pokemon")


class Grass(Pokemon):
    def __init__(self, name, element, health, speed):
        super().__init__(name, element, health, speed)
        self.moves = ["Vine Whip", "Wrap", "Grow", "Leaf Blade"]

    def special_attack(self, enemy):
        print(f"Pokemon {self.name} used {self.moves[3]}")
        if enemy.element == "WATER":
            print("It's SUPER effective!")
            damage = random.randint(35, 50)
        elif enemy.element == "FIRE":
            print("It's NOT VERY effective")
            damage = random.randint(5, 10)
        else:
            damage = random.randint(10, 20)
        print(f"it dealt {damage} damage.")
        enemy.current_health -= damage

    def move_info(self):
        """Display pokemon move info"""
        print(f"\n{self.name} Moves: ")

        # Light attack
        print(f"__{self.moves[0]}__")
        print("\tAn efficient attack...")
        print("\tGuaranteed to do damage within a range of 15 to 25 damage points.")

        # Heavy attack
        print(f"__{self.moves[1]}__")
        print("\tAn risky attack...")
        print("\tCould deal damage up to 50 points or as little as 0 damage points.")

        # Restore move
        print(f"__{self.moves[2]}__")
        print("\tA restorative move...")
        print("\tGuaranteed to heal your pokemon 15 to 25 damage points.")

        # Special attack
        print(f"__{self.moves[3]}__")
        print("\tA powerful GRASS based attack...")
        print("\tGuaranteed to deal MASSIVE damage to WATER type pokemon")


class Game:
    def __init__(self):
        self.pokemon_elements = ["FIRE", 'WATER', 'GRASS']
        self.pokemons_names = ["Eevee", "Snorlax", "Pikachu", "Mewtwo", "Ditto", "Squirtle", "Bulbasaur", "Gyarados", "Lapras", "Charmander", "Kyurem", "Garchomp", "Arcanine", "Luxray"]
        self.battels_won = 0

    def create_pokemon(self):
        health = random.randint(70, 100)
        speed = random.randint(1, 10)
        element = self.pokemon_elements[random.randint(0, 2)]
        name = self.pokemons_names[random.randint(0, 13)]
        if element == "FIRE":
            pokemon = Fire(name, element, health, speed)
        elif element == "WATER":
            pokemon = Water(name, element, health, speed)
        else:
            pokemon = Grass(name, element, health, speed)
        return pokemon

    def choose_pokemon(self):
        starters = []
        while len(starters) < 3:
            pokemon = self.create_pokemon()
            valid_pokemon = True
            for starter in starters:
                # check if the name or element is already used by another starter
                if starter.name == pokemon.name or starter.element == pokemon.element:
                    valid_pokemon = False
            # The created pokemon is unique
            if valid_pokemon:
                starters.append(pokemon)

        for starter in starters:
            starter.show_stats()
            starter.move_info()

        # present info to user
        print("\nProfessor Harish presents you three pokemons: ")
        print(f"(1) - {starters[0].name}")
        print(f"(2) - {starters[1].name}")
        print(f"(3) - {starters[2].name}")

        # selection of pokemon
        choice = int(input("\nSelect your pokemon by index of given pokemon: "))
        pokemon = starters[choice-1]

        return pokemon

    def get_attack(self, pokemon):
        print("\nWhat would you like to do....")
        print(f"(1) - {pokemon.moves[0]}")
        print(f"(2) - {pokemon.moves[1]}")
        print(f"(3) - {pokemon.moves[2]}")
        print(f"(4) - {pokemon.moves[3]}")
        choice = int(input("Please enter your move choice: "))

        print()
        print("-"*90)
        return choice

    def player_attack(self, move, player, computer):
        if move == 1:
            player.light_attack(computer)
        elif move == 2:
            player.heavy_attack(computer)
        elif move == 3:
            player.restore()
        elif move == 4:
            player.special_attack(computer)

        # check to see if the computer has fainted
        computer.faint()

    def computer_attack(self, player, computer):
        move = random.randint(1, 4)
        if move == 1:
           computer.light_attack(player)
        elif move == 2:
            computer.heavy_attack(player)
        elif move == 3:
            computer.restore()
        elif move == 4:
            computer.special_attack(player)

        # check to see if the player has fainted
        player.faint()

    def battle(self, player, computer):
        move = self.get_attack(player)
        # if the player pokemon is faster
        if player.speed >= computer.speed:
            # player attacks
            self.player_attack(move, player, computer)
            if computer.is_alive:
                # computer is still alive, let them attack
                self.computer_attack(player, computer)
        # if player pokemon slower
        else:
            self.computer_attack(player, computer)
            if player.is_alive:
                self.player_attack(move, player, computer)


# The main code
print("Welcome to Pokemon!")
print("Can you become the worlds greatest Pokemon Trainer???")
print("\nDon't worry! Prof Harish is here to help you on your quest.")
print("He would like to gift you your first Pokemon!")
print("Here are three potential Pokemon partners.")
input("Press Enter to choose your Pokemon!")
playing = True
while playing:
    game = Game()
    player = game.choose_pokemon()
    print(f"\nCongratulations Trainer,You have choosen {player.name}.")
    input(f"\nYour journey with {player.name} begins now...Press Enter")

    while player.is_alive:
        computer = game.create_pokemon()
        print(f"\nOH NO! A wild {computer.name} has approached!")
        computer.show_stats()

        while computer.is_alive and player.is_alive:
            game.battle(player, computer)

            if computer.is_alive and player.is_alive:
                player.show_stats()
                computer.show_stats()
                print("-"*90)
        if player.is_alive:
            game.battels_won += 1

    # player has finally fainted
    print(f"\nPoor {player.name} has fainted...")
    print(f"But not before defeating {game.battels_won} pokemon!")

    # Ask user if they want to play again

    choice = input("Would you like to play again (y/n): ").lower()
    if choice != 'y':
        playing = False
        print("Thank you for playing pokemon!")










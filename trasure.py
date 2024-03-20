import random

class Treasure:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def describe(self):
        return f"{self.name}: Worth {self.value} coins"
    
    def collect(self):
        return self.value

class Gold(Treasure):
    def __init__(self):
        super().__init__("Gold", random.randint(10, 100))

class Gem(Treasure):
    def __init__(self):
        super().__init__("Gem", random.randint(50, 200))

class Artifact(Treasure):
    def __init__(self):
        super().__init__("Artifact", random.randint(100, 500))

class TreasureHuntGame:
    def __init__(self, num_treasures):
        self.treasures = []
        for _ in range(num_treasures):
            treasure_type = random.choice([Gold, Gem, Artifact])()
            self.treasures.append(treasure_type)

    def play(self):
        total_value = 0
        print("Welcome to the Treasure Hunt Game!")
        print("Find and collect treasures to earn coins.")
        for treasure in self.treasures:
            print(f"You found a {treasure.describe()}")
            total_value += treasure.collect()
        print(f"\nCongratulations! You collected {total_value} coins in total.")

game = TreasureHuntGame(5)  # Generate 5 random treasures
game.play()

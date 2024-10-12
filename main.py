class Player:
    def __init__(self, name):
        self.name = name

    def main_skill(self):
        raise NotImplementedError()

class Forward(Player):
    def __init__(self, name):
        super().__init__(name)

    def main_skill(self):
        return f"{self.name} отлично забивает голы!"

class Defender(Player):
    def __init__(self, name):
        super().__init__(name)

    def main_skill(self):
        return f"{self.name} отлично справляется с захватами и блокировкой бросков!"

class Midfielder(Player):
    def __init__(self, name):
        super().__init__(name)

    def main_skill(self):
        return f"{self.name} хорош в создании игровых моментов и пасах!"

class Goalkeeper(Player):
    def __init__(self, name):
        super().__init__(name)

    def main_skill(self):
        return f"{self.name} отлично отражает удары по воротам!"

players = [
    Forward("Cristiano Ronaldo"),
    Defender("Leonel Messi"),
    Midfielder("Zinedine Zidane"),
    Goalkeeper("Lev Yashin")
]

for player in players:
    print(player.main_skill())

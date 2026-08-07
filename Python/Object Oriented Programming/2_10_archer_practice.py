class Archer:
    def __init__(self, name, health, num_arrows):
        self.name = name
        self.health = health
        self.num_arrows = num_arrows

    def take_hit(self):
        self.health -= 1
        if self.health == 0:
            raise Exception(f"{self.name} is dead")

    def shoot(self, target):
        self.target = target
        if self.num_arrows == 0:
            raise Exception(f"{self.name} can't shoot")
        else:
            self.num_arrows -= 1
            print(f"{self.name} shoots {self.target}")
            Archer.take_hit(self.target)

    # don't touch below this line

    def get_status(self):
        return self.name, self.health, self.num_arrows

    def print_status(self):
        print(f"{self.name} has {self.health} health and {self.num_arrows} arrows")

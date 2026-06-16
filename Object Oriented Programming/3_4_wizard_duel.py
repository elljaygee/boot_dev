class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.name = name
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.mana = self.__intelligence * 10
        self.health = self.__stamina * 100

    def cast_fireball(self, target, fireball_cost, fireball_damage):
        if self.mana < fireball_cost:
            raise Exception(f"{self.name} cannot cast fireball")
        else:
            self.mana -= fireball_cost
            target.get_fireballed(fireball_damage)

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def get_fireballed(self, fireball_damage):
        fireball_damage -= self.__stamina # 'fireball_damage' is the parameter, '__stamina' is an instance attribute
        self.health -= fireball_damage     # 'health' is an instance attribute, 'fireball_damage' is the modified parameter

    def drink_mana_potion(self, potion_mana):
        potion_mana += self.__intelligence # 'potion_mana' is the parameter, '__intelligence' is an instance attribute
        self.mana += potion_mana           # 'mana' is an instance attribute, 'potion_mana' is the modified parameter

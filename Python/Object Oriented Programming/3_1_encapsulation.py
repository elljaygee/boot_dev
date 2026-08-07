class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.name = name
        # private properties:
        self.__stamina = stamina
        self.__intelligence = intelligence
        
        self.health = self.__stamina * 100
        self.mana = self.__intelligence * 10

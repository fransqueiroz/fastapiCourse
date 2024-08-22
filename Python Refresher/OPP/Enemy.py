class Enemy:

    """
    Default/Empty Constructor
    Automatically created if no constructor is found
    def __init__(self):
        pass
    """

    """
    No Argument Constructor
    Automatically created if no constructor is found
    def __init__(self):
        print('New enemy created with no starging values')
    """

    """"
    Parameter Constructor
    """

    def __init__(
        self,
        type_of_enemy: str,
        health_points: int = 10,
        attack_damage: int = 1
    ):
        self.type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage

    def talk(self):
        print(f"I'm an {self.type_of_enemy}. Be prepared to figth!")

    def walk_forward(self):
        print(f"{self.type_of_enemy} moves closer to you")

    def attack(self):
        print(f"{self.type_of_enemy} attacks you for {self.attack_damage} damage")
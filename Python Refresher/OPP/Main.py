from Enemy import *

zombie = Enemy(
    type_of_enemy="Zombie",
    health_points=15,
    attack_damage=26
)

zombie.talk()
zombie.walk_forward()
zombie.attack()
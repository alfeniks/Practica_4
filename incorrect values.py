import random

class Gladiator:
    def __init__(self, alias, vitality=100, shield=50, stamina=100):
        self.alias = alias
        self.vitality = max(0, min(vitality, 100))  
        self.shield = max(0, min(shield, 50))
        self.stamina = max(0, min(stamina, 100))

    def strike(self, opponent):
        if self.stamina > 0:
            harm = random.randint(10, 30) if opponent.shield > 0 else random.randint(0, 10)
            opponent.vitality = max(0, opponent.vitality - harm)  # предотвращаем отрицательные значения
            self.stamina = max(0, self.stamina - 10)
        else:
            harm = random.randint(0, 10)
            opponent.vitality = max(0, opponent.vitality - harm)

    def guard(self):
        if self.shield > 0:
            self.vitality = max(0, self.vitality - random.randint(0, 20))
            self.shield = max(0, self.shield - random.randint(0, 10))
        else:
            self.vitality = max(0, self.vitality - random.randint(10, 30))
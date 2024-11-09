import unittest
from gladiator import Gladiator

class TestGladiator(unittest.TestCase):
    def setUp(self):
        self.gladiator_a = Gladiator("Gladiator A")
        self.gladiator_b = Gladiator("Gladiator B")

    def test_starting_conditions(self):
        self.assertEqual(self.gladiator_a.vitality, 100)
        self.assertEqual(self.gladiator_a.shield, 50)
        self.assertEqual(self.gladiator_a.stamina, 100)

    def test_strike_effects(self):
        original_vitality = self.gladiator_b.vitality
        original_stamina = self.gladiator_a.stamina
        self.gladiator_a.strike(self.gladiator_b)
        
        # проверяем, правильно ли уменьшись выносливость и здоровье
        self.assertTrue(self.gladiator_b.vitality <= original_vitality)
        self.assertTrue(self.gladiator_a.stamina <= original_stamina - 10)

    def test_guard_action(self):
        self.gladiator_a.guard()
        self.assertTrue(0 <= self.gladiator_a.vitality <= 100)
        self.assertTrue(0 <= self.gladiator_a.shield <= 50)

    def test_guard_without_shield(self):
        self.gladiator_a.shield = 0
        starting_vitality = self.gladiator_a.vitality
        self.gladiator_a.guard()
        
        self.assertLess(self.gladiator_a.vitality, starting_vitality)

    def test_values_within_limits(self):
        # проверка что атрибуты в допустимых пределах
        self.gladiator_a.vitality = -20
        self.gladiator_a.shield = -10
        self.gladiator_a.stamina = -5

        self.assertGreaterEqual(self.gladiator_a.vitality, 0)
        self.assertGreaterEqual(self.gladiator_a.shield, 0)
        self.assertGreaterEqual(self.gladiator_a.stamina, 0)

if __name__ == '__main__':
    unittest.main()
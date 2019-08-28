import unittest
from investigation import investigate

class Test_Investigation(unittest.TestCase):
    def setUp(self):
        self.solution = ('2','4','3')

    def test_return_any_when_all_differents(self):
        self.assertIn(investigate(('1', '1', '1'), self.solution), [1, 2, 3])
        self.assertIn(investigate(('3', '2', '4'), self.solution), [1, 2, 3])
        self.assertIn(investigate(('4', '3', '2'), self.solution), [1, 2, 3])

    def test_return_1_or_3_when_assassin_or_weapon(self):
        self.assertIn(investigate(('3', '4', '4'), self.solution), [1, 3])
        self.assertIn(investigate(('6', '4', '7'), self.solution), [1, 3])

    def test_return_1_when_assassin(self):
        self.assertEqual(investigate(('5','4','3'),self.solution),1)

    def test_return_2_when_place(self):
        self.assertEqual(investigate(('2','1','3'),self.solution),2)

    def test_return_3_when_weapon(self):
        self.assertEqual(investigate(('2','4','1'),self.solution),3)

    def test_return_1_or_2_when_assassin_or_place(self):
        self.assertIn(investigate(('1', '1', '3'), self.solution), [1, 2])
        self.assertIn(investigate(('3', '2', '3'), self.solution), [1, 2])

    def test_return_2_or_3_when_place_or_weapon(self):
        self.assertIn(investigate(('2', '3', '4'), self.solution), [2, 3])
        self.assertIn(investigate(('2', '1', '5'), self.solution), [2, 3])


if __name__ == '__main__':
    unittest.main()

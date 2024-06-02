import unittest
from trtable.truthtable import TruthTable


class TestMethodsTruthTable(unittest.TestCase):
    def test_generate_combinations_method(self):
        variables = ['A', 'B']
        combinations = TruthTable._generate_combinations(variables)
        expected = [{'A': True, 'B': True},
                    {'A': True, 'B': False},
                    {'A': False, 'B': True},
                    {'A': False, 'B': False}]
        self.assertCountEqual(combinations, expected)
        self.assertTrue(all(combinations.__contains__(combination) for combination in expected))

    def test_generate_combinations_with_empty_variables_raises_error(self):
        variables = []
        with self.assertRaises(ValueError):
            TruthTable._generate_combinations(variables)

    def test_generate_combinations_with_None_raises_error(self):
        variables = None
        with self.assertRaises(ValueError):
            TruthTable._generate_combinations(variables)

    def test_generate_combinations_with_one_variable(self):
        variables = ['A']
        combinations = TruthTable._generate_combinations(variables)
        expected = [{'A': True}, {'A': False}]
        self.assertCountEqual(combinations, expected)
        self.assertTrue(all(combinations.__contains__(combination) for combination in expected))

    def test_generate_combinations_with_three_variables(self):
        variables = ['A', 'B', 'C']
        combinations = TruthTable._generate_combinations(variables)
        expected = [{'A': True, 'B': True, 'C': True},
                    {'A': True, 'B': True, 'C': False},
                    {'A': True, 'B': False, 'C': True},
                    {'A': True, 'B': False, 'C': False},
                    {'A': False, 'B': True, 'C': True},
                    {'A': False, 'B': True, 'C': False},
                    {'A': False, 'B': False, 'C': True},
                    {'A': False, 'B': False, 'C': False}]
        self.assertCountEqual(combinations, expected)
        self.assertTrue(all(combinations.__contains__(combination) for combination in expected))


if __name__ == '__main__':
    unittest.main()

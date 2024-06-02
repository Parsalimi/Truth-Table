import random
import unittest
import re

from trtable.expression import Expression


def unnormalize_expression(expression: str) -> str:
    """
        A function that mutates a logical expression by replacing a random number of the following:
        - '∧' for either 'and' or '^'
        - '∨' for either 'or' or 'v'
        - '→' for either 'implies' or '->'
        - '↔' for either 'iff' or '<->'
        - '¬' for either 'not', '!', or '~'
        - '⊕' for either 'xor'
        :precondition: The expression should be normalized (not checked)
        :param expression: The expression to unnormalize
        :return: The unnormalized expression
        :postcondition: The expression will be unnormalized
    """
    equivalents = {
        '∧': ['and', '^'],
        '∨': ['or', 'v'],
        '→': ['implies', '->'],
        '↔': ['iff', '<->'],
        '¬': ['not', '!', '~'],
        '⊕': ['xor']
    }
    for _ in range(random.randint(1, len(equivalents.keys()))):
        key = random.choice(list(equivalents.keys()))
        value = random.choice(equivalents[key])
        expression = expression.replace(key, value)
    return expression


def mutate_expression(expression: str) -> str:
    """
        A function that mutates a logical expression by adding a random number of non-relevant characters
        :precondition: The expression should be normalized (not checked)
        :param expression: The expression to mutate
        :return: The mutated expression
        :postcondition: The expression will be mutated
    """
    for _ in range(random.randint(1, 10)):
        mutator = random.choice(
            ['#', '@', '$', '%', '&', '*', '_', '+', '-', '=', '[', ']', '{', '}', '|', '\\', ':',
             ';', '"', "'", ',', '.', '?', '/'])
        slice_index = random.randint(0, len(expression))
        expression = (expression[:slice_index]
                      + mutator + expression[slice_index:])
    return expression


def mutate_expression_with_invalid_parentheses(expression: str) -> str:
    """
        A function that either adds or removes a random number of parentheses with the condition being that
        the number of added and removed parentheses should not be equal to not cause an expression
        to accidentally become valid
        :precondition: The expression should be normalized (not checked)
        :param expression: The expression to mutate
        :return: The mutated expression
        :postcondition: The expression will be mutated
    """
    for _ in range(random.randint(1, 10)):
        if random.choice([True, False]):
            finding = random.choice(['(', ')'])
            indexes_of = [i for i, char in enumerate(expression) if char == finding]
            expression.replace(finding, '')
        else:
            slice_index = random.randint(0, len(expression))
            expression = (expression[:slice_index]
                          + random.choice(['(', ')']) + expression[slice_index:])


def populate_expression_placeholders_with_random_characters(base_expression: str) -> tuple[list[str], str]:
    """
        A function that replaces the placeholders in the expression with random characters
        :param base_expression: The expression with placeholders in the form '*X*'
        :return: A tuple containing the list of variables and the expression with the placeholders replaced
        :postcondition: The placeholders will be replaced with random characters
    """
    regex = r"\*([A-Z])\*"
    variables = []
    while match := re.search(regex, base_expression):
        random_choice = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
        base_expression = base_expression.replace(match.group(0), random_choice, 1)
        variables.append(random_choice)
    return list(set(variables)), base_expression


class TestMethodsExpression(unittest.TestCase):
    def testNormalizationOfTheExpressionsWorks(self):
        for i in range(100):
            base_expression = "((P∧Q)→(¬R∨S))↔((T∧U)∨(V→(¬W⊕X)))"
            mutant = unnormalize_expression(base_expression)
            expr = Expression(mutant)
            self.assertEqual(expr.expression, base_expression)

    def testExpressionContainingInvalidCharacters(self):
        for _ in range(100):
            with self.assertRaises(ValueError):
                Expression(mutate_expression("((P∧Q)→(¬R∨S))↔((T∧U)∨(V→(¬W⊕X)))"))

    def testExpressionContainingInvalidParentheses(self):
        for _ in range(100):
            with self.assertRaises(ValueError):
                base = "((P∧Q)→(¬R∨S))↔((T∧U)∨(V→(¬W⊕X)))"
                mutant = mutate_expression(base)
                Expression(mutant)

    def testExpressionCanCorrectlyIdentifyVariables(self):
        for i in range(100):
            base_expression = "((*X*∧*X*)→(¬*X*∨*X*))↔((*X*∧*X*)∨(*X*→(¬*X*⊕*X*)))"
            expected, expression = populate_expression_placeholders_with_random_characters(base_expression)
            expr = Expression(expression)
            result = expr.get_variables()
            self.assertCountEqual(expected, result)
            self.assertTrue(all(result.__contains__(var) for var in expected))


if __name__ == '__main__':
    unittest.main()

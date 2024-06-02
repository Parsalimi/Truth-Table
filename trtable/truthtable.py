from typing import Union

from trtable.expression import Expression


class TruthTable:
    def __init__(self, expression: Union[str, Expression]):
        """
        The constructor for the Table class
        :param expression: The expression to be converted into a truth table
                            This can be a string or an Expression object
        """
        if isinstance(expression, str):
            try:
                self.expression = Expression(expression)
            except ValueError as e:
                raise ValueError(f"Invalid expression: {e}")
        else:
            self.expression = expression

        self.rows = {}
        # Here the keys will be the combinations of the variables and the value will be a list of the
        # key (expression) - results pairs => {key (combination): [{key (expression): value}, {key: value}, ...], ...}
        # here the values will be boolean values (True or False)

        self._generate_table()

    def _generate_table(self):
        """
        Generates the truth table from the expression
        """
        assert self.expression is not None, "Expression is not defined"
        assert self.rows is not None, "Rows is not defined"

        # get the variables from the expression
        variables = self.expression.get_variables()

        # generate the combinations of the variables
        combinations = self._generate_combinations(variables)

        # get the sub-expressions from the expression
        sub_expressions = self.expression.get_sub_expressions()

        # generate the rows
        for combination in combinations:
            row = {}
            for variable in variables:
                row[variable] = combination[variable]
            for sub_expression in sub_expressions:
                row[sub_expression] = self.expression.evaluate(sub_expression, row)
            self.rows[combination] = row

    @staticmethod
    def _generate_combinations(variables: list[str]) -> list[dict[str, bool]]:
        """
        pre: variables is not None and len(variables) > 0
        Generates the combinations of the variables
        :param variables: The variables to generate the combinations from
        :return: The combinations of the variables
        """
        if not variables or len(variables) == 0:
            raise ValueError("No variables provided")
        combinations = []
        for i in range(2 ** len(variables)):
            combination = {}
            for j, variable in enumerate(variables):
                combination[variable] = bool(i & (1 << j))
            combinations.append(combination)
        return combinations

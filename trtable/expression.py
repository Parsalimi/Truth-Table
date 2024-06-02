class Expression:
    def __init__(self, expression: str):
        self.expression = expression
        self.__normalize_expression()
        self.variables = None
        self.get_variables()
        self.__validate_expression()

    def get_variables(self) -> list[str]:
        """
        Returns the variables in the expression
        :param expression: The expression to get the variables from (only if being called as a static method)
        :return: The variables in the expression
        """
        assert self.expression is not None, "Expression is not defined"
        if self.variables is not None:
            return self.variables

        variables = list(set(var for var in self.expression.strip() if var.isalpha()))
        return variables

    def __normalize_expression(self):
        """
        Normalize the expression to use the following symbols:
        - '∧' for 'and' (substitute 'and' and '^' for '∧')
        - '∨' for 'or'  (substitute 'or' and 'v' for '∨')
        - '→' for 'implies'  (substitute 'implies' and '->' for '→')
        - '↔' for 'iff'  (substitute 'iff' and '<->' for '↔')
        - '¬' for 'not'  (substitute 'not', '!', and '~' for '¬')
        - '⊕' for 'xor'  (substitute 'xor' for '⊕')
        """
        assert self.expression is not None, "Expression is not defined"
        self.expression = self.expression.replace(" ", "")
        self.expression = self.expression.replace("xor", "⊕")  # always keep before or as it contains 'or'
        self.expression = self.expression.replace("and", "∧").replace("^", "∧")
        self.expression = self.expression.replace("or", "∨").replace("v", "∨")
        self.expression = self.expression.replace("iff", "↔").replace("<->", "↔")
        # always keep before implies as it contains '->'
        self.expression = self.expression.replace("implies", "→").replace("->", "→")
        self.expression = (self.expression.replace("not", "¬")
                           .replace("!", "¬").replace("~", "¬"))



    def __validate_expression(self):
        """
            Method to validate that the expression is valid (i.e. contains no invalid characters)
            and has the correct number of parentheses
        """
        assert self.expression is not None, "Expression is not defined"
        counter = 0
        for char in self.expression:
            if char not in ['∧', '∨', '→', '↔', '¬', '⊕', '(', ')'] and not char.isalpha():
                raise ValueError(f"Invalid character in expression: {char}")

            if char == '(':
                counter += 1

            elif char == ')':
                counter -= 1

            if counter < 0:
                raise ValueError("Invalid expression: Too many closing parentheses")
        if counter != 0:
            raise ValueError("Invalid expression: Parentheses do not match")

from tools import *
from prettytable import PrettyTable
# → ← ⇐ ⇒ ⇔ ↔ ≡ ∧ ∨

lowercase = 'abcdefghijklmnopqrstuvwxyz'

class Main:
    equation = []
    table = []

# This Function is to Check How many variable used in the entry
def VariableTables():
    used_variables = []
    variable_counter = 0
    for char in Main.equation:
        if char in lowercase and char not in used_variables:
            variable_counter += 1
            used_variables.append(char)

    row = 2**variable_counter
    for round in range(1, len(used_variables) + 1):
        columnContent = ""
        turn = 2**(round-1)
        for repeat in range(0, turn): 
            columnContent += "T"*int((row / round)/2)
            columnContent += "F"*int((row / round)/2)
        Main.table.append([used_variables[round - 1],columnContent])

def CountParentheses():
    openParenthesesCounter = 0
    closeParenthesesCounter = 0
    for char in Main.equation:
        if char == '(':
            openParenthesesCounter += 1
        elif char == ')':
            closeParenthesesCounter += 1
    
    if openParenthesesCounter == closeParenthesesCounter:
        counter = openParenthesesCounter
        return counter
    else:
        print(ColoredNotification(f"You have opened: {openParenthesesCounter} Parentheses and Closed {closeParenthesesCounter}", "red"))
        Wait()

def PrintFinalTable():
    table = PrettyTable()
    table.field_names = [i[0] for i in Main.table]
    for i in range(len(Main.table[0][1])):
        row = [j[1][i] for j in Main.table]
        colored_row = []
        for cell in row:
            if cell == 'T':
                colored_row.append(ColoredNotification(cell, 'green'))
            elif cell == 'F':
                colored_row.append(ColoredNotification(cell, 'red'))
            else:
                colored_row.append(cell)
        table.add_row(colored_row)
    print(table)

def AddParenthesesToTable():
    for index, item in enumerate(Main.equation):
        if item == ')':
            for i in range(index, -1, -1):
                if Main.equation[i] == '(':
                    result = AddToTable(Main.equation[i+1: index])
                    lenght = index - i + 1
                    for j in range(0, lenght-1):
                        Main.equation.pop(i)
                    Main.equation[i] = f'({result[0]})'
                    break

 # Remove the Outest Parentheses
def RemoveOutestParenthese(entry: str):
    if entry[0] == '(':
        entry = entry[1:-1]    
    
    return entry

def AddToTable(Eq: list):
    ### PRIORITY ###
    # ( ... )
    # ~
    # ∧ ∨
    # → ↔

    index = 0
    while index < len(Eq):
        if Eq[index] == "~":
            var = Eq[index + 1]
            resultColumn = ""
            for column in Main.table:
                if column[0] == var:
                    for thing in column[1]:
                        if thing == 'T':
                            resultColumn += 'F'
                        else:
                            resultColumn += 'T'

            Main.table.append([f'~{var}',resultColumn])

            Eq.pop(index)
            Eq[index] = f'~{var}'
        
        index += 1

    index = 0
    while index < len(Eq):
        if Eq[index] == "∧":
            var1 = RemoveOutestParenthese(Eq[index - 1])
            var2 = RemoveOutestParenthese(Eq[index + 1])
            var1Column = ""
            var2Column = ""
            resultColumn = ""
            for column in Main.table:
                if column[0] == var1:
                    var1Column = column[1]
                if column[0] == var2:
                    var2Column = column[1]
            for i in range(len(var1Column)):
                if var1Column[i] == 'T' and var2Column[i] == 'T':
                    resultColumn += 'T'
                elif var1Column[i] == 'T' and var2Column[i] == 'F':
                    resultColumn += 'F'
                elif var1Column[i] == 'F' and var2Column[i] == 'T':
                    resultColumn += 'F'
                elif var1Column[i] == 'F' and var2Column[i] == 'F':
                    resultColumn += 'F'

            Main.table.append([f'{Eq[index - 1]}∧{Eq[index + 1]}', resultColumn])

            Eq[index - 1] = f'{Eq[index - 1]}∧{Eq[index + 1]}'
            for i in range(0, 2):
                Eq.pop(index)

        elif Eq[index] == "∨":
            # Add some ∨ to table
            var1 = RemoveOutestParenthese(Eq[index - 1])
            var2 = RemoveOutestParenthese(Eq[index + 1])
            var1Column = ""
            var2Column = ""
            resultColumn = ""
            for column in Main.table:
                if column[0] == var1:
                    var1Column = column[1]
                if column[0] == var2:
                    var2Column = column[1]
            for i in range(len(var1Column)):
                if var1Column[i] == 'T' and var2Column[i] == 'T':
                    resultColumn += 'T'
                elif var1Column[i] == 'T' and var2Column[i] == 'F':
                    resultColumn += 'T'
                elif var1Column[i] == 'F' and var2Column[i] == 'T':
                    resultColumn += 'T'
                elif var1Column[i] == 'F' and var2Column[i] == 'F':
                    resultColumn += 'F'

            Main.table.append([f'{Eq[index - 1]}∨{Eq[index + 1]}', resultColumn])

            Eq[index - 1] = f'{Eq[index - 1]}∨{Eq[index + 1]}'
            for i in range(0, 2):
                Eq.pop(index)

        index += 1

    index = 0
    while index < len(Eq):
        if Eq[index] == "→":
            var1 = RemoveOutestParenthese(Eq[index - 1])
            var2 = RemoveOutestParenthese(Eq[index + 1])
            var1Column = ""
            var2Column = ""
            resultColumn = ""
            for column in Main.table:
                if column[0] == var1:
                    var1Column = column[1]
                if column[0] == var2:
                    var2Column = column[1]
            for i in range(len(var1Column)):
                if var1Column[i] == 'T' and var2Column[i] == 'T':
                    resultColumn += 'T'
                elif var1Column[i] == 'T' and var2Column[i] == 'F':
                    resultColumn += 'T'
                elif var1Column[i] == 'F' and var2Column[i] == 'T':
                    resultColumn += 'F'
                elif var1Column[i] == 'F' and var2Column[i] == 'F':
                    resultColumn += 'T'

            Main.table.append([f'{Eq[index - 1]}→{Eq[index + 1]}', resultColumn])

            Eq[index - 1] = f'{Eq[index - 1]}→{Eq[index + 1]}'
            for i in range(0, 2):
                Eq.pop(index)

        elif Eq[index] == "↔":
            var1 = RemoveOutestParenthese(Eq[index - 1])
            var2 = RemoveOutestParenthese(Eq[index + 1])
            var1Column = ""
            var2Column = ""
            resultColumn = ""
            for column in Main.table:
                if column[0] == var1:
                    var1Column = column[1]
                if column[0] == var2:
                    var2Column = column[1]
            for i in range(len(var1Column)):
                if var1Column[i] == 'T' and var2Column[i] == 'T':
                    resultColumn += 'T'
                elif var1Column[i] == 'T' and var2Column[i] == 'F':
                    resultColumn += 'F'
                elif var1Column[i] == 'F' and var2Column[i] == 'T':
                    resultColumn += 'F'
                elif var1Column[i] == 'F' and var2Column[i] == 'F':
                    resultColumn += 'T'

            Main.table.append([f'{Eq[index - 1]}↔{Eq[index + 1]}', resultColumn])

            Eq[index - 1] = f'{Eq[index - 1]}↔{Eq[index + 1]}'
            for i in range(0, 2):
                Eq.pop(index)
        index += 1
                    
    return Eq


####################
### MAIN PROGRAM ###
####################

flag = True
while flag:
    ClearTerminal()
    print(ColoredNotification("TRUTH TABLE\nCopy these if Needed: → ↔ ∧ ∨ ~", 'cyan'))
    entry = input("Please enter: ")
    entry = entry.replace(" ", "") # remove gaps
    Main.equation = list(entry)
    VariableTables()
    for round in range(0, CountParentheses()):
        AddParenthesesToTable()
    while len(Main.equation) > 1:
        result = AddToTable(Main.equation)
        Main.equation = result
    PrintFinalTable()
    Wait()


from tools import *
# → ← ⇐ ⇒ ⇔ ↔ ≡ ∧ ∨

lowercase = 'abcdefghijklmnopqrstuvwxyz'

# This Function is to Check How many variable used in the entry
def CheckHowManyVariableUsed(entry: list):
    variable_counter = 0
    for char in entry:
        if char in lowercase:
            variable_counter += 1
    return variable_counter

# MAIN PROGRAM #
eqution = ['p','∧','q','∨','r']
table = []

flag = True
while flag:
    ClearTerminal()
    print(ColoredNotification("→ ← ∧ ∨", "green"))
    #entry = input("Please enter: ")
    #entry = entry.replace(" ", "") # remove gaps
    # How many variable
    countOfVariables = CheckHowManyVariableUsed(eqution)
    row = 2**countOfVariables
    for round in range(1, countOfVariables + 1):
        columnContent = ""
        for repeat in range(0, round): 
            columnContent += "T"*int((row / round)/2)
            columnContent += "F"*int((row / round)/2)
        table.append(columnContent)

    print(table)
    Wait()


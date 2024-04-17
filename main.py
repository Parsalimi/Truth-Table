from os import system
# -> ~ <-> ∧ ∨
# p ∨ q
lowercase = 'abcdefghijklmnopqrstuvwxyz'

# This Function is to Check How many variable used in the entry
def CheckHowManyVariableUsed(entry: str):
    variable_counter = 0
    for char in entry:
        if char in lowercase:
            variable_counter += 1
    return variable_counter


entry = input("Please enter: ")
entry = entry.replace(" ", "") # remove gaps
CheckHowManyVariableUsed(entry)

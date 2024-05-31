from ttg import Truths
from tools import *
#print(ttg.Truths(['p', 'q', 'r'],['p or q and r => r']))

lowercase = 'abcdefghijklmnopqrstuvwxyz'

def FindUsedVariables(entry: list):
    used_variables = []
    variable_counter = 0
    for char in entry:
        if char in lowercase and char not in used_variables:
            variable_counter += 1
            used_variables.append(char)

    return used_variables

print(Truths(FindUsedVariables()))


#TFTFTFTF
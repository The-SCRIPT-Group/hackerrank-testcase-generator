"""
Add functions that are going to have your input generation logic here.
Let these functions return the string we need to write to file, and the name of the zip file to be generated.
"""

from random import randint, choice


def inputLogic():
    return "meow", 'nyan'


def bov1():
    var = "".join([choice("DOPE") for _ in range(randint(0, 10000))])
    return str(len(var)) + "\n" + var, 'bov1'

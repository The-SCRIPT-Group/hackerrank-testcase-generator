'''
Add functions that are going to have your input and output generation logic here.
Let both these functions return a dictionary in which value related to key 'string' is the string we need to write to
file.
Other key-value pairs specific to each question so that we don't have to decipher that string again in output logic,
can just pass the dict to output logic as a parameter. So instead of say reading all the values in an array from a 
string, we can simply create that array while we're randomly creating values to put into input string and pass that
to the output logic.
'''

from random import randint


def inputLogic():
    return {'string': 'meow', 'arg': 'nyaa'}


def outputLogic(testDict):
    return 'result'

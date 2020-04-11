# hackerrank-testcase-generator

generating random testcases for questions on hackerrank.meow.

## How to use

* Write function for input generation in logicfile, py
    - The function should return a string, that is the input string, and the name of the zip file to be generated
    - Make sure they're returned in the same order
    - Do not change the name of zip, return static string

* Edit testcase_generator.py to actually make test cases
  + To just print text instead of generating zip file, set `to_write` to `False` . Set to `True` to generate zip file
  + Set the path of folder where we are gonna write input and output files and save zip file in `testcase_folder` 
    - Make sure the folder contains two folders `input` and `output` inside it
  + To generate output, give command to execute (e.g. `python` ) along with path to solution file (e.g. `/home/solution.py` )
    - Will probably have to use a bash script or use compiled versions for cpp / java


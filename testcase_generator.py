import logicfile
import zipfile
import os
from subprocess import Popen, PIPE, STDOUT

to_write = False

for i in range(1):
    # generate input string by doing stuff
    test, name = logicfile.inputLogic()

    if to_write:
        f = open(r'path/to/folder/input' + str(i) + '.txt', 'w')
        f.write(test)
    else:
        print('\ninput :\n', test, sep='\n')

    # generate a string value res which is output string by passing input string to solution file
    res = (
        Popen(
            ['command', 'path/to/solution/file'],
            stdout=PIPE,
            stdin=PIPE,
            stderr=STDOUT,
        ).communicate(input=bytes(test, 'utf-8'))[0]
    ).decode('utf-8')

    if to_write:
        f = open(r'path/to/output/output' + str(i) + '.txt', 'w')
        f.write(res)
    else:
        print('\noutput :\n', res, sep='\n')

if to_write:
    # write all test cases (input and output) to zipfile
    with zipfile.ZipFile(f'path/to/{name}.zip', 'w', zipfile.ZIP_DEFLATED) as zip_file:
        # walk through input folder, and write all files to zip file as 'input\inputx.txt'
        for root, directories, files in os.walk(r'path/to/input'):
            for file in files:
                zip_file.write(os.path.join(root, file), os.path.join('input', file))

        # walk through output folder, and write all files to zip file as 'output\outputx.txt'
        for root, directories, files in os.walk(r'path/to/output'):
            for file in files:
                zip_file.write(os.path.join(root, file), os.path.join('output', file))

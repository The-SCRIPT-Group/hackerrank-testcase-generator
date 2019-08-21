import logicfile
import zipfile
import os

for i in range(1):
    # generate a dictionary which has input string by doing stuff
    testDict = logicfile.inputLogic()
    test = testDict['string']

    # the weird multiline comment is just to make it easier to switch between
    # testing the logic and writing to files
    print('input :\n', test, sep='\n')
    r'''
    f = open(r'path\to\input\input' + str(i) + '.txt', 'w')
    f.write(test)
    # '''

    # generate a string value res which is output string by doing stuff
    res = logicfile.outputLogic(testDict)

    # the weird multiline comment is just to make it easier to switch between
    # testing the logic and writing to files
    print('\noutput :\n', res, sep='\n')
    r'''
    f = open(r'path\to\output\output' + str(i) + '.txt', 'w')
    f.write(res)

# write all test cases (input and output) to zipfile
with zipfile.ZipFile(r'path\to\fib.zip', 'w', zipfile.ZIP_DEFLATED) as zip_file:
    # walk through input folder, and write all files to zip file as 'input\inputx.txt'
    for root, directories, files in os.walk(r'path\to\input'):
        for file in files:
            zip_file.write(os.path.join(root, file), os.path.join('input', file))

    # walk through output folder, and write all files to zip file as 'output\outputx.txt'
    for root, directories, files in os.walk(r'path\to\output'):
        for file in files:
            zip_file.write(os.path.join(root, file), os.path.join('output', file))
# '''

import logicfile

for i in range(1):
    # generate a dictionary which has input string by doing stuff
    testDict = logicfile.inputLogic()
    test = testDict['string']

    # the weird multiline comment is just to make it easier to switch between
    # testing the logic and writing to files
    print(test)
    r'''
    f = open(r'C:\Users\ksdfg\Desktop\rsc\input\input' + str(i) + '.txt', 'w')
    f.write(test)
    '''

    # generate a string value res which is output string by doing stuff
    res = logicfile.outputLogic(testDict)

    # the weird multiline comment is just to make it easier to switch between
    # testing the logic and writing to files
    print(res)
    r'''
    f = open(r'C:\Users\ksdfg\Desktop\rsc\output\output' + str(i) + '.txt', 'w')
    f.write(res)
    '''

r'''
The format of the zip file is that it should have two folders - input (with all
the input test files) and output (with all the output test files). akhilnarang,
zip the two folders input and output (in C:\Users\ksdfg\Desktop\rsc for me)
into a single zip file that is to be uploaded.
Someone check out if there's a hackerrank api for uploading this zip file.
'''

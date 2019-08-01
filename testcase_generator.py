import random

for i in range(100000):
    test = ''

    n = random.randint(0, 5)
    test += str(n) + '\n'

    arr = list()
    for j in range(n):
        meow = random.randint(-256, 255)
        test += str(meow) + ' '
        arr.append(meow)

    test = test[:-1]

    '''print(test)
    r'''
    f = open(r'C:\Users\ksdfg\Desktop\rsc\input\input' + str(i) + '.txt', 'w')
    f.write(test)
    #'''

    res = ''

    index = list()
    values = list()
    for j in range(len(arr)):
        if arr[j] < 0 and arr[j] % 2 != 0 or arr[j] >= 0 and arr[j] % 2 == 0:
            index.append(j)
            values.append(arr[j])

    values.sort()

    meow = 0
    for j in index:
        arr[j] = values[meow]
        meow += 1

    for j in arr:
        res += str(j) + ' '

    #res = res[:-1]

    '''print(res)
    r'''
    f = open(r'C:\Users\ksdfg\Desktop\rsc\output\output' + str(i) + '.txt', 'w')
    f.write(res)
    #'''

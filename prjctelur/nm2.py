# Enter your code here. Read input from STDIN. Print output to STDOUT
import fileinput
stdin = []
[stdin.append(int(line)) for line in fileinput.input()]

def getEvens(numbers):
    temp = []
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            temp.append(numbers[i])
    return temp

def createSequence(index):
    temp = [0,1]
    n = 2
    #for i in range(2, index):
    while (temp[n-2]+temp[n-1]) < index:
        temp.append(temp[n-1]+temp[n-2])
        n+=1
    return temp

stdin.pop(0)

for index in stdin:
    fibonacciList = createSequence(int(index))
    print sum(getEvens(fibonacciList))
    

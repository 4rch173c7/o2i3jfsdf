# Enter your code here. Read input from STDIN. Print output to STDOUT
import fileinput
stdin = []
[stdin.append(int(line)) for line in fileinput.input()]

def getMulti(iteration):
    total = 0
        
            for i in range(iteration):
                        if i % 3 == 0 or i % 5 == 0:
                                        total += i
                                            
                                                return total

                                                for i in range(stdin[0]):
                                                        print getMulti(stdin[i+1])

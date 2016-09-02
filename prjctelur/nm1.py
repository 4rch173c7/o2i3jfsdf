# Enter your code here. Read input from STDIN. Print output to STDOUT
# stdin expects multiple lines and checks their sum for each line
import fileinput
stdin = []
[stdin.append(int(line)) for line in fileinput.input()]

def getMulti(iteration):
    s1 = set(range(0,iteration,3))
    s2 = set(range(0,iteration,5))
    ss = s1.union(s2)
    return sum(ss)
    
for i in range(stdin[0])
    print getMulti(stdin[i+1])
    

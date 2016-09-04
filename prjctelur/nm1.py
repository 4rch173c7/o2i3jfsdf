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

# Enter your code here. Read input from STDIN. Print output to STDOUT
import fileinput
stdin = []
[stdin.append(int(line)) for line in fileinput.input()]

for i in range(stdin[0]):
    print sum( number for number in xrange(stdin[i+1]) if not (number % 3 and number % 5) )
    
#------------------------------------------------------------------------
# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import floor
import fileinput
stdin = []
[stdin.append(int(line)) for line in fileinput.input()]

#for i in range(stdin[0]):
    #print sum( number for number in xrange(stdin[i+1]) if not (number % 3 and number % 5) )
for i in range(stdin[0]):
    total  = (3 *  (((stdin[i+1]-1)//3)  *  (((stdin[i+1]-1)//3)+1))/2)
    total += (5 *  (((stdin[i+1]-1)//5)  *  (((stdin[i+1]-1)//5)+1))/2)
    total -= (15 * (((stdin[i+1]-1)//15)  *  (((stdin[i+1]-1)//15)+1))/2)
    print total

'''
You don't need iteration at all for this problem.

Consider; the sum of all numbers from 1 to n is equal to n*(n+1)/2. Also the sum of all numbers less than n that divides d equals d times the sum of all numbers less than n/d.

So the sum of all numbers less than 1000 that divides 3 is

3*floor(999/3)*(floor(999/3)+1)/2
Likewise the sum of all numbers less than 1000 that divides 5 is

5*floor(999/5)*(floor(999/5)+1)/2
Adding the two numbers would overcount though. Since the numbers that divides both 3 and 5 would get counted twice. The numbers that divides both 3 and 5 is precisely the numbers that divides 3*5/gcd(3,5)=15/1=15.

The sum of all numbers less than 1000 that divides 15 is

15*floor(999/15)*(floor(999/15)+1)/2
So the final result is that the sum of all numbers less than 1000 that divides either 3 or 5 equals:

  3 * (floor(999/3)  *  (floor(999/3)+1))/2
+ 5 * (floor(999/5)  *  (floor(999/5)+1))/2
-15 * (floor(999/15) * (floor(999/15)+1))/2
    '''

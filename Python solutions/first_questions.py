#######################################
##                                   ##
## Solutions to hacker rank problems ##
##                                   ##
#######################################

#######################################
##                                   ##
##          Solve Me First           ##
##                                   ##
#######################################

def solveMeFirst(a,b):
   c = a + b
   return c
  
num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)


#######################################
##                                   ##
##          Simple Array Sun         ##
##                                   ##
#######################################

import sys

def simpleArraySum(n, ar):
    answer = 0
    for i in range(n):
        answer += ar[i]
    return answer

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)

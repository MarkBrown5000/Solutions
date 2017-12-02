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

#######################################
##                                   ##
##       Compare The Triplets        ##
##                                   ##
#######################################

def solve(a0, a1, a2, b0, b1, b2):
    aScores = [a0, a1, a2]
    bScores = [b0, b1, b2]
    aScore = 0
    bScore = 0
    for i in range(3):
        if(aScores[i] > bScores[i]):
            aScore += 1
        elif(aScores[i] < bScores[i]):
            bScore += 1
    return aScore, bScore

a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))
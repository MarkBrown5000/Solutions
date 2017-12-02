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

#######################################
##                                   ##
##          A Very Big Sum           ##
##                                   ##
#######################################

def aVeryBigSum(n, ar):
    answer = 0
    for i in range(n):
        answer += ar[i]
    return answer

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)

#######################################
##                                   ##
##        Diagonal Difference        ##
##                                   ##
#######################################

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
#print(a[0][0])
primaryDiag = 0
secondaryDiag = 0
#print(int(n/2))
if n % 2 != 0:
    secondaryDiag += a[int(n/2)][int(n/2)]
for i in range(n):
    for j in range(n):
        if i == j:
            primaryDiag += a[i][j]
            #print("Primary Diagonal: ", i, j)
        elif ((i < j) and (j == ((n - 1) - i))) or ((i > j) and (i == (n - 1) - j)):
            secondaryDiag += a[i][j]
            #print("Secondary Diagonal: ", i, j)
        
difference = abs(primaryDiag - secondaryDiag) 
print(difference)
#Let's learn about list comprehensions! You are given three integers x,y and z 
# representing the dimensions of a cuboid along with an integer n. Print a list of all possible 
# coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n. Here, 
# 0<=i<=x: 0<=j<=y: 0<=k<=z
# Please use list comprehensions rather than multiple loops, as a learning exercise.

#Example 
#x=1
#y=1
#z=2
#n=3
#All permutations of (i,j,k) such that 0<=i<=x,0<=j<=y,0<=k<=z are:
# (0,0,0)  sum=0
# (0,0,1)  sum=1
# (0,0,2)  sum=2
# (0,1,0)  sum=1
# (0,1,1)  sum=2
# (0,1,2)  sum=3
# (1,0,0)  sum=1
# (1,0,1)  sum=2
# (1,0,2)  sum=3
# (1,1,0)  sum=2
# (1,1,1)  sum=3
# (1,1,2)  sum=4
#The coordinates that sum to 3 are:

#This classic problem (often found on HackerRank) tests your understanding of multi-level iteration and 
# filtering using Python's list comprehensions.What the Problem AsksYou need to generate all possible 3D coordinates $[i, j, k]$ starting from 
# $[0, 0, 0]$ up to $[x, y, z]$, but with one rule: exclude any coordinate where $i + j + k = n$.How the Code WorksInstead 
# of writing three nested for loops and manually building a list, a list comprehension handles the creation, 
# iteration, and filtering all in a single line.Here is how the list comprehension breaks down step-by-step:

x= int(input("Enter x: "))
y= int(input("Enter y: "))
z= int(input("Enter z: "))
n= int(input("Enter n: "))

result = [[i,j,k] for i in range(x+1)
for j in range(y+1)
for k in range(z+1)
if (i+j+k) != n ]

print(result)
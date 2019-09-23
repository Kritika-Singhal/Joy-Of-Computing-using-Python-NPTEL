'''Given a positive integer number n, you have to write a program that generates a dictionary d which contains (i, i*i*i) such that i is the key and i*i*i is its value, where i is from 1 to n (both included).
Then you have to just print this dictionary d.

Example:
Input: 4

will give output as
{1: 1, 2: 8, 3: 27, 4: 64}

Input Format:
Take the number n in a single line.

Output Format:
Print the dictionary d in a single line.'''

# Code
n=int(input())
d={}
for i in range(1,n+1):
  d[i]=i*i*i
print(d)


'''Example:

Input:
8

Output:
{1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512}'''

"""Write a program that reads a number N and prints three lines with each line containing N pluses (+).
Note
There is a space after every plus symbol.
Input
The input will be a single line containing an integer.
Output
The output should be three lines containing N space separated pluses (+) in each line.
Constraints
N is always greater than 0
Explanation
For example, if the given number N is 4, the output should be
++
++ +
Sample Input 1
4
Sample Output 1
+ ++"""
a=input()
b=("+ "*int(a))
print(b)
print(b)
print(b)
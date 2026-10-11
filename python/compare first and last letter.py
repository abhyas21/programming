"""Compare First & Last Letters
20/20
Easy
Write a program that reads a word and checks if the first letter and last letter of the word are not the same.
Input
The input will be a single line containing a string.
Output
The output should be a single line containing a boolean. True should be printed if the first letter and last letter of the word are not the same, otherwise False should be printed.
Explanation
For example, if the given word is Python,
P
0
3
5
The output should be True as the first letter Pand the last letter of the word are not the same.
Sample Input 1
Python
Sample Output 1
True
Sample Input 2
Label
Sample Output 2
False"""
a=input()
b=a[0]
f=a[-1]
print(b!=f)
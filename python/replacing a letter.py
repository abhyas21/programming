"""Write a program that reads a word W , an index I, and a letter C
Print the word W by replacing the letter at the index I with the given letter C
Input
The first line of input contains a string.
The second line of input contains an integer.
The third line of input contains a string.
Output
The output should be a single line containing a string obtained by replacing the letter at the index I of the word W with the letter C
Constraints
The index is always greater than 0 and one less than word length (length - 1).
Explanation
For example, if the given word W is Prime, the index I is 3
and the letter C is Z.
P
r
i
m
e
0
1
2
3
4
The letters before the 3rd index are Pri.
The letter at the 3rd index m should be replaced with Z.
The letter after the 3rd index is e.
The output should be Prize as the letter m in Prime is replaced with the letter Z."""
a=input()
b=int(input())
c=input()
d=a[:b]+c+a[b+1:]
print(d)
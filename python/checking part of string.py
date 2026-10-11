"""B, and an index Write a program that reads two words
In Check if B starts at Index
Input
The first line of input contains a string representing
The second line of input contains a string representing B
The third line of input contains an integer representing I
Output
The output should be a single line containing a boolean. True should be printed if the word B starts at index of the word , otherwise False should be printed.
Constraints
Length of B is less than or equal to the length of
Explanation
For example, if the given words are. A = Repeat B = pea, and the index is l = 2
R
P
0
2
3
4
5
The word Pea is a part of the word Repeat
The word Pea starts at the 2nd index of the word Repeat.
The output should be True as the string pea starts from the index 2 of the string Repeat.
Sample Input 1
Repeat
pea
2
Sample Output 1
True"""
a=input()
b=input()
c=int(input())
d=a[c:c+len(b)]
print(d==b)
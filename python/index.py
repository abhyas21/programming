"""Given a word W and an integer N, write a program to print the character present at the index N in the word W.
Input
The first line contains the word W
The second line contains the integer N
Explanation
For example, when the given word W is Chocolate and the integer N is 2. Since the index starts from zero. The character present at index 2 is o.
C
h
0
C
0
1 a
t
e
0
1
2
3
4
5
6
7
8
Similarly, for Table the character at index 1 is a
Similarly, for Table the character at index 1 is a
T
a
b
1
e
0
1
2
3
4
Constraints
0 <= N < len(W)
Sample Input 1
Chocolate
2
Sample Output 1
0"""
a=input()
b=int(input())
c=a[b]
print(c)
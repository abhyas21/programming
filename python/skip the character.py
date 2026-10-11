"""The output should be a single line containing a string excluding the fourth letter of the word.
Explanation
For example, if the given word is Equality,
E q u
a
i
t
y
0
1
2
3
4
5
6
7
The letters before the fourth letter are Equ.
The fourth letter is a.
The letters after the fourth letter are lity
The output should be Equlity as the fourth letter is excluded."""
a=input()

b=a[:3]+a[4:]
print(b)
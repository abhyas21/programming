"""Write a program that reads two numbers
and B and checks if A is greater than or equal to 8
Print the result as shown in the sample output.
Input
The first line of input contains a float.
The second line of input contains a float.
Output
The output should be a single line containing a string as shown in the sample output.
Explanation
For example, if the given numbers are A = 4.3 and B = 3.2
Is greater than or equal to 8: True. (4.3 is greater than or equal to 3.2)
Add the string "A >= B is" before True.
The output should be A > B is True.
Sample Input 1
3.2
Sample Output 1
A Bis
True
Sample Input 2
9.9
18.8
Sample Output 2
> B is False"""
a=input()
b=input()
d=float(a) >= float(b)
c="A >= B is "
print(c+str(d))
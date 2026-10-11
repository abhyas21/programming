"""Write a program that reads two numbers A and B and checks if the A is greater than B
Print the result as shown in the sample output.
Input
The first line of input contains an integer.
The second line of input contains an integer.
Output
The output should be a single line containing a string as shown in the sample output.
Explanation
For example, if the given numbers are A8 and B = 5
A is greater than B True. (8 is greater than 5)
Add the string "A > B is " before True.
The output should be A > B is True.
Sample Input 1
8 5
Sample Output 1
A
Bis
True"""
a=input()
b=input()
c="A > B is "
d=int(a) > int(b)
print(c+str(d))
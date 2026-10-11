"""Write a program that prints the sum of the digits of a given three-digit number.
Input
The input will be a single line containing a three-digit number.
Output
The output should be a single line containing the sum of the three digits of the given number.
Explanation
For example, if the given number is 326, the sum of its digits, 3 + 2 + 6 is 11."""
a=int(input())
b=sum(int(digits)for digits in str(a))
print(b)
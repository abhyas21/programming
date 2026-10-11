"""Write a program that reads a percentage P and prints the percentage P of the number 200.
Note
The Percentage (P) of Number (N) can be calculated as:
value = (percentage / 100) * number
Input
The input will be a single line containing an integer.
Output
The output should be a single line containing a float that is the P percentage of 200.
Explanation
For example, if the given percentage is P = 50 , the 50 percent of number 200 is,
value= (percentage / 100) value = (50 / 100) * 200 value = 0.5 * 200 value = 100.0 * number
The output should be 100.0.
Sample Input 1
50
Sample Output 1
100.0"""
a=int(input())
p=(a/100)*200
print(p)
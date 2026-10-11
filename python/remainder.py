"""Write a program that reads a dividend and a divisor and prints the remainder.
Note
For Example, if 7 is divided by 2 (7/2),
Dividend: 7
Divisor <-- 2)7 (3--> Quotient
6
1 --> Remainder
Formula to Calculate Remainder:
Quotient should be an integer to calculate the remainder. remainder = dividend - (divisor * quotient)
Input
The first line of input contains an integer.
The second line of input contains an integer.
Output
The output should be a single line containing an integer that is the remainder.
Explanation
For example, if the given dividend is 7 and the divisor is 2,
The quotient is 3.5 (7/2).
The integer of 3.5 is 3.
The remainder is 1 as shown below.
remainder = dividend -(divisor * quotient)
remainder = 7 - (2 * 3)
remainder = 7 -6
remainder = 1
The output should be 1.
Sample Input 1
7
2
Sample Output 1
1"""
a=int(input())
b=int(input())

re=a%b
print(re)
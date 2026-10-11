"""Write a program that reads a string and prints the first and last characters of the given string and prints the stars (* ) instead of the remaining characters.
Input
The input will be a single line containing a string.
Output
The output should be a single line containing the first and last characters of the given string and stars ( * ) instead of the remaining characters.
Explanation
For example, if the given string is qwerty@2020, the output should be q*********0.
Sample Input 1
qwerty@2020
Sample Output 1
Sample Input 2
9647329032
Sample Output 2"""
a=input()
le1=len(a)-1
le=len(a)-2
print(a[0]+"*"*le+a[le1])
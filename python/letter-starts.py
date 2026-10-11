"""Write a program that reads a word and prints the first letter of the given word and stars (*) instead of the other letters.
Input
The input will be a single line containing a string.
Output
The output should be a single line containing the first letter of the given word and stars ( * ) instead of the other letters.
Explanation
For example, if the given word is Queue,
The number of letters in the word Queue is 5. We have to print the first letter Q.
Now, without the first letter, there are 4 letters. So, we have to print 4 stars ( * ).
The output should be Q****.
Sample Input 1
Queue
Sample Output 1
Sample Input 2
Password
Sample Output 2"""
a=input()
le=len(a)
le1=le-1
print(a[0]+"*"*le1)
"""Write a program that reads a word and prints stars (* ) equal to the length of the word.
Input
The input will be a single line containing a string.
Output
The output should be a single line containing stars ( the length of the word. * ) equal to
Explanation
For example, if the given word is qwerty,
The number of letters in the word qwerty is 6. So, we have to print 6 stars.
The output should be ******."""
a=input()
length=(len(a))
print("*"*length)
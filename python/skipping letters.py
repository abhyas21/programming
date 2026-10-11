"""You're given a word and an index position of a character. You need to write a program that prints the given word without the character at the given index.
Input
The first line of input contains a word.
The second line of input contains the index location.
Output
The output should be a single line containing the word skipping the character at the given index location.
Explanation
For example, if the given word is "Combine", the character at the index location 4, is "i", so the output without the character at the given index location is "Combne""""
a=input()
b=int(input())
c=a[:b]
w=a[b+1:]
print(c+w)
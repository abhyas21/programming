def numbers(n):
    if n%2==1:
        return "No"
    else:
        return "Yes"
n = int(input("Enter a number: "))
print(numbers(n))
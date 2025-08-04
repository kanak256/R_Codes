x=int(input("Enter a number: "))
y=str(x)
if y==y[::-1]:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
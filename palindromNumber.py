number = int(input("Enter a number:"))
reverseNumber = 0
tempNumber = number
while tempNumber > 0:
    lastDigit = tempNumber % 10
    reverseNumber = reverseNumber * 10 + lastDigit
    tempNumber = tempNumber // 10

if number == reverseNumber:
    print(number, "is the palindrome number")
else:
    print(number, "is not the palindrome number")

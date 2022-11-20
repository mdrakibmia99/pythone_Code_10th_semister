number = int(input("Enter a number"))
tempNumber=number
reverseNumber=0
while tempNumber>0:
    lastDigit=tempNumber%10
    reverseNumber=reverseNumber * 10 + lastDigit
    tempNumber =tempNumber // 10
if number == reverseNumber:
    print(number,"is palindrome number")
else:
    print(number,"is not palindrome number")

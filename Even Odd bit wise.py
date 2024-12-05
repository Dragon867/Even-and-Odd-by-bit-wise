def inEvenOdd(n):
    if(n^1==n+1):
        return True
    else:
        return False
    
number=int(input("Enter a number of your choice : "))
if inEvenOdd(number):
    print(number,", the number is even.")
else:
    print(number,", the number is odd.")
#Function to decide whether a number is palindrom
def isPalindrom(number):
    #Set a variable palindrom True
    palindrom = True

    #Convert integer to string
    strNumber = str(number)

    #Check palindrom
    for i in range(len(strNumber)):
        palindrom = palindrom and (strNumber[i] == strNumber[len(strNumber)-(i+1)])

    #Return result
    return palindrom

#Input number
number = int(input())

#Decide whether a number is palindrom
if(isPalindrom(number)):
    print("YES")
else:
    print("NO")
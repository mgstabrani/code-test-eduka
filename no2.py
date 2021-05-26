#Function to decide whether two numbers are anagram
def isAnagram(number1, number2):
    #Allocate frequency arrays
    frekNumber1 = [0 for i in range(10)]
    frekNumber2 = [0 for i in range(10)]

    #Convert integer to string
    strNumber1 = str(number1)
    strNumber2 = str(number2)

    #Put the element based on the frequency array
    for i in range(len(strNumber1)):
        frekNumber1[int(strNumber1[i])] += 1
    for i in range(len(strNumber2)):
        frekNumber2[int(strNumber2[i])] += 1

    #Set anagram variable True
    anagram = True

    #Check whether they are anagram
    if(len(strNumber1) == len(strNumber2)):
        for i in range(10):
            anagram = anagram and (frekNumber1[i] == frekNumber2[i])
    else:
        anagram = False

    #Return result
    return anagram

#Input the numbers
string = list(map(int, input().split(" ")))

#Assign input numbers to new variables
number1 = string[0]
number2 = string[1]

#Decide whether those two numbers are anagram
if(isAnagram(number1, number2)):
    print("YES")
else:
    print("NO")
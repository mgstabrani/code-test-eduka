#Function to check a string is palindrom
def isPalindrom(string):
    #Set palindrom variable True
    palindrom = True

    #Check whether a string is palindrom
    for i in range(len(string)):
        palindrom = palindrom and (string[i] == string[len(string)-(i+1)])

    #Return result
    return palindrom

#Function to find first and last index of longest palindrom substring
def longestPalindrom(string):
    #Set longest variable 0
    longest = 0

    #Set index of first and last
    ifirst = 0
    ilast = 1

    #Allocate candidate answer array
    candidateAnswer = []

    #Find all palindrom substring
    for i in range(len(string)-1):
        for j in range(i+1,len(string)):
            if(isPalindrom(string[i:j+1])):
                candidateAnswer.append([i,j])

    #Find the longest substring in candidate answer
    for i in range(len(candidateAnswer)):
        if(abs(candidateAnswer[i][0]-candidateAnswer[i][1]) > longest):
            longest = abs(candidateAnswer[i][0]-candidateAnswer[i][1])
            ifirst = candidateAnswer[i][0]
            ilast = candidateAnswer[i][1]

    #Return result
    return(ifirst,ilast)

#Input string
string = input()

#Display first and last index of longest palindrom substring
ans = longestPalindrom(string)
print(ans[0],ans[1])
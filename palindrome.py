def checkpalindrome(str):
    size=len(str)
    k=(size//2)-1
    for i in range (0,k):
        if(str[i]!=str[size-1-i]):
            result="NOT Palindrome"
            return result
    result="Palindrome"
    return result

def checksymmetric(str):
    size=len(str)
    if(size%2==1):
        result="NOT Symmetric"
        return result
    
    k=int(size/2)
    for i in range (0,k-1):
        if(str[i]!=str[k+i]):
            result="NOT Symmetric"
            return result
    result="Symmetric"
    return result

str=input("Enter string: ")

print("The given String ", str," is ", checkpalindrome(str))
print("The given string ",str," is ",checksymmetric(str))
def reverseString(string):
    s=string.split(' ')
    length=len(s)

    s_reverse=[]

    for i in range(0,s):
        s_reverse.append(s[length-1-i])
    
    string_reverse=(" ".join(s_reverse))
    return string_reverse


string=input("Enter string: ")

print("Reverse String:",reverseString(string))

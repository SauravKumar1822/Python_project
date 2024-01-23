# Python code

def reverseString(str):
    # To reverse words in a given string

    # reversing words in a given string
    # s = str.split()[::-1]
    # print(s)

    # rev_string=(" ".join(s))
    # return rev_string
    s=str.split(' ')
    length=len(s)

    s_reverse=[]

    for i in range(0,length):
        s_reverse.append(s[length-1-i])
    
    string_reverse=(" ".join(s_reverse))
    return string_reverse




str=input("Enter string: ")

print("Reverse String:",reverseString(str))

def newlist(list):
    size=len(list)

    temp=list[0]
    list[0]=list[size-1]
    list[size-1]=temp

    return list



#Creating an empty list
list = []

n = int(input("Enter number of input in List: "))

#Loop
for i in range(0,n):
    element=int(input())
    list.append(element)

print("Oldlist: ",list)

print("Newlist: ",newlist(list))


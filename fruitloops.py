
#sorting list algorithm in python O(n)

list_one=[] #initializing an empty list

#adding items in the list
size_of_list=int(input("Enter the size of the list"))

print(f"Enter {size_of_list} elements")

for i in range(size_of_list):
    value=int(input())
    list_one.append(value)

#ascending order sorting
for i in range(size_of_list):
    for j in range(size_of_list):
        if list_one[i]<list_one[j]:
            temp=list_one[i]
            list_one[i]=list_one[j]
            list_one[j]=temp

print(list_one)

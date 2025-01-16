arr = ["Apple","Banana","Watermelon","chiku"]

#Lenght of an Array
lenght=len(arr)
print(lenght)


#Adding new element
arr.append("guava")
print(arr)

#Removing an Element
arr.remove("chiku")
print(arr)

#Modifying/Replacing an Element
arr[2]=("chiku")
print(arr)

#Adding two Arrays (Concatenation)
arr_2=["Rose","Lily","Lotus"]

arr += arr_2
print(arr)

#Repeating An element
repeat = arr[2]*5 
print(repeat)
def removedup(myList):
    unique=set(myList)
    print(unique)

dup=removedup([1,2,3,4,5,6,7,8,9,1,2,3,4,5])
print(dup)

studentdetails={
    "name":"join",
    "age":20,
    "gender":"male"
}

print(studentdetails.get("name"))
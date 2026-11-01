
def howmany(num):
    count=0
    while num>0:
        count+=1
        num=num//10
    return count

num=int(input("Enter a number: "))
print("The number of digits in the number is:", howmany(num))
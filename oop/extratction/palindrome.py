

def is_palindrome(num):
    reverse=0
    while num>0:
        lastdogo=num%10
        reverse=reverse*10+lastdogo
        num=num//10
    return reverse


num=int(input("Enter a number: "))
last=is_palindrome(num)
print("The reverse of the number is:", last)
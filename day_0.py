#Write a program to reverse a number in Python?
#input 123
#output 321

n= 123
rev=0
while(n>0):
    print("n=",n)
    dig=n%10
    print("dig=",dig)
    rev=rev*10+dig
    print("rev=",rev)
    n=n//10
    print("n=",n)
    print("=======================")
print("The reverse of the number:",rev)
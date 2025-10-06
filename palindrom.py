def palindrom(x):
    
    a=x
    b=rev(a)
    if(a==b):
        print("IS Palindrom")
    else:
        print("IS NOT Palindrom")    
def rev(x):
    n=0
    while(x>0):
        t=x%10 
        n=(n*10)+t
        x=x//10
    return n

 
c=int(input("Enter no to check: "))
palindrom(c)
# OUTPUT:
# Enter no to check: 1211
# IS NOT Palindrom

# Enter no to check: 12121
# IS Palindrom
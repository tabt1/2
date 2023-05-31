def hcf(a,b):
    if(b==0):
        return a
    else:
        return hcf(b,a%b)


a = int(input("enter the first number"))
b = int(input("enter the second number"))
print("The GCD is : ",end="")
print(hcf(a,b))
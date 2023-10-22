def bi(n):
    if n==0:
        return ""
    else:
        return bi(n//2)+str(n%2)

n=int(input("Enter the decimal number: "))
# print ("Binary equivalent of",n,"is",bin(n)[2:])
res=bi(n)
print("Binary:",res)

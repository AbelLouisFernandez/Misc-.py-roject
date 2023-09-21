import math as mt
print("Welcome to calculator")
o="y"
while o in ("y","Y"):
    no1=float(input("Enter the first number"))
    op=input("Enter the operation")
    if op in ("root","square","log"):
        if op=="root":
            v=mt.sqrt(no1)
        if op=="square":
            v=no1**2
        if op=="log":
            v=mt.log(no1)
        
    else:
        no2=float(input("Enter the second number"))
        if op=="**":
            v=no1**no2
        if op=="^":
            v=no1**no2
        if op=="+":
            v=no1+no2
        if op=="-":
           v=no1-no2
        if op=="*":
           v=no1*no2
        if op=="/":
           v=no1/no2
    no1=str(no1)
    v=str(v)
    j=" "
    file=open("History.txt","a")
    if op in ("root","square","log"):
         z="\n"+no1+j+op+j+"="+j+v
    else:
        no2=str(no2)
        z="\n"+no1+j+op+j+no2+j+"="+j+v
    file.writelines(z)
    file.close()
    print(v)
    o=input("Do you want to calculate again Y/N")
    
print("Thank you for using calculator  (•◡•)/")

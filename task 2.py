print("////Welcome to maths calculater////")
a= int(input(" Enter 1st value:"))
b=int(input(" Enter 2nd value :"))
sy=input("Enter the symbol=")
c = a+b
d=a-b
e=a*b
f=a/b
if sy== '+':
    print("Addition:",c)
elif sy == '-':
    print("Subraction:",d)
elif sy =='*':
    print("Mul:",e)
elif sy =='/':
    print("Div:",f)
else:
    print("Try again error")
    prtint("Thank for using ")
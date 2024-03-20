import sys
a=  int(sys.argv[1])
b=  int(sys.argv[2])
c=  int(sys.argv[3])
Delta= b**2-4*a*c
if Delta > 0:
    Root1= (-b-Delta**(1/2))/(2*a)
    Root2= (-b+Delta**(1/2))/(2*a)
    print("There are two solutions")
    print("Solutions:",Root1,Root2)
elif Delta ==0:
    Root1=(-b+Delta**(1/2))/(2*a)
    print("There are two repeated real number solutions:",Root1)
else :
    print("There is no real solution")

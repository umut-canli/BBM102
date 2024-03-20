import sys
S= sys.argv[1]
S=S.split(",")
B =[]
a=0
for number in S :
    number=int(number)
    if number>0 and number%2==0:
        B.append((number))
        a += number
c=0
for sum_t in S :
    sum_t=int(sum_t) 
    if sum_t >0 :
        c += sum_t
B=str(B)
print("Even Numbers:",B)
print("Even number rate:",round(a/c,3))
print("Sum Of Even Numbers:",a)
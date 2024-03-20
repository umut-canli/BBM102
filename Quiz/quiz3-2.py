import sys


numbers=sys.argv[1].replace('"','').split(",")

A=[int(i) for i in numbers ]
A=[b for b in A if b > 0]
A.sort()

#listeyi sete dönüştürdükten sonra error verdiği için tekrar listeye dönüştürdüm.

List1=set(A)
List=list(List1)
def lucky_number(List):
    if 1 in List:
        del List[1::2]
        x=1
        while  List[x]  <= len(List):
            a = List[x]
            del List[a - 1::a]
            x+=1
            try:
                List[x]
            except IndexError:
                break
    else:
        x=0
        while List[x] <= len(List):
            a=List[x]
            del List[a-1::a]
            x+=1
            try:
                List[x]
            except IndexError:
                break
    Last=' '.join(str(e) for e in List)

    print("Output:",Last)

lucky_number(List)

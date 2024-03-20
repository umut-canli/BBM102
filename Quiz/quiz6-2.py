import sys
n=5
start=0
med=0
def main(start,n,med):
    if start==n-1 and med==0:
        med=1
        main(start,n,med)
    elif start==0 and med==1:
        print(" "*(n-start),"*"*(2*start+1))
        return
    elif start!=0 and med==1:
        print(" "*(n-start),"*"*(2*start+1) )
        main(start-1,n,1)
       
    
    else:
        print(" "*(n-start),"*"*(2*start+1) )
        main(start+1,n,0)
main(start,n,med)
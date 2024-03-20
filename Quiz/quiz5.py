import sys


def main():
    count=0
    for u in f2.readlines():
        u=u.split()
        b=[]
        for i in u:
            try:
                i=int(i)
                b.append(i)
            except:
                b.append(i)
        c.append(b)

    for j in file.readlines():
        j=j.split()
        try:
            l=[]
            div=float(j[0])
            nondiv=float(j[1])
            From=float(j[2])
            to=float(j[3])
            div=int(div)
            nondiv=int(nondiv)
            From=int(From)
            to=int(to)
            try:
                for k in range(From,to+1):
                    if k%div==0 and k%nondiv!=0:
                        l.append(k)
                print("-----------------------------------------")
                print("My results:      ",*l,sep=" ")
                print("Results to compare:      ",*c[count],sep=" ")
                try:
                    assert c[count]==l
                    print("Goool!!!")
                except AssertionError:
                    print("AssertionError: results don’t match.")
                count+=1
            except ZeroDivisionError:
                print("-----------------------------------------")
                print("ZeroDivisionError: You can’t divide by 0.")
                print("Given input:"  ,*j,sep=" ")   
                count+=1 
        except ValueError:
            print("-----------------------------------------")
            print("ValueError: only numeric input is accepted.")
            print("Given input:"  ,*j,sep=" ")
            count+=1 
        except IndexError:
            print("-----------------------------------------")
            print("IndexError: number of operands less than expected.")
            print("Given input:"  ,*j,sep=" ")     
            count+=1
        except:
            print("kaBOOM: run for your life!")
    print("--- Game Over ! ---")


            
c=[]
try:
    file=open(sys.argv[1],"r")
except IOError:
    print("IOError: cannot open {}".format(sys.argv[1]))
    print("--- Game Over ! ---")

try:
    f2=open(sys.argv[2],"r")
except IOError:
    print("IOError: cannot open {}".format(sys.argv[2]))
    print("--- Game Over ! ---")

except IndexError:
    print("IndexError: number of input files less than expected.")
    print("--- Game Over ! ---")


else:
    main()
    

    

    








    



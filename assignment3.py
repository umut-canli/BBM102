import sys
a=[]
b=[]
d = {}
y=None
count=0
x=None

f2=open("output.txt","w")
with open(sys.argv[1],"r") as file:
    for i in file.readlines():
        d[i.split(":")[0]]=list(i.split(":")[1].split())


#Function part
def ANU(x):
    if x in d.keys():
        f2.write("ERROR: Wrong input type! for 'Anu'! -- This user already exists!!"+"\n")
    else:
        d[x] = list()
        f2.write("User {} has been added to the social network successfully" .format(x)+"\n")
    return d
def DEU(x):
    if x not in d.keys():
        f2.write("ERROR: Wrong input type! for 'DEU'!--There is no user named {} !!" .format(x)+"\n")
    else:
        del d[x]
        for i in d.values():
            if x in i:
                i.remove(x)
        f2.write("User {} and his/her all relations have been deleted successfully".format(x)+"\n")
    return d
def ANF(x,y):
    if x in d.keys() and y in d.keys():
        if x in d[y] and y in d[x]:
            f2.write("ERROR: A relation between {} and {} already exists!!".format(x,y)+"\n")
        else:
            d[y].append(x)
            d[x].append(y)
            f2.write("Relation between {} and {} has been added successfully".format(x,y)+"\n")


    elif x not in d.keys() and y in d.keys():
        f2.write("ERROR: Wrong input type! for'ANF'! -- No user named {} found!!".format(x)+"\n")
    elif y not in d.keys() and x in d.keys():
        f2.write("ERROR: Wrong input type! for'ANF'! -- No user named {} found!!".format(y)+"\n")
    elif x and y not in d.keys():
        f2.write("ERROR: Wrong input type! for 'ANF'! -- No user named {} and {} found!".format(x,y)+"\n")
    return d

def DEF(x,y):
    if x in d.keys() and y in d.keys():
        if x in d[y] and y in d[x]:
            d[y].remove(x)
            d[x].remove(y) 
            f2.write("Relation between {} and {} has been deleted successfully".format(x,y)+"\n")
        else:
            f2.write("ERROR: No relation between {} and {} found!!".format(x,y)+"\n")
    elif x in d.keys():
        f2.write("ERROR: Wrong input type! for'DEF'! -- No user named {} found!!".format(y)+"\n")
    elif y in d.keys():
        f2.write("ERROR: Wrong input type! for'DEF'! -- No user named {} found!!".format(x)+"\n")
    elif x and y not in d.keys():
        f2.write("ERROR: Wrong input type! for 'DEF'! -- No user named {} and {} found!".format(x,y)+"\n")
     
    return d
def CF(x):
    if x in d.keys():
        count=0
        count=len(d[x])
        f2.write("User {} has {} friends".format(x,count)+"\n")
    else:
        f2.write("ERROR: Wrong input type! for 'CF'! -- No user named {} found!".format(x)+"\n")
def FPF(X,y):
    possible_f=[]
    y=int(y)
    if y<1 or y>3:
        f2.write("ERROR: Maximum distance should be between 1<= maximum distance <=3"+"\n")

    elif x in d.keys() and  y==2:
        for k in d[x]:
            for j in d[k]:
                possible_f.append(j)
            possible_f.append(k)
        possible_f.sort()
        while x in possible_f:
            possible_f.remove(X)
        possible_f=sorted(set(possible_f))
        f2.write("User {} has {} possible friends when maximum distance is {} ".format(x,len(possible_f),y)+"\n")
        f2.write("These possible friends: {}".format({str(possible_f)[1:-1]})+"\n")
    
    elif x in d.keys() and y==3:
        for a in d[x]:
            for b in d[a]:
                for c in d[b]:
                    possible_f.append(c)
                possible_f.append(b)
            possible_f.append(a)
        while x in possible_f:
            possible_f.remove(X)
        possible_f=sorted(set(possible_f))
        f2.write("User {} has {} possible friends when maximum distance is {}".format(x,len(possible_f),y)+"\n")
        f2.write("These possible friends: {}".format({str(possible_f)[1:-1]})+"\n")
    elif x in d.keys() and y==1:
        possible_f=d[x]
        possible_f=sorted(set(possible_f))
        f2.write("User {} has {} possible friends when maximum distance is {} ".format(x,len(possible_f),y)+"\n")
        f2.write("These possible friends: {}".format({str(possible_f)[1:-1]})+"\n")
    else:
        f2.write("ERROR: Wrong input type! for 'FPF'! -- No user named {} found!".format(X)+"\n")
    return d
def SF(x,y):
    if x in d.keys():
        y=int(y)
        n=[]
        t2=[]
        t3=[]
        d_count={}
        for i in d[x]:
            for h in d[i]:
                n.append(h)
        while x in n:
            n.remove(x)
        for m in n:
            d_count[m]=n.count(m)
        for k,v in d_count.items():
            if v==2:
                t2.append(k)
        
            elif v==3:
                t3.append(k)
        t2.sort()
        t3.sort()
        t2_t3=t2+t3
        t2_t3.sort()
        t2=str(t2)[1:-1]
        t3=str(t3)[1:-1]
        t2_t3=str(t2_t3)[1:-1]
        if y==2:
            if len(t2) or lent(3)!=0:
                f2.write("Suggestion list for {} (when MD is {}):".format(x,y)+"\n")
                if len(t2) !=0:
                    for i in t2.split(","):
                        f2.write("{} has 2 mutual friends with {}".format(x,i)+"\n")
                if len(t3) !=0:
                    for j in t3.split(","):
                        f2.write("{} has 3 mutual friends with {}".format(x,j)+"\n")
                
                f2.write("The suggested friends for {}:{}".format(x,t2_t3)+"\n")
            if len(t3) and len(t2)==0:
                f2.write("ERROR: There is no suggested friend for {} (when MD is 2)".format(x)+"\n")

        elif y==3:
            if len(t3)==0:
                f2.write("ERROR: There is no suggested friend for {} (when MD is 3)".format(x)+"\n")
            else:
                f2.write("Suggestion list for {} (when MD is {})".format(x,y)+"\n")
                for b in t3.split(","):
                    f2.write("{} has 3 mutual friends with {}".format(x,b)+"\n")
                f2.write("The suggested friends for {}:{}".format(x,t3)+"\n")
        else:
            f2.write("Error: Mutually Degree cannot be less than 2 or greater than 3"+"\n")
    
    
    else:
        f2.write("Error: Wrong input type! for 'SF'! -- No user named {} found!!".format(x)+"\n")
    

#command part

input=open(sys.argv[2],"r")
for z in input:
        a.append(z.split())
input.close()


while count<(len(a)):
        if a[count][0]=="ANU":
            x=a[count][1]
            ANU(x)
            count+=1
        elif a[count][0]=="DEU":
            x=a[count][1]
            DEU(x)
            count+=1
        elif a[count][0]=="ANF":
            x=a[count][1]
            y=a[count][2]
            ANF(x,y)
            count+=1
        elif a[count][0]=="DEF":
            x=a[count][1]
            y=a[count][2]
            DEF(x,y)
            count+=1
        elif a[count][0]=="CF":
            x=a[count][1]
            CF(x)
            count+=1
        elif a[count][0]=="FPF":
            x=a[count][1]
            y=a[count][2]
            FPF(x,y)
            count+=1
        elif a[count][0]=="SF":
            x=a[count][1]
            y=a[count][2]
            SF(x,y)
            count+=1
        else:
            count+=1

f2.close()
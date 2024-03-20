import sys
a=[]
    

with open(sys.argv[1],"r") as File:
    for i in File:
        i=i[:-1]
        liste=i.split("\t")
        a.append(liste)
a.sort()
x=0
y=0
z=0
message_count=2
value=a[0][0]
with open(sys.argv[2],"w") as f2:
    f2.write("Message 1"+"\n")
    while x < len(a):
        if value !=a[x][0]:
            #write komutunu kullanmak için stringe  dönüştürdüm sonra tekrar inte çevirdim
            f2.write("Message ")
            message_count=str(message_count)
            f2.write(message_count+"\n")
            message_count=int(message_count)
            value=a[x][0]
            message_count+=1
        f2.write(a[x][0]+"\t")
        f2.write(a[y][1]+"\t")
        f2.write(a[z][2]+"\n")
        x+=1
        y+=1
        z+=1
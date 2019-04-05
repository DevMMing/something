f=open('newdata.csv',"r")
num_lines = sum(1 for line in open('newdata.csv'))
print(num_lines)
a=0
b=0
c=0
d=0
e=0
for i in range(num_lines):
    if i==0:
        f.readline()
    else:
        string=f.readline().split(",")[2]
        if string=="BRONX":
            a+=1
        if string=="MANHATTAN":
            b+=1
        if string=="BROOKLYN":
            c+=1
        if string=="QUEENS":
            d+=1
        if string=="STATEN ISLAND":
            e+=1
f.close()
print("done")
f=open("save.csv","w")
f.write("Boroughs,Accidents\n")
f.write("Bronx,"+str(a)+"\n")
f.write("Manhattan,"+str(b)+"\n")
f.write("Brooklyn,"+str(c)+"\n")
f.write("Queens,"+str(d)+"\n")
f.write("Staten Island,"+str(e)+"\n")
f.close()

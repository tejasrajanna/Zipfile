import zipfile
zf=zipfile.ZipFile("names.zip","r") #creating object using ZipFile constructor
zf.printdir()   #prints contents of zipfile with details
zf.extractall()
l=zf.namelist()   #list of files in the zip
con=[]      #to store contents of file
cou=0
for filename in l:
    con.append([])   #make a new list in the con list for each file
    print(filename)
    fh=open(filename,'r')
    a=' '  #to store each line
    while a:
        a=fh.readline()
        a=a.strip()
        con[cou].append(a)
        print(a)
    con[cou].pop()  # removes blank space which is last element
    cou=cou+1   #to move to next index for new file
for i in range(len(con)):
    con[i]=set(con[i])
out=con[0]
j=1
while j<len(con):
    out=out & con[j]  #to find common elements
    j=j+1
n=list(out)
n.sort()
with open("output.txt","w") as f:
    for item in n:
        f.write(item + "\n")
print("output.txt")
with open("output.txt","r") as fh:
     for line in fh:
         t = line.strip()
         print(t)













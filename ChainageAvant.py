from expression import Expression
import unification as Unif
class ChainageAvant:
    def __init__(self):
        myBfFile=open("BF.txt",'r')
        lines=myBfFile.readlines()
        for line in lines:
            line.strip()
        self.BF=lines

myBfFile=open("BF.txt",'r')
lines=myBfFile.readlines()
for line in lines:
    go=line.split(", ")
f=open("alo.txt","w+")
for l in go:
    f.write(l+"\n")
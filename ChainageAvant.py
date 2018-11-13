from expression import Expression
import unification as Unif
from Rule import Rule
class ChainageAvant:
    def __init__(self):
        myBfFile=open("BF.txt",'r')
        lines=myBfFile.readlines()
        treatedLines=[]
        for line in lines:
            newLine=line.strip().replace("\n","")
            treatedLines.append(newLine)
        self.BF=treatedLines
        myBrFile=open("BR.txt","r")
        lines=myBrFile.readlines()
        for line in lines:
            newLine=line.strip().replace("\n","")
            treatedLines.append(newLine)
        self.BR=treatedLines


    def chainageUtil(self,rule:Rule,Bf):
        if(rule.has_premisses()):
            for fait in Bf:
                





# # test
# a=ChainageAvant()
# print(a.BF)
# print(a.BR)
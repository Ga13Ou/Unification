from expression import Expression
import unification as Unif
from Rule import Rule
import sys
class ChainageAvant:
    Ok=False
    newFaits=[]
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
        treatedLines=[]
        for line in lines:
            newLine=line.strip().replace("\n","")
            treatedLines.append(newLine)
        self.BR=treatedLines
        self.BrExp=self.getRulesFromStringArray()
        self.BfExp=self.getFactsFromStringArray()

    def getRulesFromStringArray(self):
        rulesExp=[]
        for s in self.BR:
            rulesExp.append(Rule(s))
        return rulesExp


    def getFactsFromStringArray(self):
        faitExp=[]
        for s in self.BF:
            faitExp.append(Expression(s))
        return faitExp       

    # Bf is a list of Expression
    def chainageUtil(self,rule:Rule):
        if(rule.has_premisses()):
            p1=rule.get_first_premiss()
            print(p1)
            for fait in self.BfExp:
                x=Unif.unifier(fait,p1)
                print("\t",fait,"   ",x)
                if(x is not None):
                    Unif.beautifulResult(x)
                    ruleS=rule.spread(x)
                    p=ruleS.get_first_premiss()
                    ruleSP=ruleS.pop_premisse()
                    self.chainageUtil(ruleSP)
                    # rule.push_premisse(p)
        elif(not rule.has_premisses()):
            if(rule.checkExtra()):
                c=rule.conclusion_to_string()
                if(c not in self.BF):
                    self.newFaits.append(c)
                    self.BF.append(c)
                    self.BfExp.append(rule.conclusion)
                    self.Ok=True

    def chainage_avant(self):
        self.Ok=True
        i=0
        while(self.Ok):
            i+=1
            self.Ok=False
            for r in self.BrExp:
                self.chainageUtil(r)
        print(i)





sys.setrecursionlimit(1000)
# # # test
# a=ChainageAvant()
# # print(a.BF)
# print(a.BR)
# # print(a.BfExp)
# print()
# print(a.BrExp)
# print(a.newFaits)
# a.chainage_avant()
# print(a.newFaits)

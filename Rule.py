# Travaille TP1 AI
# Gastli Oussama
# Hanana Nour
# GL4

from expression import Expression
import unification as Unif
import copy

class Rule:
    #une regle doit etre de la forme
    #pere(?X,?Y):-parent(?X,?Y); homme(?X)
    
    
    def __init__(self, string):
        assert isinstance(string,str)
        self.extraCheck=[]
        self.premisses=[]
        resultat=string.split(":-")
        conclusionString=resultat[0].strip()
        premisseString=resultat[1].split(";")
        treatedPremisses=[]
        for i in range(len(premisseString)):
            premisseString[i]=premisseString[i].strip()
            if('\=='in premisseString[i]):
                self.extraCheck.append(premisseString[i])
            else:
               treatedPremisses.append(Expression(premisseString[i]))
        self.conclusion=Expression(conclusionString)
        self.premisses=treatedPremisses
        

    def pop_premisse(self):
        # self.premisses.pop(0)
        a=copy.deepcopy(self)
        a.premisses.pop(0)
        return a
       
    def spreadUtil(self,array,unification):
        assert isinstance(unification,list)
        for i in range(len(array)):
            if(isinstance(array[i],str)):
                for unif in unification:
                    if(unif[0]==array[i]):
                        array[i]=unif[1]
            elif(isinstance(array[i],list)):
                self.spreadUtil(array[i],unification)


    def spreadUtil_forExtra(self,array,unification):
        assert isinstance(unification,list)
        newWordArray=[]
        for word in array:
            for u in unification:
                word=word.replace(u[0],Unif.functionToString(u[1]))
            newWordArray.append(word)
        self.extraCheck=newWordArray


    
    
    # propagation
    def spread(self,unification):
        a=copy.deepcopy(self)
        Unif.beautifulResult(unification)
        conclusionExpression=a.conclusion.expression
        a.spreadUtil(conclusionExpression,unification)
        # to spread the unification to the extrachecks
        a.spreadUtil_forExtra(a.extraCheck,unification)

        # array of premisses
        premisseArray=[]

        for p in a.premisses:
            premisseArray.append(p.expression)

        a.spreadUtil(premisseArray,unification)

        # array of expressions
        premisseArrayExpression=[]
        for p in premisseArray:
            premisseArrayExpression.append(Expression(p))

        a.conclusion=Expression(conclusionExpression)
        a.premisses=premisseArrayExpression
        return a

    def has_premisses(self):
        if(len(self.premisses)==0):
            return False
        return True

    def get_first_premiss(self):
        if(self.has_premisses()):
            return self.premisses[0]
        return None

    def conclusion_to_string(self):
        c=self.conclusion.expression
        return Unif.functionToString(c)

    def checkExtra(self):
        for word in self.extraCheck:
            a=word.split("\==")
            if(a[0]==a[1]):
                return False
        return True
    def __repr__(self):
        return str({"premisse":self.premisses,"conclusion":self.conclusion,"check":self.extraCheck})+"\n"





        
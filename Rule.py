from expression import Expression
import unification as Unif

class Rule:
    #une regle doit etre de la forme
    #pere(?X,?Y):-parent(?X,?Y); homme(?X)
    premisses=[]
    extraCheck=[]
    def __init__(self, string):
        assert isinstance(string,str)
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
        self.premisses.pop(0)
        return self

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
        Unif.beautifulResult(unification)
        conclusionExpression=self.conclusion.expression
        self.spreadUtil(conclusionExpression,unification)
        # to spread the unification to the extrachecks
        self.spreadUtil_forExtra(self.extraCheck,unification)

        # array of premisses
        premisseArray=[]

        for p in self.premisses:
            premisseArray.append(p.expression)

        self.spreadUtil(premisseArray,unification)

        # array of expressions
        premisseArrayExpression=[]
        for p in premisseArray:
            premisseArrayExpression.append(Expression(p))

        self.conclusion=Expression(conclusionExpression)
        self.premisses=premisseArrayExpression

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
            if(a[0]!=a[1]):
                return False
        return True




#Test
    
a=Rule('frere_ou_soeur(?X,?Y) :- pere(P,?X);pere(P,?Y);mere(M,?X);?Z\==rt;mere(M,?Y);?X\==?Y')
unif=[['?X', ['#f', 'A', 'C', 'B']], ['?Z', '?B'], ['?B', 'rt'], ['?Y', ['#f', 'A', 'C', 'B']]]
a.spread(unif)
# a.pop_premisse()
print(a.conclusion)
# print(a.conclusion_to_string())
# print(a.get_first_premiss())
print(a.checkExtra())
print("allo",a.extraCheck)
        
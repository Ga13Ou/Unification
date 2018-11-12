from expression import Expression
import unification as Unif

class Rule:
    #une regle doit etre de la forme
    #pere(?X,?Y):-parent(?X,?Y); homme(?X)
    premisses=[]
    def __init__(self, string):
        assert isinstance(string,str)
        resultat=string.split(":-")
        conclusionString=resultat[0].strip()
        premisseString=resultat[1].split(";")
        for i in range(len(premisseString)):
            premisseString[i]=premisseString[i].strip()
            premisseString[i]=Expression(premisseString[i])
        self.conclusion=Expression(conclusionString)
        self.premisses=premisseString

    def pop_premisse(self):
        return self.premisses.pop(0)

    def spreadUtil(self,array,unification):
        assert isinstance(unification,list)
        for i in range(len(array)):
            if(isinstance(array[i],str)):
                for unif in unification:
                    if(unif[0]==array[i]):
                        array[i]=unif[1]
            elif(isinstance(array[i],list)):
                self.spreadUtil(array[i],unification)
        
    # propagation
    def spread(self,unification):
        Unif.beautifulResult(unification)
        conclusionExpression=self.conclusion.expression
        self.spreadUtil(conclusionExpression,unification)

        # array of list
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

        






#Test
    
# a=Rule("pere(fils(?X,?Z),?Y):-parent(?X,?Y); homme(?X);enfant(?X,?Y)")
# unif=[['?X', ['#f', 'A', 'C', 'B']], ['?x', 'B'], ['?z', 'C'], ['?Y', 'allo']]
# a.spread(unif)
# #a.pop_premisse()
# print(a.premisses)
# print(a.conclusion)
        
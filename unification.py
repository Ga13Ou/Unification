# Travaille TP AI
# Gastli Oussama
# Hanana Nour
# GL4
from expression import Expression
import ast


def unifier_atom(expr1:Expression,expr2:Expression):
    if(expr2.isAtom()):
        expr1,expr2=expr2,expr1

    if(expr1==expr2):
        return []

    if(expr2.isVariable()):
        expr1,expr2 = expr2,expr1

    if(expr1.isVariable()):
        if(expr1 in expr2):
            return None
        if (expr2.isAtom()):
           return [[expr1.expression[0],expr2.expression[0]]]
        if(expr2.isFunction()):
            return [[expr1.expression[0],expr2.expression.__str__()]]

    return None

def unifier(terms1:Expression,terms2:Expression):

    if(terms1.isAtom() or terms2.isAtom()):
        return unifier_atom(terms1,terms2)

    F1,T1=terms1.separate()
    F2,T2=terms2.separate()


    Z1=unifier(F1,F2)
    if(Z1==None):
        return None

    T1.substitute(Z1)
    T2.substitute(Z1)


    Z2=unifier(T1,T2)

    if(Z2==None):
        return None
    Z2+=Z1
    return Z2

# utilisée pour avoir un bon format d'affichage des fonctions
def functionToString(f):
        if(isinstance(f,str)):
            return f
        else:
            s=str(f[0])+"("
            for k in range(1,len(f)):
                s+=functionToString(f[k])+","
            s=s[1:-1]
            s+=")"
            return s

# utilisée pour afficher les permutations de l'unification de façon lisible
def beautifulResult(a):
    if(a is None):
        return "non unifiable"
    elif (a==[]):
        return "already unified"
    s=""
    for i in a:
        if(i[1][0]=='['):
            i[1]=ast.literal_eval(i[1])
        s+="("+i[0]+"/"+functionToString(i[1])+") "
    return s





# e1=Expression("q(f(A,?x),?x)")
# e2=Expression("q(f(A,?x),?x)")
# print(beautifulResult(unifier(e1,e2)))
# # print(unifier(e1,e2))
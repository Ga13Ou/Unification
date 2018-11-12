from expression import Expression
import unification as unif

def CLI_app():
    a=input("type the first expression to unify: ")
    b=input("type the second expression to unify: ")
    print(a,b)
    x=unif.unifier(e1,e2)
    result=unif.beautifulResult(x)
    print(result)


def FILE_app():
    myFile=open("testExpression.txt","r")
    lines = myFile.readlines()
    for line in lines:
        a=line.split(";")
        s1,s2=a[0],a[1].strip('\n')
        e1=Expression(s1)
        e2=Expression(s2)
        x=unif.unifier(e1,e2)
        result=unif.beautifulResult(x)
        print(s1)
        print(s2)
        print()
        print(result)
        print("-----------------------------------------------------")
        # print(s1,s2)

# main function
choice=0
while((choice != "1") and (choice!="2")):
    print("======================Menu=====================")
    print("=1- Read from the command Line                =")
    print("=2- Read from the file \"testExpression.txt\"   =")
    print("===============================================")
    choice = input()

if(choice=="1"):
    CLI_app()
else:
    FILE_app()

# Travaille TP1 AI
# Gastli Oussama
# Hanana Nour
# GL4

from expression import Expression
import unification as unif
from ChainageAvant import ChainageAvant
import copy

def CLI_app():
    a=input("ecrire la 1ere expression a unifier: ")
    b=input("ecrire la 2eme expression a unifier: ")
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
        

def chainageAvant_app():
    a=ChainageAvant()
    oldBF=copy.deepcopy(a.BF)
    a.chainage_avant()
    newBF=a.newFaits

    myFile=open("resultat.txt","w")

    myFile.write("============anciens faits=====================\n")
    for s in oldBF:
        myFile.write(s+"\n")
    myFile.write("============nouveaux faits====================\n")
    for s in newBF:
        myFile.write(s+"\n")

    print("un fichier resultat.txt contenant les faits a été généré")
    print("l'algorithme de chainage a déduit {} nouveaux faits".format(len(newBF)))

    print("====FIN du programme====")







# main function
choice=-1
while(int(choice)<0 or int(choice)>3):
    print("============================Menu============================")
    print("=1- Unification a partir de la console                     =")
    print("=2- unification a partir du fichier \"testExpression.txt\"   =")
    print("=3- Algorithme de chainage avant d'ordre 1                 =")
    print("=                                                          =")
    print("=        Binome:                                           =")
    print("=                Gastli Oussama & Hanana Nour GL4          =")
    print("============================================================")
    choice = input()

if(choice=="1"):
    CLI_app()
elif(choice=="2"):
    FILE_app()
elif(choice=="3"):
    chainageAvant_app()
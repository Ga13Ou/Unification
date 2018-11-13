from Rule import Rule
import copy

a=Rule('frere_ou_soeur(?X,?Y) :- pere(P,?X);pere(P,?Y);mere(M,?X);?Z\==rt;mere(M,?Y);?X\==?Y')
b=a.pop_premisse()
b=b.pop_premisse()
print(a.premisses)
print(b.premisses)

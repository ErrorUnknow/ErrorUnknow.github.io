# -*- coding: Utf-8 -*-
# ---------------------------------------------------
print ("\n")
print ( "\t ** Exo 1 : quelques calculs élémentaires ")
print ("\n")
# Pour ce corrigé, pas de gestion d'exceptions, on verra plus tard..
a = input("""Saisir l'entier "a" : """)
a = int ( a )     
# ci-dessous, saisie faite en 1 fois, pour l'exemple
b = int(input("""Saisir l'entier "b" : """))

# le affichages sont fait d'abord en 2 fois, puis directement, pour l'exemple
s = "a vaut {0}, b vaut {1}".format(a,b)
print ( s )                      
print ("somme de a et b : {0}".format(a+b) )
print ( "produit de a et b : {0}".format(a*b) )
print ( "rapport a / b : {0:.2f}".format(float(a)/b))

input("une touche pour quitter")
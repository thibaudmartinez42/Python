# lib TP2 Jeanne Champion Thibaud Martinez 22/11/2022
# D =Dictionnaire ou l'on va vérifier les mots
# P = phrase rentré par l'utilisateur 
#p = phrase rentré par l'utilisateur transformé en liste 
#T =Table de Transistion
#M = Mot rentré par l'utilisateur 
#vm est vla valeur associé au mot qui definit sa fonction dans la phrase
def Recup_Données(P): # prend la phrase et la transforme en liste avec chaque element de celle si qui est un mot
    p=P.split(" ")
    return p
def VerificationPhrase(D,p,T): # verifie que la phrase est correct
    Etat =0
    i=0
    while Etat != 8 and Etat !=9 and i <= len(p):
        Valeur_Mot = VerificationMot(D,p[i])
        if Valeur_Mot == "erreur":
            print("Mot non reconnu")
            return
        E = T[Etat]
        Etat = E[Valeur_Mot]
        i = i + 1
    print(T[Etat])
    return

def VerificationMot(D,M): #vérifie que les mot de la phrase don dans le dictionnaire
    if M in D :
        vm=D[M]
        return vm
    else:
        vm ="erreur"
        return
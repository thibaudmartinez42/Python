# lib TP2 Jeanne Champion Thibaud Martinez 22/11/2022
# D =Dictionnaire ou l'on va vérifier les mots
# P = phrase rentré par l'utilisateur 
#p = phrase rentré par l'utilisateur transformé en liste 
#T =Table de Transistion
#M = Mot rentré par l'utilisateur 
#vm est la valeur associé au mot qui definit sa fonction dans la phrase
def Recup_Données(P): # prend la phrase et la transforme en liste avec chaque element de celle si qui est un mot
    p=P.split(" ")
    print(p)
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
    if Etat !=8 and Etat != 9: # si l'etats n'est ni 8 ni 9 le met automatiquement a 8 car phrase non complet
        Etat = 8
    if Etat == 8:
        print("Phrase incorect.")
        return
    if Etat == 9:
        print("phrase correct.")
        return


def VerificationMot(D,M): #vérifie que les mot de la phrase est dans le dictionnaire
    if M in D :
        vm=D[M]
        return vm
    else:
        vm ="erreur"
        return
# lib TP2 Jeanne Champion Thibaud Martinez 22/11/2022
# D =Dictionnaire ou l'on va vérifier les mots
# P = phrase rentré par l'utilisateur 
#p = phrase rentré par l'utilisateur transformé en liste 
#T =Table de Transistion
#M = Mot rentré par l'utilisateur 
def Recup_Données(P):

    return
def VerificationPhrase(D,p,T):
    Etat =0
    i=0
    while Etat != 8 or 9 or i != len(p):
        Valeur_Mot = VerificationMot(D,p[i])
        E = T[Etat]
        Etat = E[Valeur_Mot]
        i =+ 1
    if Etat !=8 and 9:
        Etat = 8
    if Etat == 8:
        print("Phrase incorect")
        return
    if Etat == 9:
        print("phrase ccorrect")
        return


def VerificationMot(D,M):

    return
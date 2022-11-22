# TP2 partie code général Jeanne Champion et Thibaud Martinez le 22/11/2022
import LibTP2 

Table_Transition = {
0:[1,8,8,8,4,8],
1:[8,2,1,8,8,8],
2:[8,8,2,3,8,8],
3:[5,8,8,8,7,9],
4:[8,8,8,3,8,8],
5:[8,5,6,8,8,8],
6:[8,8,8,3,8,8],
7:[8,8,8,8,8,9],
 }
dictionnaire ={"le" : 0, "la" : 0, "chat" : 2, "souris" : 2, "martin" : 4,
"mange" : 3, "la" : 0, "petite" : 1, "joli" : 1, "grosse" : 1,
"bleu" : 1, "verte" : 1, "dort" : 3,"julie" : 4, "jean" : 4, "." : 5}

print(dictionnaire)
phrase=input("rentre une phrase a partir du dictionnaire il faut mettre un espace entre le point et le dernier mot")
Entree_Act=LibTP2.Recup_Données(phrase)
LibTP2.VerificationPhrase(dictionnaire,Entree_Act,Table_Transition)

#!Generer un nombre aléatoire
import random
nbre_alea = random.randint(0,9)
rep_user = None
#!Entrer le nombre de comparaison
while rep_user != nbre_alea:
      rep_user =int(input("Saisir un nombre entre 0 et 9:"))
#!Comparaison avec le nombre génèré
      if rep_user > nbre_alea:
            print("Désolé le nombre est plus petit")
      elif rep_user < nbre_alea:
            print("Désolé le nombre est plus grand")
      else:
            print("Bravo! Tu as trouvé le nombre")

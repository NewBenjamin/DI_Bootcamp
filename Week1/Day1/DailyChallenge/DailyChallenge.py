# DI Bootcamp - Week 1 - Day 1 - Daily Challenge
# Build up a string
# Author: Benjamin Ehrlich

import random 

# ÉTAPE 1 : Demander un texte de 10 caractères à l'utilisateur
user_string = input("Entre un texte de 10 caractères exactement : ")


# ÉTAPE 2 : Vérifier la longueur
# len(x) = longueur de x (combien il y a de caractères)
if len(user_string) < 10:
    print("String not long enough.")
elif len(user_string) > 10:
    print("String too long.")
else:
    # Le texte fait EXACTEMENT 10 caractères → on continue
    print("Perfect string")

    # ÉTAPE 3 : Afficher 1er et dernier caractère
    # [0] = 1er caractère (Python compte à partir de 0)
    # [-1] = dernier caractère
    print(f"First character : {user_string[0]}")
    print(f"Last character : {user_string[-1]}")

    # ÉTAPE 4 : Construire le texte caractère par caractère
    # range(1, 11) génère les nombres 1, 2, 3... jusqu'à 10
    # user_string[:i] prend les i premiers caractères
    print("progressive construction of the string :")
    for i in range(1, len(user_string) + 1):
        print(user_string[:i])

    # ÉTAPE 5 (BONUS) : Mélanger les caractères du texte
    # On transforme le texte en liste de caractères
    char_list = list(user_string)
    # random.shuffle() mélange la liste sur place
    random.shuffle(char_list)
   
    jumbled = "".join(char_list)
    print(f"Jumbled string : {jumbled}")
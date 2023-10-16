# -*- coding: utf-8 -*- ## Pour s’assurer de la compatiblite entre correcteurs
import random
random.seed()

#Bonjour, ce fichier est la représentation python du JEU ARUBA
#### REPRESENTATION DES DONNEES
###Initialisation des grilles et du message debut jeu

message = r"""                          __________ __
                                        \______   \__| ____   _______  __ ____   ____  __ __  ____
                                         |    |  _/  |/ __ \ /    \  \/ // __ \ /    \|  |  \/ __ \
                                         |    |   \  \  ___/|   |  \   /\  ___/|   |  \  |  |  ___/
                                         |______  /__|\___  >___|  /\_/  \___  >___|  /____/ \___
                                                \/        \/     \/          \/     \/
                                                         .___
                                                       __| _/____    ____   ______
                                                      / __ |\__  \  /    \ /  ___/
                                                     / /_/ | / __ \|   |  \\___ \
                                                     \____ |(____  /___|  /____  >
                                                          \/     \/     \/     \/
                                               _____ __________ ____ _____________    _____
                                              /  _  \\______   \    |   \______   \  /  _  \
                                             /  /_\  \|       _/    |   /|    |  _/ /  /_\  \
                                            /    |    \    |   \    |  / |    |   \/    |    \
                                            \____|__  /____|_  /______/  |______  /\____|__  /
                                                    \/       \/                 \/         \/  """

grille_debut = [
        [ ["A1", '●'], ["A2", '●'], ["A3", '●'], ["A4", '●'], ["A5", '●'], ["A6", '●'], ["A7",'○'] ],
        [ ["B1", '●'], ["B2", '●'], ["B3", '●'], ["B4", '●'], ["B5", '●'], ["B6", '○'], ["B7", '○'] ],
        [ ["C1", '●'], ["C2", '●'], ["C3", '●'], ["C4", '●'], ["C5", '○'], ["C6", '○'], ["C7", '○'] ],
        [ ["D1", '●'], ["D2", '●'], ["D3", '●'], ["D4",' '], ["D5", '○'], ["D6", '○'], ["D7", '○'] ],
        [ ["E1", '●'], ["E2", '●'], ["E3", '●'], ["E4", '○'], ["E5", '○'], ["E6", '○'], ["E7", '○'] ],
        [ ["F1", '●'], ["F2", '●'], ["F3", '○'], ["F4", '○'], ["F5", '○'], ["F6", '○'], ["F7", '○'] ],
        [ ["G1", '●'], ["G2", '○'], ["G3", '○'], ["G4", '○'], ["G5", '○'], ["G6", '○'], ["G7", '○'] ]
        ]

grille_milieu = [
        [ ["A1", ' '], ["A2", '●'], ["A3", '●'], ["A4", ' '], ["A5", '○'], ["A6", '●'], ["A7",'○'] ],
        [ ["B1", '●'], ["B2", '●'], ["B3", ' '], ["B4", ' '], ["B5", ' '], ["B6", '○'], ["B7", ' '] ],
        [ ["C1", '●'], ["C2", ' '], ["C3", '●'], ["C4", ' '], ["C5", ' '], ["C6", ' '], ["C7", ' '] ],
        [ ["D1", '●'], ["D2", ' '], ["D3", ' '], ["D4",'●'], ["D5", '○'], ["D6", ' '], ["D7", ' '] ],
        [ ["E1", '●'], ["E2", '●'], ["E3", ' '], ["E4", ' '], ["E5", '○'], ["E6", '○'], ["E7", ' '] ],
        [ ["F1", ' '], ["F2", '●'], ["F3", ' '], ["F4", '○'], ["F5", ' '], ["F6", ' '], ["F7", '○'] ],
        [ ["G1", '●'], ["G2", '○'], ["G3", ' '], ["G4", ' '], ["G5", ' '], ["G6", ' '], ["G7", '○'] ]
        ]

grille_fin = [
        [ ["A1", ' '], ["A2", ' '], ["A3", ' '], ["A4", ' '], ["A5", ' '], ["A6", ' '], ["A7",' '] ],
        [ ["B1", ' '], ["B2", '○'], ["B3", ' '], ["B4", ' '], ["B5", ' '], ["B6", ' '], ["B7", ' '] ],
        [ ["C1", ' '], ["C2", ' '], ["C3", ' '], ["C4", ' '], ["C5", ' '], ["C6", '●'], ["C7", ' '] ],
        [ ["D1", ' '], ["D2", ' '], ["D3", ' '], ["D4",'○'], ["D5", '●'], ["D6", ' '], ["D7", ' '] ],
        [ ["E1", ' '], ["E2", ' '], ["E3", ' '], ["E4", ' '], ["E5", ' '], ["E6", ' '], ["E7", ' '] ],
        [ ["F1", ' '], ["F2", ' '], ["F3", ' '], ["F4", ' '], ["F5", ' '], ["F6", ' '], ["F7", ' '] ],
        [ ["G1", ' '], ["G2", ' '], ["G3", ' '], ["G4", ' '], ["G5", ' '], ["G6", ' '], ["G7", ' '] ]
        ]

#### REPRESENTATION GRAPHIQUE
def afficher_grille(grille):
    print()
    ligne=["A","B","C","D","E","F","G"] #Pour l'instalation de l'indice de la ligne
    print("    1   2   3   4   5   6   7") #Pour l'instalation de l'indice de la colonne
    print("", (" + " + "―"*1)*7, "+")
    for i in range (0,7):
        print(ligne[i],"|",end=" ") #Pour l'affichage de la grille ligne par ligne
        for y in range(0,7):
            print(grille[i][y][1] + " |",end=" ") #Pour traiter chaque element dans la grille
        print(" ",end=" ")
        print()
        print("", (" + " + "―"*1)*7, "+")
    print("  ", "joueur1 = ●", "   ", "joueur2 = ○" )
    print()

#### SAISIE
###fonctions de verification
#jeux de tests
def test_est_au_bon_format():
    print("Test de la fonction est_au_bon_format:")
    assert est_au_bon_format("A3")[0] == True, "Validation d'indice de colonne majuscule"
    assert est_au_bon_format("a3")[0] == True, "Validation d'indice de colonne minuscule"

    assert est_au_bon_format("aa")[0] == False, "Deux indices de ligne valides"
    assert est_au_bon_format("33")[0] == False, "Deux indices de colonne valides"
    assert est_au_bon_format("km")[0] == False, "Deux indices de ligne non valides"
    assert est_au_bon_format("90")[0] == False, "Deux indices de colonne non valides"
    assert est_au_bon_format("k3")[0] == False, "l'indice de ligne est non valide"
    assert est_au_bon_format("b0")[0] == False, "L'indice de colonne est non valide"
    assert est_au_bon_format("b")[0] == False , "Il n'y a pas d'indice de colonne"
    assert est_au_bon_format("5")[0] == False, "Il n'y a pas d'indice de ligne"
    assert est_au_bon_format(" ")[0] == False, "Coordonnées vides"
    print("OK")

def test_est_dans_grille():
    print("Test de la fonction est_dans_grille:")
    assert est_dans_grille("A","1",grille_debut) == True, "le pion est dans grille"
    assert est_dans_grille("A","7",grille_debut) == True, "le pion est dans grille"
    assert est_dans_grille("G","1",grille_debut) == True, "le pion est dans grille"
    assert est_dans_grille("G","7",grille_debut) == True, "le pion est dans grille"
    assert est_dans_grille("B","3",grille_debut) == True, "le pion est dans grille"

    assert est_dans_grille("A","0",grille_debut) == False, "erreur : n'est pas dans grille"
    assert est_dans_grille("A","9",grille_debut) == False, "erreur : n'est pas dans grille"
    assert est_dans_grille("","",grille_debut) == False, "erreur : n'est pas dans grille"
    assert est_dans_grille("1","A",grille_debut) == False,"erreur : n'est pas dans grille"
    print("OK")

#verification au bon format
def est_au_bon_format(position):
    if len(position) != 2:
        return False, "Coordonnées non valide"   #Rend une booléen s'il est dans la grille ou pas et un message d'erreur
    else:
        indice_ligne, indice_col = position[0], position[1]
        if indice_ligne.upper() not in "ABCDEFG":
            return False, "L'indice de la ligne doit être dans ABCDEFG"
        else:
            if indice_col in "1234567":
                return True, "Coordonnées valides:"
            else:
                return False, "L'indice de la colonne doit être dans 1234567"

#verification si les coordonnées données sont dans la grille
def est_dans_grille(ligne,colonne,grille):
    position = ligne + colonne
    if est_au_bon_format(position)[0]:
        if (ord("G")< ord(ligne) <ord("A")) and (ord("7")< ord(colonne) <ord("1")):
            return False
        else:
            return True
    else:
        return False

###fonctions de saisie des coordonnées
def saisir_coordonnees() :
    saisie_correct = False
    while not saisie_correct:
        saisie_correct = True
        position = input("Entrez les coordonnées: ")
        saisie = est_au_bon_format(position)
        saisie_correct = saisie[0]  #Prend la valeur booléen s'il est dans la grille ou pas
        if saisie_correct:
            print(saisie[1], position.upper())
            return position
        else:
            print(saisie[1])  #Pour imprimer le message d'erreur
            print("Veuillez saisir les coordonnées avec le format suivant : A1")

###Fonctions d'affichage des pions captures et fin de jeu
def affichage_pion_capture(grille):
    reste_pion_j1, reste_pion_j2 = pion_en_jeu(grille)
    pion_capture_j1 = 24 - reste_pion_j1
    pion_capture_j2 = 24 - reste_pion_j2
    print("Pion capture par J1 =", pion_capture_j2, "| Pion capture par J2 =", pion_capture_j1)
    print("")
    if pion_capture_j1 == 24 or pion_capture_j2 == 24:
        grille = reset_fin_de_partie()
        if pion_capture_j2 == 24:
            return "Joueur 1 gagne!"
        elif pion_capture_j1 == 24:
            return "Joueur 2 gagne!"

def pion_en_jeu(grille):  #Compte le nombre des pions en jeu
    reste_pion_j1, reste_pion_j2 = 0, 0
    for ligne in range (len(grille)):
        for case in range(len(grille[ligne])):
            if grille[ligne][case][1] == '●' :
                reste_pion_j1 +=1
            elif grille[ligne][case][1] == '○':
                reste_pion_j2 +=1
    return (reste_pion_j1, reste_pion_j2)

def reset_fin_de_partie():  #Declare la fin du jeu
    print("Le jeu est termine!")
    valide = False
    return grille_debut, valide

###Fonctions de verification de la distance des deplacements
def verif_deplacement_simple_distance(position_depart, position_arrivee):  #Calcule la distance dans une deplacement simple qui doit etre egale a 1 cases
    if (ord(position_depart[0]) - ord(position_arrivee[0]) == 0):
        if max(ord(position_depart[1]),ord(position_arrivee[1])) -1 == min(ord(position_depart[1]),ord(position_arrivee[1])):
            return True

    elif (ord(position_depart[1]) - ord(position_arrivee[1]) == 0):
        if max(ord(position_depart[0]),ord(position_arrivee[0])) -1 == min(ord(position_depart[0]),ord(position_arrivee[0])):
            return True

    elif max(ord(position_depart[0]),ord(position_arrivee[0])) -1 == min(ord(position_depart[0]),ord(position_arrivee[0])):
        if max(ord(position_depart[1]),ord(position_arrivee[1])) -1 == min(ord(position_depart[1]),ord(position_arrivee[1])):
            return True

    else: return False

def verif_deplacement_saut_distance(position_depart, position_arrivee):  #Calcule la distance dans une deplacement avec saut qui doit etre egale a 2 cases
    if (ord(position_depart[0]) - ord(position_arrivee[0]) == 0):
        if max(ord(position_depart[1]),ord(position_arrivee[1])) -2 == min(ord(position_depart[1]),ord(position_arrivee[1])):
            return True

    elif (ord(position_depart[1]) - ord(position_arrivee[1]) == 0):
        if max(ord(position_depart[0]),ord(position_arrivee[0])) -2 == min(ord(position_depart[0]),ord(position_arrivee[0])):
            return True

    elif max(ord(position_depart[0]),ord(position_arrivee[0])) -2 == min(ord(position_depart[0]),ord(position_arrivee[0])):
        if max(ord(position_depart[1]),ord(position_arrivee[1])) -2 == min(ord(position_depart[1]),ord(position_arrivee[1])):
            return True

    else: return False

###Fonctions de verification de la possibilite des deplacements
def milieu_position(position_depart, position_arrivee):  #Donne la case qui se trouve au milieu entre deux cases pour tester si il y a un pion de l'adversaire ou non
    if (ord(position_depart[0]) - ord(position_arrivee[0]) == 0):
        posi_colon = position_depart[0]
        posi_ligne = chr(max(ord(position_depart[1]),ord(position_arrivee[1])) -1)

    elif (ord(position_depart[1]) - ord(position_arrivee[1]) == 0):
        posi_colon = chr(max(ord(position_depart[0]),ord(position_arrivee[0])) -1)
        posi_ligne = position_depart[1]

    else:
        posi_colon = chr(max(ord(position_depart[0]),ord(position_arrivee[0])) -1)
        posi_ligne = chr(max(ord(position_depart[1]),ord(position_arrivee[1])) -1)

    return posi_colon+posi_ligne

def validite_position_depart(grille, position, pion_j_courant):  #Verifie qu'il y a un pion du joueur au position du depart
    for ligne in grille:
        for case in ligne:
            if case[0] == position:
                if case[1] == pion_j_courant:
                    return True
                else:
                    return False

def validite_position_arrivee_depla_simple(grille, position):  #Verifie que la position d'arrivee est une case vide
    for ligne in grille:
        for case in ligne:
            if case[0] == position:
                if case[1] == ' ':
                    return True
                else:
                    return False

def validite_position_arrivee_depla_saut(grille, position_depart, position_arrivee, pion_j_courant):  #Verifie si il y a un pion de l'adversaire ou non
    position = milieu_position(position_depart, position_arrivee)
    for ligne in grille:
        for case in ligne:
            if case[0] == position:
                if case[1] != pion_j_courant and case[1] != ' ':
                    return True
                else:
                    return False

###Fonctions de changement du grille apres deplacement
def change_grille_deplacement_simple(grille, position_depart, position_arrivee, pion_j_courant): #Modifie la grille apres une deplacement simple effectuee
    for ligne in grille:
        for case in ligne:
            if case[0]  == position_depart:
                case[1] = ' '
    for ligne in grille:
        for case in ligne:
            if case[0] == position_arrivee:
                case[1] = pion_j_courant
    return grille

def change_grille_deplacement_saut(grille, position_depart, position_arrivee, pion_j_courant):  #Modifie la grille apres une deplacement avec saut effectuee
    position_milieu = milieu_position(position_depart, position_arrivee)
    for ligne in grille:
        for case in ligne:
            if case[0] == position_depart:
                case[1] = ' '
    for ligne in grille:
        for case in ligne:
            if case[0] == position_arrivee:
                case[1] = pion_j_courant
    for ligne in grille:
        for case in ligne:
            if case[0] == position_milieu:
                case[1] = ' '
    return grille

###Fonctions des deplacements
def deplacement_simple(grille, position_depart, position_arrivee, pion_j_courant):  #Fonction principale de la deplacement simple
    if verif_deplacement_simple_distance(position_depart, position_arrivee) and validite_position_depart(grille, position_depart, pion_j_courant) and validite_position_arrivee_depla_simple(grille, position_arrivee):
        change_grille_deplacement_simple(grille, position_depart, position_arrivee, pion_j_courant)
        afficher_grille(grille)
        affichage_pion_capture(grille)
    else:
        print("Désolé! Faux coordonnées attendez votre prochain tour")

def deplacement_saut(grille, position_depart, position_arrivee, pion_j_courant):  #Fonction principale de la deplacement avec saut
    if verif_deplacement_saut_distance(position_depart, position_arrivee) and validite_position_depart(grille, position_depart, pion_j_courant) and validite_position_arrivee_depla_simple(grille, position_arrivee) and validite_position_arrivee_depla_saut(grille, position_depart, position_arrivee, pion_j_courant):
        change_grille_deplacement_saut(grille, position_depart, position_arrivee, pion_j_courant)
        afficher_grille(grille)
        affichage_pion_capture(grille)
        saut_continue(grille, position_arrivee, pion_j_courant)
    else:
        print("Désolé! Faux coordonnées attendez votre prochain tour")

def saut_continue(grille, position_arrivee, pion_j_courant):  #Fonction qui permet de faire une sequence de saut
    reponse = int(input("Voulez vous entrez dans une séquence: (Oui : 1, Non : 2)"))
    if reponse == 1:
        position_depart = position_arrivee
        print("Entrez la position d'arrivee:")
        position_arrivee = saisir_coordonnees()
        deplacement_saut(grille, position_depart, position_arrivee, pion_j_courant)
    elif reponse == 2:
        print()
    else:
        print("Vous devez choisir entre 1 et 2 seulement!")
        saut_continue(grille, position_arrivee, pion_j_courant)

###Fonctions du tour de jeu ordinateur contre joueur (mode naive)
liste_indices_ligne = [" ", "A", "B", "C", "D", "E", "F", "G"]

def choisir_hasard(a, b):
    random_nbr = random.randint(a, b)
    return random_nbr

def nomb_en_lettre(nbr):
    for i in range(8):
        if nbr == i:
            return liste_indices_ligne[i]

def lettre_en_nomb(ltr):
    for i in range(7):
        if ltr == liste_indices_ligne[i]:
            return i

def pions_ordi(grille):  #Fait une liste de tous les pions de l'ordi en jeu
    pions = []
    for ligne in range (len(grille)):
        for case in range(len(grille[ligne])):
            if grille[ligne][case][1] == '○':
                pions.append([ligne, case + 1])
    return pions

def depla_ordi(coord, grille):  #Fait une liste de toutes les deplacements possibles d'un pion
    pions_depla = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            if 0 < coord[0] + x <= 7 and 0 < coord[1] + y <= 7:
                if grille[coord[0] + x][coord[1] + y][1] == ' ':
                    pions_depla.append([coord[0] + x, coord[1] + y])
            if 0 < coord[0] + x * 2 <= 7 and 0 < coord[1] + y * 2 <= 7:
                if grille[coord[0] + x * 2][coord[1] + (y * 2) - 1][1] == ' ':
                    if grille[coord[0] + x][coord[1] + y - 1][1] == '●':
                        pions_depla.append([coord[0] + x * 2, coord[1] + y * 2])
    pions_depla.remove(coord)
    return pions_depla

def tour_ordi(grille):  #Choisit un pion au hasard et puis choisit sa deplacement au hasard et modifie la grille tout de suite
    liste_pions = pions_ordi(grille)
    pion_choisi = liste_pions[choisir_hasard(0, len(liste_pions) - 1)]
    positi_possible = depla_ordi(pion_choisi, grille)

    while len(positi_possible) < 1:
        pion_choisi = liste_pions[choisir_hasard(0, len(liste_pions) - 1)]
        positi_possible = depla_ordi(pion_choisi, grille)

    print("\nL'ordinateur a choisit la pièce", nomb_en_lettre(pion_choisi[0]), pion_choisi[1])
    positi_choisi = positi_possible[choisir_hasard(0, len(positi_possible) - 1)]
    print("L'ordinateur déplace sa pièce en", nomb_en_lettre(positi_choisi[0]), positi_choisi[1])

    if -1 <= positi_choisi[0] - pion_choisi[0] <= 1 and -1 <= positi_choisi[1] - pion_choisi[1] <= 1:
        grille[pion_choisi[0]][pion_choisi[1] - 1][1] = ' '
        grille[positi_choisi[0]][positi_choisi[1] - 1][1] = '○'
        afficher_grille(grille)
        affichage_pion_capture(grille)
    else:
        grille[pion_choisi[0]][pion_choisi[1] - 1][1] = ' '
        grille[(pion_choisi[0]+positi_choisi[0])//2][((pion_choisi[1]+positi_choisi[1])//2) - 1][1] = ' '
        grille[positi_choisi[0]][positi_choisi[1] - 1][1] = '○'
        print("L'ordinateur mange donc la pièce en", nomb_en_lettre((pion_choisi[0]+positi_choisi[0])//2), ((pion_choisi[1]+positi_choisi[1])//2))
        afficher_grille(grille)
        affichage_pion_capture(grille)

###Fonctions du tour de jeu ordinateur contre joueur (mode expert)
#A completer...

###Fonctions du menu principale
def choisir_grille(nb_grille): #Affiche la grille choisie
    print()
    if nb_grille == 1:
        print("Grille debut de partie:")
        grille = grille_debut
    elif nb_grille == 2:
        print("Grille milieu de partie:")
        grille = grille_milieu
    elif nb_grille == 3:
        print("Grille fin de partie:")
        grille = grille_fin
    else :
        print("Vous devez choisir entre 1, 2 et 3 seulement!")
        tour_jeu()
    afficher_grille(grille)
    affichage_pion_capture(grille)
    return grille

def choisir_depla(deplacement, grille, position_depart, position_arrivee, pion_j_courant):  #Effectue le type de deplacement choisie
    if deplacement == 1:
        deplacement_simple(grille, position_depart, position_arrivee, pion_j_courant)
    elif deplacement == 2:
        deplacement_saut(grille, position_depart, position_arrivee, pion_j_courant)
    else :
        print("Vous devez choisir entre 1 et 2 seulement!")
        tour_jeu()

def contre_qui(type_jeu, nb_de_tour_joue, grille):  #Controle le jeu (Si c'est un j contre j ou j contre ordi)
    if  type_jeu == 1:
        return nb_de_tour_joue +1
    elif type_jeu == 2:
        tour_ordi(grille)
        return nb_de_tour_joue +2
    else :
        print("Vous devez choisir entre 1 et 2 seulement!")
        tour_jeu()

def tour_pion_joueur(nb_de_tour_joue):  #Declare le joueur courant et son pion
    if nb_de_tour_joue %2 != 0 :
        print("Tour du joueur 1 ...")
        return '●'
    else:
        print("Tour du joueur 2 ...")
        return '○'

def tour_jeu():
    type_jeu = int(input("Choisissez le type de jeu (1 pour Joueur contre Joueur, 2 pour Joueur contre Ordinateur):"))
    nb_grille = int(input("Choisissez la grille voulue (1 pour la grille debut, 2 pour la grille milieu et 3 pour la grille fin):"))
    grille = choisir_grille(nb_grille)
    nb_de_tour_joue = 1
    while valide:
        pion_j_courant = tour_pion_joueur(nb_de_tour_joue)
        deplacement = int(input("Choisissez le type de deplacement voulu (1 pour une deplacement simple, 2 pour une deplacement avec saut):"))
        print("Entrez la position de depart:")
        position_depart = saisir_coordonnees()
        print("Entrez la position d'arrivee:")
        position_arrivee = saisir_coordonnees()
        choisir_depla(deplacement, grille, position_depart, position_arrivee, pion_j_courant)
        nb_de_tour_joue = contre_qui(type_jeu, nb_de_tour_joue, grille)

#### CODE PRINCIPAL
#execution test est_dans_grille
test_est_dans_grille() #uniquement pour la mise au point
test_est_au_bon_format()

# execution affichage de la grille et autres variables de jeux
print(message)
valide = True
while valide:
    tour_jeu()
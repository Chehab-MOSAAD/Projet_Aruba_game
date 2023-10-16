# Projet_Aruba_game
1) L'Objectif :
Le but du jeu est de s’emparer de l’ensemble des pions de l’adversaire.

2) Le Matériel :
— Plateau de 7 x 7.
— 48 pions, 24 pour chaque joueur.
— Configuration de départ :
![image](https://github.com/Chehab-MOSAAD/Projet_Aruba_game/assets/114508258/f59f77ba-2d98-4ab3-ab24-9758782140de)

3) Les Déplacements possibles :
— Déplacement simple :
  Un pion peut se déplacer vers un emplacement adjacent (diagonal ou orthogonal) si cet emplacement est vide.
— Déplacement saut avec prise
  Un pion peut sauter un pion adverse si le pion adverse est à un emplacement adjacent (diagonal ou orthogonal) et si juste derrière et dans l’axe de ce pion adverse, l’emplacement est vide. Dans ce cas, le pion adverse est capturé. Lorsque cela est possible, le joueur peut effectuer un enchainement de plusieurs sauts (uniquement des sauts) et ainsi capturer plusieurs pions.
  Ce schéma montre les déplacements "simples" en rouge et "sauts" en vert.
![image](https://github.com/Chehab-MOSAAD/Projet_Aruba_game/assets/114508258/08c5c5ed-3e35-4c9b-8cf6-02f47e369802)
  Voici un exemple d’enchainement et sa conséquence sur le plateau.
![image](https://github.com/Chehab-MOSAAD/Projet_Aruba_game/assets/114508258/98c3429d-25a1-4288-a5ad-0c76d1aa359b)
![image](https://github.com/Chehab-MOSAAD/Projet_Aruba_game/assets/114508258/639bf965-d183-4f61-a71b-2a4808cb599f)

4) La Fin du jeu :
Le gagnant est celui qui le premier réussit à s’emparer de tous les pions de l’adversaire. Cela met fin à la partie.

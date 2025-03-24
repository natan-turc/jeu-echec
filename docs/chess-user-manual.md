# Manuel Utilisateur - Jeu d'Échecs en Python

## Table des matières

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Démarrage du jeu](#démarrage-du-jeu)
4. [Configuration de la partie](#configuration-de-la-partie)
   - [Orientation du plateau](#orientation-du-plateau)
   - [Thème du plateau](#thème-du-plateau)
   - [Temps de jeu](#temps-de-jeu)
5. [Interface de jeu](#interface-de-jeu)
   - [Plateau de jeu](#plateau-de-jeu)
   - [Informations des joueurs](#informations-des-joueurs)
   - [Chronomètres](#chronomètres)
   - [Pièces capturées](#pièces-capturées)
6. [Comment jouer](#comment-jouer)
   - [Déplacer une pièce](#déplacer-une-pièce)
   - [Règles spéciales](#règles-spéciales)
7. [Fin de partie](#fin-de-partie)
8. [Raccourcis clavier](#raccourcis-clavier)
9. [Dépannage](#dépannage)
10. [Crédits](#crédits)

## Introduction

Bienvenue dans ce jeu d'échecs développé en Python ! Ce manuel vous guidera à travers l'installation, la configuration et l'utilisation du jeu. Notre application propose une expérience d'échecs complète avec toutes les règles officielles, une interface graphique personnalisable et différents modes de jeu.

## Installation

1. Assurez-vous d'avoir Python 3.x installé sur votre ordinateur
2. Téléchargez ou clonez le dépôt du jeu d'échecs :
   ```
   git clone https://github.com/natan-turc/jeu-echec.git
   ```
3. Accédez au répertoire du jeu :
   ```
   cd jeu-echec
   ```
4. Installez les dépendances requises :
   ```
   pip install -r requirements.txt
   ```

## Démarrage du jeu

1. Pour lancer le jeu, exécutez le fichier principal :
   ```
   python src/main.py
   ```
2. Le jeu s'ouvrira en plein écran et vous présentera les options de configuration.

## Configuration de la partie

Avant de commencer une partie, vous devrez configurer trois paramètres :

### Orientation du plateau

Vous pouvez choisir l'orientation du plateau :
- Option 1 : Les pièces blanches sont placées en bas de l'écran
- Option 2 : Les pièces noires sont placées en bas de l'écran

Cliquez sur l'image correspondant à l'orientation souhaitée.

### Thème du plateau

Le jeu propose 18 thèmes de couleurs différents pour le plateau. Cliquez sur la miniature du thème que vous souhaitez utiliser. Les options incluent :
- Classique (beige et vert)
- Bleu
- Violet
- Sépia
- Brun
- Rouge
- Gris
- Gris foncé
- Noir et Blanc
- Forêt
- Océan
- Aube
- Orage
- Sable
- Lave
- Neon
- Espace
- Or

### Temps de jeu

Choisissez le temps alloué à chaque joueur parmi les options suivantes :
- **Blitz** : 3 minutes ou 5 minutes
- **Rapide** : 10 minutes ou 15 minutes
- **Classique** : 30 minutes ou 45 minutes
- **Sans limite** : Aucune contrainte de temps

## Interface de jeu

Une fois les paramètres configurés, un compte à rebours (3, 2, 1, Go !) s'affichera, puis la partie commencera.

### Plateau de jeu

Le plateau d'échecs est affiché au centre de l'écran. Il est composé de 64 cases alternant deux couleurs selon le thème choisi.

### Informations des joueurs

De chaque côté du plateau, vous trouverez :
- Le nom du joueur (Joueur blanc / Joueur noir)
- Une icône représentant le joueur
- L'indication de qui doit jouer ("Les blancs jouent" / "Les noirs jouent")
- Un avertissement si vous êtes en échec ("Vous êtes en échec")

### Chronomètres

Chaque joueur dispose d'un chronomètre indiquant le temps restant. Le chronomètre du joueur actif décompte pendant son tour.

### Pièces capturées

Les pièces capturées par chaque joueur sont affichées sur les côtés du plateau, permettant de suivre l'évolution du matériel au cours de la partie.

## Comment jouer

### Déplacer une pièce

1. Cliquez sur la pièce que vous souhaitez déplacer
2. Les cases vers lesquelles la pièce peut se déplacer seront surlignées en vert
3. Cliquez sur une case verte pour déplacer la pièce à cet endroit
4. Si le déplacement est invalide, rien ne se passera

### Règles spéciales

Le jeu implémente toutes les règles spéciales des échecs :

- **Roque** : Sélectionnez le roi et cliquez sur la case située à deux positions de distance dans la direction où vous souhaitez roquer (si les conditions sont réunies)
- **Promotion des pions** : Lorsqu'un pion atteint la dernière rangée, une fenêtre s'affiche vous permettant de choisir la pièce en laquelle vous souhaitez le promouvoir (Dame, Tour, Fou ou Cavalier)
- **Prise en passant** : Si un pion adverse avance de deux cases et se place à côté de votre pion, vous pouvez le capturer en diagonale comme s'il n'avait avancé que d'une case (uniquement au tour suivant)

## Fin de partie

Une partie peut se terminer de plusieurs façons :

1. **Échec et mat** : Si un joueur met le roi adverse en échec sans possibilité d'y échapper, la partie est gagnée
2. **Temps écoulé** : Si le temps d'un joueur atteint zéro, son adversaire remporte la partie
3. **Abandon** : Un joueur peut abandonner en fermant la fenêtre de jeu

Dans tous les cas, un écran de victoire s'affichera indiquant le vainqueur. Vous aurez alors la possibilité de cliquer sur le bouton "Rejouer" pour commencer une nouvelle partie.

## Raccourcis clavier

- **Échap** : Quitter le jeu

## Dépannage

Si vous rencontrez des problèmes :

1. **Le jeu ne démarre pas** :
   - Vérifiez que Python 3.x est correctement installé
   - Assurez-vous que toutes les dépendances sont installées via `pip install -r requirements.txt`
   - Vérifiez que le dossier `data/images/` contient toutes les images nécessaires

2. **Problèmes d'affichage** :
   - Le jeu s'adapte automatiquement à la résolution de votre écran en mode plein écran
   - Si certains éléments ne s'affichent pas correctement, essayez de relancer le jeu

3. **Plantage pendant la partie** :
   - Assurez-vous que votre ordinateur répond aux exigences minimales pour exécuter Pygame
   - Fermez les applications gourmandes en ressources avant de lancer le jeu

## Crédits

Ce jeu d'échecs a été développé collectivement par l'équipe jeu-echec, composée de Natan Turc, Tidiane Cremer, Killian Mejean et Maëlan Sadoudi.

---

## Comment convertir ce manuel en PDF

Pour convertir ce manuel utilisateur en PDF, vous pouvez utiliser :

1. **Pandoc** (en ligne de commande) :
   ```
   pandoc manuel-utilisateur.md -o manuel-utilisateur.pdf
   ```

2. **Éditeurs Markdown** comme Typora, qui permettent l'exportation directe en PDF

3. **Extensions de navigateur** comme "Markdown to PDF" pour Chrome ou Firefox

4. **Services en ligne** comme MD2PDF (https://md2pdf.netlify.app/)

---

© 2025 Équipe jeu-echec. Tous droits réservés.
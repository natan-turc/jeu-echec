# Documentation du projet Jeu d'Échecs en Python

## Structure générale du projet

Le projet est une implémentation complète du jeu d'échecs en Python avec interface graphique Pygame. Il est conçu de manière modulaire avec une séparation claire entre la logique du jeu et l'interface utilisateur.

## Organisation des fichiers

Le projet est structuré en trois fichiers principaux qui interagissent entre eux :

1. **main.py.py** : Point d'entrée principal du programme qui gère l'affichage de la fenêtre principale et coordonne l'ensemble des fonctionnalités visuelles.
2. **interface1.py** : Contient l'implémentation de l'affichage du plateau d'échecs et des fenêtres de sélection avant le début de la partie.
3. **Jeu_echec1.py** : Implémente la logique du jeu, les règles des échecs et les mouvements des pièces.

De plus, le projet utilise un dossier `data/images/` qui contient toutes les ressources graphiques nécessaires.

## Hiérarchie d'exécution

La hiérarchie d'appel du programme est la suivante :
- L'utilisateur exécute `main.py.py`
- `main.py.py` importe et utilise `interface1.py`
- `interface1.py` importe et utilise `Jeu_echec1.py`

## Description détaillée des composants

### 1. Jeu_echec1.py - Logique du jeu

Ce fichier constitue le cœur de la logique du jeu d'échecs et contient :

#### Classes des pièces
Chaque type de pièce est implémenté via une classe spécifique :
- `Pion`
- `Roi` 
- `Cavalier`
- `Fou`
- `Tour`
- `Reine`

Toutes les pièces partagent des caractéristiques communes :
- Un attribut `camp` (0 pour noir, 1 pour blanc)
- Une représentation visuelle (chemin vers l'image)
- Un type (valeur numérique identifiant la pièce)
- Une méthode `position()` qui retrouve les coordonnées de la pièce sur le plateau
- Une méthode `deplacements_possibles()` qui calcule les mouvements légaux
- Une méthode `chemin()` qui retourne le chemin de l'image représentant la pièce

#### Fonctions de gestion des règles
- `verification_deplacement_valide()` : Vérifie si un déplacement respecte les règles du jeu
- `verification_echec()` : Détecte si un roi est en échec
- `est_case_attaquee()` : Détermine si une case est menacée par une pièce adverse
- `executer_roque()` : Applique le mouvement spécial du roque
- `executer_en_passant()` : Applique la règle de prise en passant pour les pions

#### Initialisation du plateau
- Création des instances de toutes les pièces
- Définition de la liste `Lst_position` qui représente l'état initial du plateau

### 2. interface1.py - Interface graphique du plateau

Ce fichier gère l'affichage du plateau et la sélection des options de jeu :

#### Fenêtres de sélection
Plusieurs fonctions permettent de configurer la partie :
- `afficher_choix_orientation()` : Choix de l'orientation du plateau
- `afficher_selection_couleurs()` : Sélection du thème de couleurs
- `afficher_selection_temps()` : Définition du temps de jeu
- `deconte()` : Animation de décompte avant le début du jeu

#### Classe JeuEchecs
Classe principale qui :
- Initialise et gère le plateau de jeu
- Effectue le rendu graphique du plateau
- Gère les sélections et déplacements de pièces
- Vérifie l'état du jeu (échec, mat)
- Implémente les règles spéciales (promotion des pions, roque)

#### Fonctions d'affichage
- `charger_pieces()` : Charge les images des pièces et les adapte
- `creer_surface_surbrillance()` : Crée la surbrillance pour les mouvements possibles
- `dessiner_echiquier()` : Dessine le plateau de jeu
- `afficher_promotion()` : Affiche l'interface de choix lors de la promotion d'un pion

### 3. main.py.py - Fenêtre principale et orchestration

Ce fichier est le point d'entrée du programme et contient :

#### Classe FenetrePrincipale
Classe qui gère l'ensemble de l'interface en plein écran et coordonne tous les éléments visuels :
- Initialise la fenêtre et adapte les dimensions à l'écran
- Gère le chronomètre pour chaque joueur
- Affiche les informations de jeu (pièces capturées, tour actuel, échec)
- Dessine le plateau dans la zone centrale
- Gère les interactions utilisateur (clics, touches clavier)
- Affiche les écrans de fin de partie

#### Fonctions d'affichage spécifiques
- `texte_echec()` : Affiche quel joueur doit jouer
- `infos_blancs()` et `infos_noirs()` : Affichent les informations des joueurs
- `afficher_conteur_p_b()` et `afficher_conteur_p_n()` : Compteurs de pièces capturées
- `affichage_echec()` : Gère l'affichage en cas d'échec et de mat
- `afficher_chrono()` : Affiche et met à jour les chronomètres
- `fin_partie_temps()` : Gère la fin de partie par temps écoulé

## Fonctionnement des interactions entre fichiers

1. Le fichier `main.py.py` crée une instance de `FenetrePrincipale`
2. `FenetrePrincipale` initialise une instance de `JeuEchecs` (depuis `interface1.py`)
3. `JeuEchecs` utilise les règles et classes définies dans `Jeu_echec1.py`
4. Les interactions utilisateur sont capturées dans `main.py.py` et transmises au plateau via `JeuEchecs`

## Flux de données

1. Les entrées utilisateur (clics, touches) sont capturées dans `main.py.py`
2. Ces actions sont traduites en interactions de jeu et transmises à `JeuEchecs`
3. `JeuEchecs` utilise la logique définie dans `Jeu_echec1.py` pour valider et appliquer les actions
4. L'état du jeu est mis à jour et renvoyé à `FenetrePrincipale` pour affichage

## Systèmes d'adaptation et de personnalisation

Le jeu offre plusieurs options de personnalisation gérées principalement dans `interface1.py` :
- **Orientation du plateau** : La fonction `afficher_choix_orientation()` permet au joueur de choisir si les pièces blanches ou noires sont en bas
- **Thèmes de couleurs** : La fonction `afficher_selection_couleurs()` propose 18 thèmes différents
- **Temps de jeu** : La fonction `afficher_selection_temps()` permet de choisir parmi plusieurs options de durée

## Points techniques spécifiques

### Gestion de l'échec et du mat
Le jeu vérifie à chaque coup si un joueur est en échec (`est_en_echec()`) et si cet échec est un mat (`est_mat()`).

### Filtrage des mouvements légaux
La méthode `filtrer_deplacements_echec()` s'assure qu'un joueur ne peut pas faire un mouvement qui mettrait ou laisserait son roi en échec.

### Règles spéciales des échecs
Le jeu implémente toutes les règles spéciales :
- **Roque** : Géré par `peut_roquer()` et `executer_roque()`
- **Prise en passant** : Gérée par `peut_etre_pris_en_passant()` et `executer_en_passant()`
- **Promotion des pions** : Gérée par `promotion()` et `afficher_promotion()`

### Adaptabilité à différentes résolutions d'écran
L'interface s'adapte dynamiquement à la résolution de l'écran grâce à l'utilisation de dimensions relatives dans `FenetrePrincipale`.

## Extensions possibles du projet

Le code est structuré de façon modulaire pour faciliter d'éventuelles extensions :
- Ajout d'une IA pour jouer contre l'ordinateur
- Implémentation d'un mode multijoueur en réseau
- Sauvegarde et chargement de parties
- Analyse de parties et suggestions de coups
- Intégration de bases de données d'ouvertures d'échecs

## Conclusion

Ce projet présente une implémentation complète et modulaire du jeu d'échecs avec une séparation claire entre la logique du jeu et l'interface graphique. L'organisation en trois fichiers principaux permet une maintenance facile et des extensions futures.
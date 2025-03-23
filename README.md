# Jeu d'Échecs en Python

Une implémentation complète du jeu d'échecs avec interface graphique Pygame, multiples thèmes de couleurs, options de temps de jeu et toutes les règles officielles.

## 📋 Description

Ce projet est une implémentation complète du jeu d'échecs en Python utilisant la bibliothèque Pygame. Il offre une interface graphique personnalisable et inclut toutes les règles officielles des échecs.

## ✨ Fonctionnalités

- **Interface graphique complète** en plein écran s'adaptant à toutes les résolutions
- **18 thèmes de couleurs** pour le plateau
- **Modes de jeu variés** : blitz (3min, 5min), rapide (10min, 15min), classique (30min, 45min), sans limite
- **Orientation du plateau** ajustable (pièces blanches ou noires en bas)
- **Règles complètes des échecs** :
  - Mouvements spéciaux (roque, promotion des pions, prise en passant)
  - Détection automatique d'échec et d'échec et mat
  - Fin de partie par temps écoulé
- **Fonctionnalités de suivi de jeu** :
  - Chronomètre pour chaque joueur
  - Affichage des pièces capturées
  - Surlignage des déplacements possibles

## 🛠️ Installation

1. Clonez ce dépôt :
   ```
   git clone https://github.com/votre-pseudo/jeu-echec.git
   ```
2. Installez les dépendances requises :
   ```
   pip install -r requirements.txt
   ```

## 🎮 Comment jouer

1. Lancez le jeu avec :
   ```
   python src/main.py.py
   ```
2. Suivez les instructions à l'écran pour :
   - Choisir l'orientation du plateau
   - Sélectionner un thème de couleurs
   - Définir le temps de jeu
3. Pendant la partie :
   - Cliquez sur une pièce pour la sélectionner
   - Les déplacements valides seront surlignés en vert
   - Cliquez sur une case valide pour déplacer la pièce

## 🏗️ Structure du projet

```
jeu-echec/
├── data/            # Images des pièces et éléments graphiques
├── src/
│   ├── interface1.py  # Affichage du plateau et fenêtres de sélection
│   ├── Jeu_echec1.py  # Logique du jeu et règles des échecs
│   └── main.py.py     # Point d'entrée principal et interface utilisateur
├── .gitignore         # Fichiers ignorés par Git
├── LICENSE.md         # Licence du projet
├── README.md          # Ce fichier
└── requirements.txt   # Dépendances du projet
```

## 📦 Dépendances

- Python 3.x
- Pygame
- PyAutoGUI

## 🔄 Contributions

Ce projet est sous développement actif. Seuls les membres officiels du projet peuvent apporter des modifications au code source. Les suggestions et rapports de bugs sont toutefois les bienvenus via les issues GitHub.

## 📝 Licence

Ce projet est sous licence MIT modifiée. Vous pouvez jouer et distribuer ce jeu librement, mais seuls les membres officiels du projet peuvent modifier le code source. L'utilisation commerciale est interdite sans autorisation explicite.

## 👥 Auteurs

- Ce projet a été développé collectivement par l'équipe jeu-echec, composée de Natan Turc, Tidiane Cremer, Killian Mejean et Maëlan Sadoudi.

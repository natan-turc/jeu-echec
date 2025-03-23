#################################################################################################
# Ce programme contient l'affichage du plateau d'échec et des fenetres de choix précédants le jeu
# Jeu_echec1.py est appelé et utilisé par ce fichier
# Pour lancer le jeu, il faut lancer le programme interface21.py
#################################################################################################
import pygame
import pyautogui
import time
import os
from Jeu_echec1 import *

# initialisation de pygame
pygame.init()
dimension = 8
taille_case = 80
largeur = hauteur = dimension * taille_case
ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Jeu d'Échecs")

BLANC = (238, 238, 210)
NOIR = (118, 150, 86)

def afficher_selection_temps():
    LARGEUR, HAUTEUR = pyautogui.size()
    fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR), pygame.FULLSCREEN)
    pygame.display.set_caption("Choisissez la durée de la partie")
    
    # Options de temps en secondes
    TEMPS = {
        "Blitz (3 min)": 180,
        "Blitz (5 min)": 300,
        "Rapide (10 min)": 600,
        "Rapide (15 min)": 900,
        "Classique (30 min)": 1800,
        "Classique (45 min)": 2700,
        "Sans limite": float('inf')
    }
    
    # Paramètres boutons
    BOUTON_LARGEUR = 200
    BOUTON_HAUTEUR = 150
    ESPACEMENT = 30
    
    COLONNES = 4  # 4 boutons par ligne
    X_DEBUT = (LARGEUR - (COLONNES * BOUTON_LARGEUR + (COLONNES - 1) * ESPACEMENT)) // 2 
    Y_DEBUT = (HAUTEUR - (2 * BOUTON_HAUTEUR + ESPACEMENT)) // 2  # 2 lignes max

    boutons = {}
    x_actuel = X_DEBUT
    y_actuel = Y_DEBUT
    compteur = 0

    for option in TEMPS:
        if compteur % COLONNES == 0 and compteur > 0:
            x_actuel = X_DEBUT
            y_actuel += BOUTON_HAUTEUR + ESPACEMENT

        boutons[option] = pygame.Rect(x_actuel, y_actuel, BOUTON_LARGEUR, BOUTON_HAUTEUR)
        x_actuel += BOUTON_LARGEUR + ESPACEMENT
        compteur += 1
    
    # Police txt
    police = pygame.font.Font(None, 28)
    police_titre = pygame.font.Font(None, 75)
    

    # Couleurs
    FOND = (50, 50, 50)
    BOUTON_COULEUR = (100, 100, 100)
    TEXTE_COULEUR = (255, 255, 255)
    TITRE_COULEUR = (255, 255, 255)
    SURVOL_COULEUR = (200, 200, 200)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return TEMPS["Rapide (10 min)"]  # Valeur par défaut
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                afficher_quitter(event)
                for option, rect in boutons.items():
                    if rect.collidepoint(pos):
                        return TEMPS[option]

        fenetre.fill(FOND)

        # Titre
        titre = police_titre.render("Choisissez la durée de la partie", True, TITRE_COULEUR)
        fenetre.blit(titre, ((LARGEUR - titre.get_width()) // 2, 50))

        # Dessiner les boutons avec effet de survol
        pos_souris = pygame.mouse.get_pos()
        for option, rect in boutons.items():
            couleur = SURVOL_COULEUR if rect.collidepoint(pos_souris) else BOUTON_COULEUR
            pygame.draw.rect(fenetre, couleur, rect)

            texte = police.render(option, True, TEXTE_COULEUR)
            texte_rect = texte.get_rect(center=rect.center)
            fenetre.blit(texte, texte_rect)
        
            if option == "Sans limite":
                infini = police.render("infini", True, TEXTE_COULEUR)
                infini_rect = infini.get_rect(center=(rect.centerx, rect.centery + 30))
                fenetre.blit(infini, infini_rect)

        quitter_fenetre(fenetre)  
        pygame.display.flip()

def deconte(couleur, couleur_claire) :
    LARGEUR, HAUTEUR = pyautogui.size()
    fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR), pygame.FULLSCREEN)
    pygame.display.set_caption("Choisissez la durée de la partie")

    police2 = pygame.font.Font(None, 200)
    
    fenetre.fill(couleur)
    texte = police2.render("3",1,couleur_claire)
    fenetre.blit(texte, (LARGEUR//2.1, HAUTEUR//2.1))
    pygame.display.flip()
    time.sleep(1)
    fenetre.fill(couleur)
    texte = police2.render("2",1,couleur_claire)
    fenetre.blit(texte, (LARGEUR//2.1, HAUTEUR//2.1))
    pygame.display.flip()
    time.sleep(1)
    fenetre.fill(couleur)
    texte = police2.render("1",1,couleur_claire)
    fenetre.blit(texte, (LARGEUR//2.1, HAUTEUR//2.1))
    pygame.display.flip()
    time.sleep(1)
    fenetre.fill(couleur)
    texte = police2.render("Go !",1,couleur_claire)
    fenetre.blit(texte, (LARGEUR//2.3, HAUTEUR//2.2))
    pygame.display.flip()
    time.sleep(1)

# croix d'arret du jeu
def quitter_fenetre(fenetre, couleur = (0,0,0)) :
    chemin_image = os.sep.join(["data", "images", "croix.png"])
    image = pygame.image.load(chemin_image)
    largeur_bouton, hauteur_bouton = 50, 50
    image = pygame.transform.scale(image, (largeur_bouton, hauteur_bouton))
    fenetre.blit(image, (1317, 0))

def afficher_quitter(event)  :
    if event.type == pygame.MOUSEBUTTONDOWN:
        bouton = pygame.Rect(1317, 0, 50, 50)
        if bouton.collidepoint(pygame.mouse.get_pos()):
            pygame.quit()


# Chargement des images des pièces
def charger_pieces(lst, orientation):
    lst_pieces_blanches = [0]*5
    lst_pieces_noires = [0]*5
    pieces = []
    for lo in range(8):
        pieces.append([])
        for la in range(8):
            pion = lst[lo][la]
            if pion is not None:
                if pion.camp == 1 :
                    nom_fichier = pion.chemin()
                    img = pygame.image.load(nom_fichier)
                    img = pygame.transform.scale(img, (taille_case, taille_case))
                    if pion.type == 6 :
                        lst_pieces_blanches[0] += 1
                    elif pion.type == 3 :
                        lst_pieces_blanches[1] += 1
                    elif pion.type == 2 :
                        lst_pieces_blanches[2] += 1
                    elif pion.type == 4 :
                        lst_pieces_blanches[3] += 1
                    elif pion.type == 1 :
                        lst_pieces_blanches[4] += 1
                else : 
                    if orientation == 0 :
                        angle = 0
                    else :
                        angle = 180
                    nom_fichier = pion.chemin()
                    img = pygame.image.load(nom_fichier)
                    img = pygame.transform.scale(img, (taille_case, taille_case))
                    img = pygame.transform.rotate(img, angle)
                    if pion.type == 6 :
                        lst_pieces_noires[0] += 1
                    elif pion.type == 3 :
                        lst_pieces_noires[1] += 1
                    elif pion.type == 2 :
                        lst_pieces_noires[2] += 1
                    elif pion.type == 4 :
                        lst_pieces_noires[3] += 1
                    elif pion.type == 1 :
                        lst_pieces_noires[4] += 1
            else:
                img = None
            pieces[lo].append(img)
    return pieces, lst_pieces_blanches, lst_pieces_noires

def creer_surface_surbrillance(taille):
    surface = pygame.Surface((taille, taille), pygame.SRCALPHA)
    pygame.draw.rect(surface, (100, 200, 100, 180), (0, 0, taille, taille))  # Vert semi-transparent
    return surface

SURBRILLANCE = creer_surface_surbrillance(taille_case)

# Dessine l'échiquier
def dessiner_echiquier():
    for ligne in range(dimension):
        for colonne in range(dimension):
            couleur = BLANC if (ligne + colonne) % 2 == 0 else NOIR
            pygame.draw.rect(ecran, couleur, (colonne * taille_case, ligne * taille_case, taille_case, taille_case))

def afficher_promotion(ecran, camp):
    largeur_bouton = 100
    hauteur_bouton = 100
    espacement = 20
    largeur_totale = (largeur_bouton * 2) + (espacement * 3)
    hauteur_totale = (hauteur_bouton * 2) + (espacement * 3)
    
    x_debut = (ecran.get_width() - largeur_totale) // 2
    y_debut = (ecran.get_height() - hauteur_totale) // 2
    
    # Couleurs
    FOND = (255, 255, 255)
    BORDURE = (0, 0, 0)
    SURVOL = (200, 200, 200)

    overlay = pygame.Surface((ecran.get_width(), ecran.get_height()))
    overlay.set_alpha(128)
    overlay.fill((0, 0, 0))
    ecran.blit(overlay, (0, 0))
    
    # Définir les pièces et leurs images
    pieces = {
        'reine': pygame.image.load(os.sep.join(["data", "images", "reine gris.png"]) if camp else os.sep.join(["data", "images", "reine noir.png"])),
        'tour': pygame.image.load(os.sep.join(["data", "images", "tour gris.png"]) if camp else os.sep.join(["data", "images", "tour noir.png"])),
        'fou': pygame.image.load(os.sep.join(["data", "images", "fou gris.png"]) if camp else os.sep.join(["data", "images", "fou noir.png"])),
        'cavalier': pygame.image.load(os.sep.join(["data", "images", "cavalier gris.png"]) if camp else os.sep.join(["data", "images", "cavalier noir.png"]))
    }
    
    # Redimensionner images
    for piece in pieces:
        pieces[piece] = pygame.transform.scale(pieces[piece], (largeur_bouton - 20, hauteur_bouton - 20))
    
    # Positions boutons
    positions = {
        'reine': (x_debut + espacement, y_debut + espacement),
        'tour': (x_debut + largeur_bouton + espacement * 2, y_debut + espacement),
        'fou': (x_debut + espacement, y_debut + hauteur_bouton + espacement * 2),
        'cavalier': (x_debut + largeur_bouton + espacement * 2, y_debut + hauteur_bouton + espacement * 2)
    }
    
    while True:
        mouse_pos = pygame.mouse.get_pos()
        
        # Dessiner boutons
        for piece, pos in positions.items():
            rect = pygame.Rect(pos[0], pos[1], largeur_bouton, hauteur_bouton)
            couleur = SURVOL if rect.collidepoint(mouse_pos) else FOND

            pygame.draw.rect(ecran, couleur, rect)
            pygame.draw.rect(ecran, BORDURE, rect, 2)
            
            # Centrer l'image dans le bouton
            image_rect = pieces[piece].get_rect(center=rect.center)
            ecran.blit(pieces[piece], image_rect)
        
        # Mettre à jour 
        pygame.display.flip()
        
        # Gestion clics
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for piece, pos in positions.items():
                    rect = pygame.Rect(pos[0], pos[1], largeur_bouton, hauteur_bouton)
                    if rect.collidepoint(event.pos):
                        return piece

def afficher_choix_orientation():
    # Initialisation de la fenêtre
    LARGEUR, HAUTEUR = pyautogui.size() 
    fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR), pygame.FULLSCREEN)
    pygame.display.set_caption("Choisissez l'orientation du plateau")

    # Chargement des images
    chemin_image1 = os.sep.join(["data", "images", "o1.png"])
    chemin_image2 = os.sep.join(["data", "images", "o2.png"])
    image1 = pygame.image.load(chemin_image1)
    image2 = pygame.image.load(chemin_image2)

    largeur_bouton, hauteur_bouton = 200, 400
    x1, y1 = (LARGEUR // 3 - largeur_bouton // 2, HAUTEUR // 2 - hauteur_bouton // 2)
    x2, y2 = (2 * LARGEUR // 3 - largeur_bouton // 2, HAUTEUR // 2 - hauteur_bouton // 2)

    image1 = pygame.transform.scale(image1, (largeur_bouton, hauteur_bouton))
    image2 = pygame.transform.scale(image2, (largeur_bouton, hauteur_bouton))

    bouton1 = pygame.Rect(x1, y1, largeur_bouton, hauteur_bouton)
    bouton2 = pygame.Rect(x2, y2, largeur_bouton, hauteur_bouton)

    while True:
        fenetre.fill((0, 0, 0))

        font = pygame.font.Font(None, 75)
        texte = font.render("Choisissez l'orientation :", True, (255, 255, 255))
        fenetre.blit(texte, ((LARGEUR - texte.get_width()) // 2, 50))

        pygame.draw.rect(fenetre, (100, 100, 100), bouton1)
        pygame.draw.rect(fenetre, (100, 100, 100), bouton2)

        fenetre.blit(image1, (x1, y1))
        fenetre.blit(image2, (x2, y2))
        quitter_fenetre(fenetre)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                return 0
            afficher_quitter(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bouton1.collidepoint(event.pos):
                    return 1  # Joueur choisit l'orientation 1
                elif bouton2.collidepoint(event.pos):
                    return 0  # Joueur choisit l'orientation 0



def afficher_selection_couleurs():
    LARGEUR, HAUTEUR = pyautogui.size()
    fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR), pygame.FULLSCREEN)
    pygame.display.set_caption("Choisissez les couleurs du plateau")
    
    # Combinaisons de couleurs
    THEMES = {
    "Classique": [(238, 238, 210), (118, 150, 86), (60, 90, 40)],      # Beige et Vert (vert très foncé)
    "Bleu": [(235, 235, 235), (100, 140, 190), (30, 70, 120)],        # Blanc et Bleu (bleu très foncé)
    "Violet": [(235, 235, 235), (140, 100, 180), (60, 30, 100)],      # Blanc et Violet (violet profond)
    "Sépia": [(245, 230, 210), (110, 90, 70), (50, 30, 20)],          # Beige clair et Brun (brun très foncé)
    "Brun": [(235, 210, 180), (160, 100, 60), (80, 40, 20)],          # Beige et Brun (brun très foncé)
    "Rouge": [(240, 230, 230), (180, 90, 90), (90, 20, 20)],          # Blanc cassé et Rouge (rouge très foncé)
    "Gris": [(240, 240, 240), (120, 120, 120), (40, 40, 40)],         # Blanc et Gris (gris anthracite)
    "Gris foncé": [(220, 220, 220), (80, 80, 80), (60, 60, 60)],         # Gris clair et Gris foncé (gris encore plus foncé)
    "Noir et Blanc": [(255, 255, 255), (0, 0, 0), (50,50,50)],        # Blanc et Noir
    "Forêt": [(220, 230, 210), (90, 130, 70), (40, 80, 30)],         # Vert forêt et vert très foncé
    "Océan": [(220, 240, 250), (60, 120, 180), (20, 60, 120)],       # Bleu clair et bleu océan foncé
    "Aube": [(255, 230, 200), (200, 120, 80), (120, 50, 30)],        # Orange clair et marron foncé
    "Orage": [(200, 200, 220), (90, 90, 120), (30, 30, 60)],         # Gris bleu et bleu orage foncé
    "Sable": [(250, 240, 220), (190, 150, 100), (120, 80, 40)],      # Beige sable et brun foncé
    "Lave": [(250, 200, 150), (180, 70, 30), (100, 20, 10)],        # Orange feu et rouge lave foncé
    "Neon": [(230, 255, 230), (50, 255, 50), (20, 130, 20)],        # Vert clair et vert néon foncé
    "Espace": [(220, 220, 250), (50, 50, 120), (10, 10, 60)],       # Bleu spatial et bleu nuit profond
    "Or": [(255, 250, 220), (200, 160, 50), (120, 90, 20)]          # Or brillant et or foncé
    }

    
    # Paramètres boutons
    BOUTON_LARGEUR = 185
    BOUTON_HAUTEUR = 185
    ESPACEMENT = 20
    
    def dessiner_miniature_plateau(surface, x, y, largeur, hauteur, couleurs):
        taille_case = largeur // 8
        for ligne in range(8):
            for colonne in range(8):
                couleur = couleurs[0] if (ligne + colonne) % 2 == 0 else couleurs[1]
                pygame.draw.rect(surface, couleur, 
                               (x + colonne * taille_case, 
                                y + ligne * taille_case, 
                                taille_case, taille_case))
    
    COLONNES = 6  #6 boutons par ligne pour centrer
    X_DEBUT = (LARGEUR - (COLONNES * BOUTON_LARGEUR + (COLONNES - 1) * ESPACEMENT)) // 2 
    Y_DEBUT = (HAUTEUR - (3 * BOUTON_HAUTEUR + 2 * ESPACEMENT)) // 2 + 30 # 3 lignes max

    boutons = {}
    x_actuel = X_DEBUT
    y_actuel = Y_DEBUT
    compteur = 0

    for theme in THEMES:
        if compteur % COLONNES == 0 and compteur > 0:
            x_actuel = X_DEBUT
            y_actuel += BOUTON_HAUTEUR + ESPACEMENT

        boutons[theme] = pygame.Rect(x_actuel, y_actuel, BOUTON_LARGEUR, BOUTON_HAUTEUR)
        x_actuel += BOUTON_LARGEUR + ESPACEMENT
        compteur += 1
    
    # Police txt
    police = pygame.font.Font(None, 24)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return THEMES["Classique"]
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                afficher_quitter(event)
                for theme, rect in boutons.items():
                    if rect.collidepoint(pos):
                        return THEMES[theme]

        fenetre.fill((0,0,0))

        font=pygame.font.Font(None, 75)
        text = font.render("Choisissez un plateau de jeu : ",1,(255,255,255))
        fenetre.blit(text, (300, 25))

        # Dessiner les boutons et les miniatures
        for theme, rect in boutons.items():
            pygame.draw.rect(fenetre, (255, 255, 255), rect)
            pygame.draw.rect(fenetre, (0, 0, 0), rect, 2)
            
            # Dessiner la miniature
            marge = 10
            mini_largeur = BOUTON_LARGEUR - (marge * 2)
            mini_hauteur = (BOUTON_HAUTEUR * 2) // 3
            dessiner_miniature_plateau(fenetre, 
                                    rect.x + marge, 
                                    rect.y + 5, 
                                    mini_largeur, 
                                    mini_hauteur,
                                    THEMES[theme])
            
            # Ajouter txt thème
            texte = police.render(theme, True, (0, 0, 0))
            texte_rect = texte.get_rect(centerx=rect.centerx, 
                                      bottom=rect.bottom - 2)
            fenetre.blit(texte, texte_rect)

        quitter_fenetre(fenetre)  
        pygame.display.flip()

class JeuEchecs:
    def __init__(self):
        self.orientation = afficher_choix_orientation()
        self.COULEUR_CLAIRE, self.COULEUR_FONCEE, self.COULEUR_FOND = afficher_selection_couleurs()
        self.temps_partie = afficher_selection_temps()
        deconte(self.COULEUR_FOND, self.COULEUR_CLAIRE)
        self.plateau = self.creer_plateau()
        self.images_pieces, self.dico_b, self.dico_n = charger_pieces(self.plateau, self.orientation)
        self.piece_selectionnee = None
        self.deplacements_valides = []
        self.ligne_selectionnee = None
        self.colonne_selectionnee = None
        self.tour = 1  
        self.en_echec = False
        self.partie_terminee = False
        self.echec_blanc = False
        self.echec_noir = False
        self.surface = pygame.Surface((8 * 80, 8 * 80))  # Surface pour l'échiquier
        self.victoire_noir = pygame.image.load(os.sep.join(["data", "images", "NoirWin.png"]))
        self.victoire_blanc = pygame.image.load(os.sep.join(["data", "images", "BlancWin.png"]))
        


    def creer_plateau(self):
        liste = Lst_position[:]
        return liste

    def est_en_echec(self, camp):
        # Trouver roi
        roi = None
        position_roi = None
        for i in range(8):
            for j in range(8):
                piece = self.plateau[i][j]
                if piece and piece.type == 5 and piece.camp == camp:
                    roi = piece
                    position_roi = (i, j)
                    break
            if roi:
                break

        # Vérifier échec
        for i in range(8):
            for j in range(8):
                piece = self.plateau[i][j]
                if piece and piece.camp != camp:
                    deplacements = piece.deplacements_possibles()
                    if position_roi in deplacements:
                        return True
        return False

    def simule_deplacement(self, depart, arrivee):
        piece_depart = self.plateau[depart[0]][depart[1]]
        piece_arrivee = self.plateau[arrivee[0]][arrivee[1]]
        
        # Simuler le déplacement
        self.plateau[arrivee[0]][arrivee[1]] = piece_depart
        self.plateau[depart[0]][depart[1]] = None
        
        # Vérifier si le roi est en échec après le déplacement
        en_echec = self.est_en_echec(piece_depart.camp)
        
        # Restaurer état initial
        self.plateau[depart[0]][depart[1]] = piece_depart
        self.plateau[arrivee[0]][arrivee[1]] = piece_arrivee
        
        return not en_echec

    def est_mat(self):
        camp_actuel = self.tour
        for i in range(8):
            for j in range(8):
                piece = self.plateau[i][j]
                if piece and piece.camp == camp_actuel:
                    deplacements = piece.deplacements_possibles()
                    for deplacement in deplacements:
                        if self.simule_deplacement((i, j), deplacement):
                            return False
        return True

    def filtrer_deplacements_echec(self, ligne, colonne, deplacements):
        deplacements_valides = []
        
        for deplacement in deplacements:
            if self.simule_deplacement((ligne, colonne), deplacement):
                deplacements_valides.append(deplacement)
                
        return deplacements_valides

    def selectionner_piece(self, ligne, colonne):
        piece = self.plateau[ligne][colonne]
        if piece and piece.camp == self.tour:
            self.piece_selectionnee = piece
            self.ligne_selectionnee = ligne
            self.colonne_selectionnee = colonne
            deplacements = piece.deplacements_possibles()
            self.deplacements_valides = self.filtrer_deplacements_echec(ligne, colonne, deplacements)
        else:
            self.piece_selectionnee = None
            self.deplacements_valides = []

    def deplacer_piece(self, ligne, colonne):
        self.echec_blanc = False
        self.echec_noir = False
        if self.piece_selectionnee and (ligne, colonne) in self.deplacements_valides:
            piece = self.piece_selectionnee
            pos_depart = (self.ligne_selectionnee, self.colonne_selectionnee)
            pos_arrivee = (ligne, colonne)

            # Vérifier si c un roque
            if piece.type == 5 and abs(colonne - self.colonne_selectionnee) == 2:
                executer_roque(piece, pos_arrivee)
                
            # Vérifier si c une prise en passant
            elif piece.type == 6 and colonne != self.colonne_selectionnee and self.plateau[ligne][colonne] is None:
                executer_en_passant(piece, pos_arrivee)
                
            else:
                self.plateau[ligne][colonne] = piece
                self.plateau[self.ligne_selectionnee][self.colonne_selectionnee] = None

                # Marquer les pièces comme ayant bougé pour roque
                if piece.type in [5, 4]:  # Roi ou Tour
                    piece.a_bouge = True
                
                # Vérifier la prise en passant
                if piece.type == 6:
                    piece.peut_etre_pris_en_passant(pos_depart, pos_arrivee)
                    piece.bouger = False

                # Vérifier la promotion du pion
                if piece.type == 6 and piece.promotion((ligne, colonne)):
                    
                    nouvelle_piece = None
                    choix = afficher_promotion(ecran, piece.camp) 
                    
                    if choix == 'reine':
                        nouvelle_piece = Reine(piece.camp, os.sep.join(["data", "images", "reine noir.png"]) if piece.camp == 0 else os.sep.join(["data", "images", "reine gris.png"]))
                    elif choix == 'cavalier':
                        nouvelle_piece = Cavalier(piece.camp, os.sep.join(["data", "images", "cavalier noir.png"]) if piece.camp == 0 else os.sep.join(["data", "images", "cavalier gris.png"]))
                    elif choix == 'tour':
                        nouvelle_piece = Tour(piece.camp, os.sep.join(["data", "images", "tour noir.png"]) if piece.camp == 0 else os.sep.join(["data", "images", "tour gris.png"]))
                    elif choix == 'fou':
                        nouvelle_piece = Fou(piece.camp, os.sep.join(["data", "images", "fou noir.png"]) if piece.camp == 0 else os.sep.join(["data", "images", "fou gris.png"]))
                    
                    self.plateau[ligne][colonne] = nouvelle_piece

            # Réinitialiser le en_passant 
            for i in range(8):
                for j in range(8):
                    p = self.plateau[i][j]
                    if p and p.type == 6 and p.camp != piece.camp:
                        p.en_passant = False

            # Mettre à jour l'affichage et changer de tour
            self.piece_selectionnee = None
            self.deplacements_valides = []
            self.images_pieces, self.dico_b, self.dico_n = charger_pieces(self.plateau, self.orientation)
            self.tour = 1 - self.tour


                
    # Trouve la zone cliquée
    def gerer_clic(self, pos):
        if not self.partie_terminee:
            colonne = pos[0] // taille_case
            ligne = pos[1] // taille_case
            piece = self.plateau[ligne][colonne]

            if self.piece_selectionnee:
                if piece and piece.camp == self.tour:
                    self.selectionner_piece(ligne, colonne)
                else:
                    self.deplacer_piece(ligne, colonne)
            else:
                self.selectionner_piece(ligne, colonne)

    # Dessine le plateau (dans la fenetre)
    def dessiner_plateau(self):
        for ligne in range(8):
            for colonne in range(8):
                couleur = self.COULEUR_CLAIRE if (ligne + colonne) % 2 == 0 else self.COULEUR_FONCEE
                pygame.draw.rect(self.surface, couleur, (colonne * 80, ligne * 80, 80, 80))

        for move in self.deplacements_valides:
            self.surface.blit(SURBRILLANCE, (move[1] * 80, move[0] * 80))

        for ligne in range(8):
            for colonne in range(8):
                img = self.images_pieces[ligne][colonne]
                if img is not None:
                    self.surface.blit(img, (colonne * 80, ligne * 80))

# Fonction de test pour vérifier le fonctionnemennt de cette partie
def main():
    jeu = JeuEchecs()

    en_cours = True
    while en_cours:
        ecran.fill((0, 0, 0)) 
        jeu.dessiner_plateau() 

        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                en_cours = False
            elif evenement.type == pygame.MOUSEBUTTONDOWN:
                jeu.gerer_clic(pygame.mouse.get_pos())  # Gestion de la sélection et du déplacement des pièces

        pygame.display.flip()

    pygame.quit()
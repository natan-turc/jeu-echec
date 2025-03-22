#################################################################################################
# Ce programme contient l'affichage du plateau d'échec et des fenetres de choix précédants le jeu
# interface1.py est appelé et utilisé par ce fichier
# Pour lancer le jeu, il faut lancer le programme interface21.py
#################################################################################################
import pygame
import sys
import os
import time
from interface1 import JeuEchecs, quitter_fenetre, afficher_quitter  # Importe ton jeu d'échecs

# Classe principale affichant la fenetre finale du jeu
class FenetrePrincipale:
    def __init__(self):
        pygame.init()
        self.ecran = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # Plein écran
        self.largeur, self.hauteur = self.ecran.get_size()
        pygame.display.set_caption("Jeu d'Échecs - Mode Plein Écran")
        self.couleur = (255,255,255)

        self.jeu = JeuEchecs()
        self.fond = self.jeu.COULEUR_FOND

        self.taille_case = int(self.hauteur * 0.104)
        self.taille_plateau = 8 * self.taille_case
        self.x_offset = (self.largeur - self.taille_plateau) // 2
        self.y_offset = (self.hauteur - self.taille_plateau) // 2 

        self.temps_total = self.jeu.temps_partie
        self.temps_blanc = self.temps_total
        self.temps_noir = self.temps_total
        self.dernier_changement = time.time()
        self.tour_precedent = self.jeu.tour
        self.sans_limite = (self.temps_total == float('inf'))

        # Boucle principale
        self.boucle_principale()

    # Affichage tour de jeu
    def texte_echec(self) :
        if self.jeu.tour == 1 :
            font = pygame.font.Font(None, int(self.hauteur * 0.098))  
            text = font.render("Les blancs jouent", 1, self.couleur)
            self.ecran.blit(text, (int(self.largeur * 0.329), int(self.hauteur * 0.007)))  
        else :
            if self.jeu.orientation == 1 : 
                angle = 1
            else :
                angle = 0
            font = pygame.font.Font(None, int(self.hauteur * 0.098)) 
            text = font.render("Les noirs jouent", 1, self.couleur)
            text = pygame.transform.rotate(text, angle*180)
            y_pos = angle * int(self.hauteur * 0.918) + int(self.hauteur * 0.007) 
            self.ecran.blit(text, (int(self.largeur * 0.329 + self.largeur * 0.05 * angle), y_pos))

    # Affichage icone et nom joueur blanc
    def infos_blancs(self) :
        font = pygame.font.Font(None, int(self.hauteur * 0.065)) 
        text1 = font.render("Joueur blanc", 1, self.couleur)
        nom_fichier = os.sep.join(["images", "IconeGris.png"])
        img = pygame.image.load(nom_fichier)
        img_width = int(self.largeur * 0.092)   
        img_height = int(self.hauteur * 0.13)  
        img = pygame.transform.scale(img, (img_width, img_height))
        self.ecran.blit(img, (0, int(self.hauteur * 0.065))) 
        self.ecran.blit(text1, (int(self.largeur * 0.092), int(self.hauteur * 0.111)))
    
    # Affichage icone et nom joueur noir
    def infos_noirs(self) :
        if self.jeu.orientation == 1 : 
            angle = 1
        else :
            angle = 0
        font = pygame.font.Font(None, int(self.hauteur * 0.065))  
        text2 = font.render("Joueur noir", 1, self.couleur)
        text2 = pygame.transform.rotate(text2, angle*180)
        nom_fichier = os.sep.join(["images", "IconeNoir.png"])
        img = pygame.image.load(nom_fichier)
        img_width = int(self.largeur * 0.092)  
        img_height = int(self.hauteur * 0.13)  
        img = pygame.transform.scale(img, (img_width, img_height))
        img = pygame.transform.rotate(img, angle*180)
    
        x_img = int(self.largeur * 0.915) 
        y_img = int(self.hauteur * 0.065) + int(self.hauteur * 0.729) * angle 
        x_text = int(self.largeur * 0.769) 
        y_text = int(self.hauteur * 0.111) + int(self.hauteur * 0.729) * angle 
        
        self.ecran.blit(img, (x_img, y_img))
        self.ecran.blit(text2, (x_text, y_text))

    # Affichage pieces restantes blanches
    def afficher_conteur_p_b(self) :
        font = pygame.font.Font(None, int(self.hauteur * 0.098))  
        lst = [os.sep.join(["images", "pion gris.png"]), os.sep.join(["images", "cavalier gris.png"]), os.sep.join(["images", "fou gris.png"]), os.sep.join(["images", "tour gris.png"]), os.sep.join(["images", "reine gris.png"])]
        icon_size = int(self.hauteur * 0.098) 
        for i in range(5) :
            texte = font.render(f" : {str(self.jeu.dico_b[i])}", 1, self.couleur)
            img = pygame.image.load(lst[i])
            img = pygame.transform.scale(img, (icon_size, icon_size))
            y_img = int(self.hauteur * 0.456) + i * icon_size  
            y_text = int(self.hauteur * 0.482) + i * icon_size
            self.ecran.blit(img, (0, y_img))
            self.ecran.blit(texte, (int(self.largeur * 0.037), y_text))
            
        if self.jeu.echec_blanc is True :
            font2 = pygame.font.Font(None, int(self.hauteur * 0.065))  
            texte = font2.render("Vous êtes en échec", 1, self.couleur)
            self.ecran.blit(texte, (int(self.largeur * 0.007), int(self.hauteur * 0.221)))  
    
    # Affichage pieces restantes noires
    def afficher_conteur_p_n(self) :
        if self.jeu.orientation == 1 : 
            font = pygame.font.Font(None, int(self.hauteur * 0.098)) 
            lst = [os.sep.join(["images", "reine noir.png"]), os.sep.join(["images", "tour noir.png"]), os.sep.join(["images", "fou noir.png"]), os.sep.join(["images", "cavalier noir.png"]), os.sep.join(["images", "pion noir.png"])]
            icon_size = int(self.hauteur * 0.104)  
            
            for i in range(5) :
                texte = font.render(f" : {str(self.jeu.dico_n[i])}", 1, self.couleur)
                texte = pygame.transform.rotate(texte, 180)
                img = pygame.image.load(lst[i])
                img = pygame.transform.scale(img, (icon_size, icon_size))
                img = pygame.transform.rotate(img, 180)
                x_img = int(self.largeur * 0.915)  
                y_img = int(self.hauteur * 0.065) + i * icon_size 
                x_text = int(self.largeur * 0.879) 
                y_text = int(self.hauteur * 0.462) - i * icon_size  
                
                self.ecran.blit(img, (x_img, y_img))
                self.ecran.blit(texte, (x_text, y_text))
                
            if self.jeu.echec_noir is True :
                font2 = pygame.font.Font(None, int(self.hauteur * 0.065))
                texte = font2.render("Vous êtes en échec", 1, self.couleur)
                texte = pygame.transform.rotate(texte, 180)
                self.ecran.blit(texte, (int(self.largeur * 0.75), int(self.hauteur * 0.716)))
        else :
            font = pygame.font.Font(None, int(self.hauteur * 0.098))  
            lst = [os.sep.join(["images", "pion noir.png"]), os.sep.join(["images", "cavalier noir.png"]), os.sep.join(["images", "fou noir.png"]), os.sep.join(["images", "tour noir.png"]), os.sep.join(["images", "reine noir.png"])]
            icon_size = int(self.hauteur * 0.098)  
            for i in range(5) :
                texte = font.render(f" : {str(self.jeu.dico_n[i])}", 1, self.couleur)
                img = pygame.image.load(lst[i])
                img = pygame.transform.scale(img, (icon_size, icon_size))
                x_img = int(self.largeur * 0.879) 
                y_img = int(self.hauteur * 0.456) + i * icon_size 
                x_text = int(self.largeur * 0.915) 
                y_text = int(self.hauteur * 0.482) + i * icon_size 
                
                self.ecran.blit(img, (x_img, y_img))
                self.ecran.blit(texte, (x_text, y_text))
                
            if self.jeu.echec_noir is True :
                font2 = pygame.font.Font(None, int(self.hauteur * 0.065))  
                texte = font2.render("Vous êtes en échec", 1, self.couleur)
                self.ecran.blit(texte, (int(self.largeur * 0.75), int(self.hauteur * 0.221)))  
    
    # Affichage fenetre de win du camp gagnant
    def affichage_echec(self) :
        if self.jeu.est_en_echec(self.jeu.tour):
            if self.jeu.est_mat() :
                largeur_ecran, hauteur_ecran = self.largeur, self.hauteur
                if self.jeu.tour == 1 :
                    if self.jeu.orientation == 1 :
                        self.jeu.victoire_noir = pygame.transform.rotate(self.jeu.victoire_noir, 180)
                    nouvelle_largeur = int(largeur_ecran * 0.6)
                    nouvelle_hauteur = int(hauteur_ecran * 1.2)
                    self.jeu.victoire_noir = pygame.transform.scale(self.jeu.victoire_noir, (nouvelle_largeur, nouvelle_hauteur))
                    self.ecran.fill(self.fond)
                    self.bouton_rejouer()
                    quitter_fenetre(self.ecran, self.fond)
                    x = (largeur_ecran - nouvelle_largeur) // 2  
                    y = (hauteur_ecran - nouvelle_hauteur) // 2
                    self.ecran.blit(self.jeu.victoire_noir, (x, y))
                    pygame.display.flip()

                    running = True
                    while running:
                        for event in pygame.event.get():
                            afficher_quitter(event)
                            self.afficher_rejouer(event)
                            if event.type == pygame.QUIT:
                                    running = False
                else :
                    self.ecran.fill(self.fond)
                    self.bouton_rejouer()
                    quitter_fenetre(self.ecran, self.fond)
                    nouvelle_largeur = int(largeur_ecran * 0.6)
                    nouvelle_hauteur = int(hauteur_ecran * 0.7)
                    self.jeu.victoire_blanc = pygame.transform.scale(self.jeu.victoire_blanc, (nouvelle_largeur, nouvelle_hauteur))

                    x = (largeur_ecran - nouvelle_largeur) // 2
                    y = (hauteur_ecran - nouvelle_hauteur) // 2
                    self.ecran.blit(self.jeu.victoire_blanc, (x, y))
                    pygame.display.flip()

                    running = True
                    while running:
                        for event in pygame.event.get():
                            afficher_quitter(event)
                            self.afficher_rejouer(event)
                            if event.type == pygame.QUIT:
                                running = False
                self.jeu.partie_terminee = True
            else :
                if self.jeu.tour == 1 :
                    self.jeu.echec_blanc = True
                else :
                    self.jeu.echec_noir = True
                
    # création du bouton rejouer en fin de partie
    def bouton_rejouer(self) :
        bouton_largeur = int(self.largeur * 0.183) 
        bouton_hauteur = int(self.hauteur * 0.13) 
        bouton_x = int(self.largeur * 0.403) 
        bouton_y = int(self.hauteur * 0.781)  
        
        self.bouton_rect = pygame.Rect(bouton_x, bouton_y, bouton_largeur, bouton_hauteur)
        pygame.draw.rect(self.ecran, self.jeu.COULEUR_FONCEE, self.bouton_rect)
        font = pygame.font.Font(None, int(self.hauteur * 0.098))  
        texte = font.render("Rejouer", 1, self.couleur)
        text_rect = texte.get_rect(center=self.bouton_rect.center)
        self.ecran.blit(texte, text_rect)

    # Test d'activation du bouton rejouer
    def afficher_rejouer(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN :
            pygame.init()
            # Relance totalement le programme pour une nouvelle partie
            if self.bouton_rect.collidepoint(pygame.mouse.get_pos()) :
                pygame.quit()
                python = sys.executable
                os.execl(python, python, *sys.argv)

    # Affichage des chronos
    def afficher_chrono(self) :
        largeur_chrono = int(self.largeur * 0.16)
        hauteur_chrono = int(self.hauteur * 0.13)
        x_blanc = int(self.largeur * 0.01)
        y_blanc = int(self.hauteur * 0.3)
        x_noir = int(self.largeur * 0.82)
        y_noir = int(self.hauteur * 0.57)
        font = pygame.font.Font(None, int(self.hauteur * 0.14))

        if self.sans_limite :
            texte_infini_blanc = font.render("infini", True, self.couleur)
            pygame.draw.rect(self.ecran, self.jeu.COULEUR_FONCEE, (x_blanc, y_blanc, largeur_chrono, hauteur_chrono))
            self.ecran.blit(texte_infini_blanc, (x_blanc, y_blanc + int(self.hauteur * 0.026)))  

            texte_infini_noir = font.render("infini", True, self.couleur)
            if self.jeu.orientation == 1 :
                texte_infini_noir = pygame.transform.rotate(texte_infini_noir, 180)
            pygame.draw.rect(self.ecran, self.jeu.COULEUR_FONCEE, (x_noir, y_noir, largeur_chrono, hauteur_chrono))
            self.ecran.blit(texte_infini_noir, (x_noir, y_noir + int(self.hauteur * 0.026))) 

            return

        if not self.jeu.partie_terminee :
            temps_actuel = time.time()
            temps_ecoule = temps_actuel - self.dernier_changement

            if self.tour_precedent != self.jeu.tour:
                self.dernier_changement = temps_actuel
                self.tour_precedent = self.jeu.tour
            else:
                if self.jeu.tour == 1 : 
                    self.temps_blanc -= temps_ecoule
                    if self.temps_blanc <= 0 :
                        self.temps_blanc = 0
                        self.fin_partie_temps("noir")
                else :  
                    self.temps_noir -= temps_ecoule
                    if self.temps_noir <= 0 :
                        self.temps_noir = 0
                        self.fin_partie_temps("blanc")
                
                self.dernier_changement = temps_actuel

        mins_blanc, secs_blanc = divmod(int(self.temps_blanc), 60)
        mins_noir, secs_noir = divmod(int(self.temps_noir), 60)

        texte_chrono_blanc = font.render(f"{mins_blanc:02d}:{secs_blanc:02d}", True, self.couleur)
        pygame.draw.rect(self.ecran, self.jeu.COULEUR_FONCEE, (x_blanc, y_blanc, largeur_chrono, hauteur_chrono))
        self.ecran.blit(texte_chrono_blanc, (x_blanc + int(self.largeur * 0.007), y_blanc + int(self.hauteur * 0.026))) 

        texte_chrono_noir = font.render(f"{mins_noir:02d}:{secs_noir:02d}", True, self.couleur)
        if self.jeu.orientation == 1 :
            x_noir = int(self.largeur * 0.82)
            y_noir = int(self.hauteur * 0.57)
            texte_chrono_noir = pygame.transform.rotate(texte_chrono_noir, 180)

        pygame.draw.rect(self.ecran, self.jeu.COULEUR_FONCEE, (x_noir, y_noir, largeur_chrono, hauteur_chrono))
        self.ecran.blit(texte_chrono_noir, (x_noir + int(self.largeur * 0.007), y_noir + int(self.hauteur * 0.013))) 

    # Affichage des fenetres de win à cause du temps (optimal car trop complexe à integrer a self.affichage_echec)
    def fin_partie_temps(self, gagnant) :
        self.jeu.partie_terminee = True
        largeur_ecran, hauteur_ecran = self.largeur, self.hauteur
        nouvelle_largeur = int(largeur_ecran * 0.6)
        nouvelle_hauteur = int(hauteur_ecran * 1.2)
        if gagnant == "noir" :
            self.jeu.tour = 1  
            
            if self.jeu.orientation == 1 :
                self.jeu.victoire_noir = pygame.transform.rotate(self.jeu.victoire_noir, 180)
            self.jeu.victoire_noir = pygame.transform.scale(self.jeu.victoire_noir, (nouvelle_largeur, nouvelle_hauteur))
            
            self.ecran.fill(self.fond)
            self.bouton_rejouer()
            quitter_fenetre(self.ecran, self.fond)
            
            x = (largeur_ecran - nouvelle_largeur) // 2  
            y = (hauteur_ecran - nouvelle_hauteur) // 2  
            self.ecran.blit(self.jeu.victoire_noir, (x, y))
        
        else:
            self.jeu.tour = 0  
            
            self.ecran.fill(self.fond)
            self.bouton_rejouer()
            quitter_fenetre(self.ecran, self.fond)
            
            nouvelle_largeur = int(largeur_ecran * 0.6)
            nouvelle_hauteur = int(hauteur_ecran * 0.7)
            self.jeu.victoire_blanc = pygame.transform.scale(self.jeu.victoire_blanc, (nouvelle_largeur, nouvelle_hauteur))
            
            x = (largeur_ecran - nouvelle_largeur) // 2
            y = (hauteur_ecran - nouvelle_hauteur) // 2
            self.ecran.blit(self.jeu.victoire_blanc, (x, y))
        
        pygame.display.flip()
        
        # Boucle d'attente pour rejouer ou quitter
        running = True
        while running:
            for event in pygame.event.get():
                afficher_quitter(event)
                self.afficher_rejouer(event)
                if event.type == pygame.QUIT:
                    running = False

    # Boucle regroupant tous les affichages créés précédemment sous forme de boucle tant que le jeu est en cours
    def boucle_principale(self) :
        en_cours = True
        clock = pygame.time.Clock()
        while en_cours:
            self.ecran.fill(self.fond)
            self.dessiner_zone_echecs()
            self.texte_echec()
            self.infos_blancs()
            self.infos_noirs()
            self.afficher_chrono()
            self.afficher_conteur_p_b()
            self.afficher_conteur_p_n()
            self.affichage_echec()
            quitter_fenetre(self.ecran, self.fond)

            for event in pygame.event.get() :
                afficher_quitter(event)
                if event.type == pygame.QUIT :
                    en_cours = False
                elif event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_ESCAPE :  # Quitter avec Échap
                        en_cours = False
                elif event.type == pygame.MOUSEBUTTONDOWN :
                    pos = pygame.mouse.get_pos()
                    if self.est_dans_zone_echecs(pos) :
                        self.jeu.gerer_clic((pos[0] - self.x_offset, pos[1] - self.y_offset))
                    

            pygame.display.flip()
            clock.tick(30)
        pygame.quit()

    def dessiner_zone_echecs(self) :
        self.jeu.dessiner_plateau()  # Met à jour la surface d'échecs
        self.ecran.blit(self.jeu.surface, (self.x_offset, self.y_offset))  # Affiche sur l'écran principal

    # Gesttion du clic (dans la zone d'échec créée)
    def est_dans_zone_echecs(self, pos) :
        x, y = pos
        return (self.x_offset <= x <= self.x_offset + self.taille_plateau and
                self.y_offset <= y <= self.y_offset + self.taille_plateau)

# Lancer la fenêtre principale
if __name__ == "__main__":
    FenetrePrincipale()
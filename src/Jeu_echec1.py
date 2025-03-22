#################################################################################################
# Dans ce programme, il y a les mouvements (via des méthodes) de tous les types de pièces.
# Ces mouvements sont vérifiés avant leur execution puis affichage 
# Les pièces sont stockées dans une liste qui est ensuite utilisée pour les afficher.
# Pour lancer le jeu, il faut lancer le programme interface21.py
#################################################################################################
import os

class Pion :
    
    def __init__(self, camp=0, representation=os.sep.join(["images", "pion noir.png"])):
        self.camp = camp
        self.representation = representation
        self.type = 6
        self.bouger = True
        self.en_passant = False  
    
    def position(self, Lst_position) :
        for t in range(8) :
            for z in range(8) :
                if self == Lst_position[t][z] :
                    return t, z  

    def peut_etre_pris_en_passant(self, position_depart, position_arrivee):
        if abs(position_arrivee[0] - position_depart[0]) == 2:
            self.en_passant = True
            return True
        return False

    def deplacements_possibles(self):
        positions = []
        t, z = self.position(Lst_position)
        if self.camp == 0:
            y = 1
        else:
            y = -1  
        if verification_deplacement_valide(self, (t+y, z), Lst_position):
            positions.append((t+y, z))
        if self.bouger and verification_deplacement_valide(self, (t+2*y, z), Lst_position):
            positions.append((t+2*y, z))
        if verification_deplacement_valide(self, (t+y, z-1), Lst_position):
            positions.append((t+y, z-1))
        if verification_deplacement_valide(self, (t+y, z+1), Lst_position):
            positions.append((t+y, z+1))

        if self.camp == 0 and t == 4 or self.camp == 1 and t == 3:
            for dz in [-1, 1]:
                if 0 <= z + dz <= 7:
                    piece_adjacente = Lst_position[t][z + dz]
                    if (piece_adjacente is not None and 
                        piece_adjacente.type == 6 and 
                        piece_adjacente.camp != self.camp and 
                        piece_adjacente.en_passant):
                        positions.append((t+y, z+dz))

        return positions

    def promotion(self, position):
        t, z = position
        if (self.camp == 0 and t == 7) or (self.camp == 1 and t == 0):
            return True
        return False
    
    def chemin(self):
        return self.representation
        
class Roi:
    def __init__(self, camp=0, representation=os.sep.join(["images", "roi noir.png"])):
        self.camp = camp
        self.representation = representation
        self.type = 5
        self.a_bouge = False 

    def position(self, Lst_position) :
        for t in range(8) :
            for z in range(8) :
                if self == Lst_position[t][z] :
                    return t, z  

    def peut_roquer(self, cote_roi):
        ligne, colonne = self.position(Lst_position)
        
        if self.a_bouge:
            return False
        
        if cote_roi:
            if Lst_position[ligne][colonne+1] is not None or Lst_position[ligne][colonne+2] is not None:
                return False
            
            tour = Lst_position[ligne][7]
            if tour is None or tour.type != 4 or tour.a_bouge:
                return False
            
            if est_case_attaquee(ligne, colonne, self.camp, ignore_castling=True):
                return False
            if est_case_attaquee(ligne, colonne+1, self.camp, ignore_castling=True):
                return False
            if est_case_attaquee(ligne, colonne+2, self.camp, ignore_castling=True):
                return False
        else:
            if (Lst_position[ligne][colonne-1] is not None or 
                Lst_position[ligne][colonne-2] is not None or 
                Lst_position[ligne][colonne-3] is not None):
                return False
            
            tour = Lst_position[ligne][0]
            if tour is None or tour.type != 4 or tour.a_bouge:
                return False
            
            if est_case_attaquee(ligne, colonne, self.camp, ignore_castling=True):
                return False
            if est_case_attaquee(ligne, colonne-1, self.camp, ignore_castling=True):
                return False
            if est_case_attaquee(ligne, colonne-2, self.camp, ignore_castling=True):
                return False
        
        return True

    def deplacements_sans_roque(self):
        deplacements = []
        ligne, colonne = self.position(Lst_position)
        
        for dl in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dl == 0 and dc == 0:
                    continue
                
                nl, nc = ligne + dl, colonne + dc
                if 0 <= nl < 8 and 0 <= nc < 8:
                    if Lst_position[nl][nc] is None or Lst_position[nl][nc].camp != self.camp:
                        deplacements.append((nl, nc))
        
        return deplacements

    def deplacements_possibles(self):
        positions = []
        t, z = self.position(Lst_position)
        
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), 
                     (0, 1), (1, -1), (1, 0), (1, 1)]
        for dx, dy in directions:
            if verification_deplacement_valide(self, (t+dx, z+dy), Lst_position):
                positions.append((t+dx, z+dy))

        if not self.a_bouge:
            # Petit roque
            if self.peut_roquer(True):
                positions.append((t, z+2))
            # Grand roque
            if self.peut_roquer(False):
                positions.append((t, z-2))

        return positions

    def chemin(self):
        return self.representation
        
class Cavalier :
    
    def __init__(self, camp=0, representation = os.sep.join(["images", "cavalier noir.png"])):
        self.camp = camp
        self.representation = representation
        self.type = 3
    
    def position(self, Lst_position) :
        for t in range(8) :
            for z in range(8) :
                if self == Lst_position[t][z] :
                    return t, z   
                        
    def deplacements_possibles(self) :
        positions = []
        t, z = self.position(Lst_position)
        if self.camp == 0 :
            y = 1
        else : 
            y = -1
        if verification_deplacement_valide(self, (t-y, z-2*y), Lst_position) :
            positions.append((t-y, z-2*y))
        if verification_deplacement_valide(self, (t+y, z-2*y), Lst_position) :
            positions.append((t+y, z-2*y))
        if verification_deplacement_valide(self, (t+y, z+2*y), Lst_position) :
            positions.append((t+y, z+2*y))
        if verification_deplacement_valide(self, (t-y, z+2*y), Lst_position) :
            positions.append((t-y, z+2*y))
        if verification_deplacement_valide(self, (t-2*y, z+y), Lst_position) :
            positions.append((t-2*y, z+y))
        if verification_deplacement_valide(self, (t-2*y, z-y), Lst_position) :
            positions.append((t-2*y, z-y))
        if verification_deplacement_valide(self, (t+2*y, z-y), Lst_position) :
            positions.append((t+2*y, z-y))
        if verification_deplacement_valide(self, (t+2*y, z+y), Lst_position) :
            positions.append((t+2*y, z+y))
        return positions

    def chemin(self):
        return self.representation
    
class Fou :
    
    def __init__(self, camp=0, representation = os.sep.join(["images", "fou noir.png"])):
        self.camp = camp
        self.representation = representation
        self.type = 2
    
    def position(self, Lst_position) :
        for t in range(8) :
            for z in range(8) :
                if self == Lst_position[t][z] :
                    return t, z
            
    def deplacements_possibles(self) :
        positions = []
        t, z = self.position(Lst_position)
        if self.camp == 0 :
            y = 1
        else : 
            y = -1
        for i in range(1,8) :
            if verification_deplacement_valide(self, (t+y*i, z+y*i), Lst_position) :
                positions.append((t+y*i, z+y*i))
        for i in range(1,8) :
            if verification_deplacement_valide(self, (t-y*i, z+y*i), Lst_position) :
                positions.append((t-y*i, z+y*i))
        for i in range(1,8) :
            if verification_deplacement_valide(self, (t+y*i, z-y*i), Lst_position) :
                positions.append((t+y*i, z-y*i))
        for i in range(1,8) :
            if verification_deplacement_valide(self, (t-y*i, z-y*i), Lst_position) :
                positions.append((t-y*i, z-y*i))
        return positions
    
    def chemin(self):
        return self.representation
        
class Tour :
    
    def __init__(self, camp=0, representation = os.sep.join(["images", "tour noir.png"])):
            self.camp = camp
            self.representation = representation
            self.type = 4
            self.a_bouge = False
    
    def position(self, Lst_position) :
        for t in range(8) :
            for z in range(8) :
                if self == Lst_position[t][z] :
                    return t, z
                
    def deplacements_possibles(self) :
        positions = []
        t, z = self.position(Lst_position)
        if self.camp == 0 :
            y = 1
        else : 
            y = -1
        for i in range(1,8) :
            if verification_deplacement_valide(self, (t+y*i, z), Lst_position) :
                positions.append((t+y*i, z))
        for i in range(1,8) :
            if verification_deplacement_valide(self, (t-y*i, z), Lst_position) :
                positions.append((t-y*i, z))
        for i in range(1,8) :
            if verification_deplacement_valide(self, (t, z-y*i), Lst_position) :
                positions.append((t, z-y*i))
        for i in range(1,8) :
            if verification_deplacement_valide(self, (t, z+y*i), Lst_position) :
                positions.append((t, z+y*i))
        return positions
    
    def chemin(self):
        return self.representation
    
class Reine() :

    def __init__(self, camp=0, representation=os.sep.join(["images", "reine noir.png"])):
        self.camp = camp
        self.representation = representation
        self.type = 1
    
    def position(self, Lst_position) :
        for t in range(8) :
            for z in range(8) :
                if self == Lst_position[t][z] :
                    return t, z
    
    def deplacements_possibles(self) :
        positions = []
        t, z = self.position(Lst_position)
        if self.camp == 0 :
            y = 1
        else : 
            y = -1
        for i in range(1,8) :
            if verification_deplacement_valide(self, (t+y*i, z+y*i), Lst_position) :
                positions.append((t+y*i, z+y*i))
            if verification_deplacement_valide(self, (t-y*i, z+y*i), Lst_position) :
                positions.append((t-y*i, z+y*i))
            if verification_deplacement_valide(self, (t+y*i, z-y*i), Lst_position) :
                positions.append((t+y*i, z-y*i))
            if verification_deplacement_valide(self, (t-y*i, z-y*i), Lst_position) :
                positions.append((t-y*i, z-y*i))
            if verification_deplacement_valide(self, (t+y*i, z), Lst_position) :
                positions.append((t+y*i, z))
            if verification_deplacement_valide(self, (t-y*i, z), Lst_position) :
                positions.append((t-y*i, z))
            if verification_deplacement_valide(self, (t, z-y*i), Lst_position) :
                positions.append((t, z-y*i))
            if verification_deplacement_valide(self, (t, z+y*i), Lst_position) :
                positions.append((t, z+y*i))
        return positions

    def chemin(self):
        return self.representation        

def recup_coordonnees(pion, tableau) :
    position_pion = ()
    for i in range(8) :
        for j  in range(8) :
            if tableau[i][j] == pion :
                position_pion = (i,j)
    if position_pion == () :
        return False
    return position_pion

def verification_deplacement_valide(pion, case_deplacement, tableau) :
    position_pion = recup_coordonnees(pion, tableau)
    if position_pion == False :
        return False
    x1 = case_deplacement[0] - position_pion[0]
    y1 = case_deplacement[1] - position_pion[1] 
    x = (x1)**2
    y = (y1)**2
    if x1 < 0 :
        s1 = -1
    else :
        s1 = 1
    if y1 < 0 :
        s2 = -1
    else : 
        s2 = 1
    if 0 <= case_deplacement[0] < 8 and 0 <= case_deplacement[1] < 8 :

        case = tableau[case_deplacement[0]][case_deplacement[1]]
        # Verif diagonales
        if pion.type == 1 or pion.type == 2 : #Reine ou Fou
            if position_pion[0] != case_deplacement[0] and position_pion[1] != case_deplacement[1] :
                if  x == y :
                    for l in range(1,int(x**0.5)) :
                        if tableau[position_pion[0]+(s1*l)][position_pion[1]+(s2*l)] is not None :
                            return False
                    if case is None :
                        return True
                    elif case.camp != pion.camp :
                        return True 

        # Verif Cavalier
        elif pion.type == 3 : #Cavalier
            if (x == 1 and y == 4) or (x == 4 and y == 1) :
                if case is not None :
                    if case.camp == pion.camp :
                        return False
                return True

        # Verif lignes
        if pion.type == 1 or pion.type == 4 : #Reine ou Tour
            if position_pion[0] != case_deplacement[0] :
                for m in range(1,int(x**0.5)) :
                    if tableau[position_pion[0]+(s1*m)][position_pion[1]] is not None :
                        return False
                if case is None :
                    return True 
                elif case.camp == pion.camp :
                    return False
                return True
            elif position_pion[1] != case_deplacement[1] :
                for h in range(1,int(y**0.5)) :
                    if tableau[position_pion[0]][position_pion[1]+(s2*h)] is not None :
                        return False
                if case is None :
                    return True 
                elif case.camp == pion.camp :
                    return False
                return True
    
        # Verif cases proches :
        elif pion.type == 5:  # Roi
            if case is not None:
                if case.camp != pion.camp:
                    if x == 1 and y == 1: 
                        return True
                    elif x == 1 and y == 0:
                        return True
                    elif x == 0 and y == 1:
                        return True
                return False
            directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1),  (1, 0),  (1, 1)]
            for x2, y2 in directions:
                nouv_x, nouv_y = case_deplacement[0]+x2, case_deplacement[1]+y2
                if 0 <= nouv_x < 8 and 0 <= nouv_y < 8: 
                    piece = tableau[nouv_x][nouv_y]
                    if piece is not None and piece.type == 5 and piece.camp != pion.camp:
                        return False  
            return True
                        
        elif pion.type == 6 : #Pion 
            if y == 0 and x == 1 :
                if case is None :
                    return True
            if y == 0 and x == 4 :
                if tableau[case_deplacement[0]-s1][case_deplacement[1]] is None :
                    if case is None :
                        return True
            elif y == 1 and x == 1 :
                if case is not None :
                    if case.camp != pion.camp :
                        return True
                    
    return False

def verification_echec(roi, tableau) :
    position_roi = recup_coordonnees(roi, tableau)
    if position_roi == False :
        return False
    if roi.camp == 0 :
        y = 1
    else : 
        y = -1
    lst_echec = []
    
    for l in range(1,8) :
        for signe1 in ['+','-'] :
            for signe2 in ['+','-'] :
                # Verif diagonales
                position_test = (position_roi[0] + (l if signe1 == '+' else -l), position_roi[1] + (l if signe2 == '+' else -l))
                if 0 <= position_test[0] < 8 and 0 <= position_test[1] < 8 :
                    case_e = tableau[position_test[0]][position_test[1]]
                    if case_e is not None and case_e.camp == roi.camp and (case_e.type == 1 or case_e.type == 2) :
                        lst_echec.append(case_e)

                # Verif lignes
                position_test = (position_roi[0] + (l if signe1 == '+' else -l), position_roi[1])
                if 0 <= position_test[0] < 8  :
                    case_e = tableau[position_test[0]][position_test[1]]
                    if case_e is not None and case_e.camp == roi.camp and (case_e.type == 1 or case_e.type == 4) :
                        lst_echec.append(case_e)
                position_test = (position_roi[0], position_roi[1] + (l if signe1 == '+' else -l))
                if 0 <= position_test[1] < 8 :
                    case_e = tableau[position_test[0]][position_test[1]]
                    if case_e is not None and case_e.camp == roi.camp and (case_e.type == 1 or case_e.type == 4) :
                        lst_echec.append(case_e)
    case_e =  tableau[position_roi[0]+y][position_roi[1]+y]
    if case_e is not None :
        if case_e.camp == roi.camp :
            if case_e.type == 6 :
                lst_echec.append(case_e)
    case_e =  tableau[position_roi[0]+y][position_roi[1]-y]
    if case_e is not None :
        if case_e.camp == roi.camp :
            if case_e.type == 6 :
                lst_echec.append(case_e)

    for signe1 in ['+','-'] :
        for signe2 in ['+','-'] :
            position_test = (position_roi[0] + 2*(l if signe1 == '+' else -l), position_roi[1] + (l if signe2 == '+' else -l))
            if 0 <= position_test[0] < 8 or 0 <= position_test[1] < 8 :
                case_e = tableau[position_test[0]][position_test[1]]
                if case_e is not None and case_e.camp == roi.camp and case_e.type == 3 :
                    lst_echec.append(case_e)
            position_test = (position_roi[0] + (l if signe1 == '+' else -l), position_roi[1] + 2*(l if signe2 == '+' else -l))
            if 0 <= position_test[0] < 8 and 0 <= position_test[1] < 8 :
                case_e = tableau[position_test[0]][position_test[1]]
                if case_e is not None and case_e.camp == roi.camp and case_e.type == 3 :
                    lst_echec.append(case_e)
    if len(lst_echec) > 0 :
        return lst_echec, position_roi
    return False

def est_case_attaquee(ligne, colonne, camp, ignore_castling=False):
    for i in range(8):
        for j in range(8):
            piece = Lst_position[i][j]
            if piece and piece.camp != camp:
                if ignore_castling and piece.type == 5 :
                    basic_moves = piece.deplacements_sans_roque()
                    if (ligne, colonne) in basic_moves:
                        return True
                else:
                    if (ligne, colonne) in piece.deplacements_possibles():
                        return True
    return False

def executer_roque(roi, position_arrivee):
    ligne = 0 if roi.camp == 0 else 7
    colonne_roi = 4
    
    if position_arrivee[1] == 6:
        Lst_position[ligne][6] = roi
        Lst_position[ligne][4] = None
        tour = Lst_position[ligne][7]
        Lst_position[ligne][5] = tour
        Lst_position[ligne][7] = None

    elif position_arrivee[1] == 2:
        Lst_position[ligne][2] = roi
        Lst_position[ligne][4] = None
        tour = Lst_position[ligne][0]
        Lst_position[ligne][3] = tour
        Lst_position[ligne][0] = None
        
    roi.a_bouge = True
    tour.a_bouge = True

def executer_en_passant(pion, position_arrivee):
    position_depart = pion.position(Lst_position)
    Lst_position[position_depart[0]][position_arrivee[1]] = None
    Lst_position[position_arrivee[0]][position_arrivee[1]] = pion
    Lst_position[position_depart[0]][position_depart[1]] = None

#Programme principal

pion_noir_1 = Pion()
pion_noir_2 = Pion()
pion_noir_3 = Pion()
pion_noir_4 = Pion()
pion_noir_5 = Pion()
pion_noir_6 = Pion()
pion_noir_7 = Pion()
pion_noir_8 = Pion()
roi_noir = Roi()
reine_noir = Reine()
tour_noir_1 = Tour()
tour_noir_2 = Tour()
cavalier_noir_1 = Cavalier()
cavalier_noir_2 = Cavalier()
fou_noir_1 = Fou()
fou_noir_2 = Fou()

pion_blanc_1 = Pion(1, os.sep.join(["images", "pion gris.png"]))
pion_blanc_2 = Pion(1, os.sep.join(["images", "pion gris.png"]))
pion_blanc_3 = Pion(1, os.sep.join(["images", "pion gris.png"]))
pion_blanc_4 = Pion(1, os.sep.join(["images", "pion gris.png"]))
pion_blanc_5 = Pion(1, os.sep.join(["images", "pion gris.png"]))
pion_blanc_6 = Pion(1, os.sep.join(["images", "pion gris.png"]))
pion_blanc_7 = Pion(1, os.sep.join(["images", "pion gris.png"]))
pion_blanc_8 = Pion(1, os.sep.join(["images", "pion gris.png"]))
roi_blanc = Roi(1, os.sep.join(["images", "roi gris.png"]))
reine_blanc = Reine(1, os.sep.join(["images", "reine gris.png"]))
tour_blanc_1 = Tour(1, os.sep.join(["images", "tour gris.png"]))
tour_blanc_2 = Tour(1, os.sep.join(["images", "tour gris.png"]))
cavalier_blanc_1 = Cavalier(1, os.sep.join(["images", "cavalier gris.png"]))
cavalier_blanc_2 = Cavalier(1, os.sep.join(["images", "cavalier gris.png"]))
fou_blanc_1 = Fou(1, os.sep.join(["images", "fou gris.png"]))
fou_blanc_2 = Fou(1, os.sep.join(["images", "fou gris.png"]))

Lst_position = [
    [tour_noir_1, cavalier_noir_1, fou_noir_1, reine_noir, roi_noir, fou_noir_2, cavalier_noir_2, tour_noir_2],
    [pion_noir_1, pion_noir_2, pion_noir_3, pion_noir_4, pion_noir_5, pion_noir_6, pion_noir_7, pion_noir_8],
    [None]*8,
    [None]*8,
    [None]*8,
    [None]*8,
    [pion_blanc_1, pion_blanc_2, pion_blanc_3, pion_blanc_4, pion_blanc_5, pion_blanc_6, pion_blanc_7, pion_blanc_8],
    [tour_blanc_1,cavalier_blanc_1, fou_blanc_1, reine_blanc, roi_blanc, fou_blanc_2, cavalier_blanc_2, tour_blanc_2]
]

import pygame, os, math # on importe tout les modules dont on a besoin
from random import *
pygame.init()


pygame.display.set_caption("Game")  # on change le titre de la fenètre

chemin_repertoire = os.getcwd() # on récupère le chemin du repertoire où est enregistré le fichier
print("le repertoire où est enregistré le fichier du jeu est: " + chemin_repertoire)

fps = pygame.time.Clock() # on définit la variable fps qui va permettre de pouvoir definir le nombre max de fps

fenetre_hauteur = 900
fenetre_largeur = 1500 # on definit la hauteur et la largeur de la fenetre
fenetre = pygame.display.set_mode((fenetre_largeur, fenetre_hauteur)) #on créer la fenètre

sprite = pygame.image.load(chemin_repertoire + '\contenu\sprite\sprite.png').convert_alpha()  # on charge toutes les images au début de code
sprite_ennemi = pygame.image.load(chemin_repertoire + '\contenu\sprite\sprite_ennemi.png').convert_alpha() # et on change la taille de certaines
glockgauche = pygame.image.load(chemin_repertoire + '\contenu\divers\glockg.png').convert_alpha()
glockdroite = pygame.image.load(chemin_repertoire + '\contenu\divers\glockd.png')
glockhaut = pygame.image.load(chemin_repertoire + '\contenu\divers\glockh.png')
glockbas = pygame.image.load(chemin_repertoire + '\contenu\divers\glockb.png')
image_pnj = pygame.image.load(chemin_repertoire + '\contenu\divers\pnj.png')
image_pnj = pygame.transform.scale(image_pnj, (200, 150))
texte_pnj1 = pygame.image.load(chemin_repertoire + '\contenu\divers\\pnj_dialogue1.png')
texte_pnj2 = pygame.image.load(chemin_repertoire + '\contenu\divers\\pnj_dialogue2.png')
texte_pnj3 = pygame.image.load(chemin_repertoire + '\contenu\divers\\pnj_dialogue3.png')
texte_pnj4 = pygame.image.load(chemin_repertoire + '\contenu\divers\\pnj_dialogue4.png')
parchemin_obj1 = pygame.image.load(chemin_repertoire + '\contenu\divers\\parchemin_obj1.png')
parchemin_obj2 = pygame.image.load(chemin_repertoire + '\contenu\divers\\parchemin_obj2.png')
texte_interagire = pygame.image.load(chemin_repertoire + '\contenu\divers\\texte_interagire.png')
bateau = pygame.image.load(chemin_repertoire + '\contenu\divers\\bateau.png')
pnj_bateau = pygame.image.load(chemin_repertoire + '\contenu\divers\pnj_bateau.png')
pnj_bateau = pygame.transform.scale(pnj_bateau, (70, 80))
glockgauche = pygame.transform.scale(glockgauche, (50, 26))
glockdroite = pygame.transform.scale(glockdroite, (50, 26))
glockhaut = pygame.transform.scale(glockhaut, (26, 50))
glockbas = pygame.transform.scale(glockbas, (26, 50))
bullet = pygame.image.load(chemin_repertoire + '\contenu\divers\\bullet.png')
bullet = pygame.transform.scale(bullet, (15, 12))
menuBg = pygame.image.load(chemin_repertoire + '\contenu\menu\\Background.png')
menuBg = pygame.transform.scale(menuBg, (1500,900))
coeur = pygame.image.load(chemin_repertoire + '\contenu\divers\\vie.png')
coeur = pygame.transform.scale(coeur, (70,70))
texte_tapis = pygame.image.load(chemin_repertoire + '\contenu\divers\\texte_tapis.png')
texte_tapis = pygame.transform.scale(texte_tapis, (300, 40))
phantome_mort = pygame.image.load(chemin_repertoire + '\contenu\divers\phantome_mort.png')
texte_reco_mort = pygame.image.load(chemin_repertoire + '\contenu\divers\\texte_reco_mort.png')
Boss = pygame.image.load(chemin_repertoire + '\contenu\divers\\boss.png')
Boss = pygame.transform.scale(Boss, (225, 300 ))
bouleFeu = pygame.image.load(chemin_repertoire + '\contenu\divers\\bouledefeu.png')
bouleFeu = pygame.transform.scale(bouleFeu, (70, 50))
directions=['gauche','droite','haut','bas']

musique = pygame.mixer.music.load(chemin_repertoire + '\contenu\son\musique.mp3')
pygame.mixer.music.play(-1)  # on charge la musique et on la joue tout le temps

change_fond = True
inter_pnj = False
nbr_dialogue = 0
deja_change = False
count_touche = 0
sortie_possible = False
sortie = False
trouve_arg = False
zone_arg = False
go_bateau = False
x_pnj = 700
list_nbr_e = 0  # on definit des variable pour le bon fonctionnement du code


def get_police(size):  # fonction qui récupère la police
    return pygame.font.Font(chemin_repertoire + '\contenu\menu\\font.ttf', size)


#creer une surface et cherche le sprite dans la SpriteSheet
def chercherImage(sheet, frame, ligne, largeurImage, hauteurImage, echelle, couleur):  # coupe l'image en quadrillage puis la coupe en plusieurs images (pour l'animation)
    image = pygame.Surface((largeurImage, hauteurImage)).convert()
    image.blit(sheet,(0, 0), ((frame * largeurImage), (ligne * hauteurImage), largeurImage, hauteurImage))
    image = pygame.transform.scale(image, (largeurImage * echelle, hauteurImage * echelle))
    image.set_colorkey(couleur)
    return image

police = pygame.font.SysFont('Helvetica', 20)  # on définit d'autres variable pour le code
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
BLEU = (0, 0, 255)
liste_animation = []
liste_animation_ennemi = []
etapes_anim = 9
tempsInitial = pygame.time.get_ticks()
anim_cooldown = 70
liste_ennemi = []
dico_ennemi = {}
image_pnj = pygame.transform.scale(image_pnj, (200, 150))
draw_pnj = False
nbr_fond = 3
zone_pnj = False
anim_parchemin = -150
ph_descendre = False
y_ph = 300
x_ph = 700
random = 0

def drawFenetre(): # fonction qui dessine les niveaux et leur éléments
    global anim_cooldown, tempsInitial, change_fond, fond, nbr_fond, nbr_e, draw_pnj, zone_pnj, anim_parchemin, nbr_dialogue, deja_change, trouve_arg, zone_arg, go_bateau, x_pnj, sortie, ph_descendre, y_ph, x_ph, random
    if boss.vie <=0:
            nbr_fond = "gagne"
            change_fond = True
    if change_fond == True:  # on change l'image du niveau
            #pygame.mixer.Channel(1).play(pygame.mixer.Sound(chemin_repertoire + "\contenu\son\\boss_mort.mp3"))
        if nbr_fond == 0:
            #pygame.mixer.Channel(1).play(pygame.mixer.Sound(chemin_repertoire + "\contenu\son\\passage_salle.mp3"))
            fond = pygame.image.load(chemin_repertoire + '\contenu\map\salle_accueil_1.png')
            change_fond = False
            nbr_e_func(0)

        elif nbr_fond == 1:
            #pygame.mixer.Channel(1).play(pygame.mixer.Sound(chemin_repertoire + "\contenu\son\\passage_salle.mp3"))
            fond = pygame.image.load(chemin_repertoire + '\contenu\map\\niveau1_terre.png')
            change_fond = False
            go_bateau = False
            trouve_arg = False
            sortie = False
            nbr_dialogue = 0
            for i in range(len(liste_ennemi)):
                liste_ennemi.pop()
            nbr_e_func(5)

        elif nbr_fond == 2:
            draw_pnj = False
            #pygame.mixer.Channel(1).play(pygame.mixer.Sound(chemin_repertoire + "\contenu\son\\passage_salle.mp3"))
            fond = pygame.image.load(chemin_repertoire + '\contenu\map\\niveau2_mer.png')
            change_fond = False
            draw_pnj = True
            for i in range(len(liste_ennemi)):
                liste_ennemi.pop()
            nbr_e_func(0)

        elif nbr_fond == 3:
            #pygame.mixer.Channel(1).play(pygame.mixer.Sound(chemin_repertoire + "\contenu\son\\passage_salle.mp3"))
            fond = pygame.image.load(chemin_repertoire + '\contenu\map\\niveau3.png')
            change_fond = False

        elif nbr_fond == 4:
            #pygame.mixer.Channel(1).play(pygame.mixer.Sound(chemin_repertoire + "\contenu\son\\passage_salle.mp3"))
            fond = pygame.image.load(chemin_repertoire + '\contenu\map\\niveauFin.png')
            boss.x_b = 300
            boss.y_b = 300
            gerard.vie = 5
            boss.vie = 35
            change_fond = False

        elif nbr_fond == "mort":
            #pygame.mixer.Channel(1).play(pygame.mixer.Sound(chemin_repertoire + "\contenu\son\\mort_joueur.mp3"))
            fond = pygame.image.load(chemin_repertoire + '\contenu\map\salle_mort.png')
            change_fond = False
            for i in range(len(liste_ennemi)):
                liste_ennemi.pop()

        elif nbr_fond == "gagne":
            fond = pygame.image.load(chemin_repertoire + '\contenu\map\salle_gagne.png')
            change_fond = False

        fond = pygame.transform.scale(fond, (1500, 900))

    fenetre.blit(fond,(0,0))
    if nbr_fond == "mort": # on dessine les éléments de la salle mort
        random = randint(0, 1)
        if ph_descendre == False:
            y_ph -= 2
            if random == 0:
                x_ph -= randint(0, 20)
            else:
                x_ph += randint(0, 20)
            fenetre.blit(phantome_mort, (x_ph, y_ph))
            print("false")
            if y_ph < 200:
                ph_descendre = True

        else:
            print("True")
            y_ph += 2
            if random == 0:
                x_ph -= randint(0, 20)
            else:
                x_ph += randint(0, 20)
            fenetre.blit(phantome_mort, (x_ph, y_ph))
            if y_ph > 300:
                ph_descendre = False
        fenetre.blit(texte_reco_mort, (450, 700))

        if touche[pygame.K_e]:
            change_fond = True
            nbr_fond = 0
            gerard.vie = 5

    elif nbr_fond == 2: # on dessine les éléments de la salle 2
        if draw_pnj == True:
            fenetre.blit(image_pnj, (1100, 390))
            if zone_pnj == True:
                if touche[pygame.K_e]:
                    if deja_change == False:
                        nbr_dialogue = 1
                        deja_change = True
                        trouve_arg = False
                        #pygame.mixer.Channel(2).play(pygame.mixer.Sound(chemin_repertoire + "\contenu\son\interaction_pnj.mp3"))

                    elif sortie == True and deja_change == True and trouve_arg == False:
                        nbr_dialogue = 2
                        #pygame.mixer.Channel(2).play(pygame.mixer.Sound(chemin_repertoire + "\contenu\son\interaction_pnj.mp3"))

                    elif trouve_arg == True:
                        nbr_dialogue = 3
                        #pygame.mixer.Channel(3).play(pygame.mixer.Sound(chemin_repertoire + "\contenu\son\interaction_pnj.mp3"))
                        pygame.time.delay(100)
                        #pygame.mixer.Channel(2).play(pygame.mixer.Sound(chemin_repertoire + "\contenu\son\\transaction_bateau.mp3"))

                fenetre.blit(texte_interagire, (1050, 630))
                if nbr_dialogue == 1:
                    fenetre.blit(texte_pnj1, (300, 600))
                elif nbr_dialogue == 2:
                    fenetre.blit(texte_pnj2, (300, 600))
                elif nbr_dialogue == 3:
                    fenetre.blit(texte_pnj3, (300, 600))
            if inter_pnj == True:
                if trouve_arg == True:
                    if anim_parchemin < -30:
                        anim_parchemin += 5
                    fenetre.blit(parchemin_obj2, (-30, anim_parchemin))

                else:
                    if anim_parchemin < -30:
                        anim_parchemin += 5
                    fenetre.blit(parchemin_obj1, (-30, anim_parchemin))

            if zone_arg == True:
                fenetre.blit(texte_interagire, (1200, 00))

            if nbr_dialogue == 3:
                    fenetre.blit(bateau, (x_pnj, 500))
                    if go_bateau == True:
                        fenetre.blit(texte_interagire, (700, 625))
                        if touche[pygame.K_e]:
                            print("ca part")
                            #pygame.mixer.Channel(2).play(pygame.mixer.Sound(chemin_repertoire + "\contenu\son\\bateau.mp3"))
                            if nbr_fond == 2:
                                for i in range(10):
                                    fenetre.blit(fond,(0,0))
                                    fenetre.blit(bateau, (x_pnj, 500))
                                    fenetre.blit(pnj_bateau, (x_pnj + 100, 510))
                                    fenetre.blit(image_pnj, (1100, 390))
                                    x_pnj -= 5
                                    if gerard.x_j < 100:
                                        break
                                nbr_fond = 3
                                change_fond = True

    if nbr_fond != "mort": # on dessine tout le temps sauf pour la salle mort les éléments en dessous
        tempsActuel = pygame.time.get_ticks()
        if tempsActuel - tempsInitial >= anim_cooldown:
            gerard.frame += 1
            tempsInitial = tempsActuel
            if gerard.frame >= len(liste_animation):
                gerard.frame = 0
            for e in liste_ennemi:
                e.frame += 1
                if e.frame >= len(liste_animation_ennemi):
                    e.frame = 0
        gerard.drawjoueur()
        for e in liste_ennemi:
            e.drawennemi()

    if gerard.zone_tapis == True: # on test si le joueur est a gauche pour le passage des salles
        fenetre.blit(texte_tapis, (90, 280))

    if nbr_fond == 4 or nbr_fond == 5:
        boss.drawboss()
    pygame.display.update()

def animation_sprite(liste_animation, etapes_anim, sprite):
    ligne = 0
    for _ in range(4):
        temp_img_liste = []
        for i in range(etapes_anim):
            temp_img_liste.append(chercherImage(sprite, i, ligne, 64, 64, 2, NOIR))
        liste_animation.append(temp_img_liste)
        ligne+=1


def animation_sprite_ennemi(liste_animation_ennemi, etapes_anim, sprite_ennemi):
    ligne = 0
    for _ in range(4):
        temp_img_liste = []
        for i in range(etapes_anim):
            temp_img_liste.append(chercherImage(sprite_ennemi, i, ligne, 64, 64, 2, NOIR))
        liste_animation_ennemi.append(temp_img_liste)
        ligne+=1


def Collision(personnage):
    for e in liste_ennemi:
        if e != personnage:
            if pygame.Rect.colliderect(e.hitbox, personnage.hitbox):
                return True
    if gerard != personnage:
        if pygame.Rect.colliderect(gerard.hitbox, personnage.hitbox):
            if (pygame.time.get_ticks() - gerard.timestampAttaque) > 1000:
                if gerard.vie >0:
                    gerard.vie -= 1
                    #pygame.mixer.Channel(5).play(pygame.mixer.Sound(chemin_repertoire + "\contenu\son\\joueur_hit.mp3"))
                gerard.timestampAttaque = pygame.time.get_ticks()
            return True


class joueur(object):  # class qui contient tout le éléments inérants à au joueur
    def __init__(self,x,y,hauteur,largeur):
        self.direction ='droite'
        self.x_j = x
        self.y_j = y
        self.hauteur = hauteur
        self.largeur = largeur
        self.vel = 15
        self.statique = True
        self.frame=0
        self.balles = []
        self.hitbox = pygame.Rect(self.x_j + 34, self.y_j + 22, 58, 104)
        self.timestampBalle = 0
        self.timestampAttaque = 0
        self.change_fond = True
        self.nbr_fond = 0
        self.vie = 5
        self.zone_tapis = False


    def mouvement(self,touche): # fonction qui permet le mouvement du joueur (ses déplacements ainsi que ses collisions)
        global nbr_fond, change_fond, list_nbr_e, zone_pnj, inter_pnj, deja_change, sortie, sortie_possible, trouve_arg, nbr_dialogue, anim_parchemin, zone_arg, go_bateau
        zone_arg = False
        x_j_orig = self.x_j
        y_j_orig = self.y_j

        if 420 < self.y_j < 500 and self.x_j < 1000:
            go_bateau = True
        else:
            go_bateau = False


        if list_nbr_e <= 0 and (self.x_j < 230 and 230 < self.y_j < 425):
            self.zone_tapis = True
            if touche[pygame.K_e]:
                nbr_fond +=1
                self.x_j = 1400
                self.y_j = 250
                change_fond = True
                list_nbr_e = 0

        else:
            self.zone_tapis = False

        if nbr_fond == 2 and (1050 < self.x_j < 1250 and 430 < self.y_j < 500):
            zone_pnj = True
            if nbr_dialogue == 1:
                sortie_possible = True

            if touche[pygame.K_e]:
                inter_pnj = True

        else:
            zone_pnj = False
            if sortie_possible == True:
                sortie = True

            if 1350 < self.x_j and(100 > self.y_j < 230):
                if nbr_dialogue == 1 or nbr_dialogue == 2:
                    zone_arg = True
                    if touche[pygame.K_e]:
                        trouve_arg = True
                        #pygame.mixer.Channel(2).play(pygame.mixer.Sound(chemin_repertoire + "\contenu\son\\coffre.mp3"))
                        pygame.time.delay(100)
                        #pygame.mixer.Channel(3).play(pygame.mixer.Sound(chemin_repertoire + "\contenu\son\\argent.mp3"))
                        anim_parchemin = -150
                        print('argent trouvé')

        #dash
        if touche[pygame.K_f] and self.x_j > self.vel and self.x_j < fenetre_largeur - self.largeur - self.vel and self.y_j > self.vel and self.y_j < fenetre_hauteur - self.hauteur - self.vel:
            if self.direction == 'gauche':
                self.x_j -= 200
            if self.direction == 'droite':
                self.x_j += 200
            if self.direction == 'haut':
                self.y_j -= 200
            if self.direction == 'bas':
                self.y_j += 200
            if self.x_j <= 0:
                self.x_j = 0
            if self.x_j >= fenetre_largeur - self.largeur:
                self.x_j = fenetre_largeur - self.largeur
            if self.y_j <= 0:
                self.y_j = 0
            if self.y_j >= fenetre_hauteur - self.hauteur:
                self.y_j = fenetre_hauteur - self.hauteur



        if touche[pygame.K_w] and touche[pygame.K_a] and self.x_j > self.vel and self. y_j > self.vel:
            if nbr_fond == 4 or nbr_fond == 5:
                if self.x_j > 1070 and self.y_j < 220:
                    self.statique = True
                    return
            self.x_j -= self.vel / math.sqrt(2)
            self.y_j -= self.vel / math.sqrt(2)
            self.statique = False
            self.direction = 'haut-gauche'

        elif touche[pygame.K_a] and touche[pygame.K_s] and self.x_j > self.vel and self.y_j < fenetre_hauteur - self.hauteur - self.vel:
            if nbr_fond == 4 or nbr_fond == 5:
                if self.x_j > 1070 and self.y_j > 370:
                    self.statique = True
                    return
            self.x_j -= self.vel / math.sqrt(2)
            self.y_j += self.vel / math.sqrt(2)
            self.statique = False
            self.direction = 'bas-gauche'

        elif touche[pygame.K_w] and touche[pygame.K_d] and self.y_j > self.vel and self.x_j < fenetre_largeur - self.largeur - self.vel:
            if nbr_fond == 4 or nbr_fond == 5:
                if self.x_j > 1070 and self.y_j < 220:
                    self.statique = True
                    return
                elif self.x_j > 1070 and not (self.y_j > 220 and self.y_j < 370):
                    self.statique = True
                    return
            self.x_j += self.vel / math.sqrt(2)
            self.y_j -= self.vel / math.sqrt(2)
            self.statique = False
            self.direction = 'haut-droite'

        elif touche[pygame.K_s] and touche[pygame.K_d] and self.y_j < fenetre_hauteur - self.hauteur - self.vel and self.x_j < fenetre_largeur - self.largeur - self.vel:
            if nbr_fond == 4 or nbr_fond == 5:
                if self.x_j > 1070 and self.y_j > 370:
                    self.statique = True
                    return
                elif self.x_j > 1070 and not (self.y_j > 220 and self.y_j < 370):
                    self.statique = True
                    return
            self.x_j += self.vel / math.sqrt(2)
            self.y_j += self.vel / math.sqrt(2)
            self.statique = False
            self.direction = 'bas-droite'

        elif touche[pygame.K_a] and self.x_j > self.vel:
            self.x_j -= self.vel
            self.statique = False
            self.direction = 'gauche'

        elif touche[pygame.K_d] and self.x_j < fenetre_largeur - self.largeur - self.vel:
            if nbr_fond == 4 or nbr_fond == 5:
                if self.x_j > 1070 and not (220 < self.y_j < 370):
                    self.statique = True
                    return
            self.x_j += self.vel
            self.statique = False
            self.direction = 'droite'

        elif touche[pygame.K_w] and self.y_j > self.vel:
            if nbr_fond == 4 or nbr_fond == 5:
                if self.x_j > 1070 and self.y_j < 220:
                    self.statique = True
                    return
            self.y_j -= self.vel
            self.statique = False
            self.direction = 'haut'

        elif touche[pygame.K_s] and self.y_j < fenetre_hauteur - self.hauteur - self.vel:
            if nbr_fond == 4 or nbr_fond == 5:
                if self.x_j > 1070 and self.y_j > 370:
                    self.statique = True
                    return
            self.y_j += self.vel
            self.statique = False
            self.direction = 'bas'

        else:
            self.statique = True


        if touche[pygame.K_SPACE] and (pygame.time.get_ticks() - self.timestampBalle) > 250:
            #balleSon.play()
            if len(self.balles) < 10:
                #pygame.mixer.Channel(3).play(pygame.mixer.Sound(chemin_repertoire + "\contenu\son\\sonTir.mp3"))
                self.balles.append(
                    projectile(round(self.x_j + self.largeur // 2), round(self.y_j + self.hauteur // 2), 7, NOIR,
                               self.direction))
                self.timestampBalle = pygame.time.get_ticks()
        self.hitbox = pygame.Rect(self.x_j + 34, self.y_j + 22, 58, 104)
        if Collision(self):
            self.x_j = x_j_orig
            self.y_j = y_j_orig
            self.hitbox = pygame.Rect(self.x_j + 34, self.y_j + 22, 58, 104)

        if nbr_fond == 2 and (self.x_j < 1250):
            print(self.x_j)
            if 375 > self.y_j or 550 < self.y_j:
                self.x_j += self.vel
                self.statique = True

            if 850 > self.x_j:
                self.x_j += self.vel
                self.statique = True

            elif self.x_j < 1249:
                if self.y_j < 420:
                    self.y_j += self.vel
                    self.statique = True
                elif self.y_j > 500:
                    self.y_j -= self.vel
                    self.statique = True

        if nbr_fond == 2 and (1051 == self.x_j or self.x_j == 1251):
            deja_change = False

        if Collision(self):
            self.x_j = x_j_orig
            self.y_j = y_j_orig
            self.hitbox = pygame.Rect(self.x_j + 34, self.y_j + 22, 58, 104)



    def drawjoueur(self): # fonction qui permet de dessiner le joueur et ses éléments
        global nbr_fond, change_fond

        if self.vie <= 0:
            change_fond = True
            nbr_fond = "mort"

        if not (self.statique):
            if self.direction == 'gauche' or self.direction == 'haut-gauche' or self.direction == 'bas-gauche':
                fenetre.blit(liste_animation[1][self.frame], (self.x_j, self.y_j))
                fenetre.blit(glockgauche, (round(self.x_j + self.largeur // 2) - 50, (round(self.y_j + self.hauteur // 2))))

            elif self.direction == 'droite' or self.direction == 'haut-droite' or self.direction == 'bas-droite':
                fenetre.blit(liste_animation[3][self.frame], (self.x_j, self.y_j))
                fenetre.blit(glockdroite, (round(self.x_j + self.largeur // 2) + 5, (round(self.y_j + self.hauteur // 2))))

            elif self.direction == 'haut':
                fenetre.blit(liste_animation[0][self.frame], (self.x_j, self.y_j))
                fenetre.blit(glockhaut, (round(self.x_j + self.largeur // 2) - 20, (round(self.y_j + self.hauteur // 2) - 60)))

            elif self.direction == 'bas':
                fenetre.blit(liste_animation[2][self.frame], (self.x_j, self.y_j))
                fenetre.blit(glockbas, (round(self.x_j + self.largeur // 2) - 20, (round(self.y_j + self.hauteur // 2) + 15)))

        else:
            if self.direction == 'droite' or self.direction == 'haut-droite' or self.direction == 'bas-droite':
                fenetre.blit(liste_animation[3][0], (self.x_j, self.y_j))
                fenetre.blit(glockdroite,
                             (round(self.x_j + self.largeur // 2) + 5, (round(self.y_j + self.hauteur // 2))))
            if self.direction == 'gauche' or self.direction == 'haut-gauche' or self.direction == 'bas-gauche':
                fenetre.blit(liste_animation[1][0], (self.x_j, self.y_j))
                fenetre.blit(glockgauche,
                             (round(self.x_j + self.largeur // 2) - 50, (round(self.y_j + self.hauteur // 2))))
            if self.direction == 'haut':
                fenetre.blit(liste_animation[0][0], (self.x_j, self.y_j))
                fenetre.blit(glockhaut,
                             (round(self.x_j + self.largeur // 2) - 20, (round(self.y_j + self.hauteur // 2) - 60)))
            if self.direction == 'bas':
                fenetre.blit(liste_animation[2][0], (self.x_j, self.y_j))
                fenetre.blit(glockbas,
                             (round(self.x_j + self.largeur // 2) - 20, (round(self.y_j + self.hauteur // 2) + 15)))

        for balle in self.balles:
            balle.draw(fenetre)
        if nbr_fond != 2:
            pygame.draw.rect(fenetre, ROUGE, (50, 50, 400, 40))
            pygame.draw.rect(fenetre, (0,100,0),(50, 50, 400 - ((400 / 5) * (5 - self.vie)), 40))
            fenetre.blit(coeur, (30, 50))


class boss(object):  # class qui contient tout le éléments inérants à au boss
    def __init__(self,x,y, hauteur, largeur):
        self.x_b = 3000
        self.y_b = 3000
        self.largeur = largeur
        self.hauteur = hauteur
        self.vel = 3
        self.statique = True
        self.frame = 0
        self.hitbox = pygame.Rect(self.x_b + 10, self.y_b + 15, 200, 260)
        self.vie = 30
        self.visible = True
        self.ballesFeu = []
        self.timestampBalle1 = 0
        self.timestampBalle2 = 0
        self.vie = 10

    def drawboss(self): # permet de dessiner le boss
        global nbr_fond, change_fond
        self.hitbox = pygame.Rect(self.x_b + 10, self.y_b + 15, 200, 260)
        if self.visible:
            fenetre.blit(Boss, (self.x_b, self.y_b))
        for balle in self.ballesFeu:
            balle.draw(fenetre)

        pygame.draw.rect(fenetre, ROUGE, (fenetre_largeur//2- 500, fenetre_hauteur - 80, 1000, 70))

        pygame.draw.rect(fenetre, VERT, (fenetre_largeur//2 - 500, fenetre_hauteur - 80, 1000 - ((1000 / 35) * (35 - self.vie)), 25))


    def hit(self): # permet de gérer la vie du boss
        global change_fond, nbr_fond
        if self.vie > 0:
            self.vie-=1
        else:
            self.visible = False
            change_fond = True
            nbr_fond = "gagne"
        print('hit')

    def mouvement(self): # permet de gérer les déplacement du boss
        x_b_orig = self.x_b
        y_b_orig = self.y_b
        if gerard.y_j < self.y_b:
            if (self.y_b - gerard.y_j) < self.vel:
                self.y_b = gerard.y_j
            else:
                self.y_b -= self.vel
        elif gerard.y_j > self.y_b:
            if (gerard.y_j - self.y_b) < self.vel:
                self.y_b = gerard.y_j
            else:
                self.y_b += self.vel
        if gerard.x_j < self.x_b:
            if (self.x_b - gerard.x_j) < self.vel:
                self.x_b = gerard.x_j
            else:
                self.x_b -= self.vel
        elif gerard.x_j > self.x_b:
            if (gerard.x_j - self.x_b) < self.vel:
                self.x_b = gerard.x_j
            else:
                self.x_b += self.vel
        self.hitbox = pygame.Rect(self.x_b + 10, self.y_b + 15, 200, 260)

        if len(self.ballesFeu) < 20 and (pygame.time.get_ticks() - self.timestampBalle1) > 750:
            self.ballesFeu.append(projectileBoss(round(self.x_b + self.largeur // 2), round(self.y_b + self.hauteur // 2), 7, NOIR, 'haut-gauche'))
            self.ballesFeu.append(projectileBoss(round(self.x_b + self.largeur // 2), round(self.y_b + self.hauteur // 2), 7, NOIR,'haut-droite'))
            self.ballesFeu.append(projectileBoss(round(self.x_b + self.largeur // 2), round(self.y_b + self.hauteur // 2), 7, NOIR,'bas-droite'))
            self.ballesFeu.append(projectileBoss(round(self.x_b + self.largeur // 2), round(self.y_b + self.hauteur // 2), 7, NOIR,'bas-gauche'))
            self.timestampBalle1 = pygame.time.get_ticks()
            #pygame.mixer.Channel(4).play(pygame.mixer.Sound(chemin_repertoire + "\contenu\son\\boss_tir.mp3"))

        if len(self.ballesFeu) < 20 and (pygame.time.get_ticks() - self.timestampBalle2) > 1500:
            self.ballesFeu.append(projectileBoss(round(self.x_b + self.largeur // 2), round(self.y_b + self.hauteur // 2), 7, NOIR, 'haut'))
            self.ballesFeu.append(projectileBoss(round(self.x_b + self.largeur // 2), round(self.y_b + self.hauteur // 2), 7, NOIR,'bas'))
            self.ballesFeu.append(projectileBoss(round(self.x_b + self.largeur // 2), round(self.y_b + self.hauteur // 2), 7, NOIR,'droite'))
            self.ballesFeu.append(projectileBoss(round(self.x_b + self.largeur // 2), round(self.y_b + self.hauteur // 2), 7, NOIR,'gauche'))
            self.timestampBalle2 = pygame.time.get_ticks()
            #pygame.mixer.Channel(4).play(pygame.mixer.Sound(chemin_repertoire + "\contenu\son\\boss_tir.mp3"))

        if Collision(self):
            self.x_b = x_b_orig
            self.y_b = y_b_orig
            self.hitbox = pygame.Rect(self.x_b + 10, self.y_b + 15, 200, 260)


class projectileBoss(object):  # class contenant les éléments inérants aux projectiles du boss
    def __init__(self, x, y, rayon, couleur, direction):
        self.x = x
        self.y = y
        self.rayon = rayon
        self.couleur = couleur
        self.vel = 10
        self.direction = direction

    def draw(self, fenetre): # permet de dessiner les projectiles
        fenetre.blit(bouleFeu, (self.x, self.y))

    def mouvement(self): # permet de gérer les mouvement des projectiles
        sortie = False
        if 1500 > self.x > 0 and 0 < self.y < 900:
            if self.direction == 'gauche':
                self.x -= self.vel
            if self.direction == 'droite':
                self.x += self.vel
            if self.direction == 'haut':
                self.y -= self.vel
            if self.direction == 'bas':
                self.y += self.vel
            if self.direction == 'bas-gauche':
                self.x -= round(self.vel / math.sqrt(2))
                self.y += round(self.vel / math.sqrt(2))
            if self.direction == 'bas-droite':
                self.x += round(self.vel / math.sqrt(2))
                self.y += round(self.vel / math.sqrt(2))
            if self.direction == 'haut-gauche':
                self.y -= round(self.vel / math.sqrt(2))
                self.x -= round(self.vel / math.sqrt(2))
            if self.direction == 'haut-droite':
                self.y -= round(self.vel / math.sqrt(2))
                self.x += round(self.vel / math.sqrt(2))
        else:
            sortie = True
        return sortie


class ennemi(object): # class qui contient tout le éléments inérants au ennemis
    def __init__(self, intelligence):

        self.x_e = randint(0, fenetre_largeur - 128)
        self.y_e = randint(0, fenetre_hauteur - 128)
        self.hitbox = pygame.Rect(self.x_e + 34, self.y_e + 22, 58, 104)
        while Collision(self):
            self.x_e = randint(0, fenetre_largeur - 128)
            self.y_e = randint(0, fenetre_hauteur - 128)
            self.hitbox = pygame.Rect(self.x_e + 34, self.y_e + 22, 58, 104)

        self.direction = directions[randint(0, 3)]
        self.vel = 4
        self.statique = True
        self.frame = 0
        self.Tempsdirection = pygame.time.get_ticks()
        self.intelligence = intelligence

        self.vie = 10
        self.visible = True
        self.Collision = False
        pygame.draw.rect(fenetre, ROUGE, (self.hitbox[0], self.hitbox[1] - 15, 50, 10))

    def drawennemi(self): # permet de dessiner les ennemis
        self.hitbox = pygame.Rect(self.x_e + 34, self.y_e + 22, 58, 104)

        if self.visible == True:
            pygame.draw.rect(fenetre, ROUGE, (self.hitbox[0], self.hitbox[1] - 15, 50, 10))
            if self.intelligence:
                pygame.draw.rect(fenetre, VERT, (self.hitbox[0], self.hitbox[1] - 15, 50 - ((50 / 10) * (10 - self.vie)), 10))
            else:
                pygame.draw.rect(fenetre, BLEU,(self.hitbox[0], self.hitbox[1] - 15, 50 - ((50 / 10) * (10 - self.vie)), 10))
            if self.direction == 'gauche':
                fenetre.blit(liste_animation_ennemi[1][self.frame], (self.x_e, self.y_e))
            elif self.direction == 'droite':
                fenetre.blit(liste_animation_ennemi[3][self.frame], (self.x_e, self.y_e))
            elif self.direction == 'haut':
                fenetre.blit(liste_animation_ennemi[0][self.frame], (self.x_e, self.y_e))
            elif self.direction == 'bas':
                fenetre.blit(liste_animation_ennemi[2][self.frame], (self.x_e, self.y_e))

    def hit(self): # permet de gérer la vie des ennemis quand ils sont touchés
        global list_nbr_e
        #hitSon.play()
        #pygame.mixer.Channel(2).play(pygame.mixer.Sound(chemin_repertoire + "\contenu\son\\hit.mp3"))
        if self.vie > 0:
            self.vie -= 1
        else:
            self.visible = True #False
            list_nbr_e -= 1
            self.x_e = 3000
            self.y_e = 3000
            self.vel = 0
            #mort.play()
            #pygame.mixer.Channel(4).play(pygame.mixer.Sound(chemin_repertoire + "\contenu\son\\mort.mp3"))
        print('hit')


    def mouvement(self): # permet de gérer le mouvement des ennemeis
        if self.intelligence:
            x_e_orig = self.x_e
            y_e_orig = self.y_e
            if gerard.y_j < self.y_e:
                if (self.y_e - gerard.y_j) < self.vel:
                    self.y_e = gerard.y_j
                else:
                    self.y_e -= self.vel
                self.direction = 'haut'
            elif gerard.y_j > self.y_e:
                if (gerard.y_j - self.y_e) < self.vel:
                    self.y_e = gerard.y_j
                else:
                    self.y_e += self.vel
                self.direction = 'bas'
            if gerard.x_j < self.x_e:
                if (self.x_e - gerard.x_j) < self.vel:
                    self.x_e = gerard.x_j
                else:
                    self.x_e -= self.vel
                self.direction = 'gauche'
            elif gerard.x_j > self.x_e:
                if (gerard.x_j - self.x_e) < self.vel:
                    self.x_e = gerard.x_j
                else:
                    self.x_e += self.vel
                self.direction = 'droite'
            self.hitbox = pygame.Rect(self.x_e + 34, self.y_e + 22, 58, 104)

            if Collision(self):
                self.x_e = x_e_orig
                self.y_e = y_e_orig
                self.hitbox = pygame.Rect(self.x_e + 34, self.y_e + 22, 58, 104)

        if not self.intelligence:
            if self.direction == 'droite':
                if self.x_e < (fenetre_largeur - 128):
                    self.x_e += self.vel
                else:
                    self.direction = 'gauche'
            elif self.direction == 'gauche':
                if self.x_e > 0:
                    self.x_e -= self.vel
                else:
                    self.direction = 'droite'
            elif self.direction == 'haut':
                if self.y_e > 0:
                    self.y_e -= self.vel
                else:
                    self.direction = 'bas'
            elif self.direction == 'bas':
                if self.y_e < (fenetre_hauteur - 150):
                    self.y_e += self.vel
                else:
                    self.direction = 'haut'

            if pygame.time.get_ticks() - self.Tempsdirection > randint(300, 10000):
                self.direction = directions[randint(0, 3)]
                self.Tempsdirection = pygame.time.get_ticks()

            # ACtualisation de la hitbox après le mouvement
            self.hitbox = pygame.Rect(self.x_e + 34, self.y_e + 22, 58, 104)

            if Collision(self):
                if self.direction == 'droite':
                    self.x_e -= self.vel
                    self.direction = 'gauche'
                elif self.direction == 'gauche':
                    self.x_e += self.vel
                    self.direction = 'droite'
                elif self.direction == 'haut':
                    self.y_e += self.vel
                    self.direction = 'bas'
                elif self.direction == 'bas':
                    self.y_e -= self.vel
                    self.direction = 'haut'
                self.hitbox = pygame.Rect(self.x_e + 34, self.y_e + 22, 58, 104)


class projectile(object): # class contenant tout les éléments inérants aux projectiles des  ennemeis
    def __init__(self,x,y,rayon,couleur, direction):
        self.x = x
        self.y = y
        self.rayon = rayon
        self.couleur = couleur
        self.direction = direction
        self.vel = 20

    def draw(self,fenetre): # permet de dessiner les projectiles
        fenetre.blit(bullet, (self.x - 5, self.y - 5))

    def mouvement(self): #permet de gérer les mouvement des projectiles
        sortie = False
        if self.x < 1500 and self.x > 0 and self.y > 0 and self.y < 900:
            if self.direction == 'gauche':
                self.x -= self.vel
            if self.direction == 'droite':
                self.x += self.vel
            if self.direction == 'haut':
                self.y -= self.vel
            if self.direction == 'bas':
                self.y += self.vel
            if self.direction == 'bas-gauche':
                self.x -= round(self.vel / math.sqrt(2))
                self.y += round(self.vel / math.sqrt(2))
            if self.direction == 'bas-droite':
                self.x += round(self.vel / math.sqrt(2))
                self.y += round(self.vel / math.sqrt(2))
            if self.direction == 'haut-gauche':
                self.y -= round(self.vel / math.sqrt(2))
                self.x -= round(self.vel / math.sqrt(2))
            if self.direction == 'haut-droite':
                self.y -= round(self.vel / math.sqrt(2))
                self.x += round(self.vel / math.sqrt(2))
        else:
            sortie=True
        return sortie


class Button(): # class contenant tout les éléments inérants aux boutons
    def __init__(self, image, pos, text_input, police, couleur_base, couleur_hover):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.police = police
        self.couleur_base, self.couleur_hover = couleur_base, couleur_hover
        self.text_input = text_input
        self.text = self.police.render(self.text_input, True, self.couleur_base)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, fenetre): # permet d'afficher les boutons
        if self.image is not None:
            fenetre.blit(self.image, self.rect)
        fenetre.blit(self.text, self.text_rect)

    def checkInput(self, position): # regarde si la souris est dans le carré du bouton et si on clique
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position): # permet de changer la couleur des boutons quand on met la souris dessus
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.police.render(self.text_input, True, self.couleur_hover)
        else:
            self.text = self.police.render(self.text_input, True, self.couleur_base)


def play(): # lance une première fois le jeu
    jeu()


def options(): # gère le menu des options
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        posXop = (fenetre_largeur * 1 / 8)
        posYop = (fenetre_hauteur * 2 / 8)
        fenetre.fill(NOIR)

        contenuOptions = ["- Haut: W / Z",
                          "- Bas: S",
                          "- Droite: D",
                          "- Gauche: A / Q",
                          "- Dash: F",
                          "- Interagir / Ouvrir: E",
                          "- Tirer: Espace"]
        listeTexteOptions = []

        titreOptions = get_police(50).render("Controles", True, (51, 102, 255))

        for ligne in contenuOptions:
            listeTexteOptions.append(get_police(30).render(ligne, True, (51, 102, 255)))

        fenetre.blit(titreOptions, (fenetre_largeur // 2 - 300, 50))

        for line in range(len(listeTexteOptions)):
            fenetre.blit(listeTexteOptions[line], (posXop, posYop + (line * 30) + (40 * line)))

        OPTIONS_BACK = Button(image=None, pos=(750, 800),
                            text_input="RETOUR", police=get_police(20), couleur_base=(255,255,255), couleur_hover=VERT)

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(fenetre)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkInput(OPTIONS_MOUSE_POS):
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound(chemin_repertoire + "\contenu\son\\clique_bouton1.mp3"))
                    menu()

        pygame.display.update()

def menu(): # gère le menu du jeu
    pygame.display.set_caption('Menu')

    while True:
        fenetre.blit(menuBg, (0, 0))

        menu_position_souris = pygame.mouse.get_pos()

        menu_texte = get_police(100).render("MAIN MENU", True, (182,143,64))
        menu_rect = menu_texte.get_rect(center=(750, 100))

        bouton_jouer= Button(image=pygame.image.load(chemin_repertoire+ "/contenu/menu/Play Rect.png"), pos=(750, 250),
                             text_input="PLAY", police=get_police(75), couleur_base=(0,128,128), couleur_hover=(255,255,255))
        bouton_options = Button(image=pygame.image.load(chemin_repertoire+ "/contenu/menu/Options Rect.png"), pos=(750, 400),
                                text_input="OPTIONS", police=get_police(75), couleur_base=(0,128,128), couleur_hover=(255,255,255))
        bouton_quit = Button(image=pygame.image.load(chemin_repertoire+ "/contenu/menu/Quit Rect.png"), pos=(750, 550),
                             text_input="QUIT", police=get_police(75), couleur_base=(0,128,128), couleur_hover=(255,255,255))

        fenetre.blit(menu_texte, menu_rect)

        for button in [bouton_jouer, bouton_options, bouton_quit]:
            button.changeColor(menu_position_souris)
            button.update(fenetre)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bouton_jouer.checkInput(menu_position_souris):
                    #pygame.mixer.Channel(1).play(pygame.mixer.Sound(chemin_repertoire + "\contenu\son\\clique_bouton1.mp3"))
                    play()
                if bouton_options.checkInput(menu_position_souris):
                    #pygame.mixer.Channel(1).play(pygame.mixer.Sound(chemin_repertoire + "\contenu\son\\clique_bouton1.mp3"))
                    options()
                if bouton_quit.checkInput(menu_position_souris):
                    #pygame.mixer.Channel(1).play(pygame.mixer.Sound(chemin_repertoire + "\contenu\son\\clique_bouton1.mp3"))
                    pygame.quit()

            pygame.display.update()


run = True
gerard=joueur(250,250,128,128)
boss = boss(400, 500, 260, 200)

def nbr_e_func(nbr_e): # permet de stocker les ennemies dans une liste
    for i in range(nbr_e):
        global list_nbr_e
        print(nbr_e)
        liste_ennemi.append(ennemi(choice([True, False])))
        list_nbr_e += 1



animation_sprite(liste_animation, etapes_anim, sprite)
animation_sprite_ennemi(liste_animation_ennemi, etapes_anim, sprite_ennemi)

def jeu(): # permet de faire tourner le jeu en boucle
    global touche, nbr_fond, fond, list_nbr_e
    run = True
    while run:
        if nbr_fond == "mort":
            if touche[pygame.K_e]:
                list_nbr_e = 0
        fps.tick(30)
        drawFenetre()
        touche = pygame.key.get_pressed()
        gerard.mouvement(touche)
        if nbr_fond == 4 or nbr_fond == 5:
            boss.mouvement()
        for balle in gerard.balles:
            for e in liste_ennemi:
                if balle.y - balle.rayon < e.hitbox[1] + e.hitbox[3] and balle.y + balle.rayon > e.hitbox[1]:
                    if balle.x + balle.rayon > e.hitbox[0] and balle.x - balle.rayon < e.hitbox[0] + e.hitbox[2]:
                        e.hit()
                        gerard.balles.remove(balle)

            if balle.y - balle.rayon < boss.hitbox[1] + boss.hitbox[3] and balle.y + balle.rayon > boss.hitbox[1]:
                if balle.x + balle.rayon > boss.hitbox[0] and balle.x - balle.rayon < boss.hitbox[0] + boss.hitbox[2]:

                    boss.hit()
                    gerard.balles.remove(balle)

            if balle.mouvement():
                gerard.balles.remove(balle)

        for balle in boss.ballesFeu:
            if balle.y - balle.rayon < gerard.hitbox[1] + gerard.hitbox[3] and balle.y + balle.rayon > gerard.hitbox[1]:
                if balle.x + balle.rayon > gerard.hitbox[0] and balle.x - balle.rayon < gerard.hitbox[0] + gerard.hitbox[2]:
                    # hitSon.play()
                    print('touche par le boss')
                    gerard.vie -= 1
                    boss.ballesFeu.remove(balle)


        for balle in boss.ballesFeu:
            if balle.mouvement():
                boss.ballesFeu.remove(balle)

        for e in liste_ennemi:
            e.mouvement()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

menu()
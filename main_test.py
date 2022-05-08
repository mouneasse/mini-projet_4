import pygame, os, math
from random import *
pygame.init()


pygame.display.set_caption("Game")

chemin_repertoire = os.getcwd()
print("le repertoire où est enregistré le fichier du jeu est: " + chemin_repertoire)

fps = pygame.time.Clock()

fenetre_hauteur = 900
fenetre_largeur = 1500
fenetre = pygame.display.set_mode((fenetre_largeur, fenetre_hauteur))

#fond = pygame.image.load(chemin_repertoire + '\contenu\map\salle_accueil_1.png')
sprite = pygame.image.load(chemin_repertoire + '\contenu\sprite\sprite.png').convert_alpha()
sprite_ennemi = pygame.image.load(chemin_repertoire + '\contenu\sprite\sprite_ennemi.png').convert_alpha()
#fond = pygame.transform.scale(fond, (1500, 900))
glockgauche = pygame.image.load(chemin_repertoire + '\contenu\divers\glockd.png').convert_alpha()
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
directions=['gauche','droite','haut','bas']

#balleSon = pygame.mixer.Sound(chemin_repertoire + '\contenu\son\sonTir.wav')
#hitSon = pygame.mixer.Sound(chemin_repertoire + '\contenu\son\hit.wav')
#mort = pygame.mixer.Sound(chemin_repertoire + '\contenu\son\mort.wav')

#musique = pygame.mixer.music.load(chemin_repertoire + '\contenu\son\musique.mp3')
#pygame.mixer.music.play(-1)

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
list_nbr_e = 0


def get_police(size):
    return pygame.font.Font(chemin_repertoire + '\contenu\menu\\font.ttf', size)


#creer une surface et cherche le sprite dans la SpriteSheet
def chercherImage(sheet, frame, ligne, largeurImage, hauteurImage, echelle, couleur):
    image = pygame.Surface((largeurImage, hauteurImage)).convert()
    image.blit(sheet,(0, 0), ((frame * largeurImage), (ligne * hauteurImage), largeurImage, hauteurImage))
    image = pygame.transform.scale(image, (largeurImage * echelle, hauteurImage * echelle))
    image.set_colorkey(couleur)
    return image

police = pygame.font.SysFont('Helvetica', 20)
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
nbr_fond = 0
zone_pnj = False
anim_parchemin = -150


def drawFenetre():
    global anim_cooldown, tempsInitial, change_fond, fond, nbr_fond, nbr_e, draw_pnj, zone_pnj, anim_parchemin, nbr_dialogue, deja_change, trouve_arg, zone_arg, go_bateau, x_pnj, sortie

    if change_fond == True:
        if nbr_fond == 0:
            fond = pygame.image.load(chemin_repertoire + '\contenu\map\salle_accueil_1.png')
            change_fond = False
            nbr_e_func(2)

        elif nbr_fond == 1:
            fond = pygame.image.load(chemin_repertoire + '\contenu\map\\niveau1_terre.png')
            change_fond = False
            for i in range(len(liste_ennemi)):
                liste_ennemi.pop()
            nbr_e_func(3)

        elif nbr_fond == 2:
            fond = pygame.image.load(chemin_repertoire + '\contenu\map\\niveau2_mer.png')
            change_fond = False
            for i in range(len(liste_ennemi)):
                liste_ennemi.pop()
            draw_pnj = True
        fond = pygame.transform.scale(fond, (1500, 900))

    fenetre.blit(fond,(0,0))

    if draw_pnj == True:
        fenetre.blit(image_pnj, (1100, 390))
        if zone_pnj == True:
            if touche[pygame.K_e]:
                if deja_change == False:
                    nbr_dialogue = 1
                    deja_change = True
                    trouve_arg = False

                elif sortie == True and deja_change == True and trouve_arg == False:
                    nbr_dialogue = 2

                elif trouve_arg == True:
                    nbr_dialogue = 3

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
                        for i in range(50):
                            fenetre.blit(fond,(0,0))
                            fenetre.blit(bateau, (x_pnj, 500))
                            fenetre.blit(pnj_bateau, (x_pnj + 100, 510))
                            fenetre.blit(image_pnj, (1100, 390))
                            x_pnj -= 8
                            pygame.display.update()
                        nbr_fond = 3

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
                gerard.timestampAttaque = pygame.time.get_ticks()
            return True


class joueur(object):
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


    def mouvement(self,touche):
        global nbr_fond, change_fond, list_nbr_e, zone_pnj, inter_pnj, deja_change, sortie, sortie_possible, trouve_arg, nbr_dialogue, anim_parchemin, zone_arg, go_bateau
        zone_arg = False
        x_j_orig = self.x_j
        y_j_orig = self.y_j

        if 420 < self.y_j < 500 and self.x_j < 1000:
            go_bateau = True
        else:
            go_bateau = False


        if list_nbr_e <= 0 and (self.x_j < 230 and 230 < self.y_j < 425):
            if touche[pygame.K_e]:
                nbr_fond +=1
                change_fond = True
                print(nbr_fond)
                self.x_j = 1200
                self.y_j = 500
                list_nbr_e = 0
            else:
                print("vous etes sur la zone")

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
            self.x_j -= self.vel / math.sqrt(2)
            self.y_j -= self.vel / math.sqrt(2)
            self.statique = False
            self.direction = 'haut-gauche'

        elif touche[pygame.K_a] and touche[pygame.K_s] and self.x_j > self.vel and self.y_j < fenetre_hauteur - self.hauteur - self.vel:
            self.x_j -= self.vel / math.sqrt(2)
            self.y_j += self.vel / math.sqrt(2)
            self.statique = False
            self.direction = 'bas-gauche'

        elif touche[pygame.K_w] and touche[pygame.K_d] and self.y_j > self.vel and self.x_j < fenetre_largeur - self.largeur - self.vel:
            self.x_j += self.vel / math.sqrt(2)
            self.y_j -= self.vel / math.sqrt(2)
            self.statique = False
            self.direction = 'haut-droite'

        elif touche[pygame.K_s] and touche[pygame.K_d] and self.y_j < fenetre_hauteur - self.hauteur - self.vel and self.x_j < fenetre_largeur - self.largeur - self.vel:
            self.x_j += self.vel / math.sqrt(2)
            self.y_j += self.vel / math.sqrt(2)
            self.statique = False
            self.direction = 'bas-droite'

        elif touche[pygame.K_a] and self.x_j > self.vel:
            self.x_j -= self.vel
            self.statique = False
            self.direction = 'gauche'

        elif touche[pygame.K_d] and self.x_j < fenetre_largeur - self.largeur - self.vel:
            self.x_j += self.vel
            self.statique = False
            self.direction = 'droite'

        elif touche[pygame.K_w] and self.y_j > self.vel:
            self.y_j -= self.vel
            self.statique = False
            self.direction = 'haut'

        elif touche[pygame.K_s] and self.y_j < fenetre_hauteur - self.hauteur - self.vel:
            self.y_j += self.vel
            self.statique = False
            self.direction = 'bas'

        else:
            self.statique = True


        if touche[pygame.K_SPACE] and (pygame.time.get_ticks() - self.timestampBalle) > 200:
            #balleSon.play()
            if len(self.balles) < 5:
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
            if 375 > self.y_j or 550 < self.y_j:
                self.x_j += self.vel
                self.statique = True

            if 850 > self.x_j:
                self.x_j += self.vel
                self.statique = True

            elif self.x_j < 1350:
                if self.y_j < 420:
                    self.y_j += self.vel
                    self.statique = True
                elif self.y_j > 500:
                    self.y_j -= self.vel
                    self.statique = True

        if nbr_fond == 2 and (1051 == self.x_j or self.x_j == 1251):
            deja_change = False

        if touche[pygame.K_SPACE] and (pygame.time.get_ticks() - self.timestampBalle) > 50:
            #balleSon.play()
            if len(self.balles) < 5:
                self.balles.append(
                    projectile(round(self.x_j + self.largeur // 2), round(self.y_j + self.hauteur // 2), 7, NOIR,
                               self.direction))
                self.timestampBalle = pygame.time.get_ticks()
        self.hitbox = pygame.Rect(self.x_j + 34, self.y_j + 22, 58, 104)
        if Collision(self):
            self.x_j = x_j_orig
            self.y_j = y_j_orig
            self.hitbox = pygame.Rect(self.x_j + 34, self.y_j + 22, 58, 104)



    def drawjoueur(self):
        #self.hitbox = pygame.Rect(self.x_j + 34, self.y_j + 22, 58, 104)
        #pygame.draw.rect(fenetre, NOIR, self.hitbox,2)
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

        pygame.draw.rect(fenetre, ROUGE, (220, 50, 400, 40))
        pygame.draw.rect(fenetre, (0,100,0),(220, 50, 400 - ((400 / 5) * (5 - self.vie)), 40))
        fenetre.blit(coeur, (200, 50))

#mort = False

class ennemi(object):
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

    def drawennemi(self):
        #self.hitbox = pygame.Rect(self.x_e + 34, self.y_e + 22, 58, 104)
        pygame.draw.rect(fenetre, NOIR, self.hitbox, 2)

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

    def hit(self):
        global list_nbr_e
        if self.vie > 0:
            self.vie -= 1
        else:
            self.visible = True #False
            list_nbr_e -= 1
            #self.x_e = 3000
            #self.y_e = 3000
            #mort.play()
        print('hit')


    def mouvement(self):
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


class projectile(object):
    def __init__(self,x,y,rayon,couleur, direction):
        self.x = x
        self.y = y
        self.rayon = rayon
        self.couleur = couleur
        self.direction = direction
        self.vel = 20

    def draw(self,fenetre):
        fenetre.blit(bullet, (self.x - 5, self.y - 5))

    def mouvement(self):
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


class Button():
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

    def update(self, fenetre):
        if self.image is not None:
            fenetre.blit(self.image, self.rect)
        fenetre.blit(self.text, self.text_rect)

    def checkInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.police.render(self.text_input, True, self.couleur_hover)
        else:
            self.text = self.police.render(self.text_input, True, self.couleur_base)


def play():
    jeu()


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        fenetre.fill((255,255,255))

        OPTIONS_TEXT = get_police(45).render("voici la fenetre options.", True, NOIR)
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(750, 260))
        fenetre.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(750, 460),
                            text_input="BACK", police=get_police(75), couleur_base=NOIR, couleur_hover=VERT)

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(fenetre)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkInput(OPTIONS_MOUSE_POS):
                    menu()

        pygame.display.update()

def menu():
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
                    play()
                if bouton_options.checkInput(menu_position_souris):
                    options()
                if bouton_quit.checkInput(menu_position_souris):
                    pygame.quit()

            pygame.display.update()


run = True
gerard=joueur(250,250,128,128)

def nbr_e_func(nbr_e):
    for i in range(nbr_e):
        global list_nbr_e
        print(nbr_e)
        liste_ennemi.append(ennemi(choice([True, False])))
        list_nbr_e += 1



animation_sprite(liste_animation, etapes_anim, sprite)
animation_sprite_ennemi(liste_animation_ennemi, etapes_anim, sprite_ennemi)

def jeu():
    global touche
    run = True
    while run:
        fps.tick(30)
        drawFenetre()
        touche = pygame.key.get_pressed()
        gerard.mouvement(touche)
        for balle in gerard.balles:
            for e in liste_ennemi:
                if balle.y - balle.rayon < e.hitbox[1] + e.hitbox[3] and balle.y + balle.rayon > e.hitbox[1]:
                    if balle.x + balle.rayon > e.hitbox[0] and balle.x - balle.rayon < e.hitbox[0] + e.hitbox[2]:
                        #hitSon.play()
                        e.hit()
                        gerard.balles.remove(balle)
                        break
            if balle.mouvement():
                gerard.balles.remove(balle)

        for e in liste_ennemi:
            e.mouvement()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

menu()
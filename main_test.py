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
parchemin_obj1 = pygame.image.load(chemin_repertoire + '\contenu\divers\\parchemin_obj1.png')
parchemin_obj2 = pygame.image.load(chemin_repertoire + '\contenu\divers\\parchemin_obj2.png')
texte_interagire = pygame.image.load(chemin_repertoire + '\contenu\divers\\texte_interagire.png')
directions=['gauche','droite','haut','bas']

#balleSon = pygame.mixer.Sound(chemin_repertoire + '\contenu\son\sonTir.wav')
#hitSon = pygame.mixer.Sound(chemin_repertoire + '\contenu\son\hit.wav')

#musique = pygame.mixer.music.load(chemin_repertoire + '\contenu\son\musique.mp3')
#pygame.mixer.music.play(-1)

nbr_fond = 0
change_fond = True
count_e = 0
inter_pnj = False
nbr_dialogue = 0
deja_change = False
count_touche = 0
sortie_possible = False
sortie = False
trouve_arg = False
zone_arg = False



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
nbr_fond = 2
zone_pnj = False
anim_parchemin = -150


def drawFenetre():
    global anim_cooldown, tempsInitial, change_fond, fond, nbr_fond, nbr_e, draw_pnj, zone_pnj, anim_parchemin, nbr_dialogue, deja_change, trouve_arg, zone_arg

    if change_fond == True:
        if nbr_fond == 0:
            fond = pygame.image.load(chemin_repertoire + '\contenu\map\salle_accueil_1.png')
            change_fond = False
            nbr_e_func(0)

        elif nbr_fond == 1:
            fond = pygame.image.load(chemin_repertoire + '\contenu\map\\niveau1_terre.png')
            change_fond = False
            nbr_e_func(0)

        elif nbr_fond == 2:
            fond = pygame.image.load(chemin_repertoire + '\contenu\map\\niveau2_mer.png')
            draw_pnj = True

            change_fond = False
            nbr_e_func(0)
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

            fenetre.blit(texte_interagire, (1050, 630))
            if nbr_dialogue == 1:
                fenetre.blit(texte_pnj1, (300, 600))
            elif nbr_dialogue == 2:
                fenetre.blit(texte_pnj2, (300, 600))
            elif nbr_dialogue == 3:
                fenetre.blit(texte_pnj3, (300, 600))

        if inter_pnj == True:
            if nbr_dialogue == 3:
                if anim_parchemin < -30:
                    anim_parchemin += 5
                fenetre.blit(parchemin_obj2, (-30, anim_parchemin))

            else:
                if anim_parchemin < -30:
                    anim_parchemin += 5
                fenetre.blit(parchemin_obj1, (-30, anim_parchemin))

        if zone_arg == True:
            fenetre.blit(texte_interagire, (1200, 00))

    tempsActuel = pygame.time.get_ticks()
    if tempsActuel - tempsInitial >= anim_cooldown:
        gerard.frame += 1
        tempsInitial = tempsActuel
        if gerard.frame >= len(liste_animation):
            gerard.frame = 0
        #for e in liste_ennemi:
        for e in dico_ennemi.values():
            e.frame += 1
            if e.frame >= len(liste_animation_ennemi):
                e.frame = 0
    gerard.drawjoueur()
    #for e in liste_ennemi:
    for e in dico_ennemi.values():
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


    def mouvement(self,touche):
        global nbr_fond, change_fond, count_e, zone_pnj, inter_pnj, deja_change, sortie, sortie_possible, trouve_arg, nbr_dialogue, anim_parchemin, zone_arg
        zone_arg = False

        if count_e <= 0 and (self.x_j <= 230 and 230 <= self.y_j <= 455):
            if touche[pygame.K_e]:
                nbr_fond +=1
                change_fond = True
                print(nbr_fond)
                self.x_j = 1200
                self.y_j = 500
                count_e = 0
            else:
                print("vous etes sur la zone")

        if nbr_fond == 2 and (1050 < self.x_j < 1250 and 430 < self.y_j < 500):
            zone_pnj = True
            sortie_possible = True
            if touche[pygame.K_e]:
                inter_pnj = True

        else:
            zone_pnj = False
            if sortie_possible == True:
                sortie = True

            if 1350 < self.x_j and(100 > self.y_j < 230):
                if nbr_dialogue == 1:
                    zone_arg = True
                    if touche[pygame.K_e]:
                        trouve_arg = True
                        nbr_dialogue = 3
                        anim_parchemin = -150
                        print('argent trouvé')


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
                self.balles.append(projectile(round(self.x_j + self.largeur // 2), round(self.y_j + self.hauteur//2), 7, NOIR, self.direction))
                self.timestampBalle = pygame.time.get_ticks()


    def drawjoueur(self):
        self.hitbox = pygame.Rect(self.x_j + 34, self.y_j + 22, 58, 104)
        #pygame.draw.rect(fenetre, NOIR, self.hitbox,2)
        if not (self.statique):
            if self.direction == 'gauche' or self.direction == 'haut-gauche' or self.direction == 'bas-gauche':
                fenetre.blit(liste_animation[1][self.frame], (self.x_j, self.y_j))
            elif self.direction == 'droite' or self.direction == 'haut-droite' or self.direction == 'bas-droite':
                fenetre.blit(liste_animation[3][self.frame], (self.x_j, self.y_j))
            elif self.direction == 'haut':
                fenetre.blit(liste_animation[0][self.frame], (self.x_j, self.y_j))
            elif self.direction == 'bas':
                fenetre.blit(liste_animation[2][self.frame], (self.x_j, self.y_j))
        else:
            if self.direction == 'droite' or self.direction == 'haut-droite' or self.direction == 'bas-droite':
                fenetre.blit(liste_animation[3][0], (self.x_j, self.y_j))
            if self.direction == 'gauche' or self.direction == 'haut-gauche' or self.direction == 'bas-gauche':
                fenetre.blit(liste_animation[1][0], (self.x_j, self.y_j))
            if self.direction == 'haut':
                fenetre.blit(liste_animation[0][0], (self.x_j, self.y_j))
            if self.direction == 'bas':
                fenetre.blit(liste_animation[2][0], (self.x_j, self.y_j))

        for balle in self.balles:
            balle.draw(fenetre)


mort = False

class ennemi(object):
    def __init__(self,x,y,hauteur,largeur, intelligence):
        self.direction = directions[randint(0,3)]
        self.x_e = x
        self.y_e = y
        self.hauteur = hauteur
        self.largeur = largeur
        self.vel = 4
        self.statique = True
        self.frame=0
        self.Tempsdirection=pygame.time.get_ticks()
        self.intelligence = intelligence
        self.hitbox = pygame.Rect(self.x_e + 34, self.y_e + 22, 58, 104)
        self.vie = 10
        self.visible = True
        self.Collision = False
        self.decoincerX = False
        self.decoincerY = False
        self.a_mouvement = True

    def drawennemi(self):
        self.hitbox = pygame.Rect(self.x_e + 34, self.y_e + 22, 58, 104)
        pygame.draw.rect(fenetre, NOIR, self.hitbox, 2)

        if self.visible:
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
        global mort, count_e
        if self.vie > 0:
            self.vie-=1
        elif self.vie == 0:
            count_e -=1
            print(count_e)
            self.vie -=1
        else:
            self.visible = False
            mort = True
            self.a_mouvement = False
            self.y_e = 3000
            self.x_e = 3000

            #for i in list(dico_ennemi.keys()):
                #if self.vie <= 0:
                    #del(dico_ennemi[i])
            #print(dico_ennemi)
        print('hit')


    def mouvement(self):
        #for e in liste_ennemi:
        for e in dico_ennemi.values():
            if self.a_mouvement == False:
                return
            else:
                if e != self:
                    if pygame.Rect.colliderect(e.hitbox, self.hitbox):
                        self.Collision = True
                        if self.direction == 'droite' and e.direction == 'gauche' or self.direction == 'gauche' and e.direction == 'droite':
                            self.decoincerX = True
                        if self.direction == 'haut' and e.direction == 'bas' or self.direction == 'bas' and e.direction == 'haut':
                            self.decoincerY = True
                    else:
                        self.Collision = False

        if self.decoincerX:
            #for e in liste_ennemi:
            for e in dico_ennemi.values():
                if e != self:
                    self.y_e += 200
                    print('ca va vite en y')
            self.decoincerX = False
            if self.direction == 'droite':
                self.direction = 'gauche'
            else:
                self.direction = 'droite'
            self.Collision = False

        if self.decoincerY:
            #for e in liste_ennemi:
            for e in dico_ennemi.values():
                if e != self:
                    self.x_e += 200
                    print('ca va vite en x cette fois')
            self.decoincerX = False
            if self.direction == 'bas':
                self.direction = 'haut'
            else:
                self.direction = 'bas'
            self.Collision = False


        if pygame.Rect.colliderect(gerard.hitbox, self.hitbox):
            return


        if self.intelligence and not self.Collision:
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
        if not self.intelligence and not self.Collision:
            if self.direction == 'droite':
                if self.x_e < (fenetre_largeur - 128):
                    self.x_e += self.vel
                else:
                    self.direction = 'gauche'
            if self.direction == 'gauche':
                if self.x_e > 0:
                    self.x_e -= self.vel
                else:
                    self.direction = 'droite'
            if self.direction == 'haut':
                if self.y_e > 0:
                    self.y_e -= self.vel
                else:
                    self.direction = 'bas'
            if self.direction == 'bas':
                if self.y_e < (fenetre_hauteur - 150):
                    self.y_e += self.vel
                else:
                    self.direction = 'haut'

            if pygame.time.get_ticks() - self.Tempsdirection > randint(300, 10000):
                self.direction = directions[randint(0, 3)]
                self.Tempsdirection = pygame.time.get_ticks()

class projectile(object):
    def __init__(self,x,y,rayon,couleur, direction):
        self.x = x
        self.y = y
        self.rayon = rayon
        self.couleur = couleur
        self.direction = direction
        self.vel = 20

    def draw(self,fenetre):
        pygame.draw.circle(fenetre, self.couleur, (self.x, self.y), self.rayon)

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

run = True
gerard=joueur(250,250,128,128)


def nbr_e_func(nbr_e):
    global count_e
    print(nbr_e)
    for i in range(nbr_e):
        #liste_ennemi.append(ennemi(randint(0,fenetre_largeur-128),randint(0,fenetre_hauteur-128),128,128, True))#choice([True, False])))
        dico_ennemi["ennemi" + str(count_e)] = ennemi(randint(0,fenetre_largeur-128),randint(0,fenetre_hauteur-128),128,128, True)#choice([True, False])))
        print(dico_ennemi)
        count_e += 1


animation_sprite(liste_animation, etapes_anim, sprite)
animation_sprite_ennemi(liste_animation_ennemi, etapes_anim, sprite_ennemi)


while run:
    fps.tick(30)
    drawFenetre()
    touche = pygame.key.get_pressed()
    gerard.mouvement(touche)
    for balle in gerard.balles:
        #for e in liste_ennemi:
        for e in dico_ennemi.values():
            if balle.y - balle.rayon < e.hitbox[1] + e.hitbox[3] and balle.y + balle.rayon > e.hitbox[1]:
                if balle.x + balle.rayon > e.hitbox[0] and balle.x - balle.rayon < e.hitbox[0] + e.hitbox[2]:
                    #hitSon.play()
                    ennemi.hit(e)
                    gerard.balles.remove(balle)
                    break
        if balle.mouvement():
            gerard.balles.remove(balle)

    #for e in liste_ennemi:
    for e in dico_ennemi.values():
        e.mouvement()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
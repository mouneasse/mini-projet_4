from pygame import *
import pygame
import os

pygame.init()

couleur_fond = (200, 180, 100)

chemin_repertoire = os.getcwd()
print("le repertoire où est enregistré le fichier du jeu est: " + chemin_repertoire)

fenetre_hauteur = 900
fenetre_largeur = 1500
fenetre = pygame.display.set_mode((fenetre_largeur, fenetre_hauteur))
fenetre.fill(couleur_fond)

couleur_bouton_n_clique = (170, 170, 170)
couleur_bouton_clique = (100, 100, 100)
couleur_noir = (0, 0, 0)

largeur_fenetre = fenetre.get_width()
hauteur_fenetre = fenetre.get_height()

continue_boucle_1 = True

police_bouton = pygame.font.SysFont('Arial', 35)
deroulement = 0
texte_pseudo = ""

pygame.display.set_caption("mini_projet4")
# o_depart_salle_acceuille_x = 0
# co_depart_salle_acceuille_y = 0
commencer = 0
heros = pygame.image.load(chemin_repertoire + "\contenu\personnage\heros_avant_statique.png")
position = heros.get_rect()
position = position.move(400, 200)

velocite_joueur = 14
velocite_joueur_diagonale = velocite_joueur-5

collision_droite = False
collision_gauche = False
collision_haute = False
collision_basse = False

tapis_bleu_salle_acceuille = False
tapis_rouge_salle_acceuille = False

texte_jouer_tapis_rouge = pygame.image.load(chemin_repertoire + "\contenu\divers_image\exte_jouer_tapis_rouge.png")
texte_jouer_tapis_rouge = pygame.transform.scale(texte_jouer_tapis_rouge, (500, 200))

texte_jouer_tapis_bleu = pygame.image.load(chemin_repertoire + "\contenu\divers_image\exte_jouer_tapis_bleu.png")
texte_jouer_tapis_bleu = pygame.transform.scale(texte_jouer_tapis_bleu, (500, 200))

avancement_niveau = 0

position_transition_x = 0

transition = 0

clock = pygame.time.Clock()


def reset_menu():
    fenetre.fill(couleur_fond)


def setup_menu_script():
    global deroulement
    if deroulement != 0:
        return

    setup_bouton1 = police_bouton.render("paramètre", True, couleur_bouton_n_clique)
    setup_bouton2 = police_bouton.render("jouer", True, couleur_bouton_n_clique)

    if largeur_fenetre / 2 <= co_souris[0] <= largeur_fenetre / 2 + 160 and hauteur_fenetre / 2 <= co_souris[1] <= hauteur_fenetre / 2 + 40:
        pygame.draw.rect(fenetre, couleur_bouton_n_clique, [largeur_fenetre / 2, hauteur_fenetre / 2, 160, 40])
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.mixer.music.load(chemin_repertoire + "\contenu\son\clique_bouton1.mp3")
            pygame.mixer.music.play(1)
            pygame.time.wait(100)

    elif largeur_fenetre / 2 <= co_souris[0] <= largeur_fenetre / 2 + 160 and hauteur_fenetre / 2 - 60 <= co_souris[1] <= hauteur_fenetre / 2 - 20:
        pygame.draw.rect(fenetre, couleur_bouton_n_clique, [largeur_fenetre / 2, hauteur_fenetre / 2 - 60, 160, 40])
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.mixer.music.load(chemin_repertoire + "\contenu\son\clique_bouton1.mp3")
            pygame.mixer.music.play(1)
            pygame.time.wait(100)
            deroulement = 1
            reset_menu()
            carre_pseudo()

    else:
        pygame.draw.rect(fenetre, couleur_bouton_clique, [largeur_fenetre / 2, hauteur_fenetre / 2, 160, 40])
        pygame.draw.rect(fenetre, couleur_bouton_clique, [largeur_fenetre / 2, hauteur_fenetre / 2 - 60, 160, 40])

    if deroulement == 0:
        fenetre.blit(setup_bouton1, (largeur_fenetre / 2, hauteur_fenetre / 2))
        fenetre.blit(setup_bouton2, (largeur_fenetre / 2, hauteur_fenetre / 2 - 60))


def carre_pseudo():
    global carre_pseudo, carre_bouton_valider_pseudo
    carre_pseudo = pygame.Rect(largeur_fenetre / 2, hauteur_fenetre / 2, 40, 50)


def choisir_pseudo():
    global texte_pseudo, deroulement
    if deroulement != 1:
        return

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_BACKSPACE:
            texte_pseudo = texte_pseudo[:-1]
        else:
            texte_pseudo += event.unicode

    if largeur_fenetre / 2 - 5 <= co_souris[0] <= largeur_fenetre / 2 - 5 + 120 and hauteur_fenetre / 2 + 95 <= co_souris[1] <= hauteur_fenetre / 2 + 95 + 50:
        pygame.draw.rect(fenetre, couleur_bouton_clique, (largeur_fenetre / 2 - 5, hauteur_fenetre / 2 + 95, 120, 50))
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.mixer.music.load(chemin_repertoire + "\contenu\son\clique_bouton1.mp3")
            pygame.mixer.music.play(1)
            deroulement = 2
            reset_menu()
            pygame.time.wait(100)
    else:
        pygame.draw.rect(fenetre, couleur_bouton_n_clique, (largeur_fenetre / 2 - 5, hauteur_fenetre / 2 + 95, 120, 50))

    texte_info_pseudo = police_bouton.render("Veuillez entrer votre pseudo:", True, couleur_noir)
    texte_saisie_pseudo = police_bouton.render(texte_pseudo, True, couleur_noir)
    texte_bouton_valider_pseudo = police_bouton.render("valider", True, couleur_noir)
    print(texte_pseudo)

    pygame.draw.rect(fenetre, (120, 171, 161), carre_pseudo)
    pygame.Rect(largeur_fenetre / 2, hauteur_fenetre / 2, 40, 50)
    fenetre.blit(texte_info_pseudo, (largeur_fenetre / 2 - 300, hauteur_fenetre / 2 - 80))
    fenetre.blit(texte_saisie_pseudo, (largeur_fenetre / 2 + 5, hauteur_fenetre / 2 + 5))
    fenetre.blit(texte_bouton_valider_pseudo, (largeur_fenetre / 2, hauteur_fenetre / 2 + 100, 40, 100))

    carre_pseudo.w = max(100, texte_saisie_pseudo.get_width() + 10)


while continue_boucle_1:
    co_souris = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        elif deroulement == 0:
            setup_menu_script()

        elif deroulement == 1:
            choisir_pseudo()

        elif deroulement == 2:
            continue_boucle_1 = False

    pygame.display.update()
    clock.tick(30)


def deplacement():
    global position, touche_clavier, heros

    touche_clavier = pygame.key.get_pressed()

    if touche_clavier[K_z] and touche_clavier[K_d]:
        if not (collision_haute or collision_droite):
            position = position.move(velocite_joueur_diagonale, -velocite_joueur_diagonale)

    elif touche_clavier[K_z] and touche_clavier[K_q]:
        if not (collision_haute or collision_gauche):
            position = position.move(-velocite_joueur_diagonale, -velocite_joueur_diagonale)

    elif touche_clavier[K_s] and touche_clavier[K_d]:
        if not (collision_basse or collision_droite):
            position = position.move(velocite_joueur_diagonale, velocite_joueur_diagonale)

    elif touche_clavier[K_s] and touche_clavier[K_q]:
        if not (collision_basse or collision_gauche):
            position = position.move(-velocite_joueur_diagonale, velocite_joueur_diagonale)

    elif touche_clavier[K_z]:
        if not collision_haute:
            position = position.move(0, -velocite_joueur)
            heros = pygame.image.load(chemin_repertoire + "\contenu\personnage\heros_arriere_statique.png")

    elif touche_clavier[K_s]:
        if not collision_basse:
            position = position.move(0, velocite_joueur)
            heros = pygame.image.load(chemin_repertoire + "\contenu\personnage\heros_avant_statique.png")

    elif touche_clavier[K_q]:
        if not collision_gauche:
            position = position.move(-velocite_joueur, 0)
            heros = pygame.image.load(chemin_repertoire + "\contenu\personnage\heros_cote_gauche_statique.png")

    elif touche_clavier[K_d]:
        if not collision_droite:
            position = position.move(velocite_joueur, 0)
            heros = pygame.image.load(chemin_repertoire + "\contenu\personnage\heros_cote_droit_statique.png")


couleur_animation_chargement_rouge = 255
couleur_animation_chargement_vert = 255
couleur_animation_chargement_bleu = 0

fin_couleur_animation_rouge = False
fin_couleur_animation_vert = False
fin_couleur_animation_bleu = False

couleur_animation_rouge = True
couleur_animation_vert = False
couleur_animation_bleu = False


def transition_chargement():
    global position_transition_x, commencer, couleur_animation_chargement_rouge, fin_couleur_animation_rouge, couleur_animation_chargement_vert, couleur_animation_chargement_bleu, fin_couleur_animation_bleu, fin_couleur_animation_vert, couleur_animation_rouge, couleur_animation_bleu, couleur_animation_vert
    if transition == 0:
        return

    if commencer <= 100:
        commencer += 1
        print(commencer)
        pygame.draw.rect(fenetre, (36, 38, 37), [0, 0, largeur_fenetre, hauteur_fenetre])

        texte_chargement = pygame.image.load(chemin_repertoire + "\contenu\divers_image\\texte_chargement.png")
        texte_chargement = pygame.transform.scale(texte_chargement, (1100, 618))

        pygame.draw.rect(fenetre, (210, 248, 1), [450, 400, position_transition_x, 50], 25, 30, 30, 30, 30)
        pygame.draw.rect(fenetre, (200, 236, 1), [450, 400, 600, 50], 5, 30, 30, 30, 30)
        if position_transition_x < 600:
            position_transition_x += 7

        fenetre.blit(texte_chargement, (200, 0))
        pygame.time.wait(10)

    elif commencer <= 101:
        if couleur_animation_rouge == True:
            if fin_couleur_animation_rouge == False:
                if couleur_animation_chargement_rouge == 255:
                    fin_couleur_animation_rouge = True
                else:
                    couleur_animation_chargement_rouge += 1
            else:
                couleur_animation_chargement_rouge -= 1
                couleur_animation_chargement_bleu += 1
                if couleur_animation_chargement_rouge == 0:
                    couleur_animation_vert = True
                    couleur_animation_rouge = False

        if couleur_animation_vert == True:
            if fin_couleur_animation_vert == False:
                if couleur_animation_chargement_vert == 255:
                    fin_couleur_animation_vert = True
                else:
                    couleur_animation_chargement_vert += 1
            else:
                couleur_animation_chargement_vert -= 1
                couleur_animation_chargement_rouge += 1
                if couleur_animation_chargement_vert == 0:
                    couleur_animation_bleu = True
                    couleur_animation_vert = False

        if couleur_animation_bleu == True:
            if fin_couleur_animation_bleu == False:
                if couleur_animation_chargement_bleu == 255:
                    fin_couleur_animation_bleu = True
                else:
                    couleur_animation_chargement_bleu += 1
            else:
                couleur_animation_chargement_bleu -= 1
                couleur_animation_chargement_vert += 1
                if couleur_animation_chargement_bleu == 0:
                    couleur_animation_rouge = True
                    couleur_animation_bleu = False

        texte_fin_chargement = police_bouton.render("appuyez sur une touche pour continuer", True, (couleur_animation_chargement_rouge, couleur_animation_chargement_vert, couleur_animation_chargement_bleu))
        fenetre.blit(texte_fin_chargement, (largeur_fenetre / 2 - 300, hauteur_fenetre / 2 + 100, 20, 70))
        pygame.time.delay(10)


def salle_acceuille():
    global commencer, salle_acceuille_1, position, heros, collision_basse, collision_droite, collision_gauche, collision_haute, tapis_rouge_salle_acceuille, tapis_bleu_salle_acceuille, avancement_niveau, transition
    if avancement_niveau != 0:
        return

    if commencer <= 10:
        salle_acceuille_1 = pygame.image.load(chemin_repertoire + "\contenu\map\salle_acceuille_1.png")
        salle_acceuille_1 = pygame.transform.scale(salle_acceuille_1, (1500, 900))
        fenetre.blit(salle_acceuille_1, (0, 0))
        fenetre.blit(heros, position)
        commencer += 1
        print(commencer)

    else:

        if event.type == pygame.KEYDOWN:
            print("y = ", position[1])
            print("x = ", position[0], "\n")
            fenetre.blit(salle_acceuille_1, (0, 0))

            if (525 < position[0] < 875) and (235 < position[1] < 470):  # collision des caisses au milieu de la salle
                if 505 <= position[0] <= 545:  # coté droit
                    collision_droite = True
                    position = position.move(-velocite_joueur, 0)
                elif 855 <= position[0] <= 895:  # coté gauche
                    collision_gauche = True
                    position = position.move(velocite_joueur, 0)
                elif 215 <= position[1] <= 255:  # coté bas
                    collision_basse = True
                    position = position.move(0, -velocite_joueur)
                elif 450 <= position[1] <= 490:  # coté haut
                    collision_haute = True
                    position = position.move(0, velocite_joueur)

            elif position[0] <= 95:  # collision du mur de gauche
                collision_gauche = True
                position = position.move(velocite_joueur, 0)
            elif position[0] >= 1325:  # # collision du mur de droite
                collision_droite = True
                position = position.move(-velocite_joueur, 0)
            elif position[1] <= -25:  # collision du mur du haut
                collision_haute = True
                position = position.move(0, velocite_joueur)
            elif position[1] >= 745:  # collision du mur du bas
                collision_basse = True
                position = position.move(0, -velocite_joueur)
            else:  # si il n'y a pas de collision alors on met les variable de collision à 0
                collision_haute = False
                collision_basse = False
                collision_droite = False
                collision_gauche = False

            if (position[0] <= 255) and (230 <= position[1] <= 470):
                tapis_rouge_salle_acceuille = True

            elif (position[0] >= 1160) and (235 <= position[1] <= 465):
                tapis_bleu_salle_acceuille = True

            deplacement()

            fenetre.blit(heros, position)

            if tapis_rouge_salle_acceuille == True:
                fenetre.blit(texte_jouer_tapis_rouge, (0, 200))
                tapis_rouge_salle_acceuille = False
                if event.type == pygame.KEYDOWN:
                    if touche_clavier[K_e]:
                        commencer = 0
                        avancement_niveau += 1
                        transition = 1
                        heros = pygame.image.load(chemin_repertoire + "\contenu\personnage\heros_avant_statique.png")
                        position = heros.get_rect()

            elif tapis_bleu_salle_acceuille == True:
                fenetre.blit(texte_jouer_tapis_bleu, (1000, 200))
                tapis_bleu_salle_acceuille = False


mechant_niveau1_1 = pygame.image.load(chemin_repertoire + "\contenu\personnage\mechant_alien_avant_statique.png")
position_mechant_niveau1_1 = mechant_niveau1_1.get_rect()
position_mechant_niveau1_1 = position_mechant_niveau1_1.move(300, 300)
velocite_mechant_niveau1 = velocite_joueur-13


def mechant_niveau1():
    global position, position_mechant_niveau1_1

    deplacement_mechant_niveau1_1_x = position[0] - position_mechant_niveau1_1[0]
    deplacement_mechant_niveau1_1_y = position[1] - position_mechant_niveau1_1[1]

    if deplacement_mechant_niveau1_1_x < 0:
        position_mechant_niveau1_1 = position_mechant_niveau1_1.move(-velocite_mechant_niveau1, 0)
    else:
        position_mechant_niveau1_1 = position_mechant_niveau1_1.move(velocite_mechant_niveau1, 0)

    if deplacement_mechant_niveau1_1_y < 0:
        position_mechant_niveau1_1 = position_mechant_niveau1_1.move(0, -velocite_mechant_niveau1)
    else:
        position_mechant_niveau1_1 = position_mechant_niveau1_1.move(0, velocite_mechant_niveau1)

    fenetre.blit(salle_niveau1, (0, 0))
    fenetre.blit(mechant_niveau1_1, position_mechant_niveau1_1)
    fenetre.blit(heros, position)


def niveau1():
    global heros, commencer, position, salle_niveau1, collision_gauche, collision_droite, collision_haute, collision_basse, mechant_niveau1_1

    if avancement_niveau != 1:
        return

    if commencer <= 100:
        print(commencer)

    elif commencer == 101:
        if event.type == pygame.KEYDOWN:
            salle_niveau1 = pygame.image.load(chemin_repertoire + "\contenu\map\\niveau1_map.png")
            salle_niveau1 = pygame.transform.scale(salle_niveau1, (1500, 900))
            position = position.move(1200, 300)
            commencer += 1

    else:

        if event.type == pygame.KEYDOWN:
            print("y = ", position[1])
            print("x = ", position[0], "\n")

            if position[0] <= 55:  # collision du mur de gauche
                collision_gauche = True
                position = position.move(velocite_joueur, 0)
            elif position[0] >= 1355:  # # collision du mur de droite
                collision_droite = True
                position = position.move(-velocite_joueur, 0)
            elif position[1] <= 50:  # collision du mur du haut
                collision_haute = True
                position = position.move(0, velocite_joueur)
            elif position[1] >= 675:  # collision du mur du bas
                collision_basse = True
                position = position.move(0, -velocite_joueur)
            else:  # si il n'y a pas de collision alors on met les variable de collision à 0
                collision_haute = False
                collision_basse = False
                collision_droite = False
                collision_gauche = False

            deplacement()


pygame.key.set_repeat(10, 40)

while True:
    transition_chargement()
    if avancement_niveau == 1 and commencer >= 102:
        mechant_niveau1()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        salle_acceuille()
        niveau1()

    pygame.display.update()
    clock.tick(30)

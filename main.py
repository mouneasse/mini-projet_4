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

pygame.display.set_caption("mini_projet8")
#o_depart_salle_acceuille_x = 0
#co_depart_salle_acceuille_y = 0
commencer = 0
heros = pygame.image.load(chemin_repertoire + "\contenu\personnage\heros_avant_statique.png")
position = heros.get_rect()

velocite_joueur = 15

clock = pygame.time.Clock()

def reset_menu():
    fenetre.fill(couleur_fond)


def setup_menu_script():
    global deroulement
    if deroulement != 0:
        return

    setup_bouton1 = police_bouton.render("paramètre", True, couleur_bouton_n_clique)
    setup_bouton2 = police_bouton.render("jouer", True, couleur_bouton_n_clique)

    if largeur_fenetre / 2 <= co_souris[0] <= largeur_fenetre/ 2 + 160 and hauteur_fenetre / 2 <= co_souris[1] <= hauteur_fenetre / 2 + 40:
        pygame.draw.rect(fenetre, couleur_bouton_n_clique, [largeur_fenetre / 2, hauteur_fenetre / 2, 160, 40])
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.mixer.music.load(chemin_repertoire + "\contenu\son\clique_bouton1.mp3")
            pygame.mixer.music.play(1)
            pygame.time.wait(100)

    elif largeur_fenetre / 2 <= co_souris[0] <= largeur_fenetre / 2 + 160 and hauteur_fenetre / 2 - 60 <= co_souris[1] <= hauteur_fenetre / 2 - 20:
        pygame.draw.rect(fenetre, couleur_bouton_n_clique, [largeur_fenetre / 2, hauteur_fenetre / 2-60, 160, 40])
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

    if largeur_fenetre / 2-5 <= co_souris[0] <= largeur_fenetre / 2-5+120 and hauteur_fenetre / 2+95 <= co_souris[1] <= hauteur_fenetre / 2+95+50:
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
    fenetre.blit(texte_info_pseudo, (largeur_fenetre / 2-300, hauteur_fenetre / 2-80))
    fenetre.blit(texte_saisie_pseudo, (largeur_fenetre / 2+5, hauteur_fenetre / 2+5))
    fenetre.blit(texte_bouton_valider_pseudo, (largeur_fenetre / 2, hauteur_fenetre / 2+100, 40, 100))

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


def salle_acceuille():
    global commencer, salle_acceuille_1, position, heros
    if commencer <= 10:
            salle_acceuille_1 = pygame.image.load(chemin_repertoire + "\contenu\map\salle_acceuille_1.png")
            heros = pygame.transform.scale(heros, (300, 260))
            salle_acceuille_1 = pygame.transform.scale(salle_acceuille_1, (1500, 900))
            fenetre.blit(salle_acceuille_1, (0, 0))
            fenetre.blit(heros, position)
            commencer += 1
            print((commencer))
    elif commencer > 10:
        if event.type == pygame.KEYDOWN:
            touche_clavier = pygame.key.get_pressed()
            fenetre.blit(salle_acceuille_1, (0, 0))

            if touche_clavier[K_z] and touche_clavier[K_d]:
                position = position.move(velocite_joueur, -velocite_joueur)

            elif touche_clavier[K_z] and touche_clavier[K_q]:
                position = position.move(-velocite_joueur, -velocite_joueur)

            elif touche_clavier[K_s] and touche_clavier[K_d]:
                position = position.move(velocite_joueur, velocite_joueur)

            elif touche_clavier[K_s] and touche_clavier[K_q]:
                position = position.move(-velocite_joueur, velocite_joueur)

            elif touche_clavier[K_z]:
                position = position.move(0, -velocite_joueur)
                heros = pygame.image.load(chemin_repertoire + "\contenu\personnage\heros_arriere_statique.png")

            elif touche_clavier[K_s]:
                position = position.move(0, velocite_joueur)
                heros = pygame.image.load(chemin_repertoire + "\contenu\personnage\heros_avant_statique.png")

            elif touche_clavier[K_q]:
                position = position.move(-velocite_joueur, 0)
                heros = pygame.image.load(chemin_repertoire + "\contenu\personnage\heros_cote_gauche_statique.png")

            elif touche_clavier[K_d]:
                position = position.move(velocite_joueur, 0)
                heros = pygame.image.load(chemin_repertoire + "\contenu\personnage\heros_cote_droit_statique.png")

            heros = pygame.transform.scale(heros, (300, 260))
            fenetre.blit(heros, position)


pygame.key.set_repeat(10, 40)

while True:
    co_souris = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()

        salle_acceuille()

    pygame.display.update()
    clock.tick(300)


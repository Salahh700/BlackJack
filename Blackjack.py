import random
print("Bienvenue sur le BlackJack de l'avenir ")
play_or_not=0
start_game=False
compteur_un=0
compteur_deux=0
stop_or_not1=False
stop_or_not2=False
test_random2=0
test_random1=0
stop_game=False
mise_gagnant=0
mise_player1=0
mise_player2=0
choice_1=0
choice_2=0
is_stop = False
choice_stop=0
final=False
is_stop2=False

while start_game !=True:
    play_or_not=str(input("Êtes vous prêts à jouer, oui ou non "))
    if play_or_not == "non" or play_or_not=="NON":
        print("Revenez lorsque vous voulez jouer !")
    else:
        print("C'est parti !")
        start_game=True
name_player1=input("Joueur 1 quel est ton nom ? ")
name_player2=input("Joueur 2 quel est ton nom ? ")
print(f"Parfait {name_player1} et {name_player2} commençons le jeu")



while stop_game !=True:
    mise_player1 = int(input(f"{name_player1} De combien est ta mise? "))
    print(mise_player1)
    mise_player2 = int(input(f"{name_player2} De combien est ta mise? "))
    print(f"{mise_player2}")
    print("Nous allons maintenant tirer les cartes")


    while stop_or_not1==False :
        if compteur_un <= 21:
            print("Piochons")
            test_random1=random.randint(1,10)
            print(f'La carte tirée est {test_random1}')
            compteur_un = compteur_un + test_random1
            print(compteur_un)
            choice_1=input(f'{name_player1} Veux tu t\'arrêter ? ')
            if choice_1=="Oui" or choice_1=="OUI" or choice_1=="oui" or choice_1=="We" or choice_1=="we":
                stop_or_not1=True
                is_stop=True
            print(compteur_un)
        elif compteur_un>21:
            final=True
            stop_or_not1=True
            is_stop=False
            print("Tu as dépassé 21, tu as donc perdu ")


    if is_stop==True:
        print(f'Au tour de {name_player2} !')
        while stop_or_not2==False :
            if compteur_deux<21:
                print("Piochons ")
                test_random2=random.randint(1, 10)
                print(f"la carte tirée est {test_random2} ")
                compteur_deux = compteur_deux + test_random2
                print(compteur_deux)
                choice_2=input(f'{name_player2} Veux tu t\'arrêter ? ')
                if choice_2=="Oui" or choice_2=="OUI" or choice_2=="oui" or choice_2=="We" or choice_2=="we":
                    stop_or_not2=True
                    print(compteur_deux)
            elif compteur_deux>21 :
                final=True
                stop_or_not2=True
                print ("Tu as dépassé 21, tu as donc perdu ")


    while final==True:
        if compteur_un>21 :
            mise_gagnant = mise_player1 + mise_player2
            print(f'{name_player2} tu as gagné {mise_gagnant} car l\'autre joueur a dépassé')
            mise_player1=0
        elif compteur_deux>21:
            mise_gagnant = mise_player1 + mise_player2
            print(f'{name_player1}tu as gagné {mise_gagnant} car l\'autre joueur a dépassé')
            mise_player2=0
        final=False
        is_stop2=True



    while final==False and is_stop2==False:
        if compteur_un<compteur_deux :
            mise_gagnant=mise_player1+mise_player2
            print(f'{name_player2}tu as gagné {mise_gagnant}')
            mise_player1=0

        elif compteur_deux<compteur_un:
            mise_gagnant = mise_player1 + mise_player2
            print(f'{name_player1}tu as gagné {mise_gagnant}')
            mise_player2=0
        final=True
    final=True

    compteur_deux=0
    compteur_un=0
    choice_1=0
    choice_2=0
    stop_or_not1=False
    stop_or_not2=False
    is_stop=False
    choice_stop=input("Voulez vous continuer ? ")

    if choice_stop=="oui" or choice_stop=="OUI" or choice_stop=="Oui" :
        stop_game=False
        print("Letsgo")
        choice_stop=0
        mise_player1=0
        mise_player2=0
    else:
        stop_game=True
        print("A une prochaine !")



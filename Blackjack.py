import random
print("Bienvenue sur le BlackJack tah les fous ")
sale=0
mal=False
Blackos1=0
Blackos2=0
StopOrNot2=False
StopOrNot1=False
testrandom2=0
testrandom1=0
stopGame=False
MiseGagnant=0
MisePlayer1=0
MisePlayer2=0
choix1=0
choix2=0
isStop = False
Choix_stop=0
ContreUno=True

while mal !=True:
    sale=str(input("Êtes vous prêts à jouer, oui ou non "))
    if sale == "non":
        print("Revenez lorsque vous voulez jouer !")
    else:
        print("C'est parti !")
        mal=True
NamePlayer1=input("Joueur 1 quel est ton nom ? ")
NamePlayer2=input("Joueur 2 quel est ton nom ? ")
print(f"Carré {NamePlayer1} et {NamePlayer2} commençons le jeu")



while stopGame !=True:
    MisePlayer1 = int(input(f"{NamePlayer1} De combien est ta mise?"))
    print(MisePlayer1)
    MisePlayer2 = int(input(f"{NamePlayer2} De combien est ta mise?"))
    print(f"{MisePlayer2}")
    print("Nous allons maintenant tirer les cartes")


    while StopOrNot1==False :
        if Blackos1<=21:
            print("Tiens ça")
            testrandom1=random.randint(1,10)
            print(f'La carte tirée est {testrandom1}')
            Blackos1 = Blackos1 + testrandom1
            print(Blackos1)
            choix1=input(f'{NamePlayer1} Veux tu t\'arrêter ? ')
            if choix1=="Oui" or choix1=="OUI" or choix1=="oui" or choix1=="We" or choix1=="we":
                StopOrNot1=True
                isStop=True
            print(Blackos1)
        elif Blackos1>21:
            ContreUno=True
            StopOrNot1=True
            isStop=False
            print("Tu as dépassé t'as perdu ")

    if isStop==True:
        while StopOrNot2==False :
            if Blackos2<21:
                print("Tiens ça ")
                testrandom2=random.randint(1, 10)
                print(f"la carte tirée est {testrandom2}")
                Blackos2 = Blackos2 + testrandom2
                print(Blackos2)
                choix2=input(f'{NamePlayer2} Veux tu t\'arrêter ? ')
                if choix2=="Oui" or choix2=="OUI" or choix2=="oui" or choix2=="We" or choix2=="we":
                    StopOrNot2=True
                    print(Blackos2)
            elif Blackos2>21 :
                ContreUno=True
                StopOrNot2=True
                print ("gros con t'as dépassé t'as perdu ")




    while ContreUno==True:
        if Blackos1>21 :
            MiseGagnant = MisePlayer1 + MisePlayer2
            print(f'{NamePlayer2}tu as gagné {MiseGagnant} car l\'autre con a dépassé')
            MisePlayer1=0
        elif Blackos2>21:
            MiseGagnant = MisePlayer1 + MisePlayer2
            print(f'{NamePlayer1}tu as gagné {MiseGagnant} car l\'autre con a dépassé')
            MisePlayer2=0
        ContreUno=False
    ContreUno=True



    while ContreUno==False :
        if Blackos1<Blackos2 :
            MiseGagnant=MisePlayer1+MisePlayer2
            print(f'{NamePlayer2}tu as gagné {MiseGagnant}')
            MisePlayer1=0

        elif Blackos2<Blackos1:
            MiseGagnant = MisePlayer1 + MisePlayer2
            print(f'{NamePlayer1}tu as gagné {MiseGagnant}')
            MisePlayer2=0
        ContreUno=True
    ContreUno=True

    Blackos1=0
    Blackos2=0
    choix1=0
    choix2=0
    StopOrNot1=False
    StopOrNot2=False
    isStop=False
    Choix_stop=input("Voulez vous continuer ? ")

    if Choix_stop=="oui" or Choix_stop=="OUI" or Choix_stop=="Oui"or Choix_stop=="We"or Choix_stop=="we" :
        stopGame=False
        print("Letsgo")
        Choix_stop=0
        MisePlayer1=0
        MisePlayer2=0
    else:
        stopGame=True
        print("Cassez vous alors !")










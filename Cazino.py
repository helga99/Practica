#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#PROBLEMA CU CAZINO:
#Un faimos cazino din București dorește să detecteze mai rapid trișorii de la mesele lor de cărți.
#Folosind un program de recunoaștere a imaginilor se pot detecta ce cărți sunt jucate de fiecare jucător
#de la masă și se dorește să se descopere dacă vreunul din ei a scos cărți din buzunar. Jocul monitorizat
#se joacă cu două pachete clasice (52 de cărți fiecare, fără Joker).
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#CERINTA:
#
#Scrieți un program care să ajute la detectarea trișorilor. În cazul în care se detectează că o carte apare
#de prea multe ori, programul va afișa cartea și va opri jocul.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#DATE DE INTRARE:
#
#Se vor citi de la tastatură (fluxul stdin) următoarele date:
#  • Pe prima linie se află numărul n, reprezentând numărul maxim de mâini ce vor fi jucate;
#  • Pe următoarele n linii se află cartea jucată, în formatul:
#    <număr_carte> <semn_carte>
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#DATE DE IESIRE:
#
#În cazul în care nimeni nu încearcă să trișeze se va afișa textul JOC OK. În cazul în care cineva a
#încercat sa trișeze, se va afișa cartea problemă în același format ca la intrare: numărul cărții urmat de
#semn, separate prin spațiu.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#REZOLVARE:

n = int(input("Number n, number of cards: "))

card_dict ={}
i = 0
message = "JOC OK"

while i < n:
    card = input()
    if card in card_dict:   #checking the card appearance
        card_dict[card] += 1
        if card_dict[card] == 3:    #check if the card has appeard 3 times
            message = card
    else:
        card_dict[card] = 1
    i += 1

print(message) 


#REZOLVARE CU OPRIRE DUPA A 3-A APARITIE:

n = int(input("Number n, number of cards: "))

card_dict ={}
i = 0

while i < n:
    card = input()
    if card in card_dict:   #checking the card appearance
        card_dict[card] += 1
        if card_dict[card] == 3:    #check if the card has appeard 3 times
            print(card)
            exit()
    else:
        card_dict[card] = 1
    i += 1

print("JOC OK")  


#TIMP NECESAR = 50 min

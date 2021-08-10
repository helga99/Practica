#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#PROBLEMA CU CIFRU DE SUBSTITUTIE:
#
#Una din cele mai vechi metode de a cripta informaţia este printr-un cifru de substituţie. Acest cifru
#se realizează prin înlocuirea fiecărui caracter din textul de intrare cu alt caracter.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#CERINTA:
#
#Dându-se un text de intrare şi un tabel de substituţie, să se scrie un program care să cripteze textul
#de intrare.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#DATE DE INTRARE:
#
#Pe prima linie citită de la tastatură (stream-ul stdin) se află textul de intrare. Pe următoarea linie se
#află perechi de câte două caractere: caracterul din textul de intrare şi caracterul cu care acesta
#trebuie înlocuit. Cele două caractere sunt separate prin virgulă şi perechile sunt separate prin spaţiu.
#Doar literele mici (26), literele mari (26) şi cifrele (10) se vor înlocui în text, în total tabelul de
#substituţie are deci 62 de elemente. Lungimea maximă a textului este de 1000 de caractere. Ambele
#linii se termină cu apăsarea tastei Enter (caracterul newline, \n).
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#DATE DE IESIRE:
#
#Programul va afişa pe ecran (stream-ul standard de ieşire), pe o singură linie, textul criptat. Din
#textul de intrare se vor înlocui doar literele mici şi mari şi cifrele, restul caracterelor rămânând
#nemodificate. Linia se termină obligatoriu cu caracterul newline (\n).
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#REZOLVARE:

text = input("Text: ")
pairs = input().split(" ")
substitution = {}
text_subst = ""
i = 0
j = 0

for i in range(len(pairs)):
    char = pairs[i].split(",")
    substitution[char[0]] = char[1]
 
for j in range(len(text)):
    if text[j] in substitution.keys():
        text_subst += substitution[text[j]]
    else:
        text_subst += text[j]

print("After substitution: ", text_subst)
    

#TIMP NECESAR = 40 min

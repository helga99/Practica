#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#PROBLEMA CU NUMERE DE INMATRICULARE:
#
#Se va dezvolta un program care interpretează o secvenţă de date de intrare, formată din una sau mai
#multe linii. Programul parcurge secvenţa de intrare şi determină dacă fiecare din linii reprezintă un
#număr de înmatriculare românesc valid, caz în care afişează linia respectivă în consolă.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#DATE DE INTRARE:
#
#Secvenţa de intrare este formată din linii terminate de caracterul newline (\n), generat prin apăsarea
#tastei Enter. Fiecare linie este formată din 3 şiruri de caractere separate de spaţiu. Structura fiecărei
#linii este ilustrată generic în cele ce urmează:
#String1 String2 String3
#unde String1, String2 şi String3 sunt şiruri de caractere a căror structură va fi descrisă în continuare.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#LOGICA INTERNA
#
#Programul va verifica dacă, luate împreună, cele 3 şiruri de caractere din fiecare linie reprezintă un
#număr de înmatriculare valid, folosind următoarele reguli:
#       ~ Valorile valide pentru String1 sunt: AB, AR, AG, B, BC, BH, BN, BT, BV, BR, BZ, CS,
#CL, CJ, CT, CV, DB, DJ, GL, GR, GJ, HR, HD, IL, IS, IF, MM, MH, MS, NT, OT, PH,
#SM, SJ, SB, SV, TR, TM, TL, VS, VL, VN (atenţie: doar litere mari!)
#       ~ String2 e format din 2 sau 3 caractere numerice (numărul de caractere numerice nu este
#condiţionat de valoarea String1)
#       ~ String3 e format din exact 3 caractere litere mari
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#DATE DE IESIRE:
#
#Programul trebuie să afişeze la ieşire, în consolă (pe stream-ul stdout), exclusiv liniile de intrare
#care reprezintă un număr de înmatriculare valid conform regulilor de mai sus. Liniile ce conţin
#numere valide nu vor fi modificate în niciun fel, iar ordinea lor va fi păstrată. Fiecare dintre liniile
#afişate va fi terminată de caracterul newline (\n).
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#REZOLVARE:

string1 = ["AB", "AR", "AG", "B", "BC", "BH", "BN", "BT", "BV", "BR", "BZ", "CS", "CL", "CJ", "CT", "CV", "DB", "DJ", "GL", "GR", "GJ", "HR", "HD", "IL", "IS", "IF", "MM", "MH", "MS", "NT", "OT", "PH", "SM", "SJ", "SB", "SV", "TR", "TM", "TL", "VS", "VL", "VN" ]
string3 = ['A', 'B', 'C', 'D', 'E' , 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']

while True:
        nr_inmat = input().split(" ")
        
        if nr_inmat[0] in string1:
                if nr_inmat[1].isdecimal() and (len(nr_inmat[1]) == 2 or len(nr_inmat[1]) == 3) :
                        if nr_inmat[2].isalpha() and len(nr_inmat[2]) == 3:
                                if  nr_inmat[2][0] in string3 and nr_inmat[2][1] in string3 and nr_inmat[2][2] in string3:
                                        print(" ".join(nr_inmat))
                        
#TIMP NECESAR = 35 min

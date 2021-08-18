#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#PROBLEMA CU BOMBOANE:
#
#Tuturor copiilor le plac bomboanele, aşa că tatăl lui Andrei îi dă o anumită sumă de bani în fiecare zi să îşi cumpere
#bomboane. În zona unde locuieşte Andrei există un singur magazin de bomboane, iar în fiecare zi se vinde un singur tip
#de bomboană cu un anumit preţ şi o anumită aromă. Pe zi ce trece, bomboanele sunt înlocuite cu altele cu alt preţ şi cu
#altă aromă. Andrei cumpără bomboane într-o anumită zi dacă el are destui bani de la tatăl său şi acest lucru duce la
#creşterea fericirii lui cu un anumit număr de puncte egal cu aroma bomboanei. Obligatoriu, dacă are destui bani, el va
#cumpăra bomboana. El păstrează toţi banii rămaşi după ce a cumpărat bomboanele pentru a-şi putea cumpăra mai multe
#următoarea zi. Dacă el nu are destui bani să îşi cumpere bomboane într-o anumită zi, asta nu înseamnă că este necesar
#ca punctele lui de fericire să scadă (evident că nici mai fericit nu îl vor face). Punctele de fericire vor scădea doar dacă
#el nu a cumpărat, în oricare din zilele trecute, cel puţin o bomboană cu o aromă mai bună decât cea din ziua curentă, pe
#care nu şi-o permite.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#CERINTA:
#
#Dându-se un număr n pozitiv, reprezentând numărul de zile în care băiatul primeşte bani de la tatăl său, apoi n numere
#pozitive, reprezentând suma de bani pe care o primeşte băiatul într-o anumită zi, apoi n perechi de numere pozitive, care
#reprezintă costul şi aroma bomboanelor din magazin într-o anumită zi, să se calculeze numărul de puncte de fericire al
#lui Andrei. Numărul de puncte de fericire va creşte sau va scădea cu numărul pozitiv prin care este reprezentată aroma,
#conform spuselor din enunţ. Presupunem că la început Andrei avea 0 lei şi 0 puncte de fericire.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#DATE DE INTRARE:
#
#Pe prima linie se află numărul întreg pozitiv n, reprezentând numărul de zile în care băiatul primeşte bani de la tatăl său,
#urmat de caracterul newline. Pe următoarea linie se află n valori întregi pozitive, separate prin whitespace, reprezentând
#suma de bani pe care o primeşte băiatul într-o anumită zi, urmate de caracterul newline. Pe următoarele n linii se află
#perechi de numere întregi de forma "cost_bomboana aroma_bomboana", care reprezintă costul şi aroma
#bomboanelor din magazin în fiecare zi.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#DATE DE IESIRE:
#
#Se va afişa, pe o singură linie, un singur număr întreg, reprezentând numărul de puncte de fericire pe care le are Andrei
#la finalul celor n zile. Linia se va termina obligatoriu cu un caracter newline ("\n").
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#REZOLVARE:

n = int(input())
summ = input().split(" ")
points = 0
money = 0
price = []
aroma = []

for i in range(n):
        price_aroma = input().split(" ")
        price.append(int(price_aroma[0]))
        aroma.append(int(price_aroma[1]))
        money += int(summ[i])
        if price[i] <=  money:
                points +=  aroma[i]
                money -= price[i]
        elif max(aroma) <= aroma[i]:
                points -=  aroma[i]
        
print(points)

               
#TIMP NECESAR = 40 min

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#PROBLEMA CU LOTURI DE COMPONENTE ELECTORNICE:
#
#Sunteți șef de proiect la o companie și l-ați rugat pe Gigel să dea comandă de loturi de componente
#electronice pentru a realiza un set de plăci cu circuite electronice. Problema este că Gigel nu știe prea
#multă electronică așa că printre loturile pe care le-a comandat sunt și loturi cu tranzistoare
#condensatoare sau rezistoare insuficiente. Loturile care vă sunt utile sunt doar loturile care au un
#număr de condensatoare mai mare sau egal cu numărul de tranzistoare, numărul de rezistoare mai
#mare sau egal cu numărul de condensatoare, și au cel puțin un condensator, un tranzistor și un rezistor.
#În plus, vă interesează și lotul cu cele mai multe componente, pentru că din ele o să le mai completați
#pe cele lipsă.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#CERINTA:
#
#Scrieți un program care primește la intrare loturile de componente și afișează câte dintre aceste loturi
#vă sunt utile și câte componente are lotul cel mai mare. Un lot se consideră util dacă respectă condițiile
#impuse mai sus. Aceste condiții trebuie îndeplinite simultan.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#DATE DE INTRARE:
#
#Se va citi de la tastatură (fluxul stdin) pe o singură linie un număr întreg n reprezentând numărul de
#loturi. Apoi, se vor citi cele n loturi după cum urmează: se citește pe o linie numărul de componente
#din lotul respectiv, k, iar pe următoarea linie k litere reprezentând tipurile de componente ale lotului,
#separate prin spatii (R reprezentând un rezistor, C reprezentând un condensator și T reprezentând un
#tranzistor).
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#DATE DE IESIRE:
#
#Programul va afișa pe ecran (stream-ul standard de iesire) două numere întregi, reprezentând numărul
#de loturi utile dintre cele citite cât și numărul de componente ale lotului cel mai mare, valori separate
#printr-un spațiu.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#REZOLVARE:

n = int(input("Number of lots: "))
max_k = 0
useful = 0
i = 0

for i in range(n):
        k = int(input())
        if k > max_k:
                max_k = k
        
        comp = input().split(' ')
        components = {
                "C": 0,
                "T": 0,
                "R": 0
                }
        j = 0
        for j in range(k):
                components[comp[j]] += 1
        if  components["T"] > 0 and components["C"] >= components["T"] and components["R"] >= components["C"]:
                useful += 1

print(useful)	
print(max_k)

#TIMP NECESAR = 50 min

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#PROBLEMA CU NUMAR PALINDROMIC MAXIM:
#
#Un studiu de marketing cerut de o galerie de artă mai excentrică a arătat că, în mod surprinzător,
#clienţii analizează o perioadă mai mare de timp exponatele care au preţuri ce pot fi exprimate ca un
#palindrom şi de obicei le preferă, chiar şi în cazul în care un alt obiect similar are un preţ ceva mai
#scăzut. Pe de altă parte, din anumite motive (doar de ei ştiute) artiştii, care creează aceste produse,
#vor ca numerele care definesc preţul unui obiect de artă sa fie atent elaborate şi să conţină doar
#anumite cifre considerate de ei ca fiind foarte importante. Sub aceste constrângeri, proprietarii
#galeriei de artă vor să maximizeze câştigurile şi să afişeze cele mai mari preţuri posibile în
#condiţiile menţionate.
#Astfel, se cere să se realizeze un program care interpretează o secvenţă de cifre nenule oferite la
#intrare, în vederea obţinerii unor reprezentări zecimale (numere în bază 10). Plecând de la cifrele
#oferite sunt posibile mai multe reprezentări zecimale. Dintre numerele zecimale astfel obţinute se va
#alege cel mai mare număr care are proprietatea de palindrom (vedeţi explicaţiile de mai jos).

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#DATE DE INTRARE:
#
#La intrarea programului, pe prima linie se prezintă un număr natural n, iar pe a doua linie n cifre,
#separate prin câte un spaţiu. Cu aceste cifre se pot construi numere în baza 10.
#Fiecare dintre cele două linii de intrare se încheie cu caracterul newline (\n), obţinut prin apăsarea
#tastei Enter. 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#DATE DE IESIRE:
#
#Să se determine numărul cel mai mare de tip palindrom (în situaţia în care se pot forma mai
#multe palindromuri) ce se poate forma cu toate cifrele conţinute pe a doua linie. Programul va afişa
#la consolă (pe stream-ul stdout) numărul astfel determinat urmat de caracterul newline (\n) (tasta
#Enter).
#Dacă nu se poate forma niciun palindrom, la ieşire se va afişa cifra 0 (zero); dacă se poate forma un
#singur palindrom, acesta, evident, se va afişa la ieşire ca atare.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#REZOLVARE:

n = int(input())
lista = input().split(" ")
lista_pal = [None] * n
index = 0
temp = -1
odd = 0
i = 0

lista.sort(reverse = True)

while i < n:
        if i != n-1 and lista[i] == lista[i+1]:
                lista_pal[index] = lista_pal[n-1-index] = lista[i]
                i += 1
                index +=1
        else:
                odd += 1
                temp = lista[i]
        i += 1
                        
if odd > 1:
        print(0)
if odd == 1:
        lista_pal[index] = temp
        print("".join(lista_pal))
if odd == 0:
        print("".join(lista_pal))
  

            
#TIMP NECESAR = 40 min

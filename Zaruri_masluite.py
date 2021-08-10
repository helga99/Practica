#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#PROBLEMA CU ZARURI MASLUITE:
#
#Costică e în vacanță și l-au trimis părinții la țară. Acolo se plictisește groaznic și căutând prin dulapul
#bunicului, a dat peste o pungă plină ochi cu zaruri. Neavând cu cine să joace zaruri dar părându-i-se
#că unele din zaruri sunt mai grele decât celelalte, Costică a ales un zar și s-a apucat să îl testeze
#aruncând cu el și notând de câte ori a picat fiecare față. Încearcă apoi să-și dea seama dacă zarul e
#măsluit sau nu, considerând că diferența dintre numărul maxim de apariții a unei fețe și numărul
#minim de apariții (a oricăror alte fețe) nu trebuie să depășească 10% din numărul total de aruncări.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#CERINTA:
#
#Dându-se un număr N de aruncări cu zarul și apoi N numere naturale în intervalul [1:6] reprezentând
#numerele obținute la aruncări, să se determine dacă zarul e măsluit conform condiției de mai sus.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#DATE DE INTRARE:
#
#De la intrare (fluxul stdin) de pe prima linie se citește numărul natural N, reprezentând numărul de
#aruncări cu zarul. Pe următoarele N linii se află câte un număr natural în intervalul [1:6] reprezentând
#numerele obținute la aruncări.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#DATE DE IESIRE:
#
#La ieşire (fluxul stdout) se va afișa un singur număr, 0 sau 1, 0 dacă zarul e normal, și 1 dacă este
#măsluit.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#REZOLVARE:

N = int(input("Number N of dice rolls: "))

rolls = {
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0
    }

for i in range(N):
    rolls[input()] += 1

if (max(rolls.values()) - min(rolls.values())) <= N / 10:
    print(0)
else:
    print(1)
    
#TIMP NECESAR = 25 min

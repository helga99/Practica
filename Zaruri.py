#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#PROBLEMA CU ZARURI:
#
#Costică e în vacanță și l-au trimis părinții la țară. Acolo se plictisește groaznic și căutând prin dulapul
#bunicului, a dat peste o pungă plină ochi cu zaruri. Neavând cu cine să joace zaruri, Costică s-a apucat
#să le clădească, unul peste celălalt, cât de sus a putut. Uitându-se apoi la isprava făcută, i-a venit ideea
#să afle care sunt numerele zarurilor de pe fețele acestora care nu se văd. Dându-și seama că deși e
#posibil, e mai complicat, și că el e mai degrabă leneș decât curios, s-a hotărât să afle doar suma tuturor
#numerelor de pe toate fețele zarurilor care nu se văd.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#CERINTA:
#
#Dându-se un număr N de zaruri și valorile de pe fețele vizibile ale zarurilor, calculați suma tuturor
#fețelor care nu se văd. Se ignoră ordinea reală a numerelor pe fețele zarurilor, adică cele 6 numere
#pot apărea pe zar în orice aranjament.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#DATE DE INTERARE
#
#De la intrare (fluxul stdin) de pe prima linie se citește numărul natural N, reprezentând numărul de
#zaruri suprapuse. Pe cea de-a doua linie se află 5 numere naturale distincte în intervalul [1; 6]
#reprezentând cele 5 fețe vizibile pentru zarul de sus, apoi pe următoarele N-1 linii se află 4 numere
#de același fel, reprezentând cele 4 fețe vizibile ale zarurilor.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#DATE DE IESIRE
#
#La ieşire (fluxul stdout) se va afișa un singur număr întreg pozitiv ce reprezintă suma fețelor invizibile
#ale zarurilor.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#REZOLVARE:

N = int(input("Number of dices: "))

list_visible_surfaces = []
nr_visible_surfaces = 4 * N + 1 #first dice has 4 + 1 visible surface, rest dices 4 visible surface
sum_total_surfaces = 21 * N #(1+2+3+4+5+6)*N
sum_visible_surfaces = 0
i = 0

while i < N:
    list_visible_surfaces.clear()
    visible_surface = str(input("{:d} dice visible surfaces: ".format(i+1)))
    list_visible_surfaces = visible_surface.split(" ") #extract numbers from line
    list_visible_surfaces = [int(j) for j in list_visible_surfaces] #convert numbers to int
    sum_visible_surfaces += sum(list_visible_surfaces)
    i += 1

sum_invisible_surfaces = sum_total_surfaces - sum_visible_surfaces

print(sum_invisible_surfaces)

#TIMP NECESAR = 60 min

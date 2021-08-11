#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#PROBLEMA CU CINEMATOGRAF:
#
#V-ați hotărât în ultimul moment să mergeți la cinematograf pentru a vedea un film cu prietenii, dar în
#același timp vă grăbiți să vă întoarceți acasă cât mai repede. V-ați interesat de dinainte și ați văzut că
#filmele care rulează acum la cinema durează aproximativ același timp. Deci, vă interesează în
#principal ca filmul pe care o să îl vizionați să înceapă cât mai repede din momentul în care ajungeți
#la casa de bilete, iar, în cazul în care sunt mai multe filme care încep la ora dorită, să îl alegeți pe cel
#cu prețul biletului cel mai mic.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#CERINTA:
#
#Dându-se ora la care ajungeți la cinematograf, scrieți un program care să selecteze din lista de filme
#pe cel care respectă cel mai bine dorințele voastre.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#DATE DE INTRARE:
#
#Se vor citi de la tastatură (fluxul stdin) de pe prima linie ora la care ajungeți la cinema, în format
#hh:mm, iar de pe a doua linie un număr întreg n reprezentând numărul de oferte disponibile în
#programul cinematografului. De pe următoarele n linii se vor citi datele despre fiecare film din ofertă
#în formatul:
#       <oră> <preț> <nume film>
#Datele din format vor fi separate prin câte un spațiu. Ora de începere a fiecărui film va fi tot în
#formatul hh:mm, prețul va fi un număr întreg fără semn, iar numele filmului va fi un șir de caractere,
#el putând fi format din mai multe cuvinte, dar pentru ușurință, ele vor fi separate prin caracterul
#cratimă (‘-’). Fiecare linie se va termina cu un caracter newline (‘\n’).
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#DATE DE IESIRE:
#
#Programul va afișa pe ecran (stream-ul standard de ieșire) un singur șir de caractere, reprezentând
#numele filmului ales, în formatul dat în datele de intrare.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#REZOLVARE:

arr_time = [int(i) for i in input().split(":")]
arr_time_in_sec = arr_time[0] * 60 + arr_time[1]

n = int(input())
time_h = []
time_m = []
time_in_sec = []
price = []
name = []
diff = []

for i in range(n):
        movie = input().split(" ")
        time = movie[0].split(":")
        time_h.append(int(time[0]))
        time_m.append(int(time[1]))
        time_in_sec.append(time_h[i] * 60 + time_m[i])
        price.append(int(movie[1]))
        name.append(str(movie[2]))

for j in range(n):
        diff.append(time_in_sec[j] - arr_time_in_sec)

first_film = diff.index(min([k for k in diff if k > 0]))

for l in range(n):
        if diff[l] == diff[first_film] and price[l] < price[first_film]:
                first_film = l
                
print(name[first_film])

#TIMP NECESAR = 80 min

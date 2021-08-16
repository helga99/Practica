#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#PROBLEMA CU BURSE STUDENTESTI:
#
#Doamna secretară trebuie să stabilească numărul de studenți ce vor lua bursă de merit în anul
#universitar următor și să identifice studentul care va lua bursa de performanță (există o singură bursă
#de performanță). Are la dispoziție lista tuturor studenților și notele obținute de aceștia la diversele
#discipline. Bursa de performanță se acordă studentului integralist cu media cea mai mare. Bursele de
#merit se acordă în ordinea descrescătoare a mediilor, în limita numărului maxim de burse, tuturor
#studenților integraliști care au media generală peste 8.00.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#CERINTA:
#
#Stabiliți ce student va lua bursă de performanță și câți studenți vor lua bursă de merit în anul
#universitar următor.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#DATE DE INTRARE:
#
#Se vor citi de la tastatură (fluxul stdin) următoarele date:
#       • Trei numere întregi pozitive m, n, p separate prin spaţiu, reprezentând
#               o m – numărul de studenţi,
#               o n – numărul de discipline,
#               o p – numărul de burse de merit disponibile;
#       • 2*m linii de pe care se citesc, în ordine, în formatul:
#               o <NS>, un şir de caractere reprezentând numele studentului;
#               o <N1> <N2> ... <Nn>, n numere întregi din intervalul 1 – 10 separate prin spaţiu
#                       reprezentând notele obţinute de respectivul student la cele m discipline;
#Toate liniile conţinând date de intrare sunt finalizate cu caracterul newline (tasta Enter).
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#DATE DE IESIRE:
#
#Programul va afișa pe ecran (stream-ul standard de ieșire):
#       • Pe prima linie: numărul de studenți ce vor lua bursă de merit
#       • Pe a doua linie: numele studentului care va lua bursă de performanță și media media lui (număr
#       fracționar cu 2 zecimale) separate prin spațiu.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#REZOLVARE:

mnp = [int(i) for i in input().split(" ")]
m = mnp[0]
n = mnp[1]
p = mnp[2]
students = {}
avarage_min_8 = 0
i = 0

for i in range(m):
        name = input()
        notes = [int(ii) for ii in input().split(" ")]
        avarage = sum(notes) / n
        notes_ok = True
        for j in range(n):
                if notes[j] < 5:
                        notes_ok = False
        if notes_ok:               
                students[name] = avarage
                if avarage >= 8:
                        avarage_min_8 += 1

if avarage_min_8 - 1 > p:
        print(p)
else:
        print(avarage_min_8 - 1)

max_ind = max(students, key=students.get)

print(max_ind, "{:.2f}".format(students.get(max_ind)))
#print(''.join(sort_students[0][0]), "{:.2f}".format(sort_students[0][1]))
               
#TIMP NECESAR = 80 min

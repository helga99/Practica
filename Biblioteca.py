#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#PROBLEMA CU BIBLIOTECA:
#
#Cărţile din biblioteca UPB trebuie mutate într-o nouă locaţie, iar aranjarea lor pe rafturi se va face
#într-o manieră inovativă, urmărindu-se minimizarea numărului de rafturi necesare. Bibliotecara știe
#că are un număr suficient de rafturi încât să pună toate cărțile. Pe fiecare raft încap cărți însumând în
#total D pagini. De asemenea, ştie câte cărţi cu un anumit număr de pagini există în bibliotecă. Dat
#fiind acestea şi urmărind să ocupe cât mai puţine rafturi, bibliotecara şi-a propus să aranjeze cărţile
#pe rafturi:
#i. raft după raft,
#ii. alegând întotdeauna să completeze raftul curent cu cea mai groasă carte disponibilă,
#iii. trecând la următorul raft numai în condiţiile în care pe raftul curent nu mai poate fi plasată
#        nicio carte dintre cele rămase şi
#iv. asigurându-se că a plasat pe rafturi toate cărţile.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#CERINTA:
#
#Scrieţi un program care o poate ajuta pe bibliotecară să aranjeze cărţile pe rafturi în mod eficient,
#conform regulilor enunţate mai sus.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#DATE DE INTRARE:
#
#Se vor citi de la tastatură (fluxul stdin) următoarele date:
#• de pe prima linie: două numere întregi D şi k, separate prin spaţiu, reprezentând D –
#dimensiunea rafturilor exprimată în număr de pagini, k – numărul de dimensiuni diferite
#pentru cărţile ce trebuie aranjate în bibliotecă;
#• de pe următoarele k linii: câte două numere întregi n şi p, reprezentând numărul de cărţi n
#de grosime p pagini ce trebuie aranjate în bibliotecă.
#Cele k linii ce conțin informații despre cărți sunt date în ordinea inversă a grosimii p.
#Toate liniile conţinând date de intrare sunt finalizate cu caracterul newline (tasta Enter).
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#DATE DE IESIRE:
#
#Programul va afişa pe ecran (stream-ul standard de ieşire) m linii, corespunzătoare celor m rafturi pe
#care a fost plasată cel puţin o carte, în ordinea completării lor (conform regulilor). Fiecare dintre cele
#m linii va conţine o serie de numere întregi, separate prin spaţiu, reprezentând dimensiunile cărţilor
#ce au fost plasate pe acel raft, în ordinea plasării lor pe raft (conform regulilor).
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#REZOLVARE:

Dk = input().split(" ")
D = int(Dk[0])
k = int(Dk[1])
n = []
p = []

for i in range(k):
        np = input().split(" ")
        n.append(int(np[0]))
        p.append(int(np[1]))

j = 0        
while j < k:
        lista = []
        if n[j] > 0:
                n[j] -= 1
                lista.append(p[j])
                summ = p[j]
                jj = j
                verif = False
                while jj < k:
                        if n[jj] != 0 and summ + p[jj] <= D:
                                summ += p[jj]
                                lista.append(p[jj])
                                n[jj] -= 1
                        else:
                                jj += 1
                str_lista = [str(int) for int in lista]
                print(" ".join(str_lista))
        else:
                j += 1
               
#TIMP NECESAR = 150 min

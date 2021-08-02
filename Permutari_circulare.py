#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#PROBLEMA CU PERMUTARI CIRCULARE:
#
#George tocmai a învăţat despre sistemul de numeraţie cu bază 2 (sistemul de numeraţie binar). I
#se pare interesant şi a inventat jocul PC (permutări circulare), pe care vrea să îl joace cu prietenul
#său Armin. George îi spune lui Armin un număr natural nenul n, scris în baza 10 (sistemul zecimal),
#pe care acesta trebuie să-l transforme în baza 2. Se obţine astfel o secvenţă de cifre binare (biţi),
#care trebuie să înceapă cu 1 (primul bit din stânga în reprezentarea binară a numărului n să fie 1).
#Ideea jocului inventat de George a fost aplicarea uneia sau mai multor permutări circulare asupra
#scrierii în baza 2 a numărului n. Într-o permutare circulară, toate cifrele secvenţei date, exceptând-
#o pe ultima, sunt mutate cu o poziţie spre dreapta, ultima cifră devenind prima.
#De exemplu, dacă n=107, scrierea sa în baza 2 este 1101011. Prin permutări circulare succesive
#putem obţine, în ordine, secvenţele:
#   1110101
#   1111010
#   0111101
#   1011110
#   0101111
#   ...
#Fiecare astfel de secvenţă reprezintă transcrierea în bază 2 a unui număr natural m care are o
#anumită valoare în baza 10. Lui George jocul nu i s-ar mai părea așa interesant dacă n-ar reuși să
#scrie un program care să determine în locul lui numărul natural m. Ajutaţi-l!
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#CERINTA:
#
#Să se afle cel mai mare număr natural m, scris în baza 10, a cărui scriere în baza 2 se poate obține
#prin una sau mai multe permutări circulare ale scrierii în baza 2 a numărului n.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#DATE DE INTRARE:
#
#Se va citi de la tastatură (fluxul standard de intrare, stdin) pe o singură linie, numărul natural nenul
#n, în baza 10, care respectă cerinţa din enunţ (primul bit din stânga al reprezentării sale în bază 2
#să fie 1).
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#DATE DE IESIRE:
#
#Programul va afişa la consolă (stream-ul standard de ieşire, stdout), pe o singură linie, numărul
#natural m, cu semnificaţia cerută în enunţ.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#REZOLVARE:

def list_str(numList): #convert list to string number
    s = ''.join(map(str, numList))
    return s

n = int(input("Number n in base 10: "))

n_bin = list(bin(n).replace("0b","")) #convert number n in base 2    
n_bin = [int(i) for i in n_bin] #convert numbers to int

length = len(n_bin)-1
i = 0
max_m = int(list_str(n_bin),2)

while i < length: #generate permutations
    list_perm = [n_bin[length]]
    list_perm += n_bin[0:length]
    n_bin = list_perm.copy()
    i += 1
    if int(list_str(n_bin),2) > max_m: #compare maximum number with curent number
        max_m = int(list_str(n_bin),2)

print(max_m)

#TIMP NECESAR = 70 min

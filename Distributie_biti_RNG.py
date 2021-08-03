#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#PROBLEMA CU DISTRIBUTIE BITI RNG:
#
#Împreună cu echipa de la firmă ați inventat un nou algoritm de generare de numere pseudo-aleatoare.
#Pentru a valida că generatorul poate fi folosit în algoritmi criptografici (cryptographically secure)
#trebuie să implementați și să rulați o baterie de teste. Unul din aceste teste verifică numărul de apariții
#pentru fiecare secvență posibilă de doi biți: 00, 01, 10 și 11 cât și raportul între numărul de biți de 0
#și de 1. Pentru ca secvența de biți să fie aleatoare, trebuie ca numărul de apariții pentru fiecare din
#cele patru perechi să fie aproximativ egale și în același timp numărul de biți de 0 să fie aproximativ
#egal cu cei de 1. Mai precis, trebuie ca raporturile R1 dintre numărul de apariții a perechii care apare
#de cele mai multe ori și numărul de apariții a perechii care apare de cele mai puține ori, cât și raportul
#R2 între numărul de apariții ale celui mai frecvent bit și numărul de apariții ale celui mai puțin frecvent
#bit să fie mai mici sau egale cu 110%.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#CERINTA:
#
#Dându-se un număr n reprezentând numărul de biți generat de RNG și secvența de n biți, să se
#calculeze raporturile R1 și R2 și să se decidă dacă generatorul este valid sau nu.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#DATE DE INTRARE:
#
#Pe prima linie se află n, numărul de biți generați. Pe a doua linie se află o secvență continuă de n biți
#(valori de 0 sau 1), ne-separați prin spații.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#DATE DE IESIRE:
#
#Programul va afișa în consolă (pe stream-ul stdout) pe prima linie raporturile R1 și R2 calculate
#conform descrierii, valori fracționare cu două zecimale, separate prin spațiu, iar pe a doua linie
#valoarea 1 dacă generatorul este valid sau 0 dacă nu este.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#REZOLVARE:

n = int(input("Number n, number of bits RNG: "))
bits = str(input("Bits sequence: "))

bits_dict = {
    "00": 0,
    "01": 0,
    "10": 0,
    "11": 0
    }
bit_0 = 0
bit_1 = 0
i = 0
R1 = 0
R2 = 0

while i < n:    #number of bit pairs (00, 01, 10, 11)
    bits_dict[bits[i:i+2]] += 1
    i += 2

for i in bits:      #number of bits "0" and "1"
    if(i == '0'):
        bit_0 += 1
    if(i == '1'):
        bit_1 += 1
        
if min(bits_dict.values()) > 0:     #calculate value of R1 and R2 with function min and max
    R1 = max(bits_dict.values())/min(bits_dict.values())
if min(bit_0,bit_1) > 0:
    R2 = max(bit_0,bit_1)/min(bit_0,bit_1)

print("%.2f" %R1,"%.2f" %R2)
if R1 <= 1.1 and R2 <= 1.1:    #validity check
    print("1")
else:
    print("0")


#TIMP NECESAR = 60 min

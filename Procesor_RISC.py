#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#PROBLEMA CU PROCESOR RISC:
#
#Pentru că echipa cu care lucrați a dezvoltat o nouă arhitectură de procesor RISC, ați decis să-i ajutați
#în etapa de dezvoltare prin realizarea unui simulator software pentru procesorul respectiv. Simulatorul
#va primi, ca și procesorul real, o secvență de instrucțiuni care va trebui executată iar starea finală a
#datelor va trebui afișată la ieșire. Procesorul are un set de 16 registre numerotate de la 0 la 15 și
#deocamdată nu are memorie.
#Procesorul știe să execute următoarele instrucțiuni, pe care trebuie să le interpreteze și programul
#vostru:
#• lconst <dst> <val> – se scrie valoarea <val> în registrul <dst>;
#• add <dst> <src0> <src> – se adună valorile din registrele <src0> și <src1> și rezultatul se
#   scrie în registrul <dst>;
#• mul <dst> <src0> <src> – se înmulțesc valorile din registrele <src0> și <src1> și rezultatul se
#   scrie în registrul <dst>;
#• div <dst> <src0> <src> – se împart valorile din registrele <src0> și <src1> și câtul se scrie în
#   registrul <dst>;
#• print <reg> - se afișează valoarea din registrul <reg>.
#Dacă la execuția unei instrucțiuni de tip div împărțitorul este zero, se va afișa fraza Exception: line
#<index>, unde index reprezintă a câta instrucțiune nu a putut fi executată, iar programul se va încheia.
#Toate registrele au inițial valoarea 0.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#CERINTA:
#
#Dându-se o secvență de instrucțiuni ca cele de mai sus, executați-le și afișați valorile printate de
#program.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#DATE DE INTRARE:
#
#Se va citi de la tastatură (fluxul standard de intrare, stdin) de pe prima linie un număr n, reprezentând
#numărul de instrucțiuni. Pe următoarele n linii se află câte o instrucțiune din cele de mai sus.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#DATE DE IESIRE:
#
#Programul va afişa la consolă (stream-ul standard de ieşire, stdout), valorile printate de program (prin
#instrucțiuni de tip print), câte una pe linie.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#REZOLVARE:

n = int(input("Number n, number of instructions: "))
i = 0

register={}
for i in range(0,15):
    register[str(i)]=0  #empty registers
    
instructions = {}
for i in range(n):
    instructions[i] = input();

for i in range(n):
    inst = instructions[i].split()

    if inst[0] == "lconst":
        register[inst[1]] = int(inst[2])

    if inst[0] == "add":
        register[inst[1]] = register[inst[2]] + register[inst[3]]

    if inst[0] == "mul":
        register[inst[1]] = register[inst[2]] * register[inst[3]]

    if inst[0] == "div":
        if register[inst[3]] == 0:
            print("Exception: line", i+1)
            exit()
        register[inst[1]] = register[inst[2]] / register[inst[3]]

    if inst[0] == "print":
        print(register[inst[1]])
        

#TIMP NECESAER = 70 min

l = []

while True:
    try:
        line = input()
        l.append(line)
    except EOFError:
        break
OP = {"add": ("0000000", "A"),
      "sub": ("0000100", "A"),
      "mov": ("0001000000", "C"),
      "ld": ("00100", "D"),
      "st": ("00101", "D"),
      "mul": ("0011000", "A"),
      "div": ("0011100000", "C"),
      "rs": ("01000", "B"),
      "ls": ("01001", "B"),
      "xor": ("0101000", "A"),
      "or": ("0101100", "A"),
      "and": ("0110000", "A"),
      "not": ("0110100000", "C"),
      "cmp": ("0111000000", "C"),
      "jmp": ("01111000", "E"),
      "jlt": ("10000000", "E"),
      "jgt": ("10001000", "E"),
      "je": ("10010000", "E"),
      "hlt": ("1001100000000000", "F"), }

Reg = {"R0": "000",
       "R1": "001",
       "R2": "010",
       "R3": "011",
       "R4": "100",
       "R5": "101",
       "R6": "110",
       "FLAGS": "111"}


def dtob(n):
    n = int(n)
    bnr = bin(n).replace('0b', '')
    x = bnr[::-1]
    while len(x) < 8:
        x += '0'
    bnr = x[::-1]
    return bnr


lineno = -1
lineno2 = -1
vari = 0
l3 = []
l2 = []
jmp = ["jmp", "jlt", "jgt", "je"]
for i in l:
    lineno += 1
    c = i.split()
    if len(c) >= 1:
        if c[0] == "var":
            l2.append([c[1], vari])
            vari += 1
        if c[0][-1] == ":":
            l3.append([c[0][:-1], lineno - vari])
for i in l:
    d = ""
    lineno2 += 1
    c = i.split()
    if len(c) >= 1:
        if c[0][-1] == ":":
            if len(c) >= 2:
                if c[1] not in OP:
                    print("Error : Typo")
                    break

                if c[1] == "mov":
                    if c[2] in Reg:
                        d = "0001000000"
                    elif c[2][1:].isnumeric() and (255 > int(c[2][1:]) > 0):
                        d = "00010"
                    else:
                        print("Error : Illegal Immediate Values")
                        break

                elif c[1] == "st" or c[1] == "ld":
                    d = OP[c[1]][0] + Reg[c[2]]
                    e = len(l) - vari
                    if i not in l2 :
                        print("Error : Undefined Variable")
                    for i in l2:
                        if i[0] == c[3]:
                            e2 = e + int(i[1])
                            d += dtob(str(e2))
                    print(d)
                    continue

                elif c[1] in jmp:
                    d = OP[c[1]][0]
                    for i in l3:
                        if i[0] == c[2]:
                            d += dtob(str(i[1]))
                    print(d)
                    continue
                elif c[1] in OP:
                    d = OP[c[1]][0]

            if len(c) >= 3:
                if c[2] in Reg:
                    d += Reg[c[2]]
            if len(c) >= 4:
                if c[3] in Reg:
                    d += Reg[c[3]]
                elif c[3][1:].isnumeric():
                    d += dtob(c[3][1:])
            if len(c) == 5:
                if c[4] in Reg:
                    d += Reg[c[4]]
            print(d)
            continue
        elif c[0] == "mov":
            if c[2] in Reg:
                d = "0001000000"
            elif c[2][1:].isnumeric() and (255 > int(c[2][1:]) > 0):
                d = "00010"
            else:
                print("Error : Illegal Immediate Values")
                break

        elif c[0] == "st" or c[0] == "ld":
            d = OP[c[0]][0] + Reg[c[1]]
            e = len(l) - vari
            #if i not in l2:
                #print("Error : Use of Undefined Variables")
                #break

            for i in l2:
                if i[0] == c[2]:
                    e2 = e + int(i[1])
                    d += dtob(str(e2))
            print(d)
            continue

        elif c[0] in jmp:
            d = OP[c[0]][0]
            for i in l3:
                if i[0] == c[1]:
                    d += dtob(str(i[1]))

            print(d)
            continue
        elif c[0] in OP:
            d = OP[c[0]][0]

        #elif (c[0][-1] != ":") and (c[0] not in OP) :
            #print("Typo")
            #break

    if len(c) >= 2:
        if c[1] in Reg:
            d += Reg[c[1]]
    if len(c) >= 3:
        if c[2] in Reg:
            d += Reg[c[2]]
        elif c[2][1:].isnumeric():
            d += dtob(c[2][1:])
    if len(c) == 4:
        if c[3] in Reg:
            d += Reg[c[3]]
    print(d)

if l[-1] != "hlt":
    print("Error : Missing Halt Statement or Halt not being used as Last Instruction")



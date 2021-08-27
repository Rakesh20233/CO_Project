
def dtob(n):
    n=int(n)
    bnr = bin(n).replace('0b','')
    x = bnr[::-1] 
    while len(x) < 8:
        x += '0'
    bnr = x[::-1]
    return bnr
def padded_bin(x):
    return bin(x)[2:].zfill(16)
def add(ro,r1,r2,mem,Reg,pc):
        Reg[ro]=padded_bin(int(Reg[r1],2)+int(Reg[r2],2))
        if(int(Reg[r1],2) > 0 and int(Reg[r2],2) > 0 and int(Reg[ro],2) < 0):
                Reg["111"]="0000000000001000"
        if(int(Reg[r1],2) < 0 and int(Reg[r2],2) < 0 and int(Reg[ro],2) > 0):
                Reg["111"]="0000000000001000"
        else:
                Reg["111"]="0000000000000000"
        pc+=1
        return [mem,Reg,pc]
def sub(ro,r1,r2,mem,Reg,pc):
        Reg[ro]=padded_bin(int(Reg[r1],2)-int(Reg[r2],2))
        pc+=1
        return [mem,Reg,pc]
def mul(ro,r1,r2,mem,Reg,pc):
        Reg[ro]=padded_bin(int(Reg[r1],2)*int(Reg[r2],2))
        if (int(Reg[r1],2) == 0 or int(Reg[r2],2) == 0) :
                Reg["111"]="0000000000000000"
        if (int(Reg[r1],2) == (int(Reg[ro],2) // int(Reg[r2],2))):
                Reg["111"]="0000000000000000"
        else:
                Reg["111"]="0000000000001000"
        pc+=1
        return [mem,Reg,pc]
def div(ro,r1,r2,mem,Reg,pc):
        Reg[ro]=padded_bin(int(Reg[r1],2)/int(Reg[r2],2))
        pc+=1
        Reg["111"]="0000000000000000"
        return [mem,Reg,pc]
def mov(ro,num,mem,Reg,pc):
        num=int(num,2)
        Reg[ro]=padded_bin(num)
        pc+=1
        Reg["111"]="0000000000000000"
        return [mem,Reg,pc]
def movb(ro,r1,mem,Reg,pc):
        Reg[ro]=Reg[r1]
        pc+=1
        Reg["111"]="0000000000000000"
        return [mem,Reg,pc]
def ld(ro,memadd,mem,Reg,pc):
        Reg[ro]=mem[memadd]
        pc+=1
        Reg["111"]="0000000000000000"
        return [mem,Reg,pc]
def st(ro,memadd,mem,Reg,pc):
        mem[memadd]=Reg[ro]
        pc+=1
        Reg["111"]="0000000000000000"
        return [mem,Reg,pc]
def rs(ro,imm,mem,Reg,pc):
        Reg[ro]=padded_bin(int(imm,2)//2)
        pc+=1
        Reg["111"]="0000000000000000"
        return [mem,Reg,pc]
def ls(ro,imm,mem,Reg,pc):
        Reg[ro]=padded_bin(int(imm,2)*2)
        pc+=1
        Reg["111"]="0000000000000000"
        return [mem,Reg,pc]
def xor(ro,r1,r2,mem,Reg,pc):
        Reg[ro]=padded_bin(int(Reg[r1],2) ^ int(Reg[r2,2]))
        pc+=1
        Reg["111"]="0000000000000000"
        return [mem,Reg,pc]
def OR(ro,r1,r2,mem,Reg,pc):
        Reg[ro]=padded_bin(int(Reg[r1],2) | int(Reg[r2,2]))
        pc+=1
        Reg["111"]="0000000000000000"
        return [mem,Reg,pc]
def AND(ro,r1,r2,mem,Reg,pc):
        Reg[ro]=padded_bin(int(Reg[r1],2) & int(Reg[r2,2]))
        pc+=1
        Reg["111"]="0000000000000000"
        return [mem,Reg,pc]
def NOT(ro,r1,mem,Reg,pc):
        e2=""
        for i in range(len(Reg[r1])):
            if Reg[r1][i]=="1":
                e=Reg[r1][i:len(Reg[r1])]
                break
        for i in e:
            if i=="0":
                e2+="1"
            else:
                e2+="0"
        Reg[ro]=padded_bin(int(e2,2))
        pc+=1
        Reg["111"]="0000000000000000"
        return [mem,Reg,pc]
def cmp(ro,r1,mem,Reg,pc):
        if int(Reg[ro],2)<int(Reg[ro],2):
                Reg["111"]="0000000000000100"
        elif int(Reg[ro],2)>int(Reg[ro],2):
                Reg["111"]="0000000000000010"
        else:
                Reg["111"]="0000000000000001"
        pc+=1
        return [mem,Reg,pc]
def jmp(memadd,mem,Reg,pc):
        pc=memadd
        Reg["111"]="0000000000000000"
        return [mem,Reg,pc]
def jlt(memadd,mem,Reg,pc):
        if Reg["111"][-3]=="1":
            pc=memadd
        else:
            pc+=1
        Reg["111"]="0000000000000000"
        return [mem,Reg,pc]
def jgt(memadd,mem,Reg,pc):
        if Reg["111"][-2]=="1":
            pc=memadd
        else:
            pc+=1
        Reg["111"]="0000000000000000"
        return [mem,Reg,pc]
def je(memadd,mem,Reg,pc):
        if Reg["111"][-1]=="1":
            pc=memadd
        else:
            pc+=1
        Reg["111"]="0000000000000000"
        return [mem,Reg,pc]

OP={"add":"00000",
"sub":"00001",
"mov":"00010",
"mov":"00011",
"ld":"00100",
"st":"00101",
"mul":"00110",
"div":"00111",
"rs":"01000",
"ls":"01001",
"xor":"01010",
"or":"01011",
"and":"01100",
"not":"01101",
"cmp":"01110",
"jmp":"01111",
"jlt":"10000",
"jgt":"10001",
"je":"10010",
"hlt":"1001100000000000"}
def execute(ins,mem,Reg,pc):
        if ins==OP["hlt"]:
                return True
        elif ins[:5] == OP["add"]:
                l=add(ins[7:10],ins[10:13],ins[13:],mem,Reg,pc)
                return l
        elif ins[:5] == OP["sub"]:
                l=sub(ins[7:10],ins[10:13],ins[13:],mem,Reg,pc)
                return l
        elif ins[:5] == "00010":
                l=mov(ins[5:8],ins[8:],mem,Reg,pc)
                return l
        elif ins[:5] == "00011":
                l=movb(ins[10:13],ins[13:],mem,Reg,pc)#type c
                return l
        elif ins[:5] == OP["ld"]:
               l=ld(ins[5:8],ins[8:],mem,Reg,pc)
               return l
        elif ins[:5] == OP["st"]:
               l=st(ins[5:8],ins[8:],mem,Reg,pc)
               return l
        elif ins[:5] == OP["mul"]:
               l=mul(ins[7:10],ins[10:13],ins[13:],mem,Reg,pc)
               return l
        elif ins[:5] == OP["div"]:
               l=mul(ins[7:10],ins[10:13],ins[13:],mem,Reg,pc)
               return l
        elif ins[:5] == OP["mul"]:
               l=mul(ins[7:10],ins[10:13],ins[13:],mem,Reg,pc)#typeA
               return l
        elif ins[:5] == OP["rs"]:
               l=rs(ins[5:8],ins[8:],mem,Reg,pc)#type d
               return l
        elif ins[:5] == OP["ls"]:
               l=ls(ins[5:8],ins[8:],mem,Reg,pc)
               return l
        elif ins[:5] == OP["xor"]:
               l=xor(ins[7:10],ins[10:13],ins[13:],mem,Reg,pc)
               return l
        elif ins[:5] == OP["or"]:
               l=OR(ins[7:10],ins[10:13],ins[13:],mem,Reg,pc)
               return l
        elif ins[:5] == OP["and"]:
               l=AND(ins[7:10],ins[10:13],ins[13:],mem,Reg,pc)
               return l
        elif ins[:5] == OP["not"]:
               l=NOT(ins[10:13],ins[13:],mem,Reg,pc)
               return l
        elif ins[:5] == OP["cmp"]:
               l=cmp(ins[10:13],ins[13:],mem,Reg,pc)
               return l
        elif ins[:5] == OP["jmp"]:
               l=jmp(ins[8:],mem,Reg,pc)
               return l
        elif ins[:5] == OP["jlt"]:
               l=jlt(ins[8:],mem,Reg,pc)
               return l
        elif ins[:5] == OP["jgt"]:
               l=jgt(ins[8:],mem,Reg,pc)
               return l
        elif ins[:5] == OP["je"]:
               l=je(ins[8:],mem,Reg,pc)
               return l

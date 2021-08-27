import Memory
import Regis
import ExecuteEngine
import Pc
import matplotlib.pyplot as plt
l=[]

while True:
    try :
        line = input()
        l.append(line)
    except EOFError:
            break;
def dtob(n):
    n=int(n)
    bnr = bin(n).replace('0b','')
    x = bnr[::-1] 
    while len(x) < 8:
        x += '0'
    bnr = x[::-1]
    return bnr
mem={}
for i in range(256):
    mem[dtob(i)]="0000000000000000"
for i in range(len(l)):
        mem[dtob(i)]=l[i]
def padded_bin(x):
    return bin(x)[2:].zfill(16)
Reg={"000":"0000000000000000",
"001":"0000000000000000",
"010":"0000000000000000",
"011":"0000000000000000",
"100":"0000000000000000",
"101":"0000000000000000",
"110":"0000000000000000",
"111":"0000000000000000",}
pc=0
def main(mem,Reg,pc):
        halted=False
        cycle=0
        x=[]
        y=[]
        executed=True
        reset=1
        while executed:
                ins=Memory.fetch(dtob(pc),mem)
                executed=ExecuteEngine.execute(ins,mem,Reg,pc)
                Reg2=Reg
                if type(executed)!=bool:
                    mem=executed[0]
                    Reg=executed[1]
                Pc.dump(pc)
                y.append(pc)
                if type(executed)!=bool:
                    pc=executed[2]
                Regis.dump(Reg)
                if type(executed)==bool:
                    executed=False
                x.append(cycle)
                cycle+=1
                
        Memory.dump(mem)
        plt.title("Memory accesses vs cycle")
        plt.xlabel("cycle")
        plt.ylabel("Memory accesses")
        plt.plot(x,y)
        plt.show()
main(mem,Reg,pc)        

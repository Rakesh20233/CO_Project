
def dump(Reg):
        for i in Reg:
                print(Reg[i],end=" ")
        print()
def fetch(n,Reg):
        n=str(n)
        return(Reg[n])
def reset(Reg):
        Reg["111"]="0000000000000000"
        return Reg

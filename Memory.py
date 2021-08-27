
def dtob(n):
    n=int(n)
    bnr = bin(n).replace('0b','')
    x = bnr[::-1] 
    while len(x) < 8:
        x += '0'
    bnr = x[::-1]
    return bnr
def fetch(n,mem):
        return mem[n]
def dump(mem):
        for i in mem:
                print(mem[i])



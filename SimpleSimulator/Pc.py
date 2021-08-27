def dtob(n):
    n=int(n)
    bnr = bin(n).replace('0b','')
    x = bnr[::-1] 
    while len(x) < 8:
        x += '0'
    bnr = x[::-1]
    return bnr
def dump(pc):
        print(dtob(pc),end=" ")

        
        

inp = list('000000111000011101100000001010000001111100000101110000100010000000010110000111010')
while len(inp) >= 0:
    print(inp)
    iinp = ''.join(inp[:10])
    print(iinp)
    #print(int(iinp, 2))

    for i in iinp: 
        inp.remove(i)


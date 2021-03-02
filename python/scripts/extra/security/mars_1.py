#inp = list('000010001000000010110000111010000000011100001110110000000101000000111110000010111')
#inp = list('00000101110000100010000000101100001110100000001110000111011000000010100000011111')

num = []; msg = []
letter = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
inp = list('00000011100001110110000000101000000111110000010111000010001000000010110000111010')
while len(inp) >= 1: 

    _inp = ''.join(inp[:10]) 
    num.append(int(_inp, 2))
    
    for x in inp[:10]:  
        inp.remove(x)
   
for i in num: 
    if i < (len(letter) + 1): 
        msg.append(letter[i - 1])
    else:
        msg.append(i)

print(msg)

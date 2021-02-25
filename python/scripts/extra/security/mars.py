
def count(y): 
    y = list(y)
    for i in range(0,3): 
        y.remove(y[i])
    
    x = y 

    denary = 0
    print(x)
    result  = []
    for digit in x: 
        denary = denary * 2 + int(digit)
        
    
    print(denary)

circle_4 = [

        '0000001110',
        '0001110110',
        '0000001010',
        '0000011111',
        '0000010111',
        '0000100010',
        '0000001011',
        '0000111010'

]

for i in circle_4: 

    y = i
    count(y)



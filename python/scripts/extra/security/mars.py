
def count(y): 
    data = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


    y = list(y)
    for i in range(0,3): 
        y.remove(y[i])
    
    x = y 
  
    denary = 0
    
    result  = []
    for digit in x: 
        denary = denary * 2 + int(digit)
        
    print(denary)

    print('-----')

   # if denary <= (len(data) + 1): 
   #     denary = data[denary - 1]
   #     print(denary) 

   # else: 
   #     denary = denary 
   #     print(denary)


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
    print(len(y))
    count(y)

#írjuk ki a 10*10es szorzótáblát

for i in range(1,11): #i=1,2,3,4,5,6,7,8,9,10
        for j in range(1,11): # soron belüli elemek 
            print(f"{i*j:3d}",end=' ') #:3d --> 3decimális helyen írjuk ki mindent
        print() #soremelés
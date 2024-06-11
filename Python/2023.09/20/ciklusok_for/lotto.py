from random import randint
#még nem vizsgáljuk az ismétlődést
#lotto 5/90
print("Az ötös lotto eheti nyerő számai: ", end='')
for i in range(5):
    print(randint(1,90), end=" ")

#lotto 6/45
print("Az hatos lotto eheti nyerő számai: ", end='')
for i in range(6):
    print(randint(1,45), end=" ")
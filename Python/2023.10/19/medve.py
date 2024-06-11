from random import random,randint

elojovetelek_szama=0

for i in range(1,8):
    print(f'{i}. nap: ')
    reggel=randint(-5,10)+random()
    delben=randint(5,25)+random()
    este=randint(0,15)+random()
    print(f'Reggel: {reggel:.2f}')
    print(f'Délben: {delben:.2f}')
    print(f'Este: {este:.2f}')
    atlag=(reggel+delben+este)/3
    if atlag>10:
        print("Kibújt a barna maci")
        elojovetelek_szama+=1
    else:
        print("Ma nem bújt ki")
print(f"\nA héten {elojovetelek_szama} alkalommal bújt ki a barna maci")

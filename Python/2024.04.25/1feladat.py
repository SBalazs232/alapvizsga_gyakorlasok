print('LNKO kivonásos algoritmussal')
a=int(input('a = '))
b=int(input('b = '))

if a>b:
    kisebb=a
    nagyobb=a
else:
    kisebb=a
    nagyobb=b

while nagyobb!=kisebb:
    nagyobb-=kisebb
    if nagyobb<kisebb:
        nagyobb,kisebb=kisebb=kisebb,nagyobb #megcseréli a 2 változó értékét

print(f'LNKO({a},{b}) = ({nagyobb})')

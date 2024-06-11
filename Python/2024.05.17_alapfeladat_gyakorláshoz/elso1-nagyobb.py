#!/usr/bin/env python3

egyik = input('Adj meg egy számot! ')
egyik = int(egyik)
másik = input('Adj meg egy másik számot! ')
másik = int(másik)

if egyik > másik:
    print('A nagyobb érték:', egyik,)
elif másik > egyik:
    print('A nagyobb érték', másik)
else:
    print('A két szám egyenlő')

#!/usr/bin/env python3

egyik = input('Adj meg egy szót! ')
egyik_hossza = len(egyik)
másik = input('Adj meg egy másik szót! ')
másik_hossza = len(másik)

if egyik_hossza > másik_hossza:
    print('A hosszabb szó:', egyik)
elif másik_hossza > egyik_hossza:
    print('A hosszabb szó:', másik)
else:
    print('A két szó egyforma hosszú.')

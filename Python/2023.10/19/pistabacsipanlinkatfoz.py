from random import randint

ivott=False #mert kezdéas előtt mnem ivott
osszes=0



for i in range(1,31):
    if ivott==False: #ha nem ivott elozo nap
        mai_fozet=randint(1,5)
        osszes+=mai_fozet
        if randint(1,5)==5:
            ivott=True
            osszes-=1  #megisznak 1 l paleszt
        print(f"{i}. nap:{mai_fozet} liter. Eddigi termés összesen: {osszes} liter, ", end="")
        if ivott:
            print(' ma ivott pista bacsi a haverokkal.', end="")
        print() #csak soremeles miatt kell
    else:
        print("pista bacsi nem foz mert mas napos")
        ivott=False
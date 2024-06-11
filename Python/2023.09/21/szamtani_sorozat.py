#Kérjük be egy számatni sorozat eslő (a1) és elemeinek számát (n) és diferenciáját (d)
#írjuk ki a sorozat n db elemét vesszővel elválasztva

a1=int(input("Kérem a sorozat első elemét: "))
d=int(input("Kérem a sorozat differenciáját: "))
n=int(input("Kérem a sorozat elemszámát: "))

#for i in range(n):
#    an=a1+i*d
#    print(an,end=',') #ha nem számít az utolsó vessző

for i in range(n):
    an=a1+i*d
    if i==n-1: # ha az utolső elem jön
        print(an, end='')
    else: #amíg nem jön
        print(an,end=',')
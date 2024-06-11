#kérjünk be egy számot és írjuk ki a faktoriálisát
#n!=1*2*3*4...*(n-1)*n


n=int(input('n = '))
faktorialis=1 #kezdő érték



print(f'{n}!=1',end='') #kiiras eleje
for i in range(2,n+1):
    #faktorialis=faktorialis*i
    faktorialis*=i
    print(f'*{i}',end='')


print(f"={faktorialis}") #kiírás vége



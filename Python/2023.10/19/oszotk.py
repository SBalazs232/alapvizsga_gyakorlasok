#egy szám osztóinka meghatározása

#kérjünk be egy számot
#írjuk ki az osztóit, egymás mellé, szóközökkel elválasztva
#15 osztói: 1 , 3 , 5 , 15

szam=int(input("szam: "))
print(f"{szam} osztói: ",end='')
for i in range(1,int(szam/2)+1):
    if szam%i==0:
        print(f" {i}",end="")
print(f" {szam}")


print(5/2)

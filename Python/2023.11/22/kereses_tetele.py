#Mondjuk meg,hogy benne van e a lsitában, és ha ige, akkor hányadik? (az elő fordulás)

from random import randint
szamok=[]
for i in range(20):
    szamok.append(randint(-100,100))
print(szamok)

keresett=int(input('keresett zsám: '))

#v1:
#univerázil megoldás
index=0
while index<len(szamok) and szamok[index]!=keresett:
    index+=1
#az első megtalát elem sorszámát adja vissza utána kilép
if index==len(szamok):
    print('a keresett szám nincs benne a listában.')
else:
    print(f'A keresett szám a {index+1}. a listában')


#v2:
#python specifikus megoldás
for i in range(len(szamok)):
    if szamok[i]==keresett:
        print(f'A keresett szám a {i+1}. a listában')
        break
else:
    print("A keresett szuám nincs benne a lsitában")


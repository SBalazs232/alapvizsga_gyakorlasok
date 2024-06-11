#növekményes ciklus - for

for i in range(10): #range(0,10)
    print("beni meni")
print ("ezt már nem érinti")    
    #létrehoz egy i változót 
    #10 ----> 0-9-ig vesz fel értékeket
    #alsó határ (0) benne van
    #felső határ (10) már nincs benne!!!

for i in range(10,20): #----------->10-19-ig vesz fel értéket
    print(i)

for i in range(100,201,2): #------> 100-200-ig kettesével megyünk a ciklusváltozóban
    print(i,end=" ")

print() # csak azért hogfy a kövi sorba legyen
for i in range(200,180,-1): #200-181-ig vesz fel értéket
    print(i,end=" ")

for i in range(2200,2180,2):
    print(i)
    #range üres tartomány ad ----> a ciklus magja (a ciklusban lévő utasítás(ok)) egyszer sem futle

    # KÉSŐBB: for ciklus lista vagy fájl elemein/sorain is végig tud menni
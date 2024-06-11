szoveg="Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus quis ipsa quaerat cum natus ab asperiores saepe recusandae deserunt! Accusantium porro eius, dolore ex doloribus voluptate! Odio assumenda vel eveniet. Ducimus qui, fugiat voluptates ut, corrupti deleniti unde quaerat molestiae culpa placeat voluptatum laboriosam impedit velit dolorem ab quidem facilis dignissimos autem. Dolore incidunt enim totam quasi libero omnis fuga! Minus numquam minima eligendi cum architecto perferendis consequatur! Hic laboriosam repellendus nihil iste animi aperiam distinctio voluptatem blanditiis facere assumenda sunt nam similique id eaque consectetur, quod dolorem vero qui? Blanditiis voluptate incidunt voluptatem sint consectetur quod inventore reprehenderit. At, dolorum! Tempore animi corporis expedita nam, perspiciatis illo explicabo nostrum maxime necessitatibus laboriosam soluta porro voluptatum, consequatur voluptatibus quibusdam ab. Ullam molestias eius atque laborum error consequuntur a iure quibusdam eligendi, magni, quae minima, quaerat earum sequi blanditiis harum. Ipsa natus a officia. Similique magnam alias a voluptates molestiae dolores. Accusantium, impedit? Perspiciatis itaque quaerat, cupiditate, veniam modi temporibus quo ad veritatis deleniti voluptatibus provident aut quis totam fugit accusamus alias mollitia sunt enim et nulla nesciunt. Distinctio, rem nesciunt. Veniam animi, ullam corporis itaque beatae dolores soluta nam quam fuga autem, error, voluptatibus tenetur doloremque! Voluptates, ex esse repudiandae ab alias amet similique veniam. Blanditiis a praesentium necessitatibus eum! Sit repellat quis distinctio hic, veritatis perspiciatis provident. Nostrum saepe vitae quaerat vero, cumque ab reiciendis officia labore tempora repellat modi accusantium consectetur dolorum obcaecati ratione maiores alias optio quasi? Voluptatibus vero modi quibusdam nesciunt, reprehenderit maxime eum voluptatem esse explicabo exercitationem. Recusandae neque quasi quos sequi eius voluptatibus quam expedita, voluptatem error? Aut obcaecati vel consequatur provident esse eos. Expedita quaerat, magnam, perferendis nisi nam ab voluptates necessitatibus explicabo eaque beatae fuga deserunt officia voluptatibus possimus adipisci placeat nostrum quis commodi eius! Dolor ex distinctio neque dolorum sequi repudiandae!"

irasjelek='.,:?!-;'
for irasjel in irasjelek: #az írásjeleket lecseréljük a semmire
    szoveg=szoveg.replace(irasjel,'')

szoveg=szoveg.lower() #csupa kisbetűsre alakítjuk a szöveget

szavak=szoveg.split(' ')# a szöveget szétdaraboljuk a szóközök mentén

#print(szavak)

#melyik szó hányszor szerepel a szövegben?
stat={}
for szo in szavak: #végig megyünk a szavak listán
    if szo in stat.keys(): #ha a szó benne van már a kulcsmezokben 
        stat[szo]+=1             #a value mező értékét 1el növeljuk
    else:                                #ha szo meg nincs benne
        stat[szo]=1    #akkor létrehozzuk az új dict elemet

#print(stat)

#melyik szavak fordulnak elő 1nél többször (és mennyiszer)?
for key,value in stat.items():
    if value>2:
        print(f'{key} - {value} db')

#MELYIK SZO FORDLULT ELO A LEGTOBBSZOR?

# legjobb_value=-1
# legtobb_key=""
# for key, value in stat.items():
#     if value>legjobb_value:
#         legjobb_value=value
#         legtobb_key=key
# print(f'legtobbszor a {legtobb_key} szó fordul elő ({legjobb_value})') #csak az első legtobbet

#ha minden max-ot meg kell határozni
legtobb_value=max(stat.values()) #max keresés progtétel helyett
print(f'legtobbszor ({legtobb_value} alkamlommal) előforduló szavak:')
for key,value in stat.items():
    if value==legtobb_value:
        print(f'\t{key}')

brojevi = []
for i in range (101):
    brojevi.append(i)

print(brojevi)

#sintaksa SLICE-anja liste: brojevi[START : STOP : STEP]

izdvojeni_brojevi = brojevi [20 : 51 : 1]
print(izdvojeni_brojevi)

podlista1 = brojevi[20: ]
print (podlista1)

podlista2 = brojevi [ : 41]
print (podlista2)

brojevi_obrnuto = brojevi [::-1]
print (brojevi_obrnuto)

podlista3 = brojevi [-2 :] #od 99 do 100
print(podlista3)

podlista4 = brojevi [:-2] # od početka do 98
print(podlista4)

podlista5 = brojevi [:-3:-1] #kreće od kraja sve dok ne dođe do trećeg elementa od kraja, ali on nije uključen
print(podlista5)

podlista6 = brojevi [-3: : -1] #kreće od -3, odnosno trećeg elementa od kraja
print(podlista6)
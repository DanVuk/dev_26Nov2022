ucenici = {
    1 : ['Marko Markić', 'Unska 2, Zagreb', 'M', 1.68],
    2 : ['Ana Anić', 'Krivi put 5, Krapina', 'Ž', 1.55],
    3 : ['Pero Perić', 'Splitska 98, Sinj', 'M', 1.80],
    4 : ['Ivan Ivić', 'Jablanova 3, Sisak', 'M', 1.75],
    5 : ['Stjepan Stjepić', 'Brezova 23, Osijek', 'M', 1.85],
    6 : ['Sara Sarić', 'Otočna 28, Split', 'Ž', 1.61],
    7 : ['Marija Marić', 'Riječna 22, Rijeka', 'Ž', 1.59],
    8 : ['Petra Pertrić', 'Desna 54, Đakovo', 'Ž', 1.68],
    9 : ['Edo Edić', 'Kozuraška 21, Zagreb', 'M', 1.78],
    10 : ['Ante Antić', 'Lijeva 18, Imotski', 'M', 1.80]
}

#Izračunajte prosječnu visinu svih učenika u rječniku
'''
lista_ucenika = []
ucenicke_vrijednosti = ucenici.values()
print(ucenicke_vrijednosti)

for vrijednost in lista_ucenika
    print(ucenicke_vrijednosti[-1])
    lista_ucenika.append(vrijednost[-1])
print(lista_ucenika)

for kljuc, vrijednost in ucenici.items():
    print(ucenici[kljuc][-1])
    prosjecna_visina = sum(lista_ucenika) / len([lista_ucenika])
print(f'Prosječna visina svih učenika u rječniku je {prosjecna_visina}')
'''
#Napravite popis u kojem će se vidjeti samo redni broj i ime
'''
lista_rbr = []
for kljuc in ucenici.keys():
    lista_rbr.append(kljuc)
#print(lista_rbr)
lista_imena=[]
for vrijednost in ucenici.values():
    lista_imena.append(vrijednost[0])
#print(lista_imena)

for i in range(len(lista_rbr)):
    print(f'{lista_rbr[i]}. {lista_imena[i]}')
'''
#Ispišite broj učenika i učenica (M i Ž) punom rečenicom

lista_spol = []
broj_M = lista_spol.count('M')
broj_Ž = lista_spol.count('Ž')

for broj_M in lista_spol.keys():
    lista_spol.append(broj_M)
for broj_Ž in lista_spol.keys():
    lista_spol.append(broj_Ž)
print(f'Broj učenika Ž spola je {} ...')
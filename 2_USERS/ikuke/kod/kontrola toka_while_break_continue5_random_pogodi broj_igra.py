
#unos passworda
import random

broj= random.randint(1,100)
print (broj)
iteracija=0

while True:
    
    
    unos = (input('Unesi broj u rasponu 1-100: '))
    while unos.isdigit() ==False:
        
        print('krivi unos - ponovite unos')
        unos = (input('Unesi broj u rasponu 1-100: '))

    iteracija +=1
    unos=int(unos)
    if unos==broj:
        print('broj je pogođen')
        break
    
    else:
        if unos<broj:
            print('traženi broj je veći od upisanog broja')
        else:
            print('traženi broj je manji od upisanog broja')

print (f'{broj} je pogođen u {iteracija} pokušaja')





"""
while True:
    unos = int(input('Unesi broj u rasponu 1-100: '))
    if ((101>unos>0)):
        print('broj je u rasponu 1-100')
        break
    else:
        
        print('broj je van raspona')

"""

"""
while True:
    print('Sada smo u potencijalno beskonačnoj petlji')


    odgovor = int(input ('želite li prekinuti petlju? 1-DA, 0-NE   '))
    if odgovor==1:
        print('potencijalno beskonačna petlja je prekinuta') 
        break

    else:
        pass
 

kontinju='Sada smo u potencijalno beskonačnoj petlji

while True:
    print('Sada smo u potencijalno beskonačnoj petlji')


    if odgovor==1:
        print('potencijalno beskonačna petlja je prekinuta') 
        break

    else:
        pass
 

"""
"""

brojevi = []
for i in range (1,21):
    brojevi.append(i)

for broj in brojevi:
    print (broj, end='')
print(
)
i = 0

"""
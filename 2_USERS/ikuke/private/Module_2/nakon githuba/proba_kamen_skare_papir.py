

#KAMEN ŠKARE i PAPIR

# Napravite program koji će vam omogućiti igrati kamen, škare, papir protiv računala



import random   # Python modul za generiranje nasumičnih brojeva

# Definicija varijable tekst
izbornik = """
                                                         Izbornik (upišite broj ispred željenog odabira):
                                                                        1. Kamen
                                                                        2. Škare
                                                                        3. Papir
"""
bodovi_korisnik=0
bodovi_racunalo=0


while True:



    izbor_racunala = random.randint(1, 3)  # Od 1 do 3 UKLJUČIVO - nije isto kao range()

    if izbor_racunala == 1:
        izbor_racunala = 1 #'kamen'

    elif izbor_racunala == 2:
        izbor_racunala = 2 #'skare'

    else:
        izbor_racunala = 3 #'papir'

    print('POMOĆ ------>Izbor racunala', izbor_racunala) # Ovu liniju koristiti samo tijekom testiranja, kasnije komentirati


    while True:
        print(izbornik)

        
        izbor_korisnika = int(input('Izaberite: kamen, škare ili papir:\t'))
        

        if izbor_korisnika == 1:
            izbor_korisnika = 1
            break
        elif izbor_korisnika == 2:
            izbor_korisnika = 2
            break
        elif izbor_korisnika == 3:
            izbor_korisnika = 3
            break
        else:
            print('Pograšan unos! Molimo pokušajte ponovo.')#osiguranje od unošenja krivog parametra
        
    print('')
    print('____________________________________________________________________________________________________________________________________________')
    if izbor_korisnika == izbor_racunala:
        print('NERIJEŠENO! Izabrali se isto kao i računalo')


    elif izbor_korisnika == 1 and izbor_racunala == 3:
        print('Izgubili ste, računalo je odabralo papir')
        bodovi_racunalo+=1

    elif izbor_korisnika == 1 and izbor_racunala == 2:
        print('POBIJEDILI ste, računalo je odabralo škare')
        bodovi_korisnik+=1

    elif izbor_korisnika == 3 and izbor_racunala == 2:
        print('Izgubili ste, računalo je odabralo škare')
        bodovi_racunalo+=1

    elif izbor_korisnika == 3 and izbor_racunala == 1:
        print('POBIJEDILI ste, računalo je odabralo kamen')
        bodovi_korisnik+=1

    elif izbor_korisnika == 2 and izbor_racunala == 1:
        print('Izgubili ste, računalo je odabralo kamen')
        bodovi_racunalo+=1

    elif izbor_korisnika == 2 and izbor_racunala == 3:
        print('POBIJEDILI ste, računalo je odabralo papir')
        bodovi_korisnik+=1

    print()
    print('____________________________________________________________________________________________________________________________________________')
    print()
    print(f'                                                            KORISNIK: {bodovi_korisnik}  :   RACUNALO: {bodovi_racunalo}')
    print('____________________________________________________________________________________________________________________________________________')
    print()
    izbor_korisnika=0

    
    print('ŽELITE LI NASTAVAK IGRE?')
    
    while izbor_korisnika==0:
        izbor_korisnika = int(input('Izaberite: 1 - DA ili 0 - NE:\t'))
        print('izbor korisnika je', izbor_korisnika)


        if izbor_korisnika == 0:
            izbor_korisnika = 0
            break

        elif izbor_korisnika == 1:
            i=0
        else:
            print('Pograšan unos! Molimo pokušajte ponovo.')#osiguranje od unošenja krivog parametra

    if izbor_korisnika == 0:
            izbor_korisnika = 0
            break

    print('______________________________________________________________________')






# ZADATAK: Prepravite zadatak tako da se ne samo provjera izbora nego i igra ponavlja sve dok kortisnik to želi

#Modul 2 - Osnove programiranja u Pythonu
#Kontrola toka izvršavanja programskog kôda
#ZADATAK WHILE i IF PETLJE
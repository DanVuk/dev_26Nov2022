korisnici={
    'admin':['Ivan', 'Ivic', 'aei123'],
    'pperic':['Petar', 'Peric', 'ou456'],
    'mmaric':['Mara','Maric','rst567']
}

def pregled_korisnici():
    '''Funkcija koja ispisuje sve korisnike (ime i prezime) iz baze rječnika'''
    for v in korisnici.values():
        print(v[0], v[1])



def tko_je_admin():
    '''Funkcija koja ispisuje ime i prezime administratora'''
    for k,v in korisnici.items():
        if k=='admin':
            print(f'Administrator je {v[0]} {v[1]}')



def dohvati_admin_pswd():
    '''Funkcija koja vraća administratorsku lozinku'''
    for k,v in korisnici.items():
        if k=='admin':
            return v[2]

admin_pswd=dohvati_admin_pswd()
#print(admin_pswd)
#pregled_korisnici()
tko_je_admin()

def logiranje(uneseni_username):
        if uneseni_username in korisnici.keys():
            uneseni_password=input('Unesi lozinku: ')
            if uneseni_password==korisnici[uneseni_username][2]:
                print(f'Dobrodošli, {korisnici[uneseni_username][0]} {korisnici[uneseni_username][1]}')
            else:
                print('Pogršna lozinka!')
        else:
            print(f'Nepostojeće korisničko ime!')

unos_user=input('Unesi korisničko ime: ')
logiranje(unos_user)

def dodavanje_korisnika():
    korisn_ime=input('Unesi korisničko ime: ')
    ime=input('Unesi ime: ')
    prezime=input('Unesi prezime: ')
    lozinka=input('Unesi lozinku: ')
    korisnici[korisn_ime]=[ime, prezime, lozinka]
    print(korisnici)

def brisanje():
    clan_brisi=input('Unesi username korisnika za obrisati: ')
    clan_brisi=korisnici.pop(clan_brisi)
    print(korisnici)

while 1:
    odg=input('Želite li se rijaviti? da/ne')
    if odg=='da':
        unos_user=input('Unesi korisničko ime: ')
        logiranje(unos_user)
    else:
        break
#dodavanje_korisnika()

brisanje()


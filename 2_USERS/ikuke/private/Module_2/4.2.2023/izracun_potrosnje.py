import datetime as dt


def pozdrav(ime):
    if sat < 11:
        print(f'Dobro jutro {ime}')

    elif 11<= sat <=18:
         print(f'Dobar dan {ime}')

    else:
         print(f'Dobra večer {ime}')


#vase_ime=input ('Unesi svoje ime ')

#pozdrav (vase_ime)

def generiraj_racun(broj):

    sat=dt.datetime.now().hour
    minuta=dt.datetime.now().minute
    year=dt.datetime.now().year

    print( f'{dt.datetime.now()}')

    print (f'{sat}:{minuta}')
    sadasnji_trenutak=dt.datetime.now()
    day=sadasnji_trenutak.day
    month=sadasnji_trenutak.month
    year=sadasnji_trenutak.year

    sekunda=sadasnji_trenutak.second
    print('--------------------------------------------------------------------------------')
    print(f'{sat}:{minuta}:{sekunda}    {day}. {month}. {year}.')
    print (f'broj računa: {broj}')
    print('--------------------------------------------------------------------------------')



broj_racuna=2
generiraj_racun(broj_racuna)

i=2
while i<10: 

    generiraj_racun(i)
    i=i+1



#-----------------------------------------------------------------------------------------------------------------------------------------

def unos_potrosnje():
    potrosnja=input('Upisi potrosnju u litrama na 100 km: ')
    potrosnja=int(potrosnja)
    return potrosnja


def unos_cilja():
    cilj=input('unesi ciljanu mjesečnu potrošnju: ')
    cilj=float(cilj)
    return(cilj)


def izracun_potrosnje(potrosnja):
    cijena_goriva=15.5
    kune=potrosnja*cijena_goriva
    print(f'potrosnja goriva je {kune} na 100 km')
    udaljenost=unos_cilja()/kune*100


    print(f'mozete mjesečno prevaliti {udaljenost} kilometara')


izracun_potrosnje(unos_potrosnje())

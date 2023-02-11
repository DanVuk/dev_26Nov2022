import os
def Iscrtaj_Plocu():
    os.system('cls' if os.name=='nt' else 'clear')

    print('\n\tKrižić Kružić\n\n')
    print('Igrač 1 (X)  -  Igrač 2 (O)')
    print()

    print('\t    |    |    ')
    print('\t', polje_na_ploci)

#play = input("Do you wish to play? Enter y or n. ")
play = 'y'
miles = 0.6214
pounds = 2.2046
option = 1

while play == "y":
    option = str(input('''Please enter the number for desired conversion: 
        \n1) Distance
        \n2) Temperature
        \n3) Weight
        \n4) Volume
        \n5) Power
        
        \nYour input here: '''))
        ##### START OF KM - MILES CONVERSION #####
        
# TODO Vidi s Vesnom kako ovo najbolje validirati
    if option.isdigit() == True:
        print("OK DIGIT JE IDEMO DALJE.") 
        
        option = int(option)
        
        
        
        if option == 1:
            menu = int(input('''
            Choose conversion:\n
            1) Kilometers to Miles
            2) Miles to kilometers
            Your option here: '''))
            if menu == 1:
                conversion = int(input("Input kilometer number: "))
                print(f'{conversion} km are equal to {conversion * miles} miles.')
                #break
            elif menu == 2:
                conversion = int(input("Input miles number: "))
                print(f'{conversion} miles are equal to {conversion / miles} miles.')
                #break
            else:
                print("Incorrect input.")
                conversion_progress = input("Input 'y' to continue or 'n' to quit.")
                #play = 'n'
                while conversion_progress == 'y':
                    if conversion_progress == 'y':
                        play = 'y'
                        break
                    break
  
                    # elif conversion_progress == 'n':
                    #     play = 'n'
                    #     print("Thank you, bye bye")
                    #     break
                    # else: 
                    #     print("Incorect input.")
                    #     continue
    # TODO unit conversion error handling.
                        
                    
                    
        ###########################################
        
        
    #     ##### START OF KG - POUNDS CONVERSION #####
    #     elif option == 3: 
    #         input = int(input("Input the kg number: "))
    #         print(f'{input} kilograms are equal to {input * pounds} pounds.')
    #         break
        
    #     elif option == 4:
    #         input = int(input("Input the miles number: "))
    #         print(f'{input} miles are equal to {input / pounds} kilos.')
    #         break
        
    #     ###########################################
        
    #     ##### START OF FERENHEIT - CELCIUS CONVERSION #####
    #     elif option == 5:
    #         input = int(input("Input the celcius temperature: "))
    #         print(f'{input} celcius are equal to {round(input * 1.8 + 32,2)} ferenheits.')
    #         break
        
    #     elif option == 6:
    #         input = int(input("Input the ferenheit temperatue: "))
    #         print(f'{input} ferenheits are equal to {round((input - 32) / 1.8,2)} celcius.')
    #         break
    #     ###########################################
        
    #     ##### START OF LITERS - GALOONS CONVERSION #####  
    #     elif option == 7:
    #         input = int(input("Input the number of liters: "))
    #         print(f'{input} listers are equal to {round(input * 0.2642,2)} gallons.')
    #         break
        
    #     elif option == 8:
    #         input = int(input("Input the number of gallons: "))
    #         print(f'{input} gallons are equal to {round(input / 0.2642,2)} liters.')
    #         break
    #     ###########################################   

    #     ##### START OF KW - HP CONVERSION #####  
    #     elif option == 9:
    #         input = int(input("Input the number of KW: "))
    #         print(f'{input} KWs are equal to {round(input * 1.3596,2)} horse powers.')
    #         break
        
    #     elif option == 10:
    #         input = int(input("Input the number HP: "))
    #         print(f'{input} HP are equal to {round(input / 1.3596,2)} kilowatts.')
    #         break

    #     else:
    #         print("Number of range, please input the  number 1-10")
    #         answer = input("Input 'y' if you with to continue or 'n' to cancel. ")
    #         if answer == 'n':
    #             print("Thank you! Bye, bye.")
    #             break
    #         elif answer == 'y':
    #             pass
    #         else: 
    #             print("\n ############## Invalid input. ##############\n")
    #             play == 'y'
    else:
        continue
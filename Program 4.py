# -------------------------------------------------------------
# Author:
# Andrew Zeiser
# Program: Program 5
# Description: 
# To display your employee billing records. 
# ------------------------------------------------------------

import BillingModule

def main():
    again = True
    while again:
        try:
            
            loopControl = True
            while loopControl:
                print('\nBilling System Menu:\n')
                print('\t0 - end')
                print('\t1 - Enter billing data')
                print('\t2 - Display ad-hoc billing report')

                option = int(input('\nOption ==> '))

                if option == 0:
                    loopControl = False
                    again = False                    
                    print('\nProgram has ended.')
                elif option == 1:
                    BillingModule.billingEntry()
                elif option == 2:
                    BillingModule.readBillingRecords()
                else:
                    print('\nPlease enter an available option.')
            
        except ValueError:
            print('\nPlease enter an available option.')
            
            
main()
    
   


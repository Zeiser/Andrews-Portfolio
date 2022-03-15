



def readEmployeeName(prompt):
    employee = input(prompt)
    while not employee:
        print("Employee name must be entered","\n")
        employee = input(prompt)
    return employee

def readHourlyRate(prompt):
    MIN_RATE = 20.00
    rate=0
    again = True

    while again:
        
        try:
            rate = float(input(prompt))
            if rate < MIN_RATE:
               print("Invalid Hourly Rate, must be at least",\
                     "$20.00/hour.","\n")
            else:
                again=False
        except ValueError:
            print("Error! Value entered must be numeric. \n")
            
    return rate



def readWeeklyHours(prompt):
    MIN_HOURS = 35
    MAX_HOURS = 80
    again = True

    
    while again:
        try:            
            week = float(input(prompt))
            if week < MIN_HOURS or week > MAX_HOURS:
                print('Invalid number of hours, must be between 35',\
                      'and 80',"\n")
            else:
                again = False
        except ValueError:
            print("Error! Value entered must be numeric. \n")
    return week
    

def writeBillingRecord(employee,rate,week1,week2,\
                       week3,week4,totalHours,invoiceAmount):
    
    records= open("Billing.txt","a")

    records.write(employee +"\n"+ str(rate)+"\n"+ str(week1)+"\n"+\
                  str(week2)+"\n"+ str(week3)+"\n"+ str(week4)+"\n"+str(totalHours)+"\n"+str(invoiceAmount)+"\n")


    records.close()


def readBillingRecords():
    again= True
    while again:
        try:
            records = open('Billing.txt','r')
            name = records.readline().rstrip('\n')
            
            print('Employee\t','Rate\t','Week 1\t','Week 2\t','Week 3\t',\
                  'Week 4\t','Hours\t', "Total")

            sumTotal=0
            sumHours=0
            avHours=0
            employeeCount=0
            while name != '':
                employeeCount+=1
                rate = float(records.readline().rstrip('\n'))

                week1= float(records.readline().rstrip('\n'))
                week2= float(records.readline().rstrip('\n'))
                week3= float(records.readline().rstrip('\n'))
                week4= float(records.readline().rstrip('\n'))

                totalHours = float(records.readline().rstrip('\n'))

                totalDue = float(records.readline().rstrip('\n'))

                sumTotal += totalDue
                sumHours += totalHours
                avHours =(sumHours/employeeCount)
                
                print(name,'\t',sep='',end='')
                print(" $",format(rate,',.2f'),sep='',end='')
                print('\t',format(week1,'.2f'),'\t',format(week2,'.2f'),'\t',\
                      format(week3,'.2f'),'\t',format(week4,'.2f'),'\t',\
                      format(totalHours,'.2f'),end='')
                print("  $",format(totalDue,',.2f'),sep='')

                
                name = records.readline().rstrip('\n')
    
            print('\n'+'Total Billable Due:\t'," $",format(sumTotal,',.2f'),sep='')
            print('Total Billable Hours:\t',format(sumHours,'.2f'))
            print('Average Billable Hours:\t',format(avHours,'.2f'))
            
    
    
            records.close()
            again = False
        except FileNotFoundError:
            print('\nThere is no existing data for this field.')
            again= False



def billingEntry():
    ## CONSTANTS
    REGULAR_HOURS = 160
    OT_RAISE = .05
    NUMBER_OF_WEEKS = 4
    
    ## variables 
    averageHours=0.0
    otHours=0.0
    otPay=0.0
    otRate=0.0
    otAmount=0.0
    regAmount=0.0
    regHours=0.0
    hourStatement=0
    another = "y"
    
    ##Loop to enter more information
    while another == "y":
        
        employee=readEmployeeName('Employee Name: ')
        rate=readHourlyRate('Hourly Rate: ')
        week1= readWeeklyHours\
               ("Enter hours worked for week 1: ")
        week2= readWeeklyHours\
               ("Enter hours worked for week 2: ")
        week3= readWeeklyHours\
               ("Enter hours worked for week 3: ")
        week4= readWeeklyHours\
               ("Enter hours worked for week 4: ")
        
            
            ##Processing the employees info for output
        totalHours= week1+week2+week3+week4
        averageHours = totalHours/NUMBER_OF_WEEKS
        ##calculating overtime 
        if totalHours > REGULAR_HOURS:
            #How many OT hours worked
            otHours=totalHours - REGULAR_HOURS
            #hourly OT pay increase * hourly rate
            otPay = round(rate * OT_RAISE,2)
            #OT hourly rate
            otRate= otPay+rate
            #How much paid for OT worked
            otAmount = round(otHours * otRate,2)
            ##Amount owed for 160 hours
            regAmount= REGULAR_HOURS * rate
            #Total amount owed to employee
            invoiceAmount = regAmount + otAmount
            ## regular hours
            regHours = REGULAR_HOURS
            #output
            hourStatement = "\n"+employee+" worked "+str(otHours)+\
                            " hours of overtime this month."
            otOutput =  "\n"+"Overtime hours: "+format(otHours,'.2f')+\
                       " @ "+"$"+\
                       format(otRate,'.2f')+" = $"+\
                       format(otAmount,',.2f')
                    
        else:
            hourStatement = "\n"+employee+\
                            " worked no hours of overtime this month."
            invoiceAmount = round(rate*totalHours,2)
            regAmount = rate*totalHours
            regHours = totalHours
            otOutput="\t"     

            ## Output
        print(hourStatement)
        print('\nInvoice')
        print('Resource: ',employee,'\tAverage weekly hours: ',\
              format(averageHours, '.2f'))
        print('\nTotal billable hours: ',\
            format(totalHours, '.2f'),'\trate: $',\
            format(rate, '.2f'), sep='',end="")
        print(otOutput)
        print("Regular hours:",format( regHours,'.2f'),"@",end=' ')
        print("$",format(rate,'.2f'),sep="",end=" ")
        print("= $",format(regAmount,',.2f'),sep="")
        print('Amount Due: $',format(invoiceAmount,',.2f'), sep='')
        
        writeBillingRecord(employee,rate,week1,week2,week3,\
                           week4,totalHours,invoiceAmount)
        
        another = input("Enter another Employee? ('y'=yes): ")
    


















    
    
            
   


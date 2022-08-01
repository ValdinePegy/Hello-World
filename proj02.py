# Project 2 
# Purpose: A code to Print the amount billed to a player for a car he rented 
# The amount is determined based on the classification code, miles driven, rental period

import math
BANNER = "\nWelcome to Horizons car rentals. \
\n\nAt the prompts, please enter the following: \
\n\tCustomer's classification code (a character: BD, D, W) \
\n\tNumber of days the vehicle was rented (int)\
\n\tOdometer reading at the start of the rental period (int)\
\n\tOdometer reading at the end of the rental period (int)" 
print(BANNER)
PROMPT = input('''\nWould you like to continue (A/B)? ''')
while PROMPT == 'A':
    code = input("\nCustomer code (BD, D, W): ")
    while not(code == 'BD' or code == 'D' or code == 'W'):
        print("\n\t*** Invalid customer code. Try again. ***")
        code = input("\nCustomer code (BD, D, W): ") 
        if code == 'BD' or code =='D' or code == 'W':
            break     
    Number = int(input("\nNumber of days: "))
    Odometer_start = int(input("Odometer reading at the start: "))
    Odometer_end = int(input("Odometer reading at the end:   "))
    miles_driven = (Odometer_end - Odometer_start)
    
    if miles_driven < 0:
        miles_driven = miles_driven + 1000000   #since the odometer reads 6 digits
    miles_driven = miles_driven/10
    miles_driven = float(miles_driven)
    
    '''average miles per day '''
    avgD = miles_driven/Number   #avgD is average miles driven per day
    '''average miles per week'''
    avgW = miles_driven/math.ceil(Number/7)  #avgW is average mile driven per week
        
    if code =='BD':
        base_charge = 40 * Number
        mileage_charge = 0.25 * miles_driven
    elif code == 'D':
        base_charge = 60 * Number
        if avgD <= 100:
            mileage_charge = 0
        else :
            mileage_charge =  0.25 * (avgD - 100) * Number
    elif code == 'W':
        base_charge = 190 * math.ceil((Number/7))
        if avgW <= 900:
            mileage_charge = 0
        elif 900 < avgW <= 1500:
            mileage_charge = 100 * math.ceil(Number/7)
        else :
            mileage_charge = 200 * math.ceil(Number/7) + 0.25 * (avgW - 1500) * math.ceil(Number/7)
            
    amount = float(round(base_charge + mileage_charge,2))
    
    print("\nCustomer summary:")
    print("\tclassification code:",code)
    print("\trental period (days):",Number)
    print("\todometer reading at start:",Odometer_start)
    print("\todometer reading at end:  ",Odometer_end)
    print("\tnumber of miles driven: ",miles_driven)
    print("\tamount due: $",amount)
    print()
    
    PROMPT = input('''\nWould you like to continue (A/B)? ''')
    while (PROMPT != "A" and PROMPT != "B"):
        PROMPT = input('''\nWould you like to continue (A/B)? ''')

print("Thank you for your loyalty.")
    
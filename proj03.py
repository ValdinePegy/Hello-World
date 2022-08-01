# Project 03
# A program to calculate the tuition of MSU students based on conditions like their level, major

# some useful inputs for the program and declarations
Per_credit = None
Flat_Rate = None
Fee = None
tuition = None
total = None
egr_admit = ''
asmsu_tax = 21
fm_radio_tax = 3
state_news_tax = 5
jmcss_tax = 7.50    # james madison college tax
james_mc = ''   
college = None
cont= "yes"

#special fees
business_special1 = 113 #part-time
business_special2 = 226 #Full-time
egr_admit_special1 = 402 #part-time
egr_admit_special2 = 670 #full-time
health_special1 = 50 #part-time
health_special2 = 100  #full-time
science_special1 = 50  #part-time
science_special2 = 100  #full-time


print("2021 MSU Undergraduate Tuition Calculator.\n")
while cont == "yes":
    

    level = input("Enter Level as freshman, sophomore, junior, senior: ").lower()
    while not (level == 'freshman' or level == 'sophomore' or level == 'junior' or level == 'senior'):
        print("Invalid input. Try again.")
          
        level = input("Enter Level as freshman, sophomore, junior, senior: ")
    
    # if the person is junior or senior
    if (level == 'junior') or (level == 'senior'): 
        college = input("Enter college as business, engineering, health, sciences, or none:\n").lower()

    if not((college=='business') or (college=='engineering') or (college=='health') or (college=='sciences')):
        college = None
        
     # if the person is freshman or sophomore
    if (level == 'freshman') or (level == 'sophomore'): # the code has to do the following for freshman and sophomore
        egr_admit = input("Are you admitted to the College of Engineering (yes/no): ")
        egr_admit = egr_admit.lower()

        if egr_admit == 'yes':
            college = 'Engineering'

    if college == None:    # In case the input for college does not match what was specified
        james_mc = input("Are you in the James Madison College (yes/no): ")
        james_mc = james_mc.lower()

        if james_mc == 'yes':
            college = 'James Madison'
             
    #To verify if credit is an integer and if it is greater than 0
    credit = input("Credits: ")      #to verify if credit is an integer
    while (not credit.isdigit() or int(credit)<=0):
        print("Invalid input. Try again.")
        credit = input("Credits: ")

    credit = int(credit)
    
  ########################################### tuition calculation begins here ############################################################
  
    if level == 'freshman' :   
        Per_credit = 482
        Flat_Rate = 7230

        if credit <= 11:
            tuition = (Per_credit * credit) + asmsu_tax + fm_radio_tax
            if credit >= 6:
               tuition += state_news_tax
        elif 12 <= credit <= 18:
            tuition = Flat_Rate + asmsu_tax + fm_radio_tax + state_news_tax
        else:
            tuition = Flat_Rate + (credit - 18)* Per_credit + asmsu_tax + fm_radio_tax + state_news_tax

        if college=='James Madison':
            tuition += jmcss_tax
        elif college == 'Engineering':
            if(credit<=4):
                tuition += egr_admit_special1
            else:
                tuition += egr_admit_special2  
                         
    if level == 'sophomore' :  
        Per_credit = 494
        Flat_Rate = 7410

        if credit <= 11:
            tuition = (Per_credit * credit) + asmsu_tax + fm_radio_tax
            if credit >= 6:
                tuition += state_news_tax
        elif 12 <= credit <= 18:
            tuition = Flat_Rate + asmsu_tax + fm_radio_tax + state_news_tax
        else:
            tuition = Flat_Rate + (credit - 18)* Per_credit + asmsu_tax + fm_radio_tax + state_news_tax

        if college=='James Madison':
            tuition += jmcss_tax
        elif college == 'Engineering':
            if(credit<=4):
                tuition += egr_admit_special1
            else:
                tuition += egr_admit_special2  
            

    if (level == 'junior') or (level == 'senior') :   # both junior and senior have common values
        
        if college == 'business':  
            Per_credit = 573
            Flat_Rate = 8595

            if credit <= 11:
                tuition = (Per_credit * credit) + asmsu_tax + fm_radio_tax
                if credit >= 6:
                    tuition += state_news_tax
            elif 12 <= credit <= 18:
                tuition = Flat_Rate + asmsu_tax + fm_radio_tax + state_news_tax
            else:
                tuition = Flat_Rate + (credit - 18)* Per_credit + asmsu_tax + fm_radio_tax + state_news_tax

            if(credit<=4):
                tuition += business_special1
            else:
                tuition += business_special2

        elif college == 'engineering':
            Per_credit = 573
            Flat_Rate = 8595

            if credit <= 11:
                tuition = (Per_credit * credit) + asmsu_tax + fm_radio_tax
                if credit >= 6:
                    tuition += state_news_tax
            elif 12 <= credit <= 18:
                tuition = Flat_Rate + asmsu_tax + fm_radio_tax + state_news_tax
            else:
                tuition = Flat_Rate + (credit - 18)* Per_credit + asmsu_tax + fm_radio_tax + state_news_tax

            if(credit<=4):
                tuition += egr_admit_special1
            else:
                tuition += egr_admit_special2    
                
        elif college == 'health' :  
                Per_credit = 555
                Flat_Rate = 8325

                if credit <= 11:
                    tuition = (Per_credit * credit) + asmsu_tax + fm_radio_tax
                    if credit >= 6:
                        tuition += state_news_tax
                elif 12 <= credit <= 18:
                    tuition = Flat_Rate + asmsu_tax + fm_radio_tax + state_news_tax
                else:
                    tuition = Flat_Rate + (credit - 18)* Per_credit + asmsu_tax + fm_radio_tax + state_news_tax
                     
                if(credit<=4):
                    tuition += health_special1
                else:
                    tuition += health_special2 
                    
        elif college == 'science' : 
                Per_credit = 555
                Flat_Rate = 8325

                if credit <= 11:
                    tuition = (Per_credit * credit) + asmsu_tax + fm_radio_tax
                    if credit >= 6:
                        tuition += state_news_tax
                elif 12 <= credit <= 18:
                    tuition = Flat_Rate + asmsu_tax + fm_radio_tax + state_news_tax
                else:
                    tuition = Flat_Rate + (credit - 18)* Per_credit + asmsu_tax + fm_radio_tax + state_news_tax
                     
                if(credit<=4):
                    tuition += science_special1
                else:
                    tuition += science_special2
        
        else :   # if the college is not specified
            Per_credit = 555
            Flat_Rate = 8325

            if credit <= 11:
                tuition = (Per_credit * credit) + asmsu_tax + fm_radio_tax
                if credit >= 6:
                    tuition += state_news_tax
            elif 12 <= credit <= 18:
                tuition = Flat_Rate + asmsu_tax + fm_radio_tax + state_news_tax
            else:
                tuition = Flat_Rate + (credit - 18)* Per_credit + asmsu_tax + fm_radio_tax + state_news_tax

            if college=='James Madison':
                tuition += jmcss_tax  
                
    
            

    print('Tuition is ${:,.2f}.'.format(tuition))
    
# loop to ask the user if he wants to continue or not
    cont=input('Do you want to do another calculation (yes/no): ').lower()
    if cont != 'yes':
        cont = 'no'
    

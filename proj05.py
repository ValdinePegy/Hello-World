# Computer Project #5

  #  Algorithm
    
  #   Create a function which Prompt the user to input a year, builds a file name 
  
  #  loops until it can correctly open a file

  #   Create a second function to convert a numeric string representing a month into a 3-character string month

  #   Create a third function to determine which day and time had the best surf.

  #   In the main function, call the other functions to perform each calculation

  #   Display the outputs respecting the formatting provided 
    
def open_file():
    ''' 
    This function is used to open a file. A while loop is used to loop
    until the correct input is entered. Try except is used to open the file
    
    Input : year(str)
    
    Returns : fp(str)  # fp is file pointer
    '''
    a = True
    year = input('Input a year: ')
    while a:
        try:
            file_name = 'wave_data_'+year+'.txt' 
            fp = open(file_name, 'r')
            break  # if the correct year is entered, it should stop asking to input a year
        except FileNotFoundError:
            print("File does not exist. Please try again.")
            year = input('Input a year: ') # keep asking the user to input a year until it is correct
          
    return fp 
            
            
def get_month_str(mm):
    ''' 
    This fuction converts a numeric string representing 
    a month into a 3-character string month.
    
    mm : The numeric string(month) to be converted (str)
    
    Returns : The 3-character string of mm (str)
    '''
    if mm == '01':  # mm is the month in numbers
        month = 'Jan'
    elif mm == '02':
        month = 'Feb'
    elif mm == '03':
        month = 'Mar'
    elif mm == '04':
        month = 'Apr'
    elif mm == '05':
        month = 'May'
    elif mm == '06':
        month = 'Jun'
    elif mm == '07':
        month = 'Jul'
    elif mm == '08':
        month = 'Aug'
    elif mm == '09':
        month = 'Sep'
    elif mm == '10':
        month = 'Oct'
    elif mm == '11':
        month = 'Nov'
    elif mm == '12':
        month = 'Dec'
        
    return month
    

def best_surf(mm,dd,hr,WVHT,dpd,best_mm,best_dd,best_hr,best_WVHT,best_dpd):
    ''' 
    This function is to determine which day and time had the best surf.
    
    mm,dd,hr,WVHT,dpd,best_mm,best_dd,best_hr,best_WVHT,best_dpd : The vales
    to be processed(str,str,int,float,float)
    
    Returns : The best month, day,hour,WVHT,and DPD the user surfed
        best_mm,best_dd,best_hr,best_WVHT,best_dpd (str,str,int,float,float)
    '''
    
    if hr <= 6 or hr >= 19 : # At this times, the user is not surfing
        return best_mm,best_dd,best_hr,best_WVHT,best_dpd
    
    else :
        if WVHT > best_WVHT: # If current waves are bigger than best waves,
            best_mm = mm     # all current waves are returned
            best_dd = dd
            best_hr = hr
            best_WVHT = WVHT
            best_dpd = dpd
        if WVHT < best_WVHT :  # If current waves are smaller than best waves,
            best_mm = best_mm  # the best parameters are returned unchanged
            best_dd = best_dd
            best_hr = best_hr
            best_WVHT = best_WVHT
            best_dpd = best_dpd
        if WVHT == best_WVHT :  # if current wave size equal best wave size,
            if dpd > best_dpd :  # dpd is used to determine which one should be returned
                best_mm = mm    # if dpd is greater than best dpd, all current values are returned
                best_dd = dd
                best_hr = hr    
                best_WVHT = WVHT
                best_dpd = dpd
            else :  # if dpd is lesser than best dpd, best parameters are returned unchanged
                best_mm = best_mm
                best_dd = best_dd
                best_hr = best_hr
                best_WVHT = best_WVHT
                best_dpd = best_dpd
                
    return best_mm,best_dd,best_hr,best_WVHT,best_dpd
    
def main():  
    
    print("Wave Data")
    
    #initializations
    
    WVHT_max = 0  # initializing max wave height to a very small value
    WVHT_min = 10**6  # initializing min wave height to a very big value
    total = 0
    count = 0
    best_mm = ''
    best_dd = ''
    best_hr = int(0) # to convert to integer 
    best_WVHT = float(0) # to convert to float 
    best_dpd = float(0) # to convert to float
    
    fp = open_file() # the first function created at the top
    Header1 = fp.readline() # To skip the first header line
    Header2 = fp.readline()  # To skip the second header line
    
    for line in fp:
        
        WVHT = float(line[30:36])
        dpd = float(line[37:42])
        hr = int(line[11:13])
        dd = line[8:10]
        mm = line[5:7]
        
        if WVHT == 99.00 or dpd == 99.00:
            continue
       
        total += WVHT  #total of wave height
        count +=1  # counting the number of wave heights
        
        if WVHT > WVHT_max:
            WVHT_max = WVHT
        if WVHT < WVHT_min:
            WVHT_min = WVHT
         
        mm = get_month_str(mm) # Calling the function to convert the numeric month
        
        # Calling the best_surf function to determine the best parameters
        best_mm, best_dd, best_hr, best_WVHT, best_dpd = best_surf(mm, dd, hr, WVHT, dpd, best_mm, best_dd, best_hr, best_WVHT, best_dpd)
         
    avg_WVHT = total/count 
 
    print('\nWave Height in meters.')
    print("{:7s}: {:4.2f} m".format('average',avg_WVHT))
    print("{:7s}: {:4.2f} m".format('max',WVHT_max))
    print("{:7s}: {:4.2f} m".format('min',WVHT_min))
    print("\nBest Surfing Time:")
    print("{:3s} {:3s} {:2s} {:>6s} {:>6s}".format("MTH","DAY","HR","WVHT","DPD"))
    print("{:3s} {:>3s} {:2d} {:5.2f}m {:5.2f}s".format(best_mm, best_dd, best_hr, best_WVHT, best_dpd))

if __name__ == "__main__": 
    main()

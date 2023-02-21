 # Computer Project #8

  #  Algorithm
  
  #  Create a function which opens a file and prompts an error message if the file does not exist.
 
  #  loops until it can correctly open a file

  #   Create a second function to read through a csv file and also creates
  
  #   a dictionary of list of list.

  #   Create a third function to calculate the diabetes per capita and appending it to the country list.
  
  #   Create a forth function to determine the maximum diabetes per capita in the lists of dictionary
  
  #   Create a fifth function to determine the minimum diabetes per capita in the lists of dictionary

  #   Create a sixth function to display all the data created in the previous functions

  #   In the main function, call the add_per_capitafunction and display function to perform each task .


import csv
from operator import itemgetter

def open_file():
   ''' 
    
    This function is used to open a file. A while loop is used to loop
    until the correct input is entered. Try except is used to open the file
    
    Input : file_name(str)
    
   Returns : fp(str)  # fp is file pointer
  '''
   
   file_name = input("Input a file: ") #file_name is the name of the file
   while True:
       try:
           fp = open(file_name,'r', encoding='utf-8')
           break
       except FileNotFoundError:
           print("Error: file does not exist. Please try again.")
           file_name = input("Input a file: ")
   return fp

def max_in_region(D,region):
   '''
   This function finds the maximum per capita diabetes of a specified region.
   
   Input : D,region (Dictionary of lists)
   
   Returns : A tuple (string, float)
   '''
   max_r = 0 #max_r is an assignment for the maximum value
   for key,value in D.items(): #to iterate through the values
     if key == region: # It checks if yhe key is equal to the region specified
       for ele in value: # if it is equal, it proceeds with the calculations
          if ele[3] > max_r:
               max_r = ele[3]
               country_name = ele[0]
       d = country_name, max_r
   return tuple(d)
    
def min_in_region(D,region):
    '''
    This function finds the minimum per capita diabetes of a specified region.
    
    Input : D,region (Dictionary of lists)
    
    Returns : A tuple (string, float)
    '''
    min_r = 10 #min_r is an assignment for the minimum value
    for key,value in D.items(): #to iterate through the values
      if key == region: # It checks if yhe key is equal to the region specified
        for ele in value: # if it is equal, it proceeds with the calculations
           if ele[3] < min_r and ele[3] != 0: #if the min_r is 0 it should not return it
                min_r = ele[3]
                country_name = ele[0]
        d = country_name, min_r
    return tuple(d)

def read_file(fp):
    ''' Read the file referenced by the parameter. The key of the dictionary is a region and the
    
    value is a list of lists. 
    
    Input: file pointer(fp)
    
    Returns : Dictionary of sorted list of lists
    
    '''
    reader = csv.reader(fp)
    next(reader, None)
    D = {}
    for line in reader:
        region = line[1]
        country = line[2]
        population = line[5].replace(',', '')
        try: # if the population is not empty, it should convert it to a float 
            population = float(line[5].replace(',', ''))
        except: #Else, it should skip the line
            if population == '-':
                    continue
        
        diabetes = float(line[9])
        
        if region not in D:
            D[region] = []
        country_list = [country, diabetes, population]
        
        D[region].append(country_list)
        for i in D:
            D[i].sort()
    return D
            
def add_per_capita(D):
   ''' Calculates the diabetes per capita for each country and region by simply dividing the
   
   diabetes value by the population value. Append the calculated value onto each country's list. 
   
   Input : Dictionary of lists
   
   Returns : Dictionary of lists
   
   '''
   for key,value in D.items():
    for ele in value:
           if ele[2] == 0:
               ele.append('0.0')
           else:
                dpc = ele[1]/ele[2]  #dpc is diabetes per capita
                ele.append(dpc)
   return D

def display_region(D,region):
    '''Display the summary for the regionfollowed by a table with the data for each country.
    
    Input: Dictionary of lists, string
    
    Return: nothing
    
    Displays : Table of region data
    
    '''
    n = D[region] # the dictionary
    add_per_capita(D)
    l = []

    print("Type1 Diabetes Data (in thousands)")
                    
    print("{:<37s} {:>9s} {:>12s} {:>11s}".format("Region","Cases","Population","Per Capita"))
           
    for column in n:
            if column[0] == region:
                print("{:<37s} {:>9.0f} {:>12,.0f} {:>11.5f}".format((column[0]),(column[1]),(column[2]),(column[3])))
                continue
            else:
                l.append(column)
                    
    print()
    l = sorted(l, key = itemgetter(3), reverse = True) # to sort the list
                    
    print("{:<37s} {:>9s} {:>12s} {:>11s}".format("Country","Cases","Population","Per Capita"))
           
    for column in l:
           
           print("{:<37s} {:>9.1f} {:>12,.0f} {:>11.5f}".format(column[0],column[1],column[2],column[3]))
                
            
    
    max_dpc = max_in_region(D, region)  
    print("\nMaximum per-capita in the {} region".format(region))
    print("{:<37s} {:>11s}".format("Country","Per Capita"))
    print("{:<37s} {:>11.5f}".format(*max_dpc))
    
    min_dpc = min_in_region(D, region)  
    print("\nMinimum per-capita in the {} region".format(region))
    print("{:<37s} {:>11s}".format("Country","Per Capita"))
    print("{:<37s} {:>11.5f}".format(*min_dpc))
    
def main():
    fp = open_file()
    D = read_file(fp) 
    add_per_capita(D)
    
    #print("Type1 Diabetes Data (in thousands)")
    for column in D:
        region = column
        h = display_region(D,region)
        print("-"*72)
    
    
    print('\n Thanks for using this program!\nHave a good day!')
# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == "__main__": 
    main()

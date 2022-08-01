 # Computer Project #7 

  #  Algorithm
  
  #  Create a function which opens a file and prompts an error message if the file does not exist.
 
  #  loops until it can correctly open a file

  #   Create a second function to create a list of country names by reading the file and also creating
  
  #   a list of regimes if a country is not yet in the list of country names.

  #   Create a third function to determine which regime system was most dominant in each country.
  
  #   Create a forth function to determine which countries are allies based on the regimes of each.
  
  #   Create a fifth function to determine which country has the most changes in its regime system.

  #   In the main function, call the other functions to perform each task while checking for error in inputs.

  #   Display the outputs respecting the formatting provided 
 

import csv
from operator import itemgetter
from collections import Counter

REGIME=["Closed autocracy","Electoral autocracy","Electoral democracy","Liberal democracy"]
MENU='''\nRegime Options:
            (1) Display regime history
            (2) Display allies
            (3) Display chaotic regimes        
    '''

def open_file():
    ''' 
    
    This function is used to open a file. A while loop is used to loop
    until the correct input is entered. Try except is used to open the file
    
    Input : f_name(str)
    
    Returns : fp(str)  # fp is file pointer
    '''
    
    file_name = input("Enter a file: ") #file_name is the name of the file
    while True:
        try:
            fp = open(file_name,'r')
            break
        except FileNotFoundError:
            print("File not found. Please try again.")
            file_name = input("Enter a file: ")
    return fp

def read_file(fp):
    ''' 
    This function reads a file in csv format while skipping the header line.
    The function creates a list of country names and a list of regimes in each country
    
    Input : file pointer(fp) (str)
    
    Returns : country_names, list_of_regime_lists (list of str,list of list of ints)
    
    '''
    reader = csv.reader(fp)
    next(reader, None) #To skip the header
    list_of_regime_lists = []
    country_names = []
    political_list = []
    for line in reader :
        country = line[1] 
        regime = int(line[4])
        if country in country_names:  #if the country_name is already in the list
            political_list.append(regime) #put the regime in the political list
        else:
            political_list = [] #if the country is not yet in the country_name it should
            political_list.append(regime) #create an empty new list and append the regimes to it
            list_of_regime_lists.append(political_list) #append the new lists to a master list
            country_names.append(country)
    return country_names, list_of_regime_lists
      

def history_of_country(country,country_names,list_of_regime_lists):
    ''' 
    This function figures out the dominant regime in a country by using the lists
    we created.
    
    Input: country, country_names, list_of_regime_lists(str, list of str, list of list of ints)
    
    Returns : REGIME at index (str)
    
    '''
    
    idx_lst = [] #inititializing list to store indexes of most appearing regimes
    n = list(Counter(list_of_regime_lists[country_names.index(country)]).keys())
    m = list(Counter(list_of_regime_lists[country_names.index(country)]).values()) 
    e = zip(n,m) #pairing up the indexes of each regime with its count
    mx = max(m)
        
    for idx, count in e:
        if (count == mx):
            idx_lst.append(idx)
            
    if (len(idx_lst) == 1): #creating condition for if only one regime has highest count
        index = idx_lst[0]
        
    else: #if more than one regime has highest count,the index for REGIME will be the minimum in idx_lst
        index = min(idx_lst) 
    return REGIME[index]   
    
def historical_allies(regime,country_names,list_of_regime_lists):
    ''' 
    This function figures out which countries are historical allies based on their regime
    systems. If they have thesame regime, then they are historical allies.
    
    Input: regime, country_names,list_of_regime_lists (str, list of str, list of lists of ints)
    
    Returns : Allies (list of str)
        
    '''
    
    Allies = []
    for country in country_names:
        if regime == history_of_country(country, country_names, list_of_regime_lists):
            Allies.append(country) #append countries that have the same regimes in a list
    return Allies
    

def top_coup_detat_count(top, country_names,list_of_regime_lists):          
    ''' 
    This function figures out which countries had the most coups in their history.
    
    Input: top, country_names, list_of_regime_lists(int, list of str, list of lists of ints)
    
    Returns: Sorted list of tuples
    '''
    L = []
    for i in range(len(country_names)):
        Count = 0
        for j in range(1,len(list_of_regime_lists[i])): #since the length of list_of_regime_lists at i
        #is the same as that of the length of country_names
            if list_of_regime_lists[i][j] != list_of_regime_lists[i][j-1]: #if the value in the list is not
            #equal to the previous value, the count should increment, else it should stay the same
                Count += 1
        L.append((country_names[i],Count))
        L = sorted(L, key = itemgetter(1), reverse = True)
    c = 0
    returnL = [] # new list containing the number of countries requested
    for i in L :
        c+= 1
        returnL.append(i)
        if c == top :
            break
    return returnL #return the number of countries asked in a sorted order
        
    
def main():
    # by convention "main" doesn't need a docstring
    fp = open_file()
    b = read_file(fp) 
    country_names, list_of_regime_lists = b
    
    while True:
       print(MENU)
        
       prompt= input("Input an option (Q to quit): ").lower()
       while not(prompt == '1' or prompt == '2' or prompt == '3' or prompt == 'q'):
               print("Invalid choice. Please try again.")
               prompt= input("Input an option (Q to quit): ").lower()
       if prompt == '1': # if the prompt is 1, it should ask the user to enter a 
       # country and print the regime of the country. It checks until the correct
       # country is entered fist.
    
            country = input("Enter a country: ")
            while country not in country_names:
                    print("Invalid country. Please try again.")
                    country = input("Enter a country: ")
            regime = history_of_country(country, country_names, list_of_regime_lists)             
            if regime == 'Electoral autocracy' or regime == 'Electoral democracy':
                  print("\nHistorically {} has mostly been an {}".format(country, regime))
            else:
                  print("\nHistorically {} has mostly been a {}".format(country, regime))
                  
       elif prompt == '2': # if the prompt is 2, it should ask the user to enter
       # a regime and print the countries which are allies. It checks until the
       # correct regime is entered first
          
            p_regime = input("Enter a regime: ")
            while p_regime not in REGIME:
                print("Invalid regime. Please try again.")
                p_regime = input("Enter a regime: ")
            a = historical_allies(p_regime,country_names,list_of_regime_lists)
            a_str = ', '.join(item for item in a)    
            print("\nHistorically these countries are allies of type:" ,p_regime)
            print(a_str)
           
       elif prompt == '3': # if the prompt is 3, it should ask the user to enter
       # the number to display and print the number of coups the country had. It checks
       #  until the correct number is entered first
       
           top = input("Enter how many to display: ")
           if top.isdigit() is True:
               top = int(top)
               while top < 0:
                   print("Invalid number. Please try again.")
                   top = int(input("Enter how many to display: "))
           else :
               print("Invalid number. Please try again.")
               top = int(input("Enter how many to display: "))
           b = top_coup_detat_count(top, country_names,list_of_regime_lists)
           print("\n{: >25s} {: >8s}".format('Country','Changes'))
           for a, b in b:
               print("{: >25s} {: >8d}".format(a,b))
           
       elif prompt == 'q': # if the user enters q, the program ends
               print("The end.")
               break
   
# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == "__main__": 
    main() 

 # Computer Project #9

  #  Algorithm
  
  #  Create a function which prompts the user for an option and return an error message if an
  
  #  invalid option is entered
  
  #  Create another function which opens a file and prompts an error message if the file does not exist.
 
  #  loops until it can correctly open a file

  #   Create a third function to read through a json file and also creates a dictionary of dictionaries.

  #   Create a forth through a text file and create a dictionary.
  
  #   Create a fifth function which creates a set of the categories used in the 2 read functions.
  
  #   Create a sixth function which creates a mapping of each category to the list of images that 
  
  #   has an instance of that category.

  #   Create a seventh function to find the most occurences of an object across all images.
  
  #   Create an eighth function to find the most images that an object appears in.
  
  #   Create a nineth function that counts the occurences of words in captions. The captions come
  
  #   from the D_annot.

  #   In the main function, call the other functions and display function to perform each task in a loop.
  
import json,string
from operator import itemgetter

STOP_WORDS = ['a','an','the','in','on','of','is','was','am','I','me','you','and','or','not','this','that','to','with','his','hers','out','it','as','by','are','he','her','at','its']

MENU = '''
    Select from the menu:
        c: display categories
        f: find images by category
        i: find max instances of categories
        m: find max number of images of categories
        w: display the top ten words in captions
        q: quit
        
    Choice: '''

def get_option():
   '''
   
   This function is used to prompt the user for a valid option.
   If an invalid option is input, an error message is displayed.
   
   Input : An option (str)
   
   Returns : The PROMPT (str)
   
   '''
   OPTIONS = input(MENU).lower()
   if OPTIONS == 'c' or OPTIONS == 'f' or OPTIONS == 'i' or OPTIONS == 'm' or OPTIONS == 'w' or OPTIONS == 'q' :
       pass
   while not(OPTIONS == 'c' or OPTIONS == 'f' or OPTIONS == 'i' or OPTIONS == 'm' or OPTIONS == 'w' or OPTIONS == 'q'):
       print("Incorrect choice.  Please try again.")
       OPTIONS = input(MENU).lower() #keep prompting until a valid option is entered
   return OPTIONS
    
def open_file(s):
   ''' 
    
    This function is used to open a file. A while loop is used to loop
    until the correct input is entered. Try except is used to open the file
    
    Input : file_name(str)
    
   Returns : fp(str)  # fp is file pointer
   
  '''
   file_name = input("Enter a {} file name: ".format(s))
   while True:
       try:
           fp = open(file_name,'r')
           break
       except FileNotFoundError:
           print('\nInvalid file name; please try again.\n')
           file_name = input("Enter a {} file name: ".format(s)) # keep asking the user to input a file_name until it is correct
   return fp
        
def read_annot_file(fp1):
    
   '''
    
   This function reads a json file referenced by the fp1 parameter.
   
   Input: file pointer
   
   Returns: Dictionary of dictionaries
   
   '''
   
   D_annot = json.load(fp1)
   
   return D_annot

def read_category_file(fp2):
    
   '''
    
   This function creates a dictionary whose key is an int and whose 
   value is a string. It creates the dictionary from a text file where 
   each line is space separated.
   
   Input: file pointer
   
   Returns: dictionary
   
   '''
   
   D_cat = {}
   for line in fp2:
        a = line.strip().split()
        s = a[0]
        a.pop(0)  #After this step, 'a' is updated and does not contain the first value
        D_cat[int(s)] = str(a[0]) #key is an int and value is the string at the the 
        #first index when the previous first index has been removed
                   
   return D_cat
   

def collect_catogory_set(D_annot,D_cat):
    
   ''' 
   
   This function creates a set of the names of elements in the 
   'bbox_category_level' by making use of the D_annot and D_cat
   from the read_annot_file and read_category_file respectively 
   
   Input : Dictionary of dictionaries, dictionary
   
   Returns: set of strings'''
   
   cat_set = set() 
   
   for item in D_annot:
       b = D_annot[item]
       category = b['bbox_category_label']
       for i in category :
           name = D_cat[i]
           cat_set.add(name) # A set containing the category name for each 'bbox_category_label' list

   return cat_set 
   

def collect_img_list_for_categories(D_annot,D_cat,cat_set):
   ''' 
   
   This function creates a mapping of eachh category to the list of
   images that has an instance of that category.
   
   Input: dictionary of dictionaries, dictionary, set of strings
   
   Returns: D_image (Dictionary of sorted lists)
   
   '''  
   
   D_image = {}
   
   for item in D_annot:
       b = D_annot[item]
       category = b['bbox_category_label']
       for i in category :
           name = D_cat[i]
           if name in D_image.keys():
               cat_set = D_image[name]
               cat_set.append(item)
               cat_set.sort()
           if name not in D_image.keys():
               cat_set = [item]
               D_image[name] = cat_set
         
   return D_image
       
def max_instances_for_item(D_image):
   ''' 
   
   This function finds the maximum occurences of an object  across 
   all images.
   
   Input : Dictionary of sorted lists
   
   Returns: tuple
   
   '''
   
   max_i = 0
   for i in D_image:
       a = len(D_image[i])
       if a > max_i:
           max_i = a #max_i is maximum instance
           max_o = i #max_o is maximum object
   d =  max_i, max_o
   return tuple(d)

def max_images_for_item(D_image):
   ''' 
   
   This function finds the most images that an object(category) appears in.
   
   Input: Dictionary of sorted lists
   
   Returns: tuple
   
   '''
   
   max_i = 0
   for i in D_image:
       u = list(set(D_image[i]))  # convert to a set so that each value will only appear once
       a = len(u)
       if a > max_i:
           max_i = a
           max_o = i
   d = max_i, max_o
   return tuple(d)

def count_words(D_annot):
   ''' 
   
   This function counts the occurences of words in captions. 
   
   Input: D_annot (Dictionary of dictionaries)
   
   Returns: List of tuples
   
   '''
   
   D = {}
   for item in D_annot:
       c = D_annot[item]['cap_list']
       for i in c:
           liste = i.split(' ') 
           for word in liste: 
               word = word.strip('.')
               if word in STOP_WORDS:
                   continue
               if word in D:
                       D[word] += 1
               else:
                       D[word] = 1
                       
   count_l = [(v,k) for k, v in D.items()] # count_l is the final list of tuple
   count_l.sort(key = itemgetter(0,1), reverse = True) # sorted list of tuple
                    
   return count_l
                   
               
def main():    
    print("Images\n")
    fp1 = open_file("JSON image")
    
    fp2 = open_file("Category")
   
    D_annot = read_annot_file(fp1)
    D_cat = read_category_file(fp2)
    
    
    OPTION = get_option()
    while True:
        while not(OPTION == 'q'):
            if OPTION == 'c' :
                
                c = collect_catogory_set(D_annot,D_cat)
                category_l = list(c)
                category_l.sort()
                category_name = ', '.join([str(elem) for elem in category_l])
                print("\nCategories: ") 
                print(category_name)
                
            
        
            if OPTION == 'f' :
                final_ele = ''
                print("\nCategories: ") 
                print(category_name)
                a = input("Choose a category from the list above: ").lower()
                while a not in category_name:
                    print("Incorrect category choice.")
                    a = input("Choose a category from the list above: ").lower()
                
                L = []
                D_image = collect_img_list_for_categories(D_annot, D_cat, c)
                for item in D_image[a]:
                   L.append(int(item))
                L.sort()
                for ele in L:
                    ele = str(ele)
                    final_ele += (ele + ',')
                final_ele = final_ele.strip(',')
        
                print("\nThe category {} appears in the following images:".format(a))
                print(final_ele)
                
            if OPTION == 'i':
               d = max_instances_for_item(D_image)
               print("\nMax instances: the category {} appears {} times in images.".format(d[1],d[0]))
               
            if OPTION == 'm':
                d = max_images_for_item(D_image)
                print("\nMax images: the category {} appears in {} images.".format(d[1],d[0]))
                
            if OPTION == 'w':
                count_word = count_words(D_annot)
                num = int(input("\nEnter number of desired words: "))
                while num < 0:
                    num = input("Error: input must be a positive integer: ")
                    num = int(num)
                print("\nTop {} words in captions.".format(num))
                print("{:<14s}{:>6s}".format("word","count"))
                for i in range(num):
                    x = count_word[i]
                    print("{:<14s}{:>6d}".format(x[1],x[0]))
            
            OPTION = get_option()
        print("\nThank you for running my code.") 
        break
        
        
# Calls main() if this modules is called by name
if __name__ == "__main__":
    main()     

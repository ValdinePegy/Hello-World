# Reading a csv file and working on christmas songs


import csv
from operator import itemgetter

# Keywords used to find christmas songs in get_christmas_songs()
CHRISTMAS_WORDS = ['christmas', 'navidad', 'jingle', 'sleigh', 'snow',\
                   'wonderful time', 'santa', 'reindeer']

# Titles of the columns of the csv file. used in print_data()
TITLES = ['Song', 'Artist', 'Rank', 'Last Week', 'Peak Rank', 'Weeks On']

# ranking parameters -- listed here for easy manipulation
A,B,C,D = 1.5, -5, 5, 3

#The options that should be displayed
OPTIONS = "\nOptions:\n\t\
        a - display Christmas songs\n\t\
        b - display songs by peak rank\n\t\
        c - display songs by weeks on the charts\n\t\
        d - display scores by calculated rank\n\t\
        q - terminate the program \n"

#the prompt to ask the user for an option
PROMPT = "Enter one of the listed options: "

def get_option():
    '''
    This function is used to prompt the user for a valid option.
    If an invalid option is input, an error message is displayed.
    
    Input : An option (str)
    
    Returns : The PROMPT (str)
    '''
    PROMPT = input("Enter one of the listed options: ").lower()
    if PROMPT == 'a' or PROMPT == 'b' or PROMPT == 'c' or PROMPT == 'd' or PROMPT == 'q' :
        pass
    while not(PROMPT == 'a' or PROMPT == 'b' or PROMPT == 'c' or PROMPT == 'd' or PROMPT == 'q'):
        print('Invalid option!\nTry again')
        PROMPT = input("Enter one of the listed options: ").lower() #keep prompting until a valid option is entered
    return PROMPT
    

def open_file():
    '''
    This function is used to open a file. It continues to prompt
    a filename until a correct one is entered. Try except is used to open the file
    
    Input : file_name (str)
    
    Returns : fp(str)  # fp is file pointer
    '''
    a = True
    file_name = input("Enter a file name: ")
    while a :
        try:
            fp = open(file_name,'r')
            break # if the correct file_name is entered, it should stop asking to input a year
        except FileNotFoundError:
            print('\nInvalid file name; please try again.\n')
            file_name = input(" Enter a file name: ") # keep asking the user to input a file_name until it is correct
    return fp

def read_file(fp):
    '''
    This function usees the csv module's reader method to read the 
    file referenced by the parameter. It puts each song's information
    (each line in the file is a song) into a list and append that list
    to a master list. It uses try except to check is the file entry is 
    not a valid integer.
    
    Input : file pointer (str)
    
    Returns : master_list (list of lists)
    '''
    master_list =[]
    reader = csv.reader(fp)
    next(reader,None)
    for line in reader :
        if len(line)!=6:  # In case the length is longer than 6, it is erroneous
            line = line[0:6]  # slice the line to have only 6 columns
            for i in range(2,6):
                if line[i].isdigit():
                    line[i] = int(line[i])
                else:  # If the entry is not a digit, it should replace it with -1
                    line[i]=-1
            master_list.append(line)
        else:
            for i in range(2,6):
                try:
                    line[i]= int(line[i])
                except:
                    line[i] = -1
    
            master_list.append(line)
        
    return master_list

def print_data(song_list):
    '''
    This function is provided to you. Do not change it
    It Prints a list of song lists.
    '''
    if not song_list:
        print("\nSong list is empty -- nothing to print.")
        return
    # String that the data will be formatted to. allocates space
    # and alignment of text
    format_string = "{:>3d}. "+"{:<45.40s} {:<20.18s} "+"{:>11d} "*4
    
    # Prints an empty line and the header formatted as the entries will be
    print()
    print(" "*5 + ("{:<45.40s} {:<20.18s} "+"{:>11.9s} "*4+'\n'+'-'*120).format(*TITLES))

    # Prints the formatted contents of every entry
    for i, sublist in enumerate(song_list, 1):
        #print(i,sublist)
        print(format_string.format(i, *sublist).replace('-1', '- '))

def get_christmas_songs(master_list):
    '''
    This function selects chritmas songs from the master list and places
    the songs in a new list. Selection is based on whether the song title
    has any of the CHRISTMAS_WORDS(given in the beginning) in it. It then
    sorts the list alphabetically by song titles.
    
    Input : master_list (list of lists)
    
    Returns : A new list made of christmas songs (list of lists)
    '''
    new_list = []  # list of christmas songs
    a_sort = sorted(master_list)   #a_sort is the sorted list in alphabetic order
    for i in a_sort:
        song_t = i[0].lower()  #song_t is the song's title
        for words in CHRISTMAS_WORDS:
            if words in song_t:
                new_list.append(i)
    return new_list
            
def sort_by_peak(master_list):
    '''
    This function returns a sorted version of the master_list based 
    on peak_rank without modifying the original list. It does not 
    include a song if its peak rank value is -1.
    
    Input : master_list (list of lists)
    
    Returns: sorted master_list (list of lists)
    '''
    peak_sort = sorted(master_list,key=itemgetter(4))
    for line in master_list:
       if line[4]== -1:
            peak_sort.remove(line)
    peak_sortl = [] #peak_sortl is the sorted master_list based on peak_rank
    for line in peak_sort:
        peak_sortl.append(line)
    return peak_sortl
   
def sort_by_weeks_on_list(master_list):
    '''
    This function returns a sorted version of the master_list based 
    on weeks on the top 100 without modifying the original list. It does not
    include a song if its weeks on the list value is -1.
    
    Input : master_list (list of lists)
    
    Returns: sorted master_list (list of lists)
    '''
    weeks_sort = sorted(master_list, key=itemgetter(5),reverse = True)
    for line in master_list:
        if line[5]== -1:
           weeks_sort.remove(line)
    weeks_sortl = [] #weeks_sortl is the sorted master_list based on weeks on
    for line in weeks_sort:
        weeks_sortl.append(line)
    return weeks_sortl

def song_score(song):
    '''
    This function calculates the song score for each song based
    on a formula given. The song is each line in the file/master_list
    
    Input = song (list)
    
    Returns : A float value
    '''
    rank = song[2] 
    curr_rank = 100 - rank
    if rank == -1:
        curr_rank = -100 # if rank is -1, current rank should be -100
        
    peak = song[4]
    peak_rank = 100 - peak
    if peak == -1:
        peak_rank = -100 # if peak is -1, peak rank should be -100
        
    rank_delta = song[2] - song[3]  # last_week = song[3]
    
    weeks_on_chart = song[5] # weeks_on = song[5]
    
    score = A * peak_rank + B * rank_delta + C*weeks_on_chart + D*curr_rank
    return score 

def sort_by_score(master_list):

    '''This function sorts the master_list in descending order based on the score 
    song returned by the song_score function. If there is a tie, the list is sorted based 
    on the song's name in reverse order
    
    Input : master_list (list of lists)
    
    Returns: list of lists
    
    '''
    score_l = []  # score_l is score list
    for song in master_list:
        score = song_score(song)
        song.append(score)
        score_l.append(song)
 
    score_l = sorted(score_l, key = lambda x: (x[6], x[0]),reverse = True)

    score_lnew = [] #score_lnew is the new song list after sorting
    
    for line in score_l:
        line.pop()  # remove the last value in the list
        score_lnew.append(line)  
        
    return score_lnew


def main():

    print("\nBillboard Top 100\n")
    fp = open_file()
    
    L = read_file(fp) # L is master_list
    
    a = print_data(L)  
    
    b = get_christmas_songs(L) 
    
    c = sort_by_weeks_on_list(L)
    
    p = sort_by_peak(L)
    
    e = sort_by_score(L)
    
    while True : # loop to get options
    
        print(OPTIONS)
        PROMPT = get_option()
        if PROMPT == 'a':
            print_data(b)
            christmas_percent = int((len(b)/len(L))* 100)  # To calculate the percentage of christmas songs 
            
            if christmas_percent == 0:
                print('None of the top 100 songs are Christmas songs.')
            else :
                print('\n{:d}% of the top 100 songs are Christmas songs.'.format(christmas_percent))
        elif PROMPT == 'b':
            print_data(p)
            
        elif PROMPT == 'c':
            print_data(c)
            
        elif PROMPT == 'd':
            print_data(e)
            
        elif PROMPT == 'q':
            print("\nThanks for using this program!\nHave a good day!\n")
            break # Stop when prompt answer is q
        
# Calls main() if this modules is called by name
if __name__ == "__main__":
    main()           


 # Computer Project #10

  #  Algorithm
  
  #  Create a function initialize which creates and initializes the tableau and foundation, and returns a tuple
  
  #  A display function is already given.
  
  #  Create another function valid tableau to tableau which checks if a move from one tableau to the other is valid
 
  #  The function returns a boolean either True or False

  #   Create another function valid tableau to foundation which checks if a move from a tableau to the foundation is valid
  
  #  The function returns a boolean either True or False
  
  #   Create another function valid foundation to tableau which checks if a move from the foundation to a tableau is valid
  
  #  The function returns a boolean either True or False
  
  #   Create another function move tableau to tableau which moves a card from one tableau to the other 
  
  #   Create another function move tableau to foundation which moves a card from one tableau to the foundation 
  
  #   Create another function move foundation to tableau which moves a card from the foundation  to one tableau

  #   Create another function check for win which returns a boolean in case the game was won 
  
  #   Create another function get option which prompts the user for an option and check that the input supplied by the user 
  
  #   is of the form requested in the menu.

  #   In the main function, call the other functions and display function to perform each task.
  
#DO NOT DELETE THESE LINES
import cards, random
random.seed(100) #random number generator will always generate 
                 #the same 'random' number (needed to replicate tests)

MENU = '''     
Input options:
    MTT s d: Move card from Tableau pile s to Tableau pile d.
    MTF s d: Move card from Tableau pile s to Foundation d.
    MFT s d: Move card from Foundation s to Tableau pile d.
    U: Undo the last valid move.
    R: Restart the game (after shuffling)
    H: Display this menu of choices
    Q: Quit the game       
'''


the_deck = cards.Deck()
the_deck.shuffle()
               
def initialize():
    '''This function has no parameters. Thefunction creates and initializes 
    the tableau and foundation and returns them as a tuple, in that order. '''
    
    foundation = [[] for i in range(4)]
    tableau = [[] for i in range(8)] #print the empty list the number of times requested
    for i,ch in enumerate(tableau):
        if i%2 == 0: # if it is even it has 7 cards
            for ele in range(7):
                tableau[i].append(the_deck.deal())
        else: # if it is odd it has 6 cards
            for ele in range(6):
                tableau[i].append(the_deck.deal())
            
    return (tableau,foundation)

def display(tableau, foundation):
    '''Each row of the display will have
       tableau - foundation - tableau
       Initially, even indexed tableaus have 7 cards; odds 6.
       The challenge is the get the left vertical bars
       to line up no matter the lengths of the even indexed piles.'''
    
    # To get the left bars to line up we need to
    # find the length of the longest even-indexed tableau list,
    #     i.e. those in the first, leftmost column
    # The "4*" accounts for a card plus 1 space having a width of 4
    max_tab = 4*max([len(lst) for i,lst in enumerate(tableau) if i%2==0])
    # display header
    print("{1:>{0}s} | {2} | {3}".format(max_tab+2,"Tableau","Foundation","Tableau"))
    # display tableau | foundation | tableau
    for i in range(4):
        left_lst = tableau[2*i] # even index
        right_lst = tableau[2*i + 1] # odd index
        # first build a string so we can format the even-index pile
        s = ''
        s += "{}: ".format(2*i)  # index
        for c in left_lst:  # cards in even-indexed pile
            s += "{} ".format(c)
        # display the even-indexed cards; the "+3" is for the index, colon and space
        # the "{1:<{0}s}" format allows us to incorporate the max_tab as the width
        # so the first vertical-bar lines up
        print("{1:<{0}s}".format(max_tab+3,s),end='')
        # next print the foundation
        # get foundation value or space if empty
        found = str(foundation[i][-1]) if foundation[i] else ' '
        print("|{:^12s}|".format(found),end="")
        # print the odd-indexed pile
        print("{:d}: ".format(2*i+1),end="") 
        for c in right_lst:
            print("{} ".format(c),end="") 
        print()  # end of line
    print()
    print("-"*80)
          
def valid_tableau_to_tableau(tableau,s,d): 
    '''This function has three parameters. It checks whether a move
    is valid from one tableau to another. It returns a boolean 
    value ( True or False). '''

    if len(tableau[s]) == 0: # checks if the source is empty
        return False
    
    if len(tableau[d]) == 0: # checks if the destination is empty
        return True
    
    for ele in tableau[s]:
        a = ele.rank()
        
    for i in tableau[d]:
        b = i.rank()
        
    if b-a == 1 : # checks if the destination is one larger in rank than the source
        return True
    else:
        return False
    
    
def move_tableau_to_tableau(tableau,s,d):
    '''This function has three parameters. If the move is valid, determined
    by calling the validate function, the function will update the data structure
    and return True, otherwise it does nothing and returns False. '''
    
    if valid_tableau_to_tableau(tableau, s, d) == True:
        a = tableau[s].pop()
        tableau[d].append(a) #append the last element of the source to the destination
        
        return True
    else:
        return False
        
def valid_foundation_to_tableau(tableau,foundation,s,d):
    '''This function has four parameters. It checks whether a move
    is valid from the foundation to one tableau. It returns a boolean 
    value ( True or False). '''
    
    if len(foundation[s]) == 0:
        return False
    
    if len(tableau[d]) == 0:
        return  True
        
    try:      # try except is used to account for the errors raised 
        s_last = foundation[s][-1] 
    except:
        return False
    
    d_last = tableau[d][-1]
    
    try:
        if d_last.rank() - s_last.rank() == 1: # to check if the destination is one rank
            return True # larger than the source
        else:
            return False
    except:
        return False

def move_foundation_to_tableau(tableau,foundation,s,d):
    '''This function has four parameters. If the move is valid, determined
    by calling the validate function, the function will update the data structure
    and return True, otherwise it does nothing and returns False. '''
    
    if valid_foundation_to_tableau(tableau, foundation, s, d) == True:
        a = foundation[s].pop()
        tableau[d].append(a)
        return True
    else:
        return False
    
def valid_tableau_to_foundation(tableau,foundation,s,d):
    '''This function has four parameters. It checks whether a move
    is valid from one tableau to the foundation. It returns a boolean 
    value ( True or False). '''
    
    
    try:
        
        if cards.Card.rank(tableau[s][-1]) == 1 : # checks if last element of source is an ace
            if len(foundation[d]) == 0: # checks if foundation is empty
                return True
            
        elif cards.Card.suit(tableau[s][-1]) == cards.Card.suit(foundation[d][-1]) and \
        cards.Card.rank(tableau[s][-1]) - cards.Card.rank(foundation[d][-1]) == 1:
            return True # if the cards are of the same suits and destination rank one 
        # lower than source
           
        else:
            return False
        
    except:
        return False
    
    
def move_tableau_to_foundation(tableau, foundation, s,d):
    '''This function has four parameters. If the move is valid, determined
    by calling the validate function, the function will update the data structure
    and return True, otherwise it does nothing and returns False. '''
    
    if valid_tableau_to_foundation(tableau, foundation, s, d) == True:
        a = tableau[s].pop() 
        foundation[d].append(a) # append last element of source to tableau        
        return True
    else:
        return False

def check_for_win(foundation):
    '''This function checks to see if the foundation is full. If it is, it 
    returns True, else it returns False.'''
    
    try:
        for i in foundation:
            a = i.pop() # this is the last element in the foundation
            if a.rank() ==13: # if its rank is 13, then the foundation is full
                return True
            else:
                return False
    except IndexError:
        return False

def get_option():
    '''This function prompts the user for an option and checks that
    the input supplied by the user is of the form requested in the menu.
    If the input is not of the required form, the function prints an error
    message and returns None. Else, it returns the input.'''
    
    Options = ['MTT','MTF','MFT','U','R','H','Q']
    
    List_Opt  = input("\nInput an option (MTT,MTF,MFT,U,R,H,Q): " ).upper()
    
    List_Opt = List_Opt .split(' ')
    
    
    if len(List_Opt) > 3:
        print("Error in Option:")
        return None
    
    if List_Opt[0] not in Options : #checks if the input is not ofthe valid form
        print("Error in Option:")
        return None
    
    else: #if the input is amongst the options
        
       if len(List_Opt) == 3:
            
                s = int(List_Opt[1])
                d = int(List_Opt[2])
                
                List_Opt = [List_Opt[0], s, d]
                
                if List_Opt[0] == 'MFT':
                   if List_Opt[1] not in range(4): # it checks that the input is found in this interval
                       print("Error in Source.")
                       return None
                   
                   if List_Opt[2] not in range(8):
                           print("Error in Destination")
                           return None
                
                   else: # if the input is valid
                       List_Opt = [List_Opt[0], s, d]
                       return List_Opt
                   
                       
                elif List_Opt[0] == 'MTT':
                    if List_Opt[1] not in range(8):
                        print("Error in Source.")
                        return None
                    
                    if List_Opt[2] not in range(8):
                            print("Error in Destination")
                            return None
                        
                    else: # if the input is valid
                        List_Opt = [List_Opt[0], s, d]
                        return List_Opt
                        
                elif List_Opt[0] == 'MTF':
                    if List_Opt[1] not in range(8):
                        print("Error in Source.")
                        return None
                    
                    if List_Opt[2] not in range(4):
                            print("Error in Destination")
                            return None
                        
                    else: # if the input is valid
                        List_Opt = [List_Opt[0], s, d]
                        return List_Opt
         
       else: # if the input is valid but not amongst mtt s d, mtf s d, mft s d
            return List_Opt
                
  
    
def main():  
    
    print("\nWelcome to Streets and Alleys Solitaire.\n")
    
    tableau,foundation = initialize() # initializing the tableau
    display(tableau, foundation)
    
    print(MENU)
    
    val_moves = [] # list of valid moves 
    
    List_Opt = get_option()
    
    while List_Opt == None:
        List_Opt = get_option() # it should keep doing this until the output is not more None
        
    cat_move = List_Opt[0] #cat_move is category of moves
    
    while cat_move != 'Q':
        if len(List_Opt) == 3:
            
            s = int(List_Opt[1])
            d = int(List_Opt[2])
        
        if cat_move == 'MTT':
            a = move_tableau_to_tableau(tableau, s, d)
            # we don't need to check for win when we move from foundation to move
            if a == True:
                val_moves.append(List_Opt) #append valid move to a list
                display(tableau, foundation)
                        
            else: # if the move was a failure
                print("Error in move: {} , {} , {}".format(cat_move,s,d))   
                
                
        
        if cat_move == 'MTF':
            a = move_tableau_to_foundation(tableau, foundation, s, d)
            
            if a == True:
                val_moves.append(List_Opt)
                b = check_for_win(foundation)
                if b == True:  #if the user won
                    print("You won!\n")
                    
                    display(tableau, foundation)
                    print("\n- - - - New Game. - - - -\n")
                    
                    #tableau,foundation = initialize() # initializing the tableau
                    display(tableau, foundation)
                    print(MENU)
                    
                else: #if the user did not win but the move was successful
                        display(tableau, foundation)
                        
            else : # if the move was a failure
                    print("Error in move: {} , {} , {}".format(cat_move,s,d))    
                    
                    
        if cat_move == 'MFT':
            a = move_foundation_to_tableau(tableau, foundation, s, d)
            # we don't need to check for win when we move from foundation to move
            if a == True:
                val_moves.append(List_Opt)
                display(tableau, foundation)
                        
            else: # if the move was a failure
                print("Error in move: {} , {} , {}".format(cat_move,s,d))    
                                  
        if cat_move == 'U':
            if len(val_moves) == 0: # if the length is 0 that means the list is empty i.e no moves
                print("No moves to undo.")
            else:
                c = val_moves.pop() # takes the last valid move 
                d = ' '.join(map(str, c)) # convert to a string
                print("Undo:",d)                
                display(tableau, foundation)
                     
                
        if cat_move == 'R':
            the_deck.shuffle()
            tableau,foundation = initialize() # initializing the tableau
            display(tableau, foundation)
       
        
        if cat_move == 'H':
            print(MENU)
    
    
        List_Opt = get_option()
        while List_Opt == None:
            List_Opt = get_option() # it should keep doing this until the output is not more None
            
        cat_move = List_Opt[0] #cat_move is category of moves
        
        
    else:
        print("Thank you for playing.")
        
    
if __name__ == '__main__':
     main()

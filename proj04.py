# Computer Project #4

    #  Algorithm
    
    #    prompt the user to choose an option between Z,C, and Q

    #    Each option has a particular function which is performed on it

    #    loop while not q

    #    call function in each option to perform each calculation

    #    output the result of the function

    #    Ask again the prompt and perform the calculations
    
    #   Stop when q is entered at the prompt

    #    display closing message

PROMPT = "Enter Z for Zeta, C for Conway, Q to quit: "

def int_to_base13(n):
    """

    Convert an integer to base 13

    n: The value to be processed (int)

    Returns:  The base 13 of the value (str)

    """
    quotient = n
    new_string = ''
    while quotient != 0:
        
        remainder = quotient%13
        quotient = quotient//13
        
        if remainder == 10:
            value = 'A'
        elif remainder == 11:
            value = 'B'
        elif remainder == 12:
            value = 'C'
        else :
            value = str(remainder)
            
        new_string = value + new_string
    return new_string
 
def tridecimal_expansion(n_str):
    """

    Convert a base 13 value to a tridecimal value

    n_str: The value to be processed (str)

    Returns:  The tridecimal of the value(str)

    """
    tridecimal_value = ''
    for i, ch in enumerate(n_str):
        if ch == 'A':
            ch = '+'
        elif ch == 'B':
            ch = '-'
        elif ch == 'C':
            ch = '.'
        tridecimal_value += ch
    return tridecimal_value
    
def tridecimal_to_conway(n_str): 
    """

    Convert a tridecimal value to a Conway float

    n_str: The value to be processed (str)

    Returns:  The Conway float of the value(float)

    """
    if('+' in n_str):

        f = n_str.rfind('+') #To find the index of '+'
        if f == len(n_str):  #
            return 0
        else:
            new_str = n_str[f+1: ]
            return float(new_str)
        
        
    elif('-' in n_str):
            return str(0)
            
    elif n_str.isdigit():
            return str(0)
    else:
            try: # Used to check if the value is already a float
                float (n_str)
                return float(n_str)
            except ValueError:
                return 0

def zeta(s): 
    """

    Calculate the Zeta function of an input value

    s: The value to be processed (float)

    Returns:  The Zeta function of the value(float)

    """
    x = 1
    total = 0
    DELTA = 10**(-7)
    
    if s <= 0:
        return None
        
    while True:
        nxtTerm = 1/((x+1)**s)
        last_term = 1/(x**s)
        if last_term - nxtTerm < DELTA:
            total += last_term
            break
        
        total += last_term
        x += 1
    return total
     
    
def main(): 
    print("Functions")

    PROMPT = input("Enter Z for Zeta, C for Conway, Q to quit: ").lower()
    while not( PROMPT == 'z' or PROMPT == 'c' or PROMPT == 'q'): 
        print("Error in input. Please try again.")
        PROMPT = input("Enter Z for Zeta, C for Conway, Q to quit: ").lower()
    while PROMPT != 'q':
    
        if PROMPT == 'z':
            print('Zeta')                               
            s = input("Input a number: ")
            
            while s.isdigit != True:  # To check if the input is a digit 
                if s.isalpha() == True: # If it is an alphabet it should print error
                    print("Error in input. Please try again.")
                    s = input("Input a number: ") # ask again for input until a valid one is entered
                else:
                    break
                
            s = int(s)
            print(zeta(s))
            PROMPT = input("Enter Z for Zeta, C for Conway, Q to quit: ").lower()
            
   
        if PROMPT == 'c': 
            print('Conway')
            n = input("Input a positive integer: ")
            while n.isdigit() != True:
                print("Error in input. Please try again.")
                n = input("Input a positive integer: ")
            
        
            n = int(n)
            a = int_to_base13(n) # Goes back to int_to_base13 function and perform calculation
            b = tridecimal_expansion(a)  # Goes back to tridecimal_expansion function and perform calculation
            c = tridecimal_to_conway(b)  # Goes back to tridecimal_to_conway function and perform calculation
            
            print("Base 13:",a)
            print("Tridecimal:", b)
            print("Conway float:", c)  
            PROMPT = input("Enter Z for Zeta, C for Conway, Q to quit: ").lower()
        
    if PROMPT == 'q':
        print("\nThank you for playing.")

if __name__ == "__main__": 
    main()
        
    

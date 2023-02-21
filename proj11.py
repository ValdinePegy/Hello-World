 # Computer Project #11

  #  Algorithm
  
  #  Design a calendar that records and updates events for the user.
  
  #  Create a Class P11_Event which contains different functions on the event
  
  #  Create the functions init, get_date, get_time, get_time_range, str, repr, lt, and eq.
  
  #  Create the Class P11_Calendar which contains different functions for the events
  
  #  Create the functions init, add_event, delete_event, day_schedule, str, repr
  
  #  Create a function( check_time) to check if the time and duration are valid.
  
  #  Create another function event_prompt to prompt for the event.

  #  In the main function, call the other functions in a loop and display function to perform each task .
  
  #  If the user input 'q', quit the function.
  
from p11_calendar import P11_Calendar
from p11_event import P11_Event



CAL_TYPE = ['meeting','event','appointment','other']

MENU = '''Welcome to your own personal calender.
  Available options:
    (A)dd an event to calender
    (D)elete an event
    (L)ist the events of a particular date
    (Q)uit'''

def check_time(time,duration):
    ''' This function returns True if the time and duration are valid and False if otherwise.
    A valid time must start at 6AM and end at 5PM.'''
    
    try :
        h, m = map(int, time.split(':')) # converting to int and splitting the values
        start_time = h * 60 + m 
        if duration == 0: # condition for valid duration 
            return False
        else:
            end_time = start_time + duration
            
        if 360 <= start_time <= end_time <= 1020: # condition to check if the time is valid 
            return True
        else:
            return False
    except :
        return False

def event_prompt():
    ''' This function prompts an event, re-prompt until a valid event is entered. Returns the 
    event, Prompt for date, time, duration, and cal_tpe.'''
    
    while True: # it will keep prompting until a valid event is entered.
        date = input("Enter a date (mm/dd/yyyy): ")
        time = input("Enter a start time (hh:mm): ")
        duration = int(input("Enter the duration in minutes (int): "))
        cal_type = input("Enter event type ['meeting','event','appointment','other']: ")
        
        a = check_time(time, duration) # to check if the time and duration are valid
        
        event = P11_Event(date,time,duration,cal_type) # to build the event
        
        if event.valid == True and a == True: # event.valid from valid being an attribute of event
            return event 
        
        else: 
            print("Invalid event. Please try again.")
            continue
    
                
def main():
    
    thecalender = P11_Calendar()
    
    print(MENU)
    Options = ['a','d','l','q']
    Opt = input("Select an option: ").lower()
    
    while Opt not in Options:
        print("Invalid option. Please try again.") # if the option entered is not amongst the options
        Opt = input("Select an option: ").lower()
    
    while Opt != 'q':
        
        if Opt == 'a':
            event = event_prompt()
            print("Add Event")
            b = thecalender.add_event(event)
            if b == True: # if the output of add_event is True
                print("Event successfully added.")
            else:
                print("Event was not added.")
                
        if Opt == 'd':      
            print("Delete Event")
            date = input("Enter a date (mm/dd/yyyy): ")
            time = input("Enter a start time (hh:mm): ")
            d = thecalender.delete_event( date, time)
            if d == True: # if the output of delete_event is True
                print("Event successfully deleted.")
            else:
                print("Event was not deleted.")
        
        if Opt == 'l':
            print("List Events")
            date = input("Enter a date (mm/dd/yyyy): ")
            c_e = thecalender.day_schedule(date) # using the day_schedule to get the events at a 
            for i in c_e:   # particular date
                print(i)
            if c_e == []: # if the list is empty it should print this statement
                print("No events to list on ", date)
            
        print(MENU)
        Opt = input("Select an option: ").lower()

if __name__ == '__main__':
     main()

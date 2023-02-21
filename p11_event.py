#  Class P11_Event file

#  This class consists of different functions which works on an event.

#  It initializes the attributes and check for their validities

#  It has the functions get_date, get_time, get_time_range, str, repr, lt, and eq

from datetime import datetime
CAL_TYPE = ['meeting','event','appointment','other']

class P11_Event():
    def __init__(self,date=None,time='9:00',duration=60,cal_type='meeting'):
        '''This function initializes the public attributes: date, time,
        duration, cal_type, valid. 
        It checks if the attributes are well-formed and if they are not,
        it returns False. '''
        
        self.date = date
        self.time = time
        self.duration = duration
        self.cal_type = cal_type
        
        if date == None: # if the date is None it should 
            self.date = None
            valid_date = False
         
            
        else:
            try: #date (it should check for the formatting of the date)
                date_object = datetime.strptime(date, "%m/%d/%Y")
                self.date = date
                valid_date = True
    
                
            except ValueError:  # if there is a valueError, then the date is npt 
                self.date = None   # in the right format)
                valid_date = False
        
        
            try: #time (it should check for the formatting of the time)
                time_object = datetime.strptime(time, "%H:%M")
                self.time = time
                valid_time = True
    
                
            except ValueError: # if there is a valueError, then the time is npt 
                self.time = None  # in the right format)
                valid_time = False
       
                    
            # duration ( check for the duration )
            if type(duration) != int or duration < 0:
                self.duration = None
                valid_dur = False  
            else:
                valid_dur = True
            
            # cal_type ( check cal_type )
            if cal_type not in CAL_TYPE:
                self.cal_type = None 
                valid_cal = False
            else:
                valid_cal = True
            
        if valid_date == True and valid_time == True and valid_dur == True and valid_cal == True :
            self.valid = True  # return True if the valid of each attribute is True
        else:
            self.valid = False  # return False otherwise
            
    
    def get_date(self):
        '''This function returns the date which is well-formed'''
        
        return self.date
        
    def get_time(self):
        '''This function returns the time which is well-formed'''
        
        return self.time
        
    def get_time_range(self):
        '''This function calculates the end time and returns a tuple. The duration,
        start time and end time are all in minutes.'''
        
        a = self.time  # calling the time
        h, m = map(int, a.split(':')) # converting to int and splitting the values
        self.start_time = h * 60 + m 
        
        self.end_time = self.start_time + self.duration
        
        return (self.start_time, self.end_time)
    
    def __str__(self):
        '''This function returns a string formatted as specified by the instructions.'''
        
        return '{}: ''start:'' {}; ''duration:'' {}'.format(self.date, self.time, self.duration)
        if self.date == None or self.time == None or self.duration == None: # if the attributes is None,
            return 'None'   # it should return None
    
    def __repr__(self):
        if self.date and self.time and self.duration:
            return self.date + ';' + self.time + '+' + str(self.duration)
        else:
            return 'None'

    def __lt__(self,e):
        '''This function checks if the self time is less than the e time and return True if it is.
        If it is not, it returns False. First converts the time to an integer number of minutes 
        before comparing.'''
        
        a = self.time
        b = e.time
        
        h1, m1 = map(int, a.split(':')) # converting the string to int
        self.time1 = h1 *60 + m1 # calculating the total time to mins
        
        h2, m2 = map(int, b.split(':')) # converting the string to int 
        e.time1 = h2 *60 + m2 # calculating the total time in imins
        
        if self.time1 < e.time1:
            return True
        else:
            return False
        
        if self.time == None or e.time == None:
            return False
        
    def __eq__(self,e):
        '''PROVIDED'''
        return self.date == e.date and self.time == e.time and self.duration == e.duration and self.cal_type == e.cal_type # and self.status == e.status
       
        

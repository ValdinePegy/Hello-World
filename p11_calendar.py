#  Class P11_Calendar file

#  This Class consists of different functions which work on events in a calendar

#  It initializes a list of events, add events to the list, delete events at specified dates and times.


class P11_Calendar():
    def __init__(self):
        '''This function initializes the public attribute event_list to an empty list. '''
        
        self.event_list = [] # initializing event list to an empty list
        
    def add_event(self,e):
        '''This function appends event e to the list of events attribute if the
        event does not conflict with any other events in the list. It returns False if there
        is a conflict.'''
        
        start_time1, end_time1 = e.get_time_range()
        date1 = e.date
        
        for i in  self.event_list:
            start_time2, end_time2 = i.get_time_range()
            date2 = i.date
                    
            if date1 == date2: # it checks first if the dates are the same
                if start_time1 <= start_time2 <= end_time1 <= end_time2 : # to check if there is a conflict
                    return False
                else:
                    continue # so that it keeps iterating through the list
                                
        self.event_list.append(e)
        return True
        
        
    def delete_event(self,date,time):
        '''The function deletes the event at the specified date and time. Returns False if un-
        successful and True if it is successful.'''
        
        a = date
        b = time
       
        for i,ch in enumerate(self.event_list):
            
            c,d = ch.date, ch.time
           
            if a != c or b != d: # if the dates are not the same, it should continue through the 
                continue     # other elements in the list
                
            else:
                 del self.event_list[i]  # delete the event at that particular index
                 #self.event_list.remove(ch)
                 return True
        return False
         
    def day_schedule(self,date):
        '''This function returns a sorted lists of events on the date in the date parameter by the tine.
        Returns an empty list if the date is not well formatted.'''

        a = date
        date_l = []
        for ch in self.event_list:
            c = ch.date
            if c == a: # if the date is the same as the specified date, 
                date_l.append(ch) # it should append the event to a list
                
        date_l = sorted(date_l) # sort the list containing the events at that date
        return date_l
                            
    def __str__(self): 
        '''This function returns a string that has an event on each line. Have one header line'''
        
        #a = P11_Event( time, duration)
        #a.get_date()
        
        e = 'Events in Calendar:\n'
        for i in self.event_list:
            e += str(i) + '\n'  # uses the str function in the P11_Event as format to return the 
        return e  # elements in the list
            
    
    def __repr__(self):
        s = ''
        for e in self.event_list:
            s += e.__repr__() + ";"
        return s[:-1]
    
    
    def __eq__(self,cal):
        '''PROVIDED: returns True if all events are the same.'''
        if not isinstance(cal,P11_Calendar):
            return False
        if len(self.event_list) != len(cal.event_list):
            return False
        L_self = sorted(self.event_list)
        L_e = sorted(cal.event_list)
        for i,e in enumerate(L_self):
            if e != L_e[i]:
                return False
        return True
        

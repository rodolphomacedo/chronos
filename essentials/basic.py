# -*- encoding:utf-8 -*-
import numpy as np
from datetime import datetime, timedelta

class Requirements(object):

    def __init__(self):
        a = 3

class Nurse(object):
    
    """ The Nurse constructor
        self.number: Id of nurse
        
        self.name: Name of nurse
        
        self.specialization: Specialization of nurse
        
        self.wokrShifts: Days that the nurse will work
            True: The nurse will work
            False: The day off nurse
        
        self.softRestrictions: Nurse's work preferences by shifts
            Domain: [-10, 10]
            Legend: -10 implies that the nurse does not really want to work this shift
                     10 implies that the nurse really want to work this shift
        
        self.hardRestrictions = Nurse's work restrictions by shifts
            True: The nurse will not be able to work on that shifts
    """
    def __init__(self,number, name, specialization=None):
        self.number = number
        self.name = name
        self.specialization = specialization
        self.workDays = np.array()
        #self.daysOff = np.array()
        #self.softRestrictions = np.array()
        #self.hardRestrictions = np.array()

    def __repr__(self):
        return self.name

    def setWorkDays(self, day):
        pass        




class Calendar(object):
    
    def __init__(self, year, month, day, hour, minute, second, deltaTime, totalTime):
               
        self.calendar = [] 
        
        weekdays = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')
        startTime = datetime(year, month, day, hour, minute, second)
        deltaT = timedelta(hours=deltaTime)
        
        for i in (range(totalTime)):
            obj = [startTime + i * deltaT, [] ]
            self.calendar.append(obj)
        
    def show(self):

        for cal in self.calendar:
            print 'Date: ', cal['date'], ' - Nurse: ',cal['nurses'] 
    
    def show2(self):
        print self.calendar

    def insertNurse(self, Nurse):
        
        self.calendar['date']














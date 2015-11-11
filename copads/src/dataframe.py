'''
A generic series and dataframe to hold data and analysis
Date created: 24th September 2012
Licence: Python Software Foundation License version 2
'''
import string
import random

from copadsexceptions import FunctionParameterValueError

class Series(object):
    '''
    '''
    def __init__(self, name=''):
        '''
        Constructor. Initialize data series with a name.
        
        @param name: Name of this data series. Default is empty name.
        @type name: string
        '''
        self.name = str(name)
        self.data = []
        self.label = []
        self.analyses = {}
        
    def addData(self, data=[], label=[]):
        if len(label) == 0:
            label = range(len(data))
        if len(data) != len(label):
            raise FunctionParameterValueError()
        self.data = data
        self.label = label
        
    
class Dataframe(object):
    '''
    A data frame is an encapsulation of one or more data series and its 
    associated analyses.
    '''
    def __init__(self, name=''):
        '''
        Constructor. Initialize data frame with a name.
        
        @param name: Name of this data frame. Default is empty name.
        @type name: string
        '''
        self.name = str(name)
        self.series_names = []
        self.data = {}
        self.analyses = {}
    
    def _generateRandomName(self):
        name = ''.join([random.choice(string.ascii_uppercase) 
                        for i in range(8)])
        while name in self.series_name:
            name = ''.join([random.choice(string.ascii_uppercase) 
                            for i in range(8)])
        return name
        
    def addSeries(self, series, fill_in=None):
        if series.name == '':
            series.name = self._generateRandomName()
        series_length = len(self.series_name)
        for i in range(len(series.data)):
            if series.label[i] not in self.data:
                temp = [fill_in for j in range(series_length)]
                temp = temp.append(series.data[i])
                self.data[series.label[i]] = temp
            else:
                temp = self.data[series.label[i]]
                temp = temp.append(series.data[i])
                self.data[series.label[i]] = temp
                
                
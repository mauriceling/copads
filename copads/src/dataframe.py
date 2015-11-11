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
    A data series is essentially a labeled list or vector. Each item in 
    the list/vector is given a label for identification and retrieval. 
    Hence, the number of labels and the number of data elements must be 
    equal.
    
    In itself, a data series can be viewed as a column of data in a data 
    table where the name of the series corresponds to the field name; such 
    as::
    
        <Label>    Height
        Tom        165
        Ellis      191
        Richard    172
        Melvin     175
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
        for i in range(len(data)):
            self.data.append(data[i])
            self.label.append(label[i])
        
    def changeDatum(self, new_value, label):
        try: 
            index = self.label.index(label)
            self.data[index] = new_value
        except ValueError: pass
        
    def changeLabel(self, new_label, original_label):
        try:
            index = self.label.index(original_label)
            self.label[index] = new_label
        except ValueError: pass
      
    def getDatum(self, label):
        try:
            index = self.label.index(label)
            return self.data[index]
        except ValueError: pass
        
    def getLabels(self, datum):
        labels = [self.label[index] 
                  for index in range(len(self.data)) 
                     if self.data[index] == datum]
        if len(labels) == 0: return [None]
        if len(labels) > 0: return labels
        
    
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
        self.label = []
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
        df_label = self.data.keys()
        for i in range(len(series.data)):
            if series.label[i] not in df_label:
                temp = [fill_in] * len(self.series_names)
                temp.append(series.data[i])
                self.data[series.label[i]] = temp
            else:
                temp = self.data[series.label[i]]
                temp.append(series.data[i])
                self.data[series.label[i]] = temp
        self.series_names.append(series.name)
        self.label = self.data.keys()
        for k in self.label:
            if len(self.data[k]) < len(self.series_names):
                temp = self.data[k]
                temp.append(fill_in)
                self.data[k] = temp
                
                
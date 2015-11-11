'''
A generic series and data frame to hold data and analysis
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
        
    def addData(self, data, label=[]):
        '''
        Method to add data into the data series. If provided, the number 
        of elements in data and label have to be the same. However, the 
        labels need not be unique (duplicated labels are allowed) but this 
        is highly undesirable as it can cause issues which requires unique 
        labels.
        
        @param data: list of data values.
        @type data: list
        @param label: list of labels for the data values. If not given, 
        a sequential number will be given as label but this does not ensure 
        uniqueness in label names across the entire series.
        @type label: list
        '''
        if len(label) == 0:
            label = range(len(data))
        if len(data) != len(label):
            raise FunctionParameterValueError()
        for i in range(len(data)):
            self.data.append(data[i])
            self.label.append(label[i])
        
    def changeDatum(self, new_value, label):
        '''
        Method to change the data value of a label. If the label is not 
        found within the data series, nothing will be changed.
        
        @param new_value: the new value for the label.
        @param label: the label name for the data value to be changed.
        '''
        try: 
            index = self.label.index(label)
            self.data[index] = new_value
        except ValueError: pass
        
    def changeLabel(self, new_label, original_label):
        '''
        Method to change the name of an existing label. If the existing 
        (original) label is not found within the data series, nothing will 
        be changed.
        
        @param new_label: the new name for the label.
        @param original_label: the existing (original) label name to be 
        changed.
        '''
        try:
            index = self.label.index(original_label)
            self.label[index] = new_label
        except ValueError: pass
      
    def getDatum(self, label):
        '''
        Method to get data value for a given label. If the label is not 
        found within the data series, None will be returned.
        
        @param label: the label name for the data value to retrieve.
        @return: data value tagged to the label (if found), or None (if the 
        label is not found).
        '''
        try:
            index = self.label.index(label)
            return self.data[index]
        except ValueError: return None
        
    def getLabels(self, datum):
        '''
        Method to get label name(s) for a given data value.
        
        @param datum: the data value to retrieve its corresponding label.
        @return: [None] if data value is not found; list of one or more 
        label names if the data value is found.
        @rtype: list
        '''
        labels = [self.label[index] 
                  for index in range(len(self.data)) 
                     if self.data[index] == datum]
        if len(labels) == 0: return [None]
        if len(labels) > 0: return labels
        
    
class Dataframe(object):
    '''
    A data frame is an encapsulation of one or more data series and its 
    associated analyses. Hence, a data frame can be formed using one or 
    more data series where data elements across series are linked up by 
    their respective labels. As a result, a data frame can be viewed as 
    a table or spreadsheet. 
    
    For example, a data frame of ::
    
        <Label>    Height   Weight
        Tom        165      62
        Ellis      191      85
        Richard    172      68
        Melvin     175      67
        
    can be formed using 2 data series - Height, and Weight; where each 
    data series has 'Tom', 'Ellis', 'Richard', and 'Melvin' as labels.
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
        '''
        Private method to generate a 8-character upper case name to be used 
        as series names.
        
        @return: generated name.
        @rtype: string
        '''
        name = ''.join([random.choice(string.ascii_uppercase) 
                        for i in range(8)])
        while name in self.series_name:
            name = ''.join([random.choice(string.ascii_uppercase) 
                            for i in range(8)])
        return name
        
    def addSeries(self, series, fill_in=None):
        '''
        Method to add a data series into the data frame.
        
        @param series: data series (dataframe.Series object) for addition.
        @param fill_in: value to fill into missing values during process. 
        This is required as the number of data elements across each label 
        must be the same. Hence, filling in of missing values can occur 
        when (1) the newly added data series consists of new labels which 
        are not found in the current data frame (this will require filling 
        in of missing values in the current data frame), or (2) the current 
        data frame consists of labels that are not found in the newly 
        added data series (this will require filling in of missing values 
        to the newly added data series). Default = None.
        '''
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
                
    def addData(self, dataset, labels, fill_in=None):
        '''
        Method to add new data into the current data frame. For example, 
        
        >>> df = d.Dataframe('frame1')
        >>> dataset = {'seriesA': [10, 11, 12, 13, 14],
                       'seriesB': [20, 21, 22, 23, 24],
                       'seriesC': [30, 31, 32, 33, 34],
                       'seriesD': [40, 41, 42, 43, 44]}
        >>> label = ['A', 'B', 'C', 'D', 'E']
        >>> df.addData(dataset, label)
        
        will result in::
        
                seriesA  seriesB  seriesC  seriesD
            A   10       20       30       40
            B   11       21       31       41
            C   12       22       32       42
            D   13       23       33       43
            E   14       24       34       44
        
        @param fill_in: value to fill into missing values during process. 
        This is required as the number of data elements across each label 
        must be the same. Hence, filling in of missing values can occur 
        when (1) the newly added data series consists of new labels which 
        are not found in the current data frame (this will require filling 
        in of missing values in the current data frame), or (2) the current 
        data frame consists of labels that are not found in the newly 
        added data series (this will require filling in of missing values 
        to the newly added data series). Default = None.
        '''
        series_names = dataset.keys()
        series_names.sort()
        for series_name in series_names:
            s = Series(str(series_name))
            s.addData(dataset[series_name], labels)
            self.addSeries(s, fill_in)
            
    def changeDatum(self, new_value, series, label):
        '''
        Method to change the data value of a series and label. If the 
        series or label is not found within the data series, nothing will 
        be changed.
        
        @param new_value: the new value for the label.
        @param series: the series name for the data value to be changed.
        @param label: the label name for the data value to be changed.
        '''
        try: 
            s = self.series_names.index(series)
            self.data[label][s] = new_value
        except ValueError: pass
        except KeyError: pass
        
    def changeSeriesName(self, new_name, original_name):
        '''
        Method to change the name of an existing series. If the existing 
        (original) series name is not found within the data series, nothing 
        will be changed.
        
        @param new_name: the new name for the series.
        @param original_name: the existing (original) series name to be 
        changed.
        '''
        try:
            index = self.series_names.index(original_name)
            self.series_names[index] = new_name
        except ValueError: pass
  
    def changeLabel(self, new_label, original_label):
        '''
        Method to change the name of an existing label. If the existing 
        (original) label is not found within the data series, nothing will 
        be changed.
        
        @param new_label: the new name for the label.
        @param original_label: the existing (original) label name to be 
        changed.
        '''
        try:
            data = [x for x in self.data[original_label]]
            self.data[new_label] = data
            del self.data[original_label]
        except KeyError: pass
        try:
            index = self.label.index(original_label)
            self.label[index] = new_label
        except ValueError: pass
        
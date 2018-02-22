'''
A generic series and data frame to hold data and analysis
Date created: 24th September 2012
Licence: Python Software Foundation License version 2
'''
import string
import random

from .copadsexceptions import FunctionParameterValueError

class Series(object):
    '''
    A data series is essentially a labeled list or vector. Each item in
    the list/vector is given a label for identification and retrieval.
    Hence, the number of labels and the number of data elements must be
    equal.

    In itself, a data series can be viewed as a row of data in a data
    table where the name of the series corresponds to the field name; such
    as::

                    Tom     Ellis   Richard     Melvin
        Height      165     191     172         175
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

    def cast(self, type, error_replace):
        '''
        Method to cast data in the series into a specific data type.

        Allowable data types are:
            1. integer (type == 'int' or 'integer')
            2. float (type == 'real' or 'float')
            3. string (type == 'str' or 'string')

        @param type: data type to cast into
        @type type: string
        @param error_replace: in event where there is a failure to cast
        the data element (such as attempt to cast a character into an
        integer, which will result ina ValueError), the data element will
        be replace with error_replace
        '''
        data = [0] * len(self.data)
        type = str(type)
        for i in range(len(self.data)):
            try:
                if type == 'int' or type == 'integer':
                    data[i] = int(self.data[i])
                if type == 'real' or type == 'float':
                    data[i] = float(self.data[i])
                if type == 'str' or type == 'string':
                    data[i] = str(self.data[i])
            except:
                data[i] = error_replace
        self.data = data

    def toDataframe(self):
        '''
        Method to convert and return the current data series as a data
        frame object. The following will happen in the returned data frame
        object:
            1. Name of the data frame will be the name of the current data
            series
            2. Name of the series in the data frame will be the name of
            the current data series
            3. Hence, name of the returned data frame and its data series
            will be the same

        @return: dataframe.Dataframe object
        '''
        df = Dataframe(self.name)
        df.addSeries(self)
        return df

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

    def cast(self, type, error_replace, series_name='all'):
        '''
        Method to cast data in the one or all series into a specific data
        type.

        Allowable data types are:
            1. integer (type == 'int' or 'integer')
            2. float (type == 'real' or 'float')
            3. string (type == 'str' or 'string')

        @param type: data type to cast into
        @type type: string
        @param error_replace: in event where there is a failure to cast
        the data element (such as attempt to cast a character into an
        integer, which will result ina ValueError), the data element will
        be replace with error_replace
        @param series_name: series name to cast values into a specific
        data type. If 'all', the entire data frame (all data series) will
        be type casted. Default = 'all'
        '''
        if series_name != 'all':
            try:
                index = self.series_names.index(series_name)
            except:
                return 0
        if series_name == 'all':
            for k in self.data.keys():
                data = [0] * len(self.data[k])
                type = str(type)
                for i in range(len(self.data[k])):
                    try:
                        if type == 'int' or type == 'integer':
                            data[i] = int(self.data[k][i])
                        if type == 'real' or type == 'float':
                            data[i] = float(self.data[k][i])
                        if type == 'str' or type == 'string':
                            data[i] = str(self.data[k][i])
                    except:
                        data[i] = error_replace
                self.data[k] = data
        else:
            for k in self.data.keys():
                try:
                    if type == 'int' or type == 'integer':
                        self.data[k][index] = int(self.data[k][index])
                    if type == 'real' or type == 'float':
                         self.data[k][index] = float(self.data[k][index])
                    if type == 'str' or type == 'string':
                         self.data[k][index] = str(self.data[k][index])
                except:
                     self.data[k][index] = error_replace

    def toSeries(self, series_name):
        '''
        Method to extract a series within the current data frame into a
        Series object.

        @param series_name: name of series to extract
        @type series_name: string
        @return: dataframe.Series object
        '''
        series_name = str(series_name)
        s = Series(series_name)
        try:
            si = self.series_names.index(series_name)
            data = [self.data[self.label[li]][si]
                    for li in range(len(self.label))]
            s.addData(data, self.label)
            return s
        except ValueError: return s
        except KeyError: return s

    def extractSeries(self, series_names, new_dataframe_name=''):
        '''
        Method to extract one or more series from the current data frame
        into a new data frame.

        @param series_names: names of series to extract
        @type series_names: list
        @param new_dataframe_name: name for new data frame (that is to be
        returned)
        @type new_dataframe_name: string
        @return: dataframe.Dataframe object
        '''
        df = Dataframe(str(new_dataframe_name))
        for series in series_names:
            s = self.toSeries(series)
            df.addSeries(s)
        return df

    def extractGreedySeriesValue(self, series_names, operator, value,
                                 new_dataframe_name=''):
        '''
        Method for "greedy" extraction of series name(s) and value by the
        following:
            1. Generate a new data frame by extracting required series using
            Dataframe.extractSeries method, which is essentially column
            reduction.
            2. Reduce the data labels (essentially, row reduction) by finding
            data values in any remaining (one or more) series using the
            search criterion.

        This method is considered to be "greedy" as the row reduction is not
        specific to particular series (column).

        @param series_names: names of series to extract
        @type series_names: list
        @param operator: comparative operator. Allowed values are: '>' (more
        than), '<' (less than), '>=' (more than or equals to), '<=' (less
        than or equals to), '=' (equals to), '!=' (not equals to), and '*'
        (all, basically replicating the entire data frame).
        @param value: value of the data to compare.
        @param new_dataframe_name: name for new data frame (that is to be
        returned)
        @type new_dataframe_name: string
        @return: dataframe.Dataframe object
        '''
        df = self.extractSeries(series_names, new_dataframe_name)
        return df.extractValue(operator, value, new_dataframe_name)

    def extractSeriesValue(self, series_name, operator, value,
                           new_dataframe_name=''):
        '''
        Method for extraction of row data where a specified value or range of
        value is found in the current data frame.

        This method is logically identical to SQL select.

        select * from <current> where <current>.seriesA > 30

        can be represented as

        >>> df = <current>.extractSeriesValue('seriesA', '>', 30, '')

        @param series_name: name of series to extract
        @type series_name: list
        @param operator: comparative operator. Allowed values are: '>' (more
        than), '<' (less than), '>=' (more than or equals to), '<=' (less
        than or equals to), '=' (equals to), '!=' (not equals to), and '*'
        (all, basically replicating the entire data frame).
        @param value: value of the data to compare.
        @param new_dataframe_name: name for new data frame (that is to be
        returned)
        @type new_dataframe_name: string
        @return: dataframe.Dataframe object
        '''
        df = Dataframe(new_dataframe_name)
        try:
            data = {}
            index = self.series_names.index(series_name)
            for label in self.data.keys():
                if operator == '=' and self.data[label][index] == value:
                    data[label] = [x for x in self.data[label]]
                elif operator == '>' and self.data[label][index] > value:
                    data[label] = [x for x in self.data[label]]
                elif operator == '<' and self.data[label][index] < value:
                    data[label] = [x for x in self.data[label]]
                elif operator == '>=' and self.data[label][index] >= value:
                    data[label] = [x for x in self.data[label]]
                elif operator == '<=' and self.data[label][index] <= value:
                    data[label] = [x for x in self.data[label]]
                elif operator == '*':
                    data[label] = [x for x in self.data[label]]
                df.data = data
                df.series_names = [name for name in self.series_names]
                df.label = data.keys()
        except IOError: pass
        return df

    def extractLabels(self, label_names, new_dataframe_name=''):
        '''
        Method to extract one or more data labels across all series from
        the current data frame into a new data frame.

        @param label_names: names of labels to extract
        @type label_names: list
        @param new_dataframe_name: name for new data frame (that is to be
        returned)
        @type new_dataframe_name: string
        @return: dataframe.Dataframe object
        '''
        df = Dataframe(str(new_dataframe_name))
        data = {}
        for label in label_names:
            try: data[label] = [x for x in self.data[label]]
            except KeyError: pass
        df.data = data
        df.label = label_names
        df.series_names = [x for x in self.series_names]
        return df

    def extractValue(self, operator, value, new_dataframe_name=''):
        '''
        Method to extract one or more data labels across all series, based on
        criterion, from the current data frame into a new data frame.

        For example, the following will extract all data labels across all
        series where data value is more than 30, and generate and return a new
        dataframe (ndf).

        >>> ndf = df.extractValue('>', 30, 'newframe')

        @param operator: comparative operator. Allowed values are: '>' (more
        than), '<' (less than), '>=' (more than or equals to), '<=' (less
        than or equals to), '=' (equals to), '!=' (not equals to), and '*'
        (all, basically replicating the entire data frame).
        @param value: value of the data to compare.
        @param new_dataframe_name: name for new data frame (that is to be
        returned)
        @type new_dataframe_name: string
        @return: dataframe.Dataframe object
        '''
        df = Dataframe(str(new_dataframe_name))
        data = {}
        for label in self.data.keys():
            try:
                if (operator == '>') and \
                    sum([1 for item in self.data[label] if item > value]):
                    data[label] = [x for x in self.data[label]]
                elif (operator == '<') and \
                    sum([1 for item in self.data[label] if item < value]):
                    data[label] = [x for x in self.data[label]]
                elif (operator == '>=') and \
                    sum([1 for item in self.data[label] if item >= value]):
                    data[label] = [x for x in self.data[label]]
                elif (operator == '<=') and \
                    sum([1 for item in self.data[label] if item <= value]):
                    data[label] = [x for x in self.data[label]]
                elif (operator == '=') and \
                    sum([1 for item in self.data[label] if item == value]):
                    data[label] = [x for x in self.data[label]]
                elif (operator == '!=') and \
                    sum([1 for item in self.data[label] if item != value]):
                    data[label] = [x for x in self.data[label]]
                elif (operator == '*'):
                    data[label] = [x for x in self.data[label]]
            except KeyError: pass
        df.data = data
        df.label = data.keys()
        df.series_names = [x for x in self.series_names]
        return df

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

        @param dataset: set of data to add. This is formatted as a
        dictionary where the key is the series name and the value is a list
        of data values of the same number of elements as labels.
        @type dataset: dictionary
        @param labels: list of labels for the data values. If not given,
        a sequential number will be given as label but this does not ensure
        uniqueness in label names across the entire series.
        @type labels: list
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

    def addCSV(self, filepath, series_header=True, separator=',',
               fill_in=None, newline='\n'):
        '''
        Method to add data from comma-delimited file (CSV) into current
        data frame.

        @param filepath: path to CSV file.
        @type filepath: string
        @param series_header: boolean flag to denote whether the first row
        in the CSV file contains the data header. It is highly recommended
        that header is included in the CSV file. Default = True (header is
        included)
        @param separator: item separator within the CSV file. Default = ','
        @param fill_in: value to fill into missing values during process.
        This is required as the number of data elements across each label
        must be the same. Hence, filling in of missing values can occur
        when (1) the newly added data series consists of new labels which
        are not found in the current data frame (this will require filling
        in of missing values in the current data frame), or (2) the current
        data frame consists of labels that are not found in the newly
        added data series (this will require filling in of missing values
        to the newly added data series). Default = None.
        @param newline: character to denote new line or line feed in the
        CSV file.
        '''
        data = open(filepath, 'r').readlines()
        data = [x[:(-1)*len(newline)] for x in data]
        data = [[item.strip()
                 for item in x.split(separator)]
                for x in data]
        if series_header:
            series = data[0][1:]
            data = data[1:]
        labels = [x[0] for x in data]
        data = [x[1:] for x in data]
        data = zip(*data)
        for i in range(len(series)):
            s = Series(series[i])
            s.addData(data[i], labels)
            self.addSeries(s, fill_in)

    def removeSeries(self, series_name):
        '''
        Method to remove / delete a data series from the current data
        frame.

        @param series_name: names of series to remove
        @type series_name: string
        '''
        series_name = str(series_name)
        try:
            index = self.series_names.index(series_name)
            self.series_names.pop(index)
            for label in self.data.keys(): self.data[label].pop(index)
        except: pass

    def popSeries(self, series_names, new_dataframe_name=''):
        '''
        Method to pop one or more series (extract one or more series from
        the current data frame into new data frame, followed by removing
        the extracted series from the current data frame).

        @param series_names: names of series to pop
        @type series_names: list
        @param new_dataframe_name: name for new data frame (that is to be
        returned)
        @type new_dataframe_name: string
        @return: dataframe.Dataframe object
        '''
        df = self.extractSeries(series_names, new_dataframe_name)
        for series in series_names: self.removeSeries(series)
        return df

    def removeLabel(self, label):
        '''
        Method to remove / delete a label across all data series from the
        current data frame.

        @param label: names of label to remove
        @type label: string
        '''
        label = str(label)
        try:
            index = self.label.index(label)
            self.label.pop(index)
            del self.data[label]
        except: pass

    def popLabels(self, label_names, new_dataframe_name=''):
        '''
        Method to pop one or more labels across all data series (extract
        one or more labels across all data series from the current data
        frame into new data frame, followed by removing the extracted
        labels from the current data frame).

        @param label_names: names of series to pop
        @type label_names: list
        @param new_dataframe_name: name for new data frame (that is to be
        returned)
        @type new_dataframe_name: string
        @return: dataframe.Dataframe object
        '''
        df = self.extractLabels(label_names, new_dataframe_name)
        for label in label_names: self.removeLabel(label)
        return df

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

    def getDatum(self, series, label):
        '''
        Method to get data value for a given series and label names. If the
        series name or label name is not found within the data series, None
        will be returned.

        @param series: the series name for the data value to retrieve.
        @param label: the label name for the data value to retrieve.
        @return: data value tagged to the series and label (if found), or
        None (if the series or label is not found).
        '''
        try:
            s = self.series_names.index(series)
            return self.data[label][s]
        except ValueError: return None
        except KeyError: return None

    def getLabels(self, datum):
        '''
        Method to get label name(s) for a given data value. However, this
        method does not return the series name from which the data value
        is/are found.

        @param datum: the data value to retrieve its corresponding label.
        @return: [None] if data value is not found; list of one or more
        label names if the data value is found.
        @rtype: list
        '''
        labels = [label
                  for label in self.data.keys()
                     for series in range(len(self.data[label]))
                         if self.data[label][series] == datum]
        if len(labels) == 0: return [None]
        if len(labels) > 0: return labels

    def getSeries(self, datum):
        '''
        Method to get series name(s) for a given data value. However, this
        method does not return the label name from which the data value
        is/are found.

        @param datum: the data value to retrieve its corresponding series.
        @return: [None] if data value is not found; list of one or more
        series names if the data value is found.
        @rtype: list
        '''
        series = [self.series_names[series]
                  for label in self.data.keys()
                     for series in range(len(self.data[label]))
                         if self.data[label][series] == datum]
        if len(series) == 0: return [None]
        if len(series) > 0: return series

    def getSeriesLabels(self, datum):
        '''
        Method to get series name(s) and label name(s) for a given data
        value. This method returns the a list of coodinates tuples,
        (series name, label name) in which the given data value is found.

        @param datum: the data value to retrieve its corresponding
        coordinates.
        @return: [(None, None)] if data value is not found; list of one or
        more coordinates if the data value is found.
        @rtype: list
        '''
        coordinates = [(self.series_names[series], label)
                       for label in self.data.keys()
                           for series in range(len(self.data[label]))
                               if self.data[label][series] == datum]
        if len(coordinates) == 0:  return [(None, None)]
        else: return list(set(coordinates))

    def replaceLabel(self, label_name, operator, original_value, new_value):
        '''
        Method to replace values, within a label, from its original value
        to a new value, if and only if the original value meets a certain
        criterion.

        For example, the following will replace all values of more than 30,
        that are found within Label 'B', to 40.

        >>> df.replaceLabel('B', '>', 30, 40)

        @param label_name: the label name for the data value to be replaced.
        @param operator: comparative operator. Allowed values are: '>' (more
        than), '<' (less than), '>=' (more than or equals to), '<=' (less
        than or equals to), '=' (equals to), and '!=' (not equals to).
        @param original_value: original value of the data.
        @param new_value: new value to be replaced when the criterion is met.
        '''
        if label_name not in self.data: return None
        for i in range(len(self.data[label_name])):
            if (operator == '=') and \
                (self.data[label_name][i] == original_value):
                    self.data[label_name][i] = new_value
            elif (operator == '>') and \
                (self.data[label_name][i] > original_value):
                    self.data[label_name][i] = new_value
            elif (operator == '<') and \
                (self.data[label_name][i] < original_value):
                    self.data[label_name][i] = new_value
            elif (operator == '>=') and \
                (self.data[label_name][i] >= original_value):
                    self.data[label_name][i] = new_value
            elif (operator == '<=') and \
                (self.data[label_name][i] <= original_value):
                    self.data[label_name][i] = new_value
            elif (operator == '!=') and \
                (self.data[label_name][i] != original_value):
                    self.data[label_name][i] = new_value

    def replaceSeries(self, series_name, operator, original_value, new_value):
        '''
        Method to replace values, within a series, from its original value
        to a new value, if and only if the original value meets a certain
        criterion.

        For example, the following will replace all values of more than 30,
        that are found within Series 'B', to 40.

        >>> df.replaceSeries('B', '>', 30, 40)

        @param series_name: the series name for the data value to be replaced.
        @param operator: comparative operator. Allowed values are: '>' (more
        than), '<' (less than), '>=' (more than or equals to), '<=' (less
        than or equals to), '=' (equals to), and '!=' (not equals to).
        @param original_value: original value of the data.
        @param new_value: new value to be replaced when the criterion is met.
        '''
        if series_name not in self.series_names: return None
        else: index = self.series_names.index(series_name)
        for label in self.data.keys():
            if (operator == '=') and \
                (self.data[label][index] == original_value):
                    self.data[label][index] = new_value
            elif (operator == '>') and \
                (self.data[label][index] > original_value):
                    self.data[label][index] = new_value
            elif (operator == '<') and \
                (self.data[label][index] < original_value):
                    self.data[label][index] = new_value
            elif (operator == '>=') and \
                (self.data[label][index] >= original_value):
                    self.data[label][index] = new_value
            elif (operator == '<=') and \
                (self.data[label][index] <= original_value):
                    self.data[label][index] = new_value
            elif (operator == '!=') and \
                (self.data[label][index] != original_value):
                    self.data[label][index] = new_value


class MultiDataframe(object):
    '''
    A multidata frame is a container of one or more data frames. This
    allows for processing across more than one data frames.
    '''

    def __init__(self, name=''):
        '''
        Constructor. Initialize multidata frame with a name.

        @param name: Name of this data frame. Default is empty name.
        @type name: string
        '''
        self.name = str(name)
        self.frames = {}
        self.frame_names = []
        self.analyses = {}

    def addDataframe(self, dataframe, replace=False):
        '''
        Method to add a data frame. It is highly encouraged that all
        data frames to be added have their own identifying names. In event
        whereby the data frame does not have a name, a randomly generated
        8-character name will be assigned.

        This method allows for replacement of existing data frame when
        'replace' flag is set to True. In event where 'replace' flag is
        False (do not replace existing data frame, if present) and there
        is an existing data frame with the same name, a randomly generated
        8-character name will be appended to the name of the data frame to
        be added.
        '''
        df_name = dataframe.name
        used_names = self.frames.keys()
        if (not replace) and (df_name in used_names):
            while df_name in used_names:
                df_name = df_name + '_' + \
                          ''.join([random.choice(string.ascii_uppercase)
                                for i in range(8)])
            dataframe.name = df_name
        if df_name == '':
            name = ''.join([random.choice(string.ascii_uppercase)
                            for i in range(8)])
            while name in used_names:
                name = ''.join([random.choice(string.ascii_uppercase)
                                for i in range(8)])
            dataframe.name = name
        self.frames[dataframe.name] = dataframe
        self.frame_names.append(dataframe.name)

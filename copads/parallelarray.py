'''
Array Data Structures and Algorithms.

Copyright (c) Maurice H.T. Ling <mauriceling@acm.org>

Date created: 19th March 2008
'''

import types
from .copadsexceptions import ParallelArrayError

class ParallelArray(object):
    '''
    Parallel Array is an array whereby each data list in the array is of
    the same size.
    Ref: http://en.wikipedia.org/wiki/Parallel_array
    '''

    def __init__(self, fieldnames=[]):
        '''
        Constructor method.

        @param fieldnames: field names to initiate. Default = empty list.
        @type fieldnames: list
        '''
        self.data = {}
        self.fields = []
        if len(fieldnames) > 0 and isinstance(fieldnames, types.ListType):
            self.addFields(fieldnames)

    def fieldnames(self):
        '''
        Method to return a list of field names.

        @return: list of field names.
        '''
        return self.fields

    def _datalength(self):
        '''
        Private method to get the length of data (number of elements) for
        each field. Each data field will have the same number of elements.

        @return: number of elements.
        '''
        if len(self.fields) > 0:
            return len(self.data[self.fields[0]])
        else:
            return 0

    def addFields(self, fieldnames):
        '''
        Method to add one or more field names.

        @param fieldnames: field names to add.
        @type fieldnames: list or string
        '''
        self.fields = self.data.keys()
        datalength = self._datalength()
        if isinstance(fieldnames, types.StringType):
            fieldnames = [fieldnames]
        for fname in fieldnames:
            if fname in self.fields:
                pass
            else:
                self.data[fname] = [None] * datalength
                self.fields.append(fname)

    def removeField(self, fieldname):
        '''
        Method to remove a data field.

        @param fieldname: field name to remove.
        @type fieldname: string
        @return: list of data from the removed data field.
        '''
        if not isinstance(fieldname, types.StringType):
            raise ParallelArrayError('fieldnames must be a string')
        if fieldname in self.fields:
            self.fields.remove(fieldname)
            data = [x for x in self.data[fieldname]]
            del self.data[fieldname]
            return data
        else:
            return []

    def addDataList(self, fieldnames, values):
        '''
        Method to add values using an ordered list of field names and the
        corresponding ordered list of values.

        The lists of field names and and values need not be the complete
        set of field names in the array - all missing data (field names
        and values not provided) will be deemed as None, in order to
        maintain the same number of values in each field.

        Values can be added to a non-existing field. In this case, a new
        field will be added and the values will be front-padded by None.

        @param fieldnames: ordered names of fields for values to be added
        to.
        @type fieldnames: list
        @param values: ordered values to be added.
        @type values: list
        '''
        record = {}
        if not isinstance(fieldnames, types.ListType):
            raise ParallelArrayError('fieldnames must be a list')
        if not isinstance(values, types.ListType):
            raise ParallelArrayError('values must be a string')
        if len(fieldnames) != len(values):
            raise ParallelArrayError('fieldnames and values must have \
            the same number of elements')
        for index in range(len(fieldnames)):
            record[fieldnames[index]] = values[index]
        self.addDataDictionary(record)

    def addDataDictionary(self, record):
        '''
        Method to add values using a dictionary, where the key is the field
        name and the value is the value of the field.

        The set of field names and and values need not be the complete
        set of field names in the array - all missing data (field names
        and values not provided) will be deemed as None, in order to
        maintain the same number of values in each field.

        Values can be added to a non-existing field. In this case, a new
        field will be added and the values will be front-padded by None.

        @param record: data record to be added.
        @type record: dictionary
        '''
        self.fields = self.data.keys()
        datalength = self._datalength()
        self.addFields(record.keys()) # in case there are new fields
        for k in record:
            self.data[k].append(record[k])
        for nk in [k for k in self.fields
                   if k not in record.keys()]:
            self.data[nk].append(None)

    def changeFieldname(self, original_name, new_name):
        '''
        Method to change the name of an existing field.

        @param original_name: name of the existing field to be changed.
        @type original_name: string
        @param new_name: new name for the existing field.
        @type new_name: string
        '''
        if original_name in self.data:
            data = self.removeField(original_name)
            self.data[new_name] = data
        self.fields = self.data.keys()



from CopadsExceptions import ArrayError

class ParallelArray(object):
    """
    Parallel Array is an array whereby each data list in the array is of the
    same size.
    Ref: http://en.wikipedia.org/wiki/Parallel_array
    """
    def __init__(self, fields = None):
        """
        Constructor. Able to initiate the array with a list of fields names
        """
        self.data = {}
        self.fields = []
        if fields: self.initFields(kwargs['fields'])
    
    def initFields(self, fields):
        """
        Initiates a list of fields into the array."""
        if type(fields) <> type([]):
            raise ArrayError('field parameter must be a list, ' + \
                str(type(fields)) + ' given.')
        for field in fields: self.addField(field)
        
    def addField(self, field):
        """
        Method to add a new field into the array. Raises ArrayError if attempt
        to add an existing field.
        """
        if self.data.has_key(field):
            raise ArrayError(str(field) + ' existed.')
        if type(field) <> type('string'):
            raise ArrayError('field must be a string')
        if len(self.fields) == 0: self.initFields(list(field))
        else:
            ddata = [None for x in range(len(self.data[self.fields[0]]))]
            self.data[field] = ddata
            self.fields.append(field)
            self.field_len = len(self.fields)
            
    def removeField(self, field):
        """
        Removes a field, together with its data, from the array."""
        try:
            self.data.pop(field)
            self.fields.remove(field)
            self.field_len = len(self.fields)
        except KeyError: pass
        
    def changeField(self, oldname, newname):
        """
        Change a field name from I(oldname) to I(newname). If I(oldname) does 
        not exist, a new field of I(newname) will be created."""
        if self.data.has_key(newname):
            raise ArrayError(str(newname) + ' already exist in array.')
        if self.data.has_key(oldname):
            temp = self.data[oldname]
            self.removeField(oldname)
            self.data[newname] = temp
        else: self.addField(newname)
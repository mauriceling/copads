from CopadsExceptions import ArrayError

class ParallelArray(object):
    def __init__(self, **kwargs):
        self.data = {}
        self.fields = []
        if kwargs.has_key('fields'): self.initFields(kwargs['fields'])
    
    def initFields(self, fields):
        if type(fields) <> type([]):
            raise ArrayError('field parameter must be a list, ' + \
                str(type(fields)) + ' given.')
        for field in fields: self.data[field] = []
        self.fields = fields
        self.field_len = len(fields)
        
    def addField(self, field):
        if self.data.has_key('field'):
            raise ArrayError(str(field) + ' existed.')
        if type(field) <> type('string'):
            raise ArrayError('field must be a string')
        if len(self.fields) == 0: self.initFields(list(field))
        else:
            ddata = [None for x in range(len(self.data[self.fields[0]]))]
            self.data[field] = ddata
            self.fields.append(field)
            self.field_len = len(self.fields)
            
    
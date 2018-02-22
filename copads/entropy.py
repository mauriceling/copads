'''
Functions for calculating entropy / informational content of a string
Date created: 23rd July 2017
Licence: Python Software Foundation License version 2
'''

import types
import math

from . import bag
from .copadsexceptions import FunctionParameterValueError


def _listify(data):
    '''
    Private function - process data into a list when possible.

    @param data: data to be converted (possible data types are
    list, string, tuple, integer, float, long)
    @return: data in list structure
    '''
    if type(data) is types.ListType:
        return data
    elif type(data) is types.StringType:
        return [x for x in data]
    elif type(data) is types.TupleType:
        return [x for x in data]
    elif type(data) is types.IntType:
        data = str(data)
        return [x for x in data]
    elif type(data) is types.FloatType:
        data = str(data)
        return [x for x in data]
    elif type(data) is types.LongType:
        data = str(data)
        return [x for x in data]
    else:
        raise FunctionParameterValueError('%s type is not listable' % type(data))


def _process_data(data):
    '''
    Private function - process data into a Bag (bag.Bag) structure.

    @param data: data to be converted (possible data types are
    list, string, tuple, integer, float, long)
    @return: (data, length) where data is the converted data into bag
    structure, and length is the number of unique elements in the bag
    '''
    data = _listify(data)
    d = bag.Bag()
    d.update(data)
    length = float(len(d))
    return (d, length)


def Shannon(data):
    '''
    Calculates Shannon entropy.

    @param data: data for entropy calculation
    @type data: string or numerical values or list
    @return: Shanon entropy of data
    @rtype: float
    '''
    (data, length) = _process_data(data)
    result = [data[k]/length for k in data.iterunique()]
    result = [x * math.log(x, 2) for x in result]
    result = (-1) * sum(result)
    return result


def Natural(data):
    '''
    Calculates Natural entropy.

    @param data: data for entropy calculation
    @type data: string or numerical values or list
    @return: Natural entropy of data
    @rtype: float
    '''
    (data, length) = _process_data(data)
    result = [data[k]/length for k in data.iterunique()]
    result = [x * math.log(x, math.e) for x in result]
    result = (-1) * sum(result)
    return result


def Renyi(data, order=2):
    '''
    Calculates Renyi entropy, which is a generalized version of Shannon
    entropy. When order = 1, Renyi entropy = Shannon entropy,

    @param data: data for entropy calculation
    @type data: string or numerical values or list
    @param order: exponent
    @type order: integer
    @return: Renyi entropy of data
    @rtype: float
    '''
    (data, length) = _process_data(data)
    order = int(order)
    if order < 0:
        raise FunctionParameterValueError('order must be at least zero')
    if order == 1:
        return Shannon(data)
    else:
        result = [(data[k]/length) ** order for k in data.iterunique()]
        result = (1/(1-order)) * math.log(sum(result), 2)
        return result


def Collision(data):
    '''
    Calculates Collision entropy, which is the same as Renyi entropy when
    order = 2.

    @param data: data for entropy calculation
    @type data: string or numerical values or list
    @return: Collision entropy of data
    @rtype: float
    '''
    return Renyi(data, 2)


def Hartley(data):
    '''
    Calculates Hartley entropy (also known as max-entropy), which is the
    same as Renyi entropy when order = 0.

    @param data: data for entropy calculation
    @type data: string or numerical values or list
    @return: Hartley entropy of data
    @rtype: float
    '''
    return Renyi(data, 0)


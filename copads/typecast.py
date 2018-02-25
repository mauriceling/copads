'''
Functions to type cast between different objects.

Date created: 20th July 2016

Licence: Python Software Foundation License version 2

The type cast functions can be mapped as::

    digraph G {
      node [shape = tripleoctagon]; "List" "Tuple" "Sets" "Dictionary";
      node [shape = box];
      "dataframe.Series" -> "dataframe.Dataframe" [color="green" label="tc_Series_Dataframe"];
      "dataframe.Series" -> "Dictionary" [color="green" label="tc_Series_Dictionary"];
      "dataframe.Series" -> "List" [color="green" label="tc_Series_List"];
      "dataframe.Series" -> "matrix.Vector";
      "dataframe.Dataframe" -> "dataframe.Series" [color="green" label="tc_Dataframe_Series"];
      "dataframe.Dataframe" -> "dataframe.MultiDataframe";
      "dataframe.MultiDataframe" -> "dataframe.Dataframe";
      "matrix.Vector" -> "List";
      "matrix.Vector" -> "Dictionary";
      "List" -> "Dictionary";
    }
'''

from .dataframe import Series
from .dataframe import Dataframe
from .dataframe import MultiDataframe
from .matrix import Vector


def tc_Series_Dataframe(source_object):
    '''
    Function to convert from dataframe.Series object to dataframe.Dataframe
    object.

    @param source_object: object to be type casted / converted.
    @type source_object: dataframe.Series object
    @return: dataframe.Dataframe object
    '''
    return source_object.toDataframe()

def tc_Dataframe_Series(source_object, series_name):
    '''
    Function to convert from dataframe.Dataframe object to dataframe.Series
    object.

    @param source_object: object to be type casted / converted.
    @type source_object: dataframe.Series object
    @param series_name: name of series to extract
    @type series_name: string
    @return: dataframe.Series object
    '''
    return source_object.toSeries(series_name)

def tc_Dataframe_MultiDataframe(source_object):
    '''
    Function to convert from dataframe.Dataframe object to
    dataframe.MultiDataframe object.

    @param source_object: object to be type casted / converted.
    @type source_object: dataframe.Dataframe object
    @return: dataframe.MultiDataframe object
    '''
    mdf = MultiDataframe()
    mdf.addDataframe(source_object, False)
    return mdf

def tc_MultiDataframe_Dataframe(source_object, dataframe_name):
    '''
    Function to convert from dataframe.MultiDataframe object to
    dataframe.Dataframe object.

    @param source_object: object to be type casted / converted.
    @type source_object: dataframe.MultiDataframe object
    @param dataframe_name: name of dataframe to extract
    @type dataframe_name: string
    @return: dataframe.Dataframe object
    '''
    return source_object.frames[dataframe_name]

def tc_Series_List(source_object, item='data'):
    '''
    Function to convert from dataframe.Series object to a list.

    @param source_object: object to be type casted / converted.
    @type source_object: dataframe.Series object
    @param item: item type to be converted into a list. Allowable items are
    'data' and 'label'. Default = data.
    @type item: string
    @return: list.
    '''
    if item == 'data':
        return source_object.data
    if item == 'label':
        return source_object.label

def tc_Series_Vector(source_object, item='data'):
    '''
    Function to convert from dataframe.Series object to a matrix.Vector
    object.

    @param source_object: object to be type casted / converted.
    @type source_object: dataframe.Series object
    @param item: item type to be converted into a list. Allowable items are
    'data' and 'label'. Default = data.
    @type item: string
    @return: matrix.Vector object.
    '''
    if item == 'data':
        return Vector(source_object.data)
    if item == 'label':
        return Vector(source_object.label)

def tc_Series_Dictionary(source_object):
    '''
    Function to convert from dataframe.Series object to a dictionary.

    @param source_object: object to be type casted / converted.
    @type source_object: dataframe.Series object
    @return: dictionary where key is the label and value is the data value.
    '''
    data = {}
    for index in range(len(source_object.label)):
        data[source_object.label[index]] = source_object.data[index]
    return data

def tc_Vector_List(source_object):
    '''
    Function to convert from matrix.Vector object to a list.

    @param source_object: object to be type casted / converted.
    @type source_object: matrix.Vector object
    @return: list.
    '''
    return source_object.values

def tc_Vector_Dictionary(source_object):
    '''
    Function to convert from matrix.Vector object to a dictionary.

    @param source_object: object to be type casted / converted.
    @type source_object: matrix.Vector object
    @return: dictionary where key is the index and value is the data value.
    '''
    data = {}
    values = source_object.values
    for index in range(len(values)):
        data[index] = values[index]
    return data

def tc_Vector_Series(source_object):
    '''
    Function to convert from matrix.Vector object to a dataframe.Series
    object.

    @param source_object: object to be type casted / converted.
    @type source_object: matrix.Vector object
    @return: dataframe.Series object.
    '''
    series = Series()
    series.addData(source_object.values)
    return series

def tc_List_Dictionary(source_object):
    '''
    Function to convert from list to a dictionary.

    @param source_object: object to be type casted / converted.
    @type source_object: list
    @return: dictionary where key is the index and value is the data value.
    '''
    data = {}
    for index in range(len(source_object)):
        data[index] = source_object[index]
    return data

'''
Matrix Data Structures and Algorithms.

Date created: 19th March 2008

Licence: Python Software Foundation License version 2
'''

import types
import operator
import math
import random
from .copadsexceptions import VectorError
from .copadsexceptions import MatrixError

class Vector(object):
    '''
    A list based vector class, based on the implementation by A. Pletzer
    (http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/52272), that
    supports elementwise mathematical operations.
    '''
    def __init__(self, values=[]):
        '''
        Constructor method.

        @param values: values for the vector. Default is empty list.
        @type values: list
        '''
        self.values = [float(x) for x in values]

    def zeros(self, num_of_elements):
        '''
        Method to initiate the vector to a vector of zeros.

        @param num_of_elements: length of the vector to initiate.
        @type num_of_elements: integer
        '''
        self.values = [0.0] * int(num_of_elements)

    def ones(self, num_of_elements):
        '''
        Method to initiate the vector to a vector of ones.

        @param num_of_elements: length of the vector to initiate.
        @type num_of_elements: integer
        '''
        self.values = [1.0] * int(num_of_elements)

    def random(self, num_of_elements, min_value=0.0, max_value=1.0):
        '''
        Method to initiate the vector to a vector of uniformly distributed
        random values .

        @param num_of_elements: length of the vector to initiate.
        @type num_of_elements: integer
        @param min_value: minimum value of the vector. Default = 0.0.
        @type min_value: float
        @param max_value: maximum value of the vector. Default = 1.0.
        @type max_value: float
        '''
        self.values = [random.uniform(min_value, max_value)
                       for i in int(num_of_elements)]

    def log10(self):
        '''
        Method to perform element-wise log10 on the vector.

        @return: result vector as a list.
        '''
        try:
            values = [math.log10(x) for x in self.values]
        except:
            raise VectorError('Failure in Vector.log10()')
        self.values = values
        return self.values

    def log(self, base=math.e):
        '''
        Method to perform element-wise log on the vector.

        @param base: base value of the logarithmic function. Default = e.
        @type base: float
        @return: result vector as a list.
        '''
        base = float(base)
        try:
            values = [math.log(x, base) for x in self.values]
        except:
            raise VectorError('Failure in Vector.log()')
        self.values = values
        return self.values

    def exp(self):
        '''
        Method to perform element-wise exponential (e to the power of the
        value) on the vector.

        @return: result vector as a list.
        '''
        try:
            values = [math.exp(x) for x in self.values]
        except:
            raise VectorError('Failure in Vector.exp()')
        self.values = values
        return self.values

    def pow(self, n):
        '''
        Method to perform element-wise power (value to the power of n) on
        the vector.

        @param n: exponent to be raised.
        @type n: float
        @return: result vector as a list.
        '''
        n = float(n)
        try:
            values = [float(x)**n for x in self.values]
        except:
            raise VectorError('Failure in Vector.pow()')
        self.values = values
        return self.values

    def sin(self):
        '''
        Method to perform element-wise sine in radians on the vector.

        @return: result vector as a list.
        '''
        try:
            values = [math.sin(x) for x in self.values]
        except:
            raise VectorError('Failure in Vector.sin()')
        self.values = values
        return self.values

    def cos(self):
        '''
        Method to perform element-wise cosine in radians on the vector.

        @return: result vector as a list.
        '''
        try:
            values = [math.cos(x) for x in self.values]
        except:
            raise VectorError('Failure in Vector.cos()')
        self.values = values
        return self.values

    def tan(self):
        '''
        Method to perform element-wise tangent in randians on the vector.

        @return: result vector as a list.
        '''
        try:
            values = [math.tan(x) for x in self.values]
        except:
            raise VectorError('Failure in Vector.tan()')
        self.values = values
        return self.values

    def asin(self):
        '''
        Method to perform element-wise arc sine in radians on the vector.

        @return: result vector as a list.
        '''
        try:
            values = [math.asin(x) for x in self.values]
        except:
            raise VectorError('Failure in Vector.asin()')
        self.values = values
        return self.values

    def acos(self):
        '''
        Method to perform element-wise arc cosine in radians on the vector.

        @return: result vector as a list.
        '''
        try:
            values = [math.acos(x) for x in self.values]
        except:
            raise VectorError('Failure in Vector.a()')
        self.values = values
        return self.values

    def atan(self):
        '''
        Method to perform element-wise arc tangent in radians on the
        vector.

        @return: result vector as a list.
        '''
        try:
            values = [math.atan(x) for x in self.values]
        except:
            raise VectorError('Failure in Vector.atan()')
        self.values = values
        return self.values

    def sinh(self):
        '''
        Method to perform element-wise hyperbolic sine in radians on the
        vector.

        @return: result vector as a list.
        '''
        try:
            values = [math.sinh(x) for x in self.values]
        except:
            raise VectorError('Failure in Vector.sinh()')
        self.values = values
        return self.values

    def cosh(self):
        '''
        Method to perform element-wise hyperbolic cosine in radians on the
        vector.

        @return: result vector as a list.
        '''
        try:
            values = [math.cosh(x) for x in self.values]
        except:
            raise VectorError('Failure in Vector.cosh()')
        self.values = values
        return self.values

    def tanh(self):
        '''
        Method to perform element-wise hyperbolic tangent in radians on the
        vector.

        @return: result vector as a list.
        '''
        try:
            values = [math.tanh(x) for x in self.values]
        except:
            raise VectorError('Failure in Vector.tanh()')
        self.values = values
        return self.values

    def asinh(self):
        '''
        Method to perform element-wise inverse hyperbolic sine in radians
        on the vector.

        @return: result vector as a list.
        '''
        try:
            values = [math.asinh(x) for x in self.values]
        except:
            raise VectorError('Failure in Vector.asinh()')
        self.values = values
        return self.values

    def acosh(self):
        '''
        Method to perform element-wise inverse hyperbolic cosine in radians
        on the vector.

        @return: result vector as a list.
        '''
        try:
            values = [math.acosh(x) for x in self.values]
        except:
            raise VectorError('Failure in Vector.acosh()')
        self.values = values
        return self.values

    def atanh(self):
        '''
        Method to perform element-wise inverse hyperbolic tangent in radians
        on the vector.

        @return: result vector as a list.
        '''
        try:
            values = [math.atanh(x) for x in self.values]
        except:
            raise VectorError('Failure in Vector.atanh()')
        self.values = values
        return self.values

    def sqrt(self):
        '''
        Method to perform element-wise square root on the vector.

        @return: result vector as a list.
        '''
        try:
            values = [math.sqrt(x) for x in self.values]
        except:
            raise VectorError('Failure in Vector.sqrt()')
        self.values = values
        return self.values

    def root(self, n):
        '''
        Method to perform element-wise n-th root on the vector.

        @param n: value of the root.
        @type n: float
        @return: result vector as a list.
        '''
        n = float(n)
        try:
            values = [float(x)**(1.0/float(n)) for x in self.values]
        except:
            raise VectorError('Failure in Vector.root()')
        self.values = values
        return self.values

    def abs(self):
        '''
        Method to perform element-wise absolute on the vector.

        @return: result vector as a list.
        '''
        pass

    def factorial(self):
        '''
        Method to perform element-wise factorial on the vector.

        @return: result vector as a list.
        '''
        pass

    def degrees(self):
        '''
        Method to perform element-wise conversion of values in radians to
        degrees on the vector.

        @return: result vector as a list.
        '''
        pass

    def radians(self):
        '''
        Method to perform element-wise conversion of values in degrees to
        radians on the vector.

        @return: result vector as a list.
        '''
        pass

    def sum(self):
        '''
        Method to perform summation on the vector.

        @return: summation of the vector.
        '''
        pass

    def __setitem__(self, index, value):
        '''
        Method to set element in the vector.

        >>> v = Vector([0, 0, 0])
        >>> v[1] = 15

        @param index: vector index to set the value.
        @param value: value to set.
        '''
        index = int(index)
        self.values[index] = value

    def __getitem__(self, index, default_value=None):
        '''
        Method to get element in the vector.

        >>> v = Vector([0, 0, 0])
        >>> v[1] = 15
        >>> v[1]
        15
        >>> v[5]
        None

        @param index: vector index to get the value.
        @param default_value: the default value to return when the
        coordinate is not present. Default = None
        @return: value of the index (if present); or else, return
        default_value.
        '''
        try:
            return self.values[int(index)]
        except IndexError:
            return default_value

    def __add__(self, vectorX):
        '''
        Method to add a vector (of the same size) to the currect vector.
        The resulting vector will be the result of element-wise addition.

        @param vectorX: vector to be added.
        @type vectorX: copads.matrix.Vector object
        @return: resulting copads.matrix.Vector object
        '''
        if len(self.values) != len(vectorX.values):
            raise VectorError('Vectors have different sizes')
        try:
            values = [self.values[i] + vectorX.values[i]
                      for i in range(len(self.values))]
            return Vector(values)
        except:
            raise VectorError('Failure in Vector.__add__()')

    def add(self, vectorX):
        '''
        Alias to Vector.__add__(vectorX) method: add a vector (of the
        same size) to the currect vector. The resulting vector will be the
        result of element-wise addition.

        @param vectorX: vector to be added.
        @type vectorX: copads.matrix.Vector object
        @return: resulting copads.matrix.Vector object
        '''
        return self.__add__(vectorX)

    def __neg__(self):
        '''
        Method to negate the currect vector. The resulting vector will be
        the result of element-wise negation.

        @return: resulting copads.matrix.Vector object
        '''
        pass

    def negate(self):
        '''
        Alias to Vector.__neg__() method: negate the currect vector. The
        resulting vector will be the result of element-wise negation.

        @return: resulting copads.matrix.Vector object
        '''
        return self.__neg__()

    def __sub__(self, vectorX):
        '''
        Method to subtract a vector (of the same size) from the currect
        vector. The resulting vector will be the result of element-wise
        subtraction.

        @param vectorX: vector to be subtracted.
        @type vectorX: copads.matrix.Vector object
        @return: resulting copads.matrix.Vector object
        '''
        pass

    def subtract(self, vectorX):
        '''
        Alias to Vector.__sub__(vectorX) method: subtract a vector (of
        the same size) from the currect vector. The resulting vector will
        be the result of element-wise subtraction.

        @param vectorX: vector to be subtracted.
        @type vectorX: copads.matrix.Vector object
        @return: resulting copads.matrix.Vector object
        '''
        return self.__sub__(vectorX)

    def __mul__(self, vectorX):
        '''
        Method to multiply a vector (of the same size) to the currect
        vector. The resulting vector will be the result of element-wise
        multiplication.

        @param vectorX: vector to be multiplied.
        @type vectorX: copads.matrix.Vector object
        @return: resulting copads.matrix.Vector object
        '''
        pass

    def multiply(self, vectorX):
        '''
        Alias to Vector.__mul__(vectorX) method: multiply a vector (of the
        same size) to the currect vector. The resulting vector will be the
        result of element-wise multiplication.

        @param vectorX: vector to be multiplied.
        @type vectorX: copads.matrix.Vector object
        @return: resulting copads.matrix.Vector object
        '''
        return self.__mul__(vectorX)

    def __div__(self, vectorX):
        '''
        Method to divide a vector (of the same size) from the currect
        vector. The resulting vector will be the result of element-wise
        division.

        @param vectorX: vector to be divided.
        @type vectorX: copads.matrix.Vector object
        @return: resulting copads.matrix.Vector object
        '''
        pass

    def divide(self, vectorX):
        '''
        Alias to Vector.__mul__(vectorX) method: divide a vector (of the
        same size) from the currect vector. The resulting vector will be
        the result of element-wise division.

        @param vectorX: vector to be divided.
        @type vectorX: copads.matrix.Vector object
        @return: resulting copads.matrix.Vector object
        '''
        return self.__div__(vectorX)


class Matrix(object):
    '''
    A Matrix class that is implemented as a sparse matrix.

    Mathematically speaking, there is no difference between a dense matrix
    (most values are non-zero) and a sparse matrix (most values are zero).
    However, there are implementation differences and memory usage
    differences between sparse and dense matrix. In this case, this
    implementation considers all matrix as sparse and stores the values in
    a coordinate list.

    This class is based on the work of Bill McNeill (http://
    aspn.activestate.com/ASPN/Cookbook/Python/Recipe/189971) and Alexander
    Pletzer (http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/52275).
    '''

    def __init__(self, *args):
        '''
        Constructor method. Bear in mind that Python uses zero-index; that
        is, the first element of the first row is has the coordinate of
        (0,0) rather than (1,1) in regular matrix notations.

        There are 4 ways to construct a matrix.

        Firstly, a null matrix (no data elements) can be constructed as

        >>> m = Matrix()

        Secondly, a zero matrix can be constructed as

        >>> m = Matrix(2)

        This will result in a zero square matrix, [[0, 0], [0, 0]]

        A non-square matrix can be constructed by providing the (row,
        column) pairs. For example,

        >>> m = Matrix(2, 3)

        will result in [[0, 0, 0], [0, 0, 0]]

        Thirdly, a matrix can be constructed by providing a list of list in
        the format of [[first row], [second row], ... [last row]]

        >>> m = Matrix([[1, 2, 3], [4, 5, 6]])

        Lastly, a matrix can be provided by providing a dictionary
        non-zero values using (row, column) as key,

        >>> m = Matrix({(0,0): 3,
        ...             (1,1): 6})

        will result in [[3, 0], [0, 6]].

        @param args: arguments for matrix construction. Please see above
        for description.
        '''
        self.values = {}
        self.dimensions = [0, 0]
        if len(args) == 0:
            pass
        if len(args) == 1 and isinstance(args[0], types.IntType):
            self.createNullMatrix(args[0], args[0])
        if len(args) == 2 and isinstance(args[0], types.IntType) and \
            isinstance(args[1], types.IntType):
            self.createNullMatrix(args[0], args[1])
        if len(args) == 1 and isinstance(args[0], types.ListType):
            for row in range(len(args[0])):
                if isinstance(args[0][row], types.ListType):
                    self.addReplaceRow(row, args[0][row])
            self.updateDimensions()
        if len(args) == 1 and isinstance(args[0], types.DictType):
            for k in args[0].keys():
                self.addReplaceElement(k, args[0][k])
            self.updateDimensions()

    def updateDimensions(self):
        '''
        Method to update the dimension of the matrix.
        '''
        row_count = set()
        column_count = set()
        for coordinate in self.values.keys():
            row_count.update([coordinate[0]])
            column_count.update([coordinate[1]])
        self.dimensions[0] = max(list(row_count)) + 1
        self.dimensions[1] = max(list(column_count)) + 1

    def createNullMatrix(self, rows, columns):
        '''
        Method to create a null (zero) matrix.

        @param rows: number of rows.
        @type rows: integer
        @param columns: number of columns.
        @type columns: integer
        '''
        rows = int(rows)
        columns = int(columns)
        for r in range(rows):
            for c in range(columns):
                self.values[(r, c)] = 0
        self.dimensions = [rows, columns]

    def createIdentityMatrix(self, size):
        '''
        Method to create an identity matrix.

        @param size: size (number of rows and columns) of identity matrix.
        @type size: integer
        '''
        size = int(size)
        for r in range(size):
            for c in range(size):
                if r == c:
                    self.values[(r, c)] = 1.0
                else:
                    self.values[(r, c)] = 0.0
        self.dimensions = [size, size]

    def addReplaceRow(self, row_number, row_data, update_dimensions=False):
        '''
        Method to add a row (if the row does not exist) or to replace a row
        (if the row exist) in the matrix.

        @param row_number: the row number to add or replace, based on
        zero-index (the first row is zero-th row).
        @type row_number: integer
        @param row_data: data for the row to add or replace.
        @type row_data: list
        @param update_dimensions: flag to determine whether to update
        matrix dimensions, which can reduce speed if matrix is large.
        Default = false (dimensions not updated).
        @type update_dimensions: boolean
        '''
        row_number = int(row_number)
        for c in range(len(row_data)):
            self.values[(row_number, c)] = row_data[c]
        if update_dimensions:
            self.updateDimensions()

    def addReplaceElement(self, coordinate, value, update_dimensions=False):
        '''
        Method to add an element (if the element does not exist) or to
        replace the element (if the element exist) in the matrix.

        @param coordinate: (row, column) coordinate to add or replace,
        based on zero-th index (first element of first row is zero-th row
        zero-th column).
        @type coordinate: list or tuple
        @param value: value of the coordinate to add or replace.
        @param update_dimensions: flag to determine whether to update
        matrix dimensions, which can reduce speed if matrix is large.
        Default = false (dimensions not updated).
        @type update_dimensions: boolean
        '''
        if len(coordinate) == 2:
            r = int(coordinate[0])
            c = int(coordinate[1])
            self.values[(r, c)] = value
        if update_dimensions:
            self.updateDimensions()

    def __setitem__(self, index, value):
        '''
        Method to set element in the matrix.

        >>> m = Matrix()
        >>> m[(1,1)] = 15

        @param index: row and column (row, column) to set the value.
        @param value: value to set.
        '''
        self.addReplaceElement((index[0], index[1]), value, False)

    def __getitem__(self, index, default_value=None):
        '''
        Method to get element in the matrix.

        >>> m = Matrix()
        >>> m[(1,1)] = 15
        >>> m[(1,1)]
        15
        >>> m[(0,0)]
        None

        @param index: row and column (row, column) to get the value.
        @param default_value: the default value to return when the
        coordinate is not present. Default = None
        @return: value of the coordinate (if present); or else, return
        default_value.
        '''
        try:
            return self.values[(index[0], index[1])]
        except KeyError:
            return default_value

    def row(self, row_count, default_value=None, update_dimensions=False):
        '''
        Method to get the values for a specific row in the matrix.

        >>> m = m.Matrix()
        >>> m[(0,0)] = 1
        >>> m[(1,1)] = 2
        >>> m.updateDimensions()
        >>> m.row(0, None)
        [1, None]
        >>> m.row(0, 0)
        [1, 0]

        @param row_count: index of row (zero index) to get data.
        @type row_count: integer
        @param default_value: the default value to return when the
        coordinate is not present. Default = None.
        @param update_dimensions: flag to determine whether to update
        matrix dimensions, which can reduce speed if matrix is large.
        Default = false (dimensions not updated).
        @type update_dimensions: boolean
        @return: row vector in list.
        '''
        if update_dimensions:
            self.updateDimensions()
        row_count = int(row_count)
        num_of_cols = self.dimensions[1]
        return [self.__getitem__((row_count, c), default_value)
                for c in range(num_of_cols)]

    def column(self, column_count, default_value=None,
               update_dimensions=False):
        '''
        Method to get the values for a specific column in the matrix.

        >>> m = m.Matrix()
        >>> m[(0,0)] = 1
        >>> m[(1,1)] = 2
        >>> m.updateDimensions()
        >>> m.column(0, None)
        [1, None]
        >>> m.column(0, 0)
        [1, 0]

        @param column_count: index of column (zero index) to get data.
        @type column_count: integer
        @param default_value: the default value to return when the
        coordinate is not present. Default = None.
        @param update_dimensions: flag to determine whether to update
        matrix dimensions, which can reduce speed if matrix is large.
        Default = false (dimensions not updated).
        @type update_dimensions: boolean
        @return: column vector in list.
        '''
        if update_dimensions:
            self.updateDimensions()
        column_count = int(column_count)
        num_of_rows = self.dimensions[0]
        return [self.__getitem__((r, column_count), default_value)
                for r in range(num_of_rows)]

    def diagonal(self, default_value=None, update_dimensions=False):
        '''
        Method to get the diagonal values of the matrix.

        @param default_value: the default value to return when the
        coordinate is not present. Default = None.
        @param update_dimensions: flag to determine whether to update
        matrix dimensions, which can reduce speed if matrix is large.
        Default = false (dimensions not updated).
        @type update_dimensions: boolean
        @return: list of the diagonal values of the matrix.
        '''
        if update_dimensions:
            self.updateDimensions()
        return [self.__getitem__((index, index), default_value)
                for index in range(max(self.dimensions))]

    def trace(self):
        '''
        Method to calculate the trace (summation of diagonals from M[0][0]
        to M[i][i]) of the matrix.

        @return: trace of matrix.
        '''
        values = self.diagonal(0, True)
        return sum(values)

    def transpose(self):
        '''
        Method to generate tranposition of the matrix.

        @return: transposed matrix.
        '''
        result = Matrix()
        for k in self.values.keys():
            result[(k[1], k[0])] = self.values[k]
        return result

    def _addScalar(self, itemX):
        '''
        Private method for scalar addition where each element (non-None) in
        the matrix is added by a scalar value.

        @param itemX: scalar value to add.
        @type itemX: integer or float
        @return: result of addition in Matrix object.
        '''
        result = Matrix()
        for k in self.values.keys():
            result.values[k] = itemX + self.values[k]
        return result

    def _addMatrix(self, itemX):
        '''
        Private method for matrix addition where each element (non-None) to
        the current matrix.

        @param itemX: matrix to add.
        @type itemX: copads.matrix.Matrix object
        @return: result of addition in Matrix object.
        '''
        mkeys = self.values.keys()
        xkeys = itemX.values.keys()
        result = Matrix()
        for mk in [k for k in mkeys if k not in xkeys]:
            result.values[mk] = self.values[mk]
        for xk in [k for k in xkeys if k not in mkeys]:
            result.values[xk] = itemX.values[xk]
        for ck in [k for k in xkeys if k in mkeys]:
            result.values[ck] = self.values[ck] + itemX.values[ck]
        return result

    def add(self, itemX):
        '''
        Alias to Matrix.__add__(itemX) method: add a matrix or a scalar
        value to the current matrix.

        @param itemX: matrix or scalar value (integer or float) to add.
        @return: result of addition in Matrix object.
        '''
        return self.__add__(itemX)

    def __add__(self, itemX):
        '''
        Method to add a matrix or a scalar value to the current matrix.

        @param itemX: matrix or scalar value (integer or float) to add.
        @return: result of addition in Matrix object.
        '''
        if isinstance(itemX, Matrix):
            return self._addMatrix(itemX)
        elif isinstance(itemX, types.IntType) or \
            isinstance(itemX, types.FloatType):
            return self._addScalar(itemX)



# class Matrix:
    # """
    # A linear algebra matrix

    # This class defines a generic matrix and the basic matrix operations from
    # linear algebra.  An instance of this class is a single matrix with
    # particular values.

    # Arithmetic operations, trace, determinant, and minors are defined. This is a
    # lightweight alternative to a numerical Python package for people who need to do
    # basic linear algebra.

    # Vectors are implemented as 1xN and Nx1 matricies.  There is no separate vector
    # class.  This implementation enforces the distinction between row and column
    # vectors.

    # Indexing is zero-based, i.e. the upper left-hand corner of a matrix is element
    # (0,0), not element (1,1).

    # Matricies are stored as a list of lists, where the top level lists are the rows
    # and the sub-lists are the columns.  Because of the way Python handles list
    # references, you have be careful when copying matrix objects.  If you have a
    # matrix a, assign b=a, and then change values in b, you will change values in a
    # as well.  Matrix copying should be done with copy.deepcopy.

    # This implementation has no memory-saving optimization for sparse matricies.  A
    # derived class may implement a more sophisticated storage method by overriding
    # the __getitem__ and __setitem__ functions.

    # Determinants are taken by expanding by minors on the top row.  The private
    # functions supplied for expansion by minors are more generic than what is needed
    # by this implementation.  They may be used by a derived class that wishes to do
    # more efficient expansion of sparse matricies.

    # By default, Matrix elements are members of the complex field, but if you want
    # to perform linear algebra on something other than numbers you may redefine
    # Matrix.null_element, Matrix.identity_element, and Matrix.inverse_element and
    # override the is_scalar_element function.

    # References
    # George Arfken, "Mathematical Methods for Physicists", 3rd ed. San Diego.
    # Academic Press Inc. (1985)

    # Adapted from: http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/189971
    # Original author: Bill McNeill <billmcn@speakeasy.net>

    # Maintainer: Maurice H.T. Ling <mauriceling@acm.org>
    # Copyright (c) 2005 Maurice H.T. Ling <mauriceling@acm.org>
    # Date: 1st May 2005
    # """
    # null_element = 0
    # identity_element = 1
    # inverse_element = -1

    # def __str__(self):
        # s = ""
        # for row in self.m:
            # s += "%s\n" % row
        # return s

    # def __cmp__(self, other):
        # if not isinstance(other, Matrix):
            # raise TypeError("Cannot compare matrix with %s" % type(other))
        # return cmp(self.m, other.m)

    # def __neg__(self):
        # """Negate the current matrix"""
        # return self.inverse_element*self

    # def __sub__(self, other):
        # """Subtract matrix self - other"""
        # return self + -other

    # def __mul__(self, other):
        # """Multiply matrix self*other

        # other can be another matrix or a scalar.
        # """
        # if self.isScalarElement(other):
            # return self.scalarMultiply(other)
        # if not isinstance(other, Matrix):
            # raise TypeError("Cannot multiply matrix and type %s" % type(other))
        # if other.isRowVector():
            # raise MatrixMultiplicationError(self, other)
        # return self.matrixMultiply(other)

    # def __rmul__(self, other):
        # """Multiply other*self

        # This is only called if other.__add__ is not defined, so assume that
        # other is a scalar.
        # """
        # if not self.isScalarElement(other):
            # raise TypeError("Cannot right-multiply by %s" % type(other))
        # return self.scalarMultiply(other)

    # def scalarMultiply(self, scalar):
        # """Multiply the matrix by a scalar value.

        # This is a private function called by __mul__ and __rmul__.
        # """
        # r = []
        # for row in self.m:
            # r.append(map(lambda x: x*scalar, row))
        # return Matrix(r)

    # def matrixMultiply(self, other):
        # """Multiply the matrix by another matrix.

        # This is a private function called by __mul__.
        # """
        # # Take the product of two matricies.
        # r = []
        # assert(isinstance(other, Matrix))
        # if not self.cols() == other.rows():
            # raise MatrixMultiplicationError(self, other)
        # for row in xrange(self.rows()):
            # r.append([])
            # for col in xrange(other.cols()):
                # r[row].append( self.vectorInnerProduct(self.row(row),
                                                       # other.col(col)))
        # if len(r) == 1 and len(r[0]) == 1:
            # # The result is a scalar.
            # return r[0][0]
        # else:
            # # The result is a matrix.
            # return Matrix(r)

    # def isRowVector(self):
        # """Is the matrix a row vector?"""
        # return self.rows() == 1 and self.cols() > 1

    # def isColumnVector(self):
        # """Is the matrix a column vector?"""
        # return self.cols() == 1 and self.rows() > 1

    # def isSquare(self):
        # """Is the matrix square?"""
        # return self.rows() == self.cols()

    # def determinant(self):
        # """The determinant of the matrix"""
        # if not self.isSquare():
            # raise MatrixDeterminantError()
        # # Calculate 2x2 determinants directly.
        # if self.rows() == 2:
            # return self[(0, 0)]*self[(1, 1)] - self[(0, 1)]*self[(1, 0)]
        # # Expand by minors for larger matricies.
        # return self.expandByMinorsOnRow(0)

    # def expandByMinorsOnRow(self, row):
        # """Calculates the determinant by expansion of minors

        # This function returns the determinant of the matrix by doing an
        # expansion of minors on the specified row.
        # """
        # assert(row < self.rows())
        # d = 0
        # for col in xrange(self.cols()):
            # # Note: the () around -1 are needed.  Otherwise you get -(1**col).
            # d += (-1)**(row+col)* \
                # self[(row, col)]*self.minor(row, col).determinant()
        # return d

    # def expandByMinorsOnColumn(self, col):
        # """Calculates the determinant by expansion of minors

        # This function returns the determinant of the matrix by doing an
        # expansion of minors on the specified column.
        # """
        # assert(col < self.cols())
        # d = 0
        # for row in xrange(self.rows()):
            # # Note: the () around -1 are needed.  Otherwise you get -(1**col).
            # d += (-1)**(row+col) \
                # *self[(row, col)]*self.minor(row, col).determinant()
        # return d

    # def minor(self, i, j):
        # """A minor of the matrix

        # This function returns the minor given by striking out row i and
        # column j of the matrix.
        # """
        # # Verify parameters.
        # if not self.isSquare():
            # raise MatrixMinorError()
        # if i<0 or i>=self.rows():
            # raise ValueError("Row value %d is out of range" % i)
        # if j<0 or j>=self.cols():
            # raise ValueError("Column value %d is out of range" % j)
        # # Create the output matrix.
        # m = Matrix(self.rows()-1, self.cols()-1)
        # # Loop through the matrix, skipping over the row and column specified
        # # by i and j.
        # minor_row = 0
        # minor_col = 0
        # for self_row in xrange(self.rows()):
            # if not self_row == i:    # Skip row i.
                # for self_col in xrange(self.cols()):
                    # if not self_col == j:    # Skip column j.
                        # m[(minor_row, minor_col)] = self[(self_row, self_col)]
                        # minor_col = minor_col + 1
                # minor_col = 0
                # minor_row = minor_col + 1
        # return m

    # def minorMatrix(self):
        # """
        # Calculates minor matrix
        # """
        # m = Matrix(self.rows(), self.cols())
        # for row in range(self.rows()):
            # for col in range(self.cols()):
                # minor_matrix = self.minor(row, col)
                # m[(row, col)] = minor_matrix.determinant()
        # return m

    # def adjoint(self):
        # """
        # Calculates adjoint matrix
        # """
        # m = Matrix(self.rows(), self.cols())
        # for row in range(self.rows()):
            # for col in range(self.cols()):
                # minor_matrix = self.minor(row, col)
                # det = minor_matrix.determinant()
                # m[(row, col)] = ((-1)**(row+col)) * det
        # return m

    # def inverse(self):
        # """
        # Calculates inverse matrix
        # """
        # det = float(self.determinant())
        # adj = self.adjoint()
        # return adj.scalarMultiply(1/det)

    # def vectorInnerProduct(self, a, b):
        # """Takes the inner product of vectors a and b

        # a and b are lists.
        # This is a private function called by matrix_multiply.
        # """
        # assert(isinstance(a, types.ListType))
        # assert(isinstance(b, types.ListType))
        # return reduce(operator.add, map(operator.mul, a, b))

    # def isScalarElement(self, x):
        # """Is x a scalar

        # By default a scalar is an element in the complex number field.
        # A class that wants to perform linear algebra on things other than
        # numbers may override this function.
        # """
        # return isinstance(x, types.IntType) or \
                # isinstance(x, types.FloatType) or \
                # isinstance(x, types.ComplexType)

# class SparseMatrix(dict):
    # """
    # A sparse matrix class based on a dictionary, supporting matrix (dot)
    # product and a conjugate gradient solver.

    # In this version, the sparse class inherits from the dictionary; this
    # requires Python 2.2 or later.

    # Adapted from http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/52275
    # Original author: Alexander Pletzer

    # Dictionary storage format { (i,j): value, ... }
    # where (i,j) are the matrix indices
           # """

    # # no c'tor
    # def size(self):
        # " returns # of rows and columns "
        # nrow = 0
        # ncol = 0
        # for key in list(self.keys()):
            # nrow = max([nrow, key[0]+1])
            # ncol = max([ncol, key[1]+1])
        # return (nrow, ncol)

    # def __add__(self, other):
        # res = SparseMatrix(self.copy())
        # for ij in other:
            # res[ij] = self.get(ij, 0.) + other[ij]
        # return res

    # def __neg__(self):
        # return SparseMatrix(zip(list(self.keys()),
                            # map(operator.neg, list(self.values()))))

    # def __sub__(self, other):
        # res = SparseMatrix(self.copy())
        # for ij in other:
            # res[ij] = self.get(ij, 0.) - other[ij]
        # return res

    # def __mul__(self, other):
        # " element by element multiplication: other can be scalar or sparse "
        # try:
            # # other is sparse
            # nval = len(other)
            # res = SparseMatrix()
            # if nval < len(self):
                # for ij in other:
                    # res[ij] = self.get(ij, 0.)*other[ij]
            # else:
                # for ij in self:
                    # res[ij] = self[ij]*other.get(ij, 0j)
            # return res
        # except:
            # # other is scalar
            # return SparseMatrix(zip(list(self.keys()),
                                # map(lambda x: x*other, list(self.values()))))

    # def __rmul__(self, other):
        # return self.__mul__(other)

    # def __div__(self, other):
        # " element by element division self/other: other is scalar"
        # return SparseMatrix(zip(list(self.keys()),
                            # map(lambda x: x/other, list(self.values()))))

    # def __rdiv__(self, other):
        # " element by element division other/self: other is scalar"
        # return SparseMatrix(zip(list(self.keys()),
                            # map(lambda x: other/x, list(self.values()))))



    # def CGsolve(self, x0, b, tol=1.0e-10, nmax = 1000, verbose=1):
        # """
        # Solve self*x = b and return x using the conjugate gradient method
        # """
        # if not isVector(b):
            # raise TypeError, self.__class__, ' in solve '
        # else:
            # if self.size()[0] != len(b) or self.size()[1] != len(b):
                # print('**Incompatible sizes in solve')
                # print('**size()=', self.size()[0], self.size()[1])
                # print('**len=', len(b))
            # else:
                # kvec = diag(self) # preconditionner
                # n = len(b)
                # x = x0 # initial guess
                # r = b - sm_dot(self, x)
                # try:
                    # w = r/kvec
                # except: print('***singular kvec')
                # p = v_zeros(n)
                # beta = v_dot(r, w)
                # err = v_norm(dot(self, x) - b)
                # k = 0
                # if verbose: print(" conjugate gradient convergence (log error)")
                # while abs(err) > tol and k < nmax:
                    # p = w + beta*p
                    # z = sm_dot(self, p)
                    # alpha = rho/v_dot(p, z)
                    # r = r - alpha*z
                    # w = r/kvec
                    # rhoold = rho
                    # rho = v_dot(r, w)
                    # x = x + alpha*p
                    # beta = rho/rhoold
                    # err = v_norm(dot(self, x) - b)
                    # if verbose:
                        # print(k, ' %5.1f ' % math.log10(err))
                    # k = k+1
                # return x

    # def biCGsolve(self, x0, b, tol=1.0e-10, nmax = 1000):
        # """
        # Solve self*x = b and return x using the bi-conjugate gradient method
        # """

        # try:
            # if not isVector(b):
                # raise TypeError, self.__class__, ' in solve '
            # else:
                # if self.size()[0] != len(b) or self.size()[1] != len(b):
                    # print('**Incompatible sizes in solve')
                    # print('**size()=', self.size()[0], self.size()[1])
                    # print('**len=', len(b))
                # else:
                    # kvec = sm_diag(self) # preconditionner
                    # n = len(b)
                    # x = x0 # initial guess
                    # r = b - sm_dot(self, x)
                    # rbar = r
                    # w = r/kvec
                    # wbar = rbar/kvec
                    # p = v_zeros(n)
                    # pbar = v_zeros(n)
                    # beta = 0.0
                    # rho = v_dot(rbar, w)
                    # err = v_norm(dot(self, x) - b)
                    # k = 0
                    # print(" bi-conjugate gradient convergence (log error)")
                    # while abs(err) > tol and k < nmax:
                        # p = w + beta*p
                        # pbar = wbar + beta*pbar
                        # z = dot(self, p)
                        # alpha = rho/v_dot(pbar, z)
                        # r = r - alpha*z
                        # rbar = rbar - alpha* sm_dot(pbar, self)
                        # w = r/kvec
                        # wbar = rbar/kvec
                        # rhoold = rho
                        # rho = v_dot(rbar, w)
                        # x = x + alpha*p
                        # beta = rho/rhoold
                        # err = v_norm(sm_dot(self, x) - b)
                        # print(k, ' %5.1f ' % math.log10(err))
                        # k = k+1
                    # return x
        # except:
            # print('ERROR ', self.__class__, '::biCGsolve')

    # def save(self, filename, OneBased=0):
        # """
        # Save matrix in file <filaname> using format
        # OneBased, nrow, ncol, nnonzeros
        # [ii, jj, data]
        # """
        # m = n = 0
        # nnz = len(self)
        # for ij in list(self.keys()):
            # m = max(ij[0], m)
            # n = max(ij[1], n)

        # f = open(filename, 'w')
        # f.write('%d %d %d %d\n' % (OneBased, m+1, n+1, nnz))
        # for ij in list(self.keys()):
            # i, j = ij
            # f.write('%d %d %20.17f \n'% \
                # (i+OneBased, j+OneBased, self[ij]))
        # f.close()


# def vDot(a, b):
    # """dot product of two vectors."""
    # try: return reduce(lambda x, y: x+y, a*b, 0.)
    # except: raise TypeError, 'Vector::FAILURE in dot'

# def vNorm(a):
    # """Computes the norm of vector a."""
    # try: return math.sqrt(abs(dot(a, a)))
    # except: raise TypeError, 'vector::FAILURE in norm'

# def vSum(a):
    # """Returns the sum of the elements of a."""
    # try: return reduce(lambda x, y: x+y, a, 0)
    # except: raise TypeError, 'vector::FAILURE in sum'

# def smDotDot(y, a, x):
    # """double dot product y^+ *A*x """
    # if Vector.isVector(y) and isSparse(a) and Vector.isVector(x):
        # res = 0.
        # for ij in list(a.keys()):
            # i, j = ij
            # res += y[i]*a[ij]*x[j]
        # return res
    # else:
        # print('sparse::Error: dotDot takes vector, sparse , vector as args')

# def smDot(a, b):
    # """vector-matrix, matrix-vector or matrix-matrix product"""
    # if isSparse(a) and isVector(b):
        # new = v_zeros(a.size()[0])
        # for ij in list(a.keys()):
            # new[ij[0]] += a[ij]* b[ij[1]]
        # return new
    # elif isVector(a) and isSparse(b):
        # new = v_zeros(b.size()[1])
        # for ij in list(b.keys()):
            # new[ij[1]] += a[ij[0]]* b[ij]
        # return new
    # elif isSparse(a) and isSparse(b):
        # if a.size()[1] != b.size()[0]:
            # print('**Warning shapes do not match in dot(sparse, sparse)')
        # new = SparseMatrix({})
        # n = min([a.size()[1], b.size()[0]])
        # for i in range(a.size()[0]):
            # for j in range(b.size()[1]):
                # sum = 0.
                # for k in range(n):
                    # sum += a.get((i, k), 0.)*b.get((k, j), 0.)
                # if sum != 0.:
                    # new[(i, j)] = sum
        # return new
    # else:
        # raise TypeError, 'in dot'


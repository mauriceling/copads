"""
File containing classes for use in graph algorithms.

Copyright (c) Maurice H.T. Ling <mauriceling@acm.org>
Date created: 17th August 2005
"""

from Matrix import Matrix
from JMathsExceptions import VertexNotFoundError, NotAdjacencyGraphMatrixError
from JMathsExceptions import GraphEdgeSizeMismatchError, GraphParameterError


class Graph:
    """
    Class to encapsulate a Graph object. A graph is defined as a connected network of nodes (also known
    as vertex or vertices for plural), where each connection is known as an edge. Graph class uses 2 
    lists to hold the information for a graph:
        1. a list of vertices or nodes (Graph.vertices)
        2. a list of tuples of vertices which forms an edge (Graph.edges)
    
    Graph.outedge and Graph.inedge are effectively meaningful when Graph.directed is set to true, 
    signifying a directed graph. Otherwise, Graph.outedge and Graph.inedge only signifies two 2 ends of
    an edge.
    """
    vertices = []
    edges = []
    directed = False
    graph_dict = {}
    def __init__(self, EdgeList = None, vertexList = None):
        """
        Constructor method for Graph object. It takes 2 parameters, EdgeList and vertexList. Parameters 
        outEdgeList and inEdgeList must be provided, while vertexList is optional. If vertexList is not 
        provided, it will be generated.
        
        @param EdgeList: list of tuples '(o, i)' of vertices forming an edge where 'o' is the emerging
        vertex of an edge and 'i' is the terminating vertex of a edge in a directed graph
        @param vertexList: list of vertices (optional)
        """
        if not EdgeList and not vertexList:
            raise GraphParameterError('EdgeList and VertexList cannot be both None.')
        index = 0
        for edge in EdgeList:
            if len(edge) < 2 or not edge[0] or not edge[1] or edge[0] == '' or edge[1] == '' or edge[0] == ' ' or edge[1] == ' ':
                raise GraphEdgeSizeMismatchError(index, edge)
            index = index + 1
        self.edges = EdgeList
        if vertexList == None: 
            self._generateVerticesFromEdges()
        else: 
            self.vertices = vertexList
            self.vertices.sort()
    def toAdjacencyMatrix(self):
        """
        Method to convert the graph from a Graph object to its corresponding adjacency matrix of type
        Matrix.Matrix. 
        
        @return (matrix, vertexList): matrix is the adjacency matrix for the graph and vertexList is the
        list of vertices in the graph, where n-th row and column refers to the vertex in vertexList[n].
        """
        matrix = Matrix(len(self.vertices), len(self.vertices))
        for edge in self.edges:
            outedge = self.vertices.index(edge[0])
            inedge = self.vertices.index(edge[1])
            matrix[(outedge, inedge)] = 1
        return (matrix, self.vertices)
    def toIncidenceMatrix(self):
        pass
    def _generateVerticesFromEdges(self):
        """
        Method called by Graph.__init__() method to generate a list of vertices for Graph.vertices if
        it is not provided.
        """
        vDict = {}
        for edge in self.edges: 
            vDict[edge[0]] = ''
            vDict[edge[1]] = ''
        self.vertices = vDict.keys()
        self.vertices.sort()
    def verticesNumber(self):
        """Returns the number of vertices in the graph."""
        return len(self.vertices)
    def edgeNumber(self):
        """Returns the number of edges in the graph."""
        return len(self.edges)
        
        
class GraphAdjacencyMatrix(Matrix):
    adjacency = None
    verticesList = None
    def __init__(self, verticesList = None, data = None):
        if data.is_square(): self.adjacency = data
        else: raise NotAdjacencyGraphMatrixError()
        if verticesList == None: self.verticesList = range(data.cols())
        else: self.verticesList = verticesList
    def toGraph(self):
        pass
    def toIncidenceMatrix(self):
        pass
        
  
class GraphIncidenceMatrix(Matrix):
      incidence = None
      def __init__(self):
          pass
      def toGraph(self):
          pass
      def toAdjacencyMatrix(self):
          pass    
          
  
class GraphCircuitMatrix(Matrix):
      circuit = None
      def __init__(self):
          pass
      def toGraph(self):
          pass
      def toAdjacencyMatrix(self):
          pass  
      def toIncidenceMatrix(self):
          pass
           
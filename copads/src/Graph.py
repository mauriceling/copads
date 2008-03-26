"""
File containing classes for use in graph algorithms.

Copyright (c) Maurice H.T. Ling <mauriceling@acm.org>
Date created: 17th August 2005
"""

from Matrix import Matrix
from PriorityDictionary import PriorityDictionary
from CopadsExceptions import VertexNotFoundError, NotAdjacencyGraphMatrixError
from CopadsExceptions import GraphEdgeSizeMismatchError, GraphParameterError


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
    

def Dijkstra(G,start,end=None):
    """
    Find shortest paths from the start vertex to all
    vertices nearer than or equal to the end.

    The input graph G is assumed to have the following
    representation: A vertex can be any object that can
    be used as an index into a dictionary.  G is a
    dictionary, indexed by vertices.  For any vertex v,
    G[v] is itself a dictionary, indexed by the neighbors
    of v.  For any edge v->w, G[v][w] is the length of
    the edge.  This is related to the representation in
    <http://www.python.org/doc/essays/graphs.html>
    where Guido van Rossum suggests representing graphs
    as dictionaries mapping vertices to lists of neighbors,
    however dictionaries of edges have many advantages
    over lists: they can store extra information (here,
    the lengths), they support fast existence tests,
    and they allow easy modification of the graph by edge
    insertion and removal.  Such modifications are not
    needed here but are important in other graph algorithms.
    Since dictionaries obey iterator protocol, a graph
    represented as described here could be handed without
    modification to an algorithm using Guido's representation.

    Of course, G and G[v] need not be Python dict objects;
    they can be any other object that obeys dict protocol,
    for instance a wrapper in which vertices are URLs
    and a call to G[v] loads the web page and finds its links.
    
    The output is a pair (D,P) where D[v] is the distance
    from start to v and P[v] is the predecessor of v along
    the shortest path from s to v.
    
    Dijkstra's algorithm is only guaranteed to work correctly
    when all edge lengths are positive. This code does not
    verify this property for all edges (only the edges seen
     before the end vertex is reached), but will correctly
    compute shortest paths even for some graphs with negative
    edges, and will raise an exception if it discovers that
    a negative edge has caused it to make a mistake.
    """

    D = {}    # dictionary of final distances
    P = {}    # dictionary of predecessors
    Q = priorityDictionary()   # est.dist. of non-final vert.
    Q[start] = 0
    
    for v in Q:
        D[v] = Q[v]
        if v == end: break
        
        for w in G[v]:
            vwLength = D[v] + G[v][w]
            if w in D:
                if vwLength < D[w]:
                    raise ValueError, \
  "Dijkstra: found better path to already-final vertex"
            elif w not in Q or vwLength < Q[w]:
                Q[w] = vwLength
                P[w] = v
    
    return (D,P)
            
def shortestPath(G,start,end):
    """
    Find a single shortest path from the given start vertex
    to the given end vertex.
    The input has the same conventions as Dijkstra().
    The output is a list of the vertices in order along
    the shortest path.
    """

    D,P = Dijkstra(G,start,end)
    Path = []
    while 1:
        Path.append(end)
        if end == start: break
        end = P[end]
    Path.reverse()
    return Path
       
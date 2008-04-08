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
    graph = {}
    
    def __init__(self, **kwarg):
        if kwarg.has_key('graph'): 
            self.graph = kwarg['graph']
        elif kwarg.has_key('vertices'): 
            self.makeGraphFromVertices(kwarg['vertices'])
        elif kwarg.has_key('edges'): 
            self.makeGraphFromEdges(kwarg['edges'])
        elif kwarg.has_key('adjacency'): 
            self.makeGraphFromAdjacency(kwarg['adjacency'])
        else: self.graph = {}
        
    def makeGraphFromAdjacency(self, adj):
        vertices = adj.pop(0)
        for l in adj:
            if len(l) != len(vertices): raise GraphEdgeSizeMismatchError
        ends = {}
        for row in range(len(adj)):
            for col in range(len(adj[row])):
                if adj[row][col] > 0: ends[vertices[col]] = adj[row][col]
            self.graph[vertices[row]] = ends
            ends.clear()
    
    def makeGraphFromVertices(self, vertices):
        if type(vertices) != list: raise GraphParameterError('Vertices must be a list')
        for vertex in vertices: self.graph[vertex] = {}
            
    def makeGraphFromEdges(self, edges):
        if type(edges) != list: raise GraphParameterError('Edges must be a list of tuples')
        from Set import Set
        usources = list(Set([x[0] for x in edges]))
        for index in range(len(usources)):
            source = usources[index]
            t = [x[1] for x in edges if x[0] == source]
            t = [(end, t.count(end)) for end in list(Set(t))]
            self.graph[usources[index]] = dict(t)
    

    def Dijkstra(self, start,end=None):
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
        Q = PriorityDictionary()   # est.dist. of non-final vert.
        Q[start] = 0
        
        for v in Q:
            D[v] = Q[v]
            if v == end: break
            
            for w in self.graph[v]:
                vwLength = D[v] + self.graph[v][w]
                if w in D:
                    if vwLength < D[w]:
                        raise ValueError, \
      "Dijkstra: found better path to already-final vertex"
                elif w not in Q or vwLength < Q[w]:
                    Q[w] = vwLength
                    P[w] = v
        
        return (D,P)
                
    def shortestPath(self,start,end):
        """
        Find a single shortest path from the given start vertex
        to the given end vertex.
        The input has the same conventions as Dijkstra().
        The output is a list of the vertices in order along
        the shortest path.
        """
    
        D,P = self.Dijkstra(start,end)
        Path = []
        while 1:
            Path.append(end)
            if end == start: break
            end = P[end]
        Path.reverse()
        return Path
       
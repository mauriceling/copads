import unittest
import os
import sys


class testGraph(unittest.TestCase):
    """Unit test cases for Graph.Graph object."""
    def testInitNothing(self):
        try:
            g = Graph()
        except GraphParameterError, e:
            print e
            print "This test 'testInitNothing' is expected to give GraphParameterError" + os.linesep
    
    def testInitNoVertices(self):
        g = Graph(EdgeList = [('a', 'b'), ('a', 'c')])
        assert g.verticesNumber() == 3
        assert g.edgeNumber() == 2
       
    def testEdgeError1(self):
        try:
            g = Graph(EdgeList = [('a', 'b'), ('a', None)])
        except GraphEdgeSizeMismatchError, e:
            print e
            print "This test 'testEdgeError1' is expected to give GraphEdgeSizeMismatchError" + os.linesep
        
    def testEdgeError2(self):
        try: g = Graph(EdgeList = [('a', 'b'), ('a', '')])
        except GraphEdgeSizeMismatchError, e:
            print e
            print "This test 'testEdgeError2' is expected to give GraphEdgeSizeMismatchError" + os.linesep
        
    def testEdgeError3(self):
        try: g = Graph(EdgeList = [(' ', 'b'), ('a', None)])
        except GraphEdgeSizeMismatchError, e:
            print e
            print "This test 'testEdgeError3' is expected to give GraphEdgeSizeMismatchError" + os.linesep
         
    def testAdjacency(self):
        edge = [('a', 'b'), ('a', 'c'), ('a', 'd'), ('a', 'e'), ('b', 'c'), ('c', 'd'), ('e', 'e')]
        g = Graph(EdgeList = edge)
        (m, v) = g.toAdjacencyMatrix()
        print m
        print v
    
        
if __name__ == "__main__":
    #    print os.path.join(os.path.dirname(os.getcwd()), 'adalp')
    sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'copads'))
    from Graph import Graph
    from JMathsExceptions import *
    unittest.main()
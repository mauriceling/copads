import unittest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'copads'))
from graph import Graph
from copadsexceptions import *
    

G = {'s':{'u':10, 'x':5},
     'u':{'v':1, 'x':2},
     'v':{'y':4},
     'x':{'u':3, 'v':9, 'y':2},
     'y':{'s':7, 'v':6}}

class testGraph(unittest.TestCase):
    """Unit test cases for Graph.Graph object."""
    def testInit(self):
        self.assertTrue(Graph(graph=G))
        
    def testShortestPath(self):
        g = Graph(graph = G)
        self.assertEquals(g.shortestPath('s', 'v'), ['s', 'x', 'u', 'v'])
        
    def testMakeGraphFromVertices(self):
        g = Graph(vertices = ['s', 'u', 'v', 'x', 'y'])
        self.assertEquals(g.graph, {'s':{}, 'u':{}, 'v':{}, 'x':{}, 'y':{}})
        
    def testMakeGraphFromEdges1(self):
        g = Graph(edges = [('s', 'u'),('s', 'u'),('s', 'u'),('s', 'u'),
                           ('s', 'u'),('s', 'u'),('s', 'u'),('s', 'u'),
                           ('s', 'u'),('s', 'u'),('s', 'x'),('s', 'x'),
                           ('s', 'x'),('s', 'x'),('s', 'x'),('u', 'v'), 
                           ('u', 'x'),('u', 'x'),('v', 'y'),('v', 'y'),
                           ('v', 'y'),('v', 'y'),('x', 'u'),('x', 'u'),
                           ('x', 'u'),('x', 'v'),('x', 'v'),('x', 'v'),
                           ('x', 'v'),('x', 'v'),('x', 'v'),('x', 'v'),
                           ('x', 'v'),('x', 'v'),('x', 'y'),('x', 'y'),
                           ('y', 's'),('y', 's'),('y', 's'),('y', 's'),
                           ('y', 's'),('y', 's'),('y', 's'),('y', 'v'),
                           ('y', 'v'),('y', 'v'),('y', 'v'),('y', 'v'),
                           ('y', 'v')], digraph = True)
        self.assertEquals(g.graph, G)
    
        
if __name__ == "__main__":
    unittest.main()
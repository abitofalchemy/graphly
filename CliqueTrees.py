
import networkx as nx
import pprint as pp

class Node(object):

  def __init__(self,id_attrib, data_attribs):

    self.id_attrib = id_attrib
    self.data_attribs = data_attribs
    self.root = False

  def attributes(self):
    print '  id:', self.id_attrib
    print 'data:', self.data_attribs
    print 'root:', self.root

# class CTree(object):
#
#   def __init__(self):
#     from collections import defaultdict
#
#     self.root = None
#     self.nodes = defaultdict()
#
#
#
#   def add_node(self, vObj):
#     self.vObj = vObj
#
#     if len(vObj) < 1:
#       self.nodes[0] = Node({self.vObj: 'children': })
#     else:
#       dd_size = len(self.nodes) + 1
#       self.nodes[dd_size]  =Node()
#
#       return False

G = nx.karate_club_graph()
G = nx.Graph()
G.add_edges_from([(0,1),(1,2),(2,3),(3,4),(4,5),(5,2),(5,1),(4,0)])

c = [x for x in list(nx.enumerate_all_cliques(G)) if len(x)>1]
clqs = sorted(c, key=len, reverse=True)

from collections import defaultdict, Counter

def traverse(tree, vertex):
  for k,v in tree[vertex].items():
    print vertex,'->',k, v
    [traverse(tree,x) for x in v.keys()]


def tree():
  return defaultdict(tree)

T = []

for i,c in enumerate(clqs):
  T.append(Node(i, clqs[i]))
  # T[i] = Node(i,clqs[i])

# traverse(T, 0)
if 0:
  for x in T:
    print x.id_attrib,':', x.data_attribs

## Another approach


# class CliqueTree(object):
#
#   def __init__ (self):
#     self.nodes = defaultdict(set)
#     self.root = None
#     self.node = None
#
#   def add_node(self, vertex):
#     self.vertex = vertex
#     if len(self.nodes) < 1:
#       self.node = Node(0, vertex)
#       self.node.root = True
#
#
# CT = CliqueTree()
#
# CT.add_node(clqs[0])
# CT.add_node(clqs[1])
# CT.add_node(clqs[2])
#
# print traverse(CT)

ct = defaultdict(set)
v = Node(0, clqs[0])
v.root = True
ct[0].add(v)

for i,c in enumerate(clqs[1:]):
  i +=1
  ct[i].add(Node(i, clqs[i]))

pp.pprint ([ct[x].pop().attributes() for x in ct.keys()])
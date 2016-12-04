'''
Clique Tree

cT = CliqueTree()
cT.add_node({'id': 1, 'children': []})

'''
import pprint as pp
import networkx as nx

class Node(object):

  def __init__ (self,attrbts):
    self.attrbts  = attrbts
    self.children = []

  # def is_leaf(self):
  #   if len(self.children)>0:
  #     return True
  #   else
  #     return False

class CTree:
  def __init__(self):
    self.nodes = []

  def createNode(self,data):
    return Node(data)

  def insert(self, node, data):
    if node is None:
      return self.createNode(data)

    self.nodes.append(data)

  def traverseInorder (self, root):
    """
    traverse function will print all the node in the tree.
    """
    if root is not None:
      self.traverseInorder(root.children)
      print root.data
      self.traverseInorder(root.right)


from collections import defaultdict

def tree():
  return defaultdict(tree)

def add(t, keys):
  for key in keys:
    t = t[key]

def traverse(tree, vertex):
  for k,v in tree[vertex].items():
    print vertex,'->',k, v
    [traverse(tree,x) for x in v.keys()]
    # else:
    #   print k, 'is a leaf'


T = tree()
T['root']= {'children': {'1': {}, '2': {}}}
T['2'] = {'children': {'4': {}}}

traverse(T, 'root')



# import networkx as nx
# #
# # # https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/
# #
#
# # class CliqueNode(object):
# #   def __init__ (self):
# #     self.root = False
# #     self.vertex = None
# #     self.nodes = []
# #     self.otherInfo = None
# #     self.prev = None
# #
# #   def add (self,v,r):
# #     self.v = v
# #     self.r = r
# #     node1 = CliqueNode()
# #     node1.vertex = self.v
# #     node1.root = self.r
# #     self.nodes.append(node1)
# #     node1.prev = self
# #     return node1
# #
# #   def visualize (self):
# #     print [x for x in self.nodes]
# #     return
#
# G = nx.karate_club_graph()
# G = nx.Graph()
# G.add_edges_from([(0,1),(1,2),(2,3),(3,4),(4,5),(5,2),(5,1),(4,0)])
#
# c = [x for x in list(nx.enumerate_all_cliques(G)) if len(x)>1]
# c = sorted(c, key=len, reverse=True)
#
# (_ROOT, _DEPTH, _BREADTH) = range(3)
#
#
# class Node (object):
#   def __init__(self,identifier):
#     self.identifier = identifier
#     self.children = []
#
#   def identifier(self):
#     return self.identifier
#
#   def children(self):
#     return self.children
#
#   def add_child(self, identifier):
#     self.children.append(identifier)
#
# class Tree:
#   def __init__(self):
#     self.__nodes = {}
#
#   @property
#   def nodes(self):
#     return self.__nodes
#
#   def add_node(self, identifier, parent=None):
#     node = Node(identifier)
#     self[identifier] = node
#
#     if parent is not None:
#         self[parent].add_child(identifier)
#
#     return node
#
#   def display (self, identifier, depth=_ROOT):
#     children = self[identifier].children
#     if depth == _ROOT:
#       print("{0}".format(identifier))
#     else:
#       print("\t" * depth, "{0}".format(identifier))
#
#     depth += 1
#     for child in children:
#       self.display(child, depth)  # recursive call
#
#   def __getitem__ (self, key):
#       return self.__nodes[key]
#
#   def __setitem__ (self, key, item):
#     self.__nodes[key] = item
#
# T = Tree()
#
# T.add_node(c[0])
# T.add_node(c[1],c[0])
#
# # T.display(c[0])
# # print("***** DEPTH-FIRST ITERATION *****")
# # for node in T.traverse():
# #     print(node)
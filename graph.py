# explanations for member functions are provided in requirements.py
# each file that uses a graph should import it from this file.

from collections.abc import Iterable
from random import choice

# from collections import defaultdict
# Defaultdict is a very useful library that essentially makes it so that dictionaries have default
# values for keys that have not been explicity created yet. However, in light of not knowing what is allowed
# and what is not, I decided to implement the graph using regular dictionaries.


class Graph:
	def __init__(self, num_nodes: int, edges: Iterable[tuple[int, int]]):
		self.__graph = {} # defaultdict(set) 
		self.__edges = edges
		self.__degrees = {} # defaultdict(int)
		self.__num_nodes = num_nodes
		self.__num_edges = 0

		self.__build_graph()
		self.__create_degrees() 

	def size(self) -> int:
		return self.__num_nodes
	
	def get_random_node(self):
		return choice(list(range(self.__num_nodes)))
	
	def get_nodes(self) -> Iterable:
		return range(self.__num_nodes)

	def get_degrees(self) -> dict:
		return self.__degrees

	def get_num_nodes(self) -> int:
		return self.__num_nodes

	def get_num_edges(self) -> int:
		return self.__num_edges

	def get_neighbors(self, node: int) -> Iterable[int]:
		# Return a set containing all of the neighbors of a specific node
		if node in self.__graph.keys():
			return self.__graph[node]
		return set()
	
	def __build_graph(self):
		# Populates the graph with all the edges, such that key = vertex and value = set of all neighbors
		for first, second in self.__edges:
			self.__num_edges += 1 
			if first not in self.__graph.keys():
				self.__graph[first] = set()
			if second not in self.__graph.keys():
				self.__graph[second] = set()
			self.__graph[first].add(second)
			self.__graph[second].add(first)
	
	def __create_degrees(self):
		# Create a dictionary of degrees such that key = vertex and value = degree(vertex)
		for node in self.get_nodes():
			self.__degrees[node] = len(self.get_neighbors(node))

			


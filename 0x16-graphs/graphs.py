""""Implementation of a graph"""

from typing import Dict, List
class Graph:
    """Represents an undirected unweighted graph"""
    def __init__(self):
        self.adjacency_list: Dict = {}
    
    def add_vertex(self, vertex_name: any):
        """Adds a vertex to the adjacency list"""
        self.adjacency_list[vertex_name] = []
    
    def add_edge(self, vertex1: any, vertex2: any):
        """Creates a relationship between two vertex"""
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)
    
    def remove_edge(self, vertex1: any, vertex2: any):
        """Removes a vertex from the graph"""
        self.adjacency_list[vertex1].remove(vertex2)
        self.adjacency_list[vertex2].remove(vertex1)
    
    def remove_vertex(self, vertex_name: any):
        """Removes a vertex from the adjacency list"""
        for key in self.adjacency_list.keys():
            if key == vertex_name:
                continue
            current_list:List = self.adjacency_list[key]
            # check if the current list contains the element
            # if so, delete it in relation with the key
            for element in current_list:
                if element == vertex_name:
                    self.remove_edge(key, element)
        self.adjacency_list.pop(vertex_name)
    
    def remove_vertex_2(self, vertex_name: any):
        while len(self.adjacency_list[vertex_name]):
            adjacent_vertex: any = self.adjacency_list[vertex_name].pop(0)
            self.remove_edge(adjacent_vertex, vertex_name)

g: Graph = Graph()
g.add_vertex("Kenya")
g.add_vertex("Uganda")
g.add_vertex("Tanzania")
g.add_vertex("Kenya")

g.add_edge("Kenya", "Uganda")
g.add_edge("Kenya", "Tanzania")
g.add_edge("Tanzania", "Uganda")

# g.remove_edge("Tanzania", "Uganda")
g.remove_vertex("Tanzania")

print(g.adjacency_list)

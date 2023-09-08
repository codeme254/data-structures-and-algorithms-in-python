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
            for element in current_list:
                if element == vertex_name:
                    self.remove_edge(key, element)
        self.adjacency_list.pop(vertex_name)
    
    def remove_vertex_2(self, vertex_name: any):
        while len(self.adjacency_list[vertex_name]):
            adjacent_vertex: any = self.adjacency_list[vertex_name].pop(0)
            self.remove_edge(adjacent_vertex, vertex_name)
    
    def dfs_recursive(self, starting_node):
        """Performs depth first recursive traversal on a graph"""
        result: List[any] = []
        visited_nodes:Dict = {}
        
        def traverse_helper(vertex):
            if not vertex:
                return
            visited_nodes[vertex] = True
            result.append(vertex)
            for child_vertex in self.adjacency_list[vertex]:
                if not visited_nodes.get(child_vertex):
                    traverse_helper(child_vertex)
        traverse_helper(starting_node)
        return result

    def dfs_iterative(self, starting_node):
        """Performs depth first iterative traversal on a graph"""
        vertices: List[any] = []
        result: List[any] = []
        visited_vertices: Dict = {}

        vertices.append(starting_node)
        visited_vertices[starting_node] = True

        while len(vertices) > 0:
            current_vertex = vertices.pop(len(vertices)-1)
            result.append(current_vertex)
            for neighbor in self.adjacency_list[current_vertex]:
                if not visited_vertices.get(neighbor):
                    vertices.append(neighbor)
                    visited_vertices[neighbor] = True
        return result
    
    def bfs(self, starting_node):
        """Performs a breadth first traversal on the graph"""
        queue: List[any] = [starting_node]
        result: List[any] = []
        visited_nodes: Dict = {}
        visited_nodes[starting_node] = True
        
        while len(queue) > 0:
            current_vertex = queue.pop(0)
            result.append(current_vertex)
            for neighbor in self.adjacency_list[current_vertex]:
                if not visited_nodes.get(neighbor):
                    visited_nodes[neighbor] = True
                    queue.append(neighbor)
        return result

g: Graph = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")
g.add_vertex("F")

g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "E")
g.add_edge("D", "E")
g.add_edge("D", "F")
g.add_edge("E", "F")


print(g.adjacency_list)

print(g.dfs_recursive("A"))
print(g.dfs_iterative("A"))
print(g.bfs("A"))
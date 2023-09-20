"""CS 2420 Project 7 - Graphs"""
import math
import numpy as np
from graphviz import Source
import heapdict


def compare(item1):
    """Function used for comparisons"""
    return item1[1]


class StorageCollection:
    """Becomes either a Stack or a Queue based on the parameter in the Constructor."""

    def __init__(self, isStack):
        """Constructs a StorageCollection.  If isStack is true, this acts as a stack, otherwise this acts as a queue."""
        if not isinstance(isStack, bool):
            raise ValueError("isStack parameter must be true or false.")
        self.pop_index = 0
        if isStack is True:
            self.pop_index = -1
        self.storage = []

    def push(self, value):
        """Pushes a value to the collection."""
        self.storage.append(value)

    def pop(self):
        """Pops a value from the collection."""
        return self.storage.pop(self.pop_index)

    def is_empty(self):
        """Reports whether or not the collection is empty."""
        return not self.storage


class PQueueNode:
    """A class to store information needed for Dijkstra's Shortest Path."""

    def __init__(self, label, weight, index, prev):
        """Constructs the PQueueNode class."""
        self.label = label
        self.weight = weight
        self.index = index
        self.prev = prev
        self.neighbors = []

    def update(self, weight, prev):
        """Updates the weight and previous label, and then returns this node."""
        self.weight = weight
        self.prev = prev
        return self

    def __lt__(self, other):
        """Override of less than operator."""
        return self.weight < other.weight

    def __gt__(self, other):
        """Override of greater than operator."""
        return not self.__lt__(other)

    def __eq__(self, other):
        """Override of equality operator."""
        return self.weight == other.weight

    def __ne__(self, other):
        """Override of not equality operator."""
        return not self.__eq__(other)

    def __repr__(self):
        """Override of representation operator."""
        return str("(" + self.label + "," + str(self.weight) + ")")


class Graph:
    """A Graph Object."""

    def __init__(self):
        self._labels = []
        self._matrix = np.matrix(np.ones((0, 0), dtype=np.single))
        self._size = 0

    def _add_column(self):
        new_col = np.matrix(np.ones((self._matrix.shape[0], 1), dtype=np.single) * math.inf)
        self._matrix = np.hstack((self._matrix, new_col))

    def _add_row(self):
        new_row = np.matrix(np.ones((1, self._matrix.shape[1]), dtype=np.single) * math.inf)
        self._matrix = np.vstack((self._matrix, new_row))

    def _index(self, label):
        return self._labels.index(label)

    def _weight(self, src, dest):
        if src not in self._labels or dest not in self._labels:
            raise ValueError("Vertex does not exist")
        return self._matrix[self._index(src), self._index(dest)]

    def _neighbors(self, src_index):
        result = []
        for i in range(self._size):
            neighbor = self._matrix[src_index, i]
            if neighbor != math.inf:
                result.append(i)
        return result

    def _directed_str(self):
        result = "digraph {\n"
        for label in self._labels:
            index = self._index(label)
            for value in range(self._size):
                floatValue = self._matrix[index, value]
                if floatValue != math.inf:
                    floatString = "{:.1f}".format(floatValue)
                    result += "\t" + label + " -> " + self._labels[
                        value] + "[label=\"" + floatString + "\",weight=\"" + floatString + "\"];\r\n"
        result += "}\r\n"
        return result

    def _undirected_str(self):
        result = "digraph G {\n"
        edges = {}
        for label in self._labels:
            index = self._index(label)
            for value in range(self._size):
                floatValue = self._matrix[index, value]
                if floatValue != math.inf:
                    key = (index, value) if index < value else (value, index)
                    edges[key] = floatString = "{:.1f}".format(floatValue)
        for key in edges.keys():
            result += "   " + self._labels[key[0]] + " -> " + self._labels[key[1]] + " [label=\"" + edges[
                key] + "\",weight=\"" + edges[key] + "\"];\n"
        result += "}\n"
        return result

    def _traversal(self, vertex, collection):
        result = []
        visited = []
        index = self._index(vertex)
        collection.push(index)
        visited.append(index)

        while not collection.is_empty():
            v = collection.pop()
            result.append(self._labels[v])
            for neighbor in self._neighbors(v):
                if neighbor not in visited:
                    collection.push(neighbor)
                    visited.append(neighbor)
        return result

    def _populatePriorityQueue(self, src, dst):
        queue_nodes = heapdict.heapdict()
        dest_node = None
        for label in self._labels:
            queue_nodes[label] = PQueueNode(label, 0 if label == src else math.inf, self._index(label), None)
            if label == dst:
                dest_node = queue_nodes[label]

        for label in self._labels:
            for neighbor in self._neighbors(self._index(label)):
                queue_nodes[label].neighbors.append(queue_nodes[self._labels[neighbor]])

        return queue_nodes, dest_node

    def add_vertex(self, vertex):
        """Adds a vertex to the Queue."""
        if vertex == 0:
            raise ValueError
        if vertex not in self._labels:
            self._add_column()
            self._add_row()
            self._labels.append(vertex)
            self._size += 1
        return self

    def add_edge(self, src, dst, w):
        """Adds a directed edge between 2 vertices to the Queue."""
        if isinstance(w, str):
            raise ValueError
        if src not in self._labels or dst not in self._labels:
            raise ValueError()
        self._matrix[self._index(src), self._index(dst)] = w
        return self

    def add_edge2w(self, src, dst, w):
        """Adds edges both directions between 2 vertices in the Queue."""
        self.add_edge(src, dst, w)
        self.add_edge(dst, src, w)

    def dfs(self, root):
        """Depth-first Search returning a generator."""
        stack = StorageCollection(True)
        result = self._traversal(root, stack)
        for item in result:
            yield item

    def bfs(self, root):
        """Breadth-first Search returning a generator."""
        queue = StorageCollection(False)
        result = self._traversal(root, queue)
        for item in result:
            yield item

    def new_dsp(self, src, dest):
        """Used for Dijkstra's Shortest Path algorithm."""
        # Prepare my priority queue
        priorityqueue = []
        for label in self._labels:
            priorityqueue.append([label, math.inf, ""])
        for item in priorityqueue:
            if item[0] == src:
                item[1] = 0
        priorityqueue.sort(key=compare)
        visited = {}

        while True:
            currentnode = priorityqueue.pop(0)
            visited[currentnode[0]] = currentnode
            currentnodeindex = self._index(currentnode[0])
            for neighborindex in self._neighbors(currentnodeindex):
                if self._labels[neighborindex] not in visited:
                    newweight = currentnode[1] + self._weight(currentnode[0], self._labels[neighborindex])
                    neighbor = None
                    for item in priorityqueue:
                        if item[0] == self._labels[neighborindex]:
                            neighbor = item
                    if newweight < neighbor[1]:
                        neighbor[1] = newweight
                        neighbor[2] = currentnode[0]

            priorityqueue.sort(key=compare)
            if dest in visited:
                break
            if priorityqueue[0][1] == math.inf:
                break

        if dest in visited:
            path = []
            path.append(dest)
            current_node = visited[dest]
            while current_node[0] != src:
                path.insert(0, current_node[2])
                current_node = visited[current_node[2]]
            return visited[dest][1], path

        return 0, ""

    def dsp(self, src, dest):
        """Dijkstra's Shortest Path algorithm."""
        success = False
        # Set all nodes as unvisted
        # Assign to every node a tentative distance value
        tent_distance, dest_node = self._populatePriorityQueue(src, dest)
        visited_nodes = {}

        # For the current node, consider all of its unvisited neighbours and calculate their tentative distances
        # through the current node
        current_node = tent_distance.popitem()[1]
        while True:
            for neighbor in current_node.neighbors:
                if neighbor.label not in visited_nodes:
                    new_weight = current_node.weight + self._matrix[current_node.index, neighbor.index]
                    if new_weight < neighbor.weight:
                        tent_distance[neighbor.label] = neighbor.update(new_weight, current_node.label)

            # When we are done considering all of the unvisited neighbours of the current node, mark the current node
            # as visited
            visited_nodes[current_node.label] = current_node

            # If the destination node has been marked visited or if the smallest tentative distance among the nodes
            # in the unvisited set is infinity, then stop. The algorithm has finished.
            if dest_node.label in visited_nodes:
                success = True
                break
            if len(tent_distance) == 0 or tent_distance.peekitem()[1].weight == math.inf:
                break
            # Otherwise, select the unvisited node that is marked with the smallest tentative distance, set it as the
            # new "current node", and go back to step 3.
            else:
                current_node = tent_distance.popitem()[1]

        # Starting at the destination, trace back appending the previous vertex on the path
        current_node = dest_node
        if success:
            result = [current_node.label]
            while current_node.label != src:
                result.insert(0, current_node.prev)
                current_node = visited_nodes[current_node.prev]

            # Print the path from vertex “A” to vertex “F” (not shown here) using Djikstra’s
            # shortest path algorithm (DSP) as a string like #3 and #4
            print("Starting Djikstra’s shortest path starting with vertex " + src + " to vertex " + dest + ":")
            for vertex in result:
                print(str(vertex), end='')
            print()
            # End of step 5.

            return dest_node.weight, result

        return math.inf, []

    def dsp_all(self, src):
        """Djikstra's shortest path without a destination, finds path to all other nodes."""
        tent_distance, dest_node = self._populatePriorityQueue(src, "")
        visited_nodes = {}

        current_node = tent_distance.popitem()[1]
        while True:
            for neighbor in current_node.neighbors:
                if neighbor.label not in visited_nodes:
                    new_weight = current_node.weight + self._matrix[current_node.index, neighbor.index]
                    if new_weight < neighbor.weight:
                        tent_distance[neighbor.label] = neighbor.update(new_weight, current_node.label)

            visited_nodes[current_node.label] = current_node

            if len(tent_distance) == 0 or tent_distance.peekitem()[1].weight == math.inf:
                break
            current_node = tent_distance.popitem()[1]

        while len(tent_distance) > 0:
            current_node = tent_distance.popitem()[1]
            visited_nodes[current_node.label] = current_node

        result = {}
        for label in self._labels:
            current_node = visited_nodes[label]
            if current_node.prev is None and label != src:
                result[label] = []
                continue
            result[label] = [current_node.label]
            while current_node.label != src:
                result[label].insert(0, current_node.prev)
                current_node = visited_nodes[current_node.prev]

        # Print the shortest paths from “A” to each other vertex, one path per line using DSP.
        print("Starting Djikstra’s shortest path starting with vertex " + src + " to each other vertex:")
        for source in result:
            print(src + " to " + source + ": ", end='')
            for vertex in result[source]:
                print(str(vertex), end='')
            print()
        # End of step 6.

        return result

    def display(self):
        """Displays a graph visually."""
        s = Source(self.__str__())
        s.view()

    def __str__(self):
        """Override of the ToString function."""
        return self._undirected_str()

    def get_weight(self, src, dest):
        """Used to get the weight from the source vertex to destination vertex"""
        return self._weight(src, dest)


def main():
    """Main function used for Displaying Output of Graph Operations on an Example Graph G"""
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")
    graph.add_vertex("F")
    graph.add_edge2w("A", "B", 2)
    graph.add_edge2w("A", "F", 9)
    graph.add_edge2w("B", "D", 15)
    graph.add_edge2w("B", "C", 8)
    graph.add_edge2w("B", "F", 6)
    graph.add_edge2w("C", "D", 1)
    graph.add_edge2w("E", "C", 7)
    graph.add_edge2w("E", "D", 3)
    graph.add_edge2w("F", "B", 6)
    graph.add_edge2w("F", "E", 3)
    graph.display()
    print(graph._undirected_str())

    print("starting BFS with vertex A")
    for vertex in graph.bfs("A"):
        print(vertex, end="")
    print("\n")

    print("starting DFS with vertex A")
    for vertex in graph.dfs("A"):
        print(vertex, end="")
    print("\n")

    print(graph.dsp("A", "F"))
    print()
    print(graph.dsp_all("A"))


main()

# graph = Graph()
# graph.add_vertex("SQ")
# graph.add_vertex("PA")
# graph.add_vertex("ER")
# graph.add_vertex("SA")
# graph.add_vertex("WH")
# graph.add_vertex("SF")
# graph.add_vertex("MA")
# graph.add_vertex("SV")
# graph.add_vertex("PR")
# graph.add_vertex("OR")
# graph.add_vertex("LI")
# graph.add_vertex("VI")
# graph.add_vertex("PG")
# graph.add_vertex("AF")
# graph.add_vertex("HI")
# graph.add_vertex("LE")
# graph.add_vertex("SS")
# graph.add_vertex("CF")
# graph.add_vertex("EM")
# graph.add_vertex("FF")
# graph.add_vertex("EU")
# graph.add_vertex("EL")
# graph.add_vertex("GO")
# graph.add_vertex("GE")
# graph.add_edge2w("SQ", "PA", 8)
# graph.add_edge2w("SQ", "GE", 4)
# graph.add_edge2w("GE", "GO", 5)
# graph.add_edge2w("GO", "EL", 5)
# graph.add_edge2w("EL", "EM", 28)
# graph.add_edge2w("EL", "EU", 12)
# graph.add_edge2w("EU", "FF", 49)
# graph.add_edge2w("FF", "CF", 5)
# graph.add_edge2w("FF", "EM", 9)
# graph.add_edge2w("CF", "LE", 15)
# graph.add_edge2w("EM", "SS", 11)
# graph.add_edge2w("SS", "LE", 8)
# graph.add_edge2w("LE", "HI", 5)
# graph.add_edge2w("LE", "AF", 3)
# graph.add_edge2w("AF", "PG", 3)
# graph.add_edge2w("AF", "HI", 4)
# graph.add_edge2w("PG", "LI", 2)
# graph.add_edge2w("PG", "OR", 7)
# graph.add_edge2w("OR", "LI", 4)
# graph.add_edge2w("OR", "VI", 4)
# graph.add_edge2w("OR", "PR", 7)
# graph.add_edge2w("PR", "SV", 6)
# graph.add_edge2w("PR", "SF", 9)
# graph.add_edge2w("SV", "MA", 4)
# graph.add_edge2w("SV", "SF", 6)
# graph.add_edge2w("MA", "SF", 5)
# graph.add_edge2w("SF", "SA", 8)
# graph.add_edge2w("SF", "PA", 8)
# graph.add_edge2w("SA", "WH", 4)
# graph.add_edge2w("SA", "ER", 4)
# graph.add_edge2w("SA", "PA", 3)
# graph.add_edge2w("WH", "ER", 4)
# graph.add_edge2w("PA", "ER", 5)
#
# print(graph.dsp("HI", "EU"))
# print(graph.new_dsp("HI", "EU"))
#
# graph.display()

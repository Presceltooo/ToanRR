# a) Viết 1 chương trình xử lý các đồ thị gồm có các chức năng sau:
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from queue import Queue
import heapq

class GraphProcessor:
    # nhập đồ thị tu ma tran input
    def __init__(self):
        self.graph = None

    def read_graph_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                # Đọc dữ liệu từ file
                data = file.readlines()

                # Kiểm tra định dạng của đồ thị
                graph_format = data[0].strip().lower()

                # Xử lý ma trận kề hoặc danh sách kề tùy thuộc vào định dạng
                if graph_format == 'matrix':
                    self.graph = self.read_matrix(data[1:])
                elif graph_format == 'list':
                    self.graph = self.read_list(data[1:])
                else:
                    raise ValueError("Invalid graph format specified in the file.")

        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except Exception as e:
            print(f"Error reading the graph from file: {e}")

    def read_matrix(self, lines):
        # Xử lý ma trận kề và tạo đồ thị
        graph_matrix = [list(map(int, line.strip().split())) for line in lines]
        return graph_matrix

    # vẽ đồ thị
    def draw_weighted_graph(self):
        num_vertices = len(self.graph)

        # Lấy tọa độ các đỉnh trên đồ thị
        positions = np.array([[np.cos(2 * np.pi * i / num_vertices), np.sin(2 * np.pi * i / num_vertices)] for i in range(num_vertices)])

        # Vẽ các đỉnh và thêm nhãn
        for i in range(num_vertices):
            plt.scatter(positions[i, 0], positions[i, 1], color='lightblue', s=200, zorder=5)
            plt.text(positions[i, 0], positions[i, 1], str(i), color='black', ha='center', va='center', fontsize=10, fontweight='bold', zorder=10)

        # Vẽ các cạnh và thêm trọng số
        for i in range(num_vertices):
            for j in range(i + 1, num_vertices):
                if self.graph[i][j] != 0:
                    plt.plot([positions[i, 0], positions[j, 0]], [positions[i, 1], positions[j, 1]], color='black', linewidth=2)
                    weight_label = str(self.graph[i][j])
                    plt.text((positions[i, 0] + positions[j, 0]) / 2, (positions[i, 1] + positions[j, 1]) / 2, weight_label, color='black', ha='center', va='center', fontsize=10)

        plt.axis('off')
        plt.show()
    
    # thuat toan dfs
    def traversal_DFS(self, start_node=0):
        if self.graph is None:
            print("Error: Graph is not initialized.")
            return

        visited = [False] * len(self.graph)
        result = []

        def dfs(node):
            visited[node] = True
            result.append(node)

            for neighbor, weight in enumerate(self.graph[node]):
                if weight != 0 and not visited[neighbor]:
                    dfs(neighbor)

        dfs(start_node)

        print("DFS Traversal Order:")
        print(result)

    #thuat toan bfs
    def traversal_BFS(self, start_node=0):
        if self.graph is None:
            print("Error: Graph is not initialized.")
            return

        visited = [False] * len(self.graph)
        result = []

        queue = Queue()
        queue.put(start_node)
        visited[start_node] = True

        while not queue.empty():
            current_node = queue.get()
            result.append(current_node)

            for neighbor, weight in enumerate(self.graph[current_node]):
                if weight != 0 and not visited[neighbor]:
                    queue.put(neighbor)
                    visited[neighbor] = True

        print("BFS Traversal Order:")
        print(result)

    # tra ve bac cua do thi
    def degree_vertices(self):
        if self.graph is None:
            print("Error: Graph is not initialized.")
            return

        num_vertices = len(self.graph)
        degrees = [sum(self.graph[node]) for node in range(num_vertices)]

        print("Degrees of Vertices:")
        for node, degree in enumerate(degrees):
            print(f"Vertex {node}: {degree}")

    # tra ve duong di ngan nhat giua 2 nut
    def shortest_path(self, start_node, end_node):
        if self.graph is None:
            print("Error: Graph is not initialized.")
            return

        num_vertices = len(self.graph)
        if start_node < 0 or start_node >= num_vertices or end_node < 0 or end_node >= num_vertices:
            print("Error: Invalid start or end node.")
            return

        # Initialize distances and predecessors
        distances = [float('inf')] * num_vertices
        predecessors = [None] * num_vertices
        distances[start_node] = 0

        # Priority queue for Dijkstra's algorithm
        priority_queue = [(0, start_node)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_node == end_node:
                # Reconstruct the shortest path
                path = []
                while current_node is not None:
                    path.insert(0, current_node)
                    current_node = predecessors[current_node]
                return path

            for neighbor, weight in enumerate(self.graph[current_node]):
                if weight != 0:
                    new_distance = distances[current_node] + weight
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        predecessors[neighbor] = current_node
                        heapq.heappush(priority_queue, (new_distance, neighbor))

        # If no path is found
        print("No path found between the specified nodes.")
        return None

# Example usage:
processor = GraphProcessor()
processor.read_graph_from_file('filetext.txt')
processor.draw_weighted_graph()
processor.traversal_DFS()
processor.traversal_BFS()
processor.degree_vertices()
# Specify start and end nodes
start_node = 0
end_node = 5

# Find and print the shortest path
path = processor.shortest_path(start_node, end_node)
if path:
    print(f"Shortest Path from Node {start_node} to Node {end_node}: {path}")







""" b) Viết chương trình biểu diễn đơn đồ thị vô hướng từ ma trận trọng số bất 
kỳ được nhập vào. Sử dụng các giao diện hoặc biểu diễn đồ thị (ví dụ 
matplotlib, pygame, or tkinter…) """

import random
from mpl_toolkits.mplot3d import Axes3D
# vẽ đồ thị 2D
# Define the matrix size
n = 5
coefficient = 4

random.seed(coefficient)
matrix = [[random.randint(1, 100) for j in range(n)] for i in range(n)]
for i in range(n):
    matrix[i][i] = 0

# Print the matrix
print("Cost Matrix:")
for row in matrix:
    print(row)

# import numpy as np
# import matplotlib.pyplot as plt
# đã khai bao bên trên

def draw_weighted_graph(adj_matrix):
    G = nx.Graph()
    num_nodes = len(adj_matrix)
    G.add_nodes_from(range(num_nodes))
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            weight = adj_matrix[i][j]
            if weight > 0:
                G.add_edge(i, j, weight=weight)

    # Draw the graph

    pos = nx.spring_layout(G,seed=34)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=150, font_size=10)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Show the graph
    plt.show()

draw_weighted_graph(matrix)


# vẽ đồ thị 3D
def draw_3d_graph(adj_matrix):
    num_vertices = len(adj_matrix)

    # Lấy tọa độ các đỉnh trên đồ thị
    positions = np.random.rand(num_vertices, 3)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Vẽ các đỉnh
    for i in range(num_vertices):
        ax.scatter(positions[i, 0], positions[i, 1], positions[i, 2], color='lightblue', s=200, zorder=5)
        ax.text(positions[i, 0], positions[i, 1], positions[i, 2], str(i), color='white', ha='center', va='center', fontsize=12, fontweight='bold')

    # Vẽ các cạnh
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if adj_matrix[i][j] != 0:
                ax.plot([positions[i, 0], positions[j, 0]], [positions[i, 1], positions[j, 1]], [positions[i, 2], positions[j, 2]], color='black', linewidth=2)

    plt.show()

draw_3d_graph(matrix)
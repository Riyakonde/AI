
 

from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        """Adds an undirected edge between u and v."""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs_recursive(self, node, visited=None):
        """Recursive Depth First Search (DFS)."""
        if visited is None:
            visited = set()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in self.graph.get(node, []):
                self.dfs_recursive(neighbor, visited)

    def dfs_iterative(self, start):
        """Iterative Depth First Search (DFS) using a stack."""
        visited = set()
        stack = [start]

        while stack:
            node = stack.pop()
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                stack.extend(reversed(self.graph.get(node, [])))

    def bfs(self, start):
        """Breadth First Search (BFS) using a queue."""
        visited = set()
        queue = deque([start])

        while queue:
            node = queue.popleft()
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                queue.extend(self.graph.get(node, []))

def main():
    g = Graph()
    
    while True:
        print("\nGraph Traversal Menu:")
        print("1. Add Edge")
        print("2. DFS Recursive")
        print("3. DFS Iterative")
        print("4. BFS")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            u, v = map(int, input("Enter the edge (e.g., '0 1' for an edge between 0 and 1): ").split())
            g.add_edge(u, v)
        elif choice in ['2', '3', '4']:
            start_node = int(input("Enter the starting node: "))
            if choice == '2':
                print("\nDFS Recursive:")
                g.dfs_recursive(start_node)
            elif choice == '3':
                print("\nDFS Iterative:")
                g.dfs_iterative(start_node)
            elif choice == '4':
                print("\nBFS:")
                g.bfs(start_node)
            print()  # New line for better readability
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

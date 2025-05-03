import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
    
    def add_edge(self, u, v, weight):
        self.graph.append((u, v, weight))

    def prim_mst(self):
        # Initialize the MST and visited nodes
        mst = []
        visited = [False] * self.V
        edge_count = 0
        total_cost = 0

        # Priority queue to select the minimum weight edge
        min_heap = [(0, 0)]  # (weight, vertex)

        while edge_count < self.V and min_heap:
            weight, u = heapq.heappop(min_heap)

            if visited[u]:
                continue
            
            # Mark this node as visited
            visited[u] = True
            total_cost += weight
            edge_count += 1

            # Add this edge to the MST (except for the starting node)
            if u != 0:
                mst.append((prev_node, u, weight))

            # Add all adjacent edges of this vertex
            for v, w in [(v, w) for src, v, w in self.graph if src == u and not visited[v]]:
                heapq.heappush(min_heap, (w, v))
                prev_node = u

        # Output the MST and total cost
        print("\nEdges in the Minimum Spanning Tree:")
        for u, v, weight in mst:
            print(f"{u} -- {v} == {weight}")
        print("Total cost of MST:", total_cost)


# Take user inputs
vertices = int(input("Enter the number of vertices: "))
num_edges = int(input("Enter the number of edges: "))

g = Graph(vertices)

print("Enter each edge in the format: source destination weight")
for _ in range(num_edges):
    u, v, weight = map(int, input().split())
    g.add_edge(u, v, weight)

# Run Prim's algorithm
g.prim_mst()

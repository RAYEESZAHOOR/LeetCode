# # Modify Graph Edge Weights

# You are given an undirected weighted connected graph containing n nodes labeled from 0 to n - 1, and an integer array edges where edges[i] = [ai, bi, wi] indicates that there is an edge between nodes ai and bi with weight wi.

# Some edges have a weight of -1 (wi = -1), while others have a positive weight (wi > 0).

# Your task is to modify all edges with a weight of -1 by assigning them positive integer values in the range [1, 2 * 109] so that the shortest distance between the nodes source and destination becomes equal to an integer target. If there are multiple modifications that make the shortest distance between source and destination equal to target, any of them will be considered correct.

# Return an array containing all edges (even unmodified ones) in any order if it is possible to make the shortest distance from source to destination equal to target, or an empty array if it's impossible.

# Note: You are not allowed to modify the weights of edges with initial positive weights.


import heapq
import json
import sys

class Solution:
    def modifiedGraphEdges(self, n, edges, source, destination, target):
        # Create adjacency list for the graph
        adjacency_list = [[] for _ in range(n)]
        for i, (nodeA, nodeB, weight) in enumerate(edges):
            adjacency_list[nodeA].append((nodeB, i))
            adjacency_list[nodeB].append((nodeA, i))

        # Initialize distances array for two runs of Dijkstra
        distances = [[float('inf')] * 2 for _ in range(n)]
        distances[source][0] = distances[source][1] = 0

        # First run of Dijkstra with initial weights
        self.run_dijkstra(adjacency_list, edges, distances, source, 0, 0)
        difference = target - distances[destination][0]

        # If the difference is negative, the target distance is unreachable
        if difference < 0:
            return []

        # Second run of Dijkstra considering the required difference
        self.run_dijkstra(adjacency_list, edges, distances, source, difference, 1)

        # If the second run cannot meet the target, return an empty list
        if distances[destination][1] < target:
            return []

        # Finalize edges with weight -1 to have weight 1 if unchanged
        for edge in edges:
            if edge[2] == -1:
                edge[2] = 1

        return edges

    def run_dijkstra(self, adjacency_list, edges, distances, source, difference, run):
        n = len(adjacency_list)
        priority_queue = [(0, source)]
        distances[source][run] = 0

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            if current_distance > distances[current_node][run]:
                continue

            for next_node, edge_index in adjacency_list[current_node]:
                weight = edges[edge_index][2]
                if weight == -1:
                    weight = 1

                if run == 1 and edges[edge_index][2] == -1:
                    new_weight = difference + distances[next_node][0] - distances[current_node][1]
                    if new_weight > weight:
                        edges[edge_index][2] = weight = new_weight

                if distances[next_node][run] > distances[current_node][run] + weight:
                    distances[next_node][run] = distances[current_node][run] + weight
                    heapq.heappush(priority_queue, (distances[next_node][run], next_node))

def main():
    input_data = sys.stdin.read().strip()
    lines = input_data.splitlines()
    
    num_test_cases = len(lines) // 5
    results = []

    for i in range(num_test_cases):
        n = int(lines[i * 5])
        edges = json.loads(lines[i * 5 + 1])
        source = int(lines[i * 5 + 2])
        destination = int(lines[i * 5 + 3])
        target = int(lines[i * 5 + 4])
        
        result = Solution().modifiedGraphEdges(n, edges, source, destination, target)
        results.append(json.dumps(result))

    with open('user.out', 'w') as f:
        for result in results:
            f.write(f"{result}\n")

if __name__ == "__main__":
    main()
    exit(0)

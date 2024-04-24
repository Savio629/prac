# Define the graph
graph = {
    'S': [('A', 1), ('C', 10)],
    'A': [('D', 5), ('S', 1)],
    'B': [('E', 4), ('S', 3)],
    'C': [('E', 6), ('S', 10)],
    'D': [('F', 2), ('G', 1), ('A', 5)],
    'E': [('G', 7), ('C', 6), ('B', 4)],
    'F': [('D', 2)],
    'G': [('D', 1), ('E', 7)]
}

# Define the heuristic values
heuristic = {
    'A': 7,
    'B': 9,
    'C': 11,
    'D': 2,
    'E': 4,
    'F': 1,
    'S': 13,
    'G': 0
}

# Function to perform A* search
def astar(graph, heuristic, start, end):
    queue = []  # Priority queue to store nodes to be evaluated
    visited = set()  # Set to store visited nodes
    parent = {}  # Dictionary to store parent nodes

    # Initialize the queue with the start node and its priority (cost + heuristic)
    for neighbor, cost in graph[start]:
        queue.append((neighbor, cost + heuristic[neighbor]))
        parent[neighbor] = start
        visited.add(start)

    # Sort the queue by the priority (cost + heuristic)
    queue.sort(key=lambda x: x[1])

    # Perform A* search
    while queue:
        # Pop the node with the lowest priority from the queue
        node = queue.pop(0)

        # Check if the goal node is reached
        if node[0] == end:
            return parent

        # Mark the node as visited
        visited.add(node[0])

        # Explore neighbors of the current node
        for neighbor, cost in graph[node[0]]:
            if neighbor not in visited:
                # Calculate the priority for the neighbor node and add it to the queue
                priority = node[1] + cost + heuristic[neighbor] - heuristic[node[0]]
                queue.append((neighbor, priority))
                parent[neighbor] = node[0]

        # Sort the queue by priority after adding new nodes
        queue.sort(key=lambda x: x[1])

# Input: start and end nodes
start = input("Enter Starting Node: ")
end = input("Enter Ending Node: ")

# Perform A* search to find the parent nodes
parent_nodes = astar(graph, heuristic, start, end)

# Reconstruct the path from end to start
path = end + " "
current_node = end
while current_node != start:
    path += parent_nodes[current_node] + " "
    current_node = parent_nodes[current_node]

# Print the path in reverse order
print("Shortest Path:", path[::-1])
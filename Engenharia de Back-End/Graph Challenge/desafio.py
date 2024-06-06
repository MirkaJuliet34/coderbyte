'''Have the function GraphChallenge(strArr) take strArr which will be an array of strings which models a non-looping Graph. The structure of the array will be as follows: The first element in the array will be the number of nodes N (points) in the array as a string. The next N elements will be the nodes which can be anything (A, B, C .. Brick Street, Main Street .. etc.). Then after the Nth element, the rest of the elements in the array will be the connections between all of the nodes. They will look like this: (A-B, B-C .. Brick Street-Main Street .. etc.). Although, there may exist no connections at all.

An example of strArr may be: ["4","A","B","C","D","A-B","B-D","B-C","C-D"]. Your program should return the shortest path from the first Node to the last Node in the array separated by dashes. So in the example above the output should be A-B-D. Here is another example with strArr being ["7","A","B","C","D","E","F","G","A-B","A-E","B-C","C-D","D-F","E-D","F-G"]. The output for this array should be A-E-D-F-G. There will only ever be one shortest path for the array. If no path between the first and last node exists, return -1. The array will at minimum have two nodes. Also, the connection A-B for example, means that A can get to B and B can get to A.
Examples
Input: ["5","A","B","C","D","F","A-B","A-C","B-C","C-D","D-F"]
Output: A-C-D-F
Input: ["4","X","Y","Z","W","X-Y","Y-Z","X-W"]
Output: X-W
'''

def GraphChallenge(strArr):
    from collections import deque, defaultdict

    # Step 1: Parse the input
    N = int(strArr[0])
    nodes = strArr[1:N + 1]
    edges = strArr[N + 1:]

    start_node = nodes[0]
    end_node = nodes[-1]

    # Step 2: Build the graph using an adjacency list
    graph = defaultdict(list)
    for edge in edges:
        node1, node2 = edge.split('-')
        graph[node1].append(node2)
        graph[node2].append(node1)

    # Step 3: Find the shortest path using BFS
    def bfs_shortest_path(start, goal):
        # Queue for BFS, storing (current_node, path_taken)
        queue = deque([(start, [start])])
        visited = set()

        while queue:
            current, path = queue.popleft()
            if current in visited:
                continue

            visited.add(current)

            if current == goal:
                return path

            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

        return None

    # Find the shortest path from start_node to end_node
    shortest_path = bfs_shortest_path(start_node, end_node)

    # Step 4: Return the formatted result or -1 if no path found
    if shortest_path:
        return '-'.join(shortest_path)
    else:
        return '-1'


# Test cases
print(GraphChallenge(["5", "A", "B", "C", "D", "F", "A-B", "A-C", "B-C", "C-D", "D-F"]))  # Output: A-C-D-F
print(GraphChallenge(["4", "X", "Y", "Z", "W", "X-Y", "Y-Z", "X-W"]))  # Output: X-W

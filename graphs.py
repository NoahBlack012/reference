class Vertex:
    def __init__(self, value, connections=None):
        self.value = value
        if connections is None:
            self.connections = {}
        else:
            self.connections = connections

    def add_connection(self, vertex, weight=None):
        if weight is None:
            self.connections[vertex] = 1
        else:
            self.connections[vertex] = weight

def get_cost(route):
    cost = 0
    for n, i in enumerate(route):
        try:
            cost += i.connections[route[n+1]]
        except IndexError:
            pass
    return cost

# O(V + E)
def dfs(vertex, search_value, visited={}, cost=0):
    if vertex.value == search_value:
        return vertex, cost

    visited[vertex.value] = True
    for i in vertex.connections:
        weight = vertex.connections[i]
        try:
            # If space has already been visited, continue
            if visited[i.value]:
                continue
        except KeyError:
            pass

        # If the search value has been found, return it and the cost of the path
        if i.value == search_value:
            return i, cost + weight

        # Recursively call dfs with the current node
        end, cost = dfs(i, search_value, visited, cost+weight)
        if end:
            return end, cost
    return None

# O(V + E)
def bfs(start, end):
    queue = []

    # Create dict for visited vertices and add the starting vertex to it
    visited = {}
    visited[start.value] = True

    queue.append([start, ])

    # While the path is not empty
    while queue:
        # Get current path
        current_path = queue.pop()
        for i in current_path[-1].connections:
            try:
                # If space has already been visited, continue
                if visited[i.value]:
                    continue
            except KeyError:
                pass
            visited[i.value] = True
            # Create new path
            new_path = current_path + [i, ]
            if i.value == end.value:
                # If the search value has been found, return it and the cost of the path
                return new_path, get_cost(new_path)
            # Insert new path into the queue
            queue.insert(0, new_path)
    return None

def dijkstra(start, end):
    cheapest = {}
    cheapest_previous = {}

    unvisited = []
    visited = {}

    cheapest[start] = 0

    # Set current to be starting vertex
    current = start

    # Loop until there are no unvisited vertices
    while current:
        visited[current] = True
        try:
            unvisited.remove(current)
        except ValueError:
            pass
        for i in current.connections:
            # If a new vertex is found, add it to unvisited vertices
            if i not in unvisited:
                unvisited.append(i)

            # Get cost of going through vertex by adding cost of getting to current +
            # the weight of the connection from the current vertex to the adjacent one
            cost_through_vertex = cheapest[current] + current.connections[i]

            # If the cost is the cheapest so far, update the dicts for cheapest and cheapest from the previous vertex
            if i not in cheapest:
                cheapest[i] = cost_through_vertex
                cheapest_previous[i] = current
            elif cost_through_vertex < cheapest[i]:
                cheapest[i] = cost_through_vertex
                cheapest_previous[i] = current

        # Set current to be the next cheapest unvisited city
        try:
            current = unvisited[0]
        except IndexError:
            current = None
        for i in unvisited:
            if cheapest[i] < cheapest[current]:
                current = i

    #Build shortest path
    path = []
    current = end
    #Loop until start is reached
    while current != start:
        # Add current to path
        path.append(current)
        # Set current to be cheapest previous vertex for the current vertex
        current = cheapest_previous[current]

    # Add start to path and reverse
    path.append(start)
    path = path[::-1]
    return path

a = Vertex(1)
b = Vertex(2)
c = Vertex(3)
d = Vertex(4)

a.add_connection(b)
a.add_connection(c)

b.add_connection(d)

route = dijkstra(a, d)
print ([i.value for i in route])
print (get_cost(route))

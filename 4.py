import heapq

moves=[(-1,0), (1,0), (0,-1), (0,1)]

class Node:
    def __init__(self, position, parent=None, g=0, h=0):
        self.position = position
        self.parent = parent
        self.g=g
        self.h=h
        self.f=g+h

    def __lt__(self, other):
        return self.f<other.f
        
def heuristic(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])
        
def a_star(graph, start, goal):
    row, col = len(graph), len(graph[0])
    open_list = []
    closed_set = set()
    start_node = Node(start, None, 0, heuristic(start, goal))
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        current_pos = current_node.position

        if current_pos == goal:
            path=[]
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]
            
        closed_set.add(current_pos)

        for move in moves:
            neighbour = (current_pos[0] + move[0], current_pos[1]+move[1])

            if (0<=neighbour[0]<row and 0<=neighbour[1]<col and graph[neighbour[0]][neighbour[1]]== 0 and neighbour not in closed_set):
                
                g= current_node.g+1
                h=heuristic(neighbour, goal)
                neighbour_node = Node(neighbour, current_node, g, h)

                if all(neighbour!= n.position  for n in open_list):
                    heapq.heappush(open_list, neighbour_node)
    return None

graph =  [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0]
]

start = (0, 0)
goal = (3, 4)

path = a_star(graph, start, goal)

if path:
    print (path)
else:
    print("No path found")
    

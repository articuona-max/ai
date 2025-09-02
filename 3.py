from collections import deque

graph={
    'A':['B','C'],'B':['D','E'],'C':['F'],'D':[],'E':[],'F':[]
    }

#bfs
def bfs(s_node):
    visit=set()
    que=deque()
    traversal = []
    print("BFS TRAVERSAL: ")      
    que.append(s_node)
    while que:
        root=que.popleft()
        if root not in visit:
            traversal.append(root)
            visit.add(root)
            for n in graph.get(root, []):
                if n not in visit:
                    que.append(n)
    print(traversal) 
    
bfs('A')

def dfs(s_node):
    visit = set()
    stack = []
    traversal = []
    print("DFS Traversal")
    stack.append(s_node)
    while stack:
        root = stack.pop()
        if root not in visit:
            traversal.append(root)
            visit.add(root)
            for n in reversed(graph.get(root, [])):
                if n not in visit:
                    stack.append(n)
    print(traversal)
dfs('A')       

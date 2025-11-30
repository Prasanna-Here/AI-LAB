from collections import deque

def dfs(graph,start,goal,visited=None,path=None):
    if visited is None:
        visited=set()
    if path is None:
        path=[]
    
    visited.add(start)
    path.append(start)

    print(f"Visiting: {start}")
    
    if start==goal:
        print("Goal found : ","->".join(path))
        return True
    
    for neighbour in graph[start]:
        if neighbour not in visited:
            if dfs(graph,neighbour,goal,visited,path):
                return True
    path.pop()
    return False

def bfs(graph,start,goal):
    visited=set()
    queue=deque([[start]])

    while queue:
        path=queue.popleft()
        node=path[-1]

        print(f"visiting: {node}")

        if node==goal:
            print("Goal Found: ","->".join(path))
            return True
        
        if node not in visited:
            visited.add(node)

            for neighbour in graph[node]:
                new_path=list(path)
                new_path.append(neighbour)
                queue.append(new_path)
    return False

def main():
    graph={
        'S':['A','B'],
        'A':['C','D'],
        'B':['E'],
        'C':[],
        'D':['G'],
        'E':['G'],
        'G':[]
    }

    start='S'
    goal='G'
    print("DFS:")
    dfs(graph,start,goal)
    print("BFS:")
    bfs(graph,start,goal)

if __name__=="__main__":
    main()
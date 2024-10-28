def dfs(graph, start):
    visited = set()  
    stack = [start]  

    while stack:
        vertex = stack.pop()  
        if vertex not in visited:
            print("Next target node: ",vertex)  
            visited.add(vertex) 
            
            for neighbor in reversed(graph[vertex]):  
                if neighbor not in visited:
                    stack.append(neighbor)

    return visited


graph = {
    0: [1, 2, 3],
    1: [0, 2],
    2: [0, 1, 4],
    3: [0],
    4: [2]
}

visited_nodes = dfs(graph, 0)
print("Visited nodes:",visited_nodes)
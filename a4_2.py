def simpleCycle(A, k):
    visited = [0] * len(A)
    
    def dfs(currentNode, depth):
        if visited[currentNode]:
            return visited[currentNode] == depth - k
        visited[currentNode] = depth
        for neighbor in range(len(A[currentNode])):
            if A[currentNode][neighbor]:  # edge
                if dfs(neighbor, depth + 1):
                    print("true", currentNode, "to", neighbor)
                    return True
        visited[currentNode] = 0
        return False

    return dfs(0, 1)

A = [[0, 1, 0, 1, 0],
     [1, 0, 1, 0, 0],
     [0, 1, 0, 1, 1],
     [1, 0, 1, 0, 1],
     [0, 0, 1, 1, 0]]
print(simpleCycle(A, 3))
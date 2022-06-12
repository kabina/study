from collections import deque

MAX = 10**5
graph = [0]*(MAX+1)
k = 5
m = 17

def bfs():
    queue = deque([k])

    while queue:
        cur = queue.popleft()
        if cur == m:
            return graph[cur]
        for dx in [cur+1, cur-1, cur*2]:
            if 0 <= dx <= MAX and graph[dx]==0:
                graph[dx]= graph[cur]+1
                queue.append(dx)

print(bfs())
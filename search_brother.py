import sys

input = sys.stdin.readline
from collections import deque

max = 100000
n, m = map(int, input().split())
graph = [0]*(max+1)

def bfs():
    queue = deque([n])
    queue.append(n)
    while queue:
        cur = queue.popleft()
        if cur == m:
            print(graph[1:50])
            return graph[cur]
        for adj in [cur-1, cur+1, cur*2]:
            if 0 <= adj <= max and graph[adj]==0:
                graph[adj] =graph[cur]+1
                queue.append(adj)

print(bfs())

import sys
from collections import deque

input = sys.stdin.readline
from collections import deque

for _ in range(int(input())):
    m, n, k = map(int, input().split())

    lis = [[0] * m for i in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        lis[y][x] = 1
    count = 0


    def dfs(lis, i, j):
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]  # 우, 좌, 하, 상
        stack = deque()
        stack.append([i,j])
        #stack = [[i, j]]

        while stack:
            a, b = stack.popleft()
            lis[a][b] = -1
            for i in range(4):
                x = a + dx[i]
                y = b + dy[i]
                if 0 <= x < n and 0 <= y < m and lis[x][y] == 1:
                    lis[x][y] = -1
                    stack.append([x, y])


    for i in range(n):
        for j in range(m):
            if lis[i][j] <= 0:
                lis[i][j] = -1
            else:
                count += 1
                dfs(lis, i, j)

    print(count)

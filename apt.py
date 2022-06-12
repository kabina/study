import sys
from collections import deque

input = sys.stdin.readline
from collections import deque

n = int(input())

lis = []
for _ in range(n):
    str = input()
    lis.append([int(str[i]) for i in range(n)])
print(lis)
count = 0
apt = []

def dfs(lis, i, j):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]  # 우, 좌, 하, 상
    stack = deque()
    stack.append([i,j])
    #stack = [[i, j]]
    sum = 0
    while stack:
        a, b = stack.popleft()
        lis[a][b] = -1
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < n and lis[x][y] == 1:
                lis[x][y] = -1
                sum += 1
                stack.append([x, y])
    return sum

for i in range(n):
    for j in range(n):
        if lis[i][j] <= 0:
            lis[i][j] = -1
        else:
            apt.append(count)
            apt[count] = dfs(lis, i, j) + 1
            count += 1

print(count)
apt.sort()
for i in range(count):
    print(apt[i])

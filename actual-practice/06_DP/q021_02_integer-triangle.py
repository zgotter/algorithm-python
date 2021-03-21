# 문제명 : 정수 삼각형
# url : https://www.acmicpc.net/problem/1932

# 직접 풀이 (2) - 시간초과
#  - recursionlimit 지정

import sys
sys.setrecursionlimit(10000)

def DFS(p, depth, sumVal):
    global result
    if depth == N:
        result = max(result, sumVal)
        return
    for a in ADJ[p]:
        if not visited[a]:
            visited[a] = True
            sumVal += T[a[0]][a[1]]
            depth += 1
            DFS(a, depth, sumVal)
            visited[a] = False
            sumVal -= T[a[0]][a[1]]
            depth -= 1

N = int(input())
ADJ = dict()
visited = dict()
T = list()

result = 0
for i in range(N):
    row = list(map(int, input().split()))
    T.append(row)
    for j in range(i+1):
        ADJ[(i,j)] = []
        ADJ[(i,j)].append((i+1, j))
        ADJ[(i,j)].append((i+1, j+1))
        visited[(i,j)] = False

visited[(0,0)] = True
DFS((0,0), 1, T[0][0])
print(result)
# 문제명 : 정수 삼각형
# url : https://www.acmicpc.net/problem/1932

# 직접 풀이 (1) 를 위한 경로 탐색 연습
#  - https://velog.io/@myway00/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-054-%EA%B2%BD%EB%A1%9C-%ED%83%90%EC%83%89%EA%B7%B8%EB%9E%98%ED%94%84-DFS

def DFS(x):
    global cnt
    if x == N:
        for i in path:
            print(i, end= ' ')
        print()
        cnt += 1
    else:
        for i in range(1, N+1):
            if g[x][i] == 1 and ch[i] == 0:
                ch[i] = 1
                path.append(i)
                DFS(i)
                path.pop()
                ch[i] = 0

N, M = map(int, input().split())
g = [[0] * (N+1) for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    g[a][b] = 1

path = []
path.append(1)
cnt = 0
ch = [0] * (N+1)
ch[1] = 1
DFS(1)
#print(cnt)


# 문제명 : 늑대와 양
# url : https://www.acmicpc.net/problem/16956

# 직접 풀이 (1) - 실패..

R, C = map(int, input().split())

arr = []
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]

for _ in range(R):
    arr.append(input())

print(arr[0][2])
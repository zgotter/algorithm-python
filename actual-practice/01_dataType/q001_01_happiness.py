# 문제명 : 행복
# url : https://www.acmicpc.net/problem/15969

n = int(input())
#scores = [int(score) for score in input().split()]
scores = list(map(int, input().split()))
print(max(scores) - min(scores))


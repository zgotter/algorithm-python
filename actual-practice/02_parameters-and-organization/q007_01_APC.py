# 문제명 : APC는 왜 서브태스크 대회가 되었을까?
# url : https://www.acmicpc.net/problem/17224

# 직접 풀이 - 100점
#  - 예제 2번 실패
#  - 문제에서 쉬운 버전의 문제 순으로 정렬되있다고 했을 뿐, 어려운 문제가 오름차순으로 정렬되어 있지 않다.
#  - 그러다 보니 뒤에 문제에서 풀 수 있는 어려운 문제를 풀어보지도 못하고 loop를 종료시키게 된다.
#  - 그러므로 풀 수 있는 문제의 수를 쉬운 버전, 어려운 버전 각각 count 해 줘야 한다.

N, L, K = map(int, input().split()) # N: 문제의 갯수, L: 역량(난이도 기준), K: 풀 수 있는 문제의 최대 개수

scores = 0
for i in range(N):
    sub1, sub2 = map(int, input().split())
    if K == 0:
        continue
    else:
        solve = False
        if sub1 <= L:
            scores += 100
            solve = True

        if sub2 <= L:
            scores += 40
            
        if solve:
            K -= 1
        
print(scores)
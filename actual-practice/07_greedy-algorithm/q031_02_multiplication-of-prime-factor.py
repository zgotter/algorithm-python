# 문제명 : 소수의 곱
# url : https://www.acmicpc.net/problem/2014

# 해설 (1)
#  - 성공

#  - 힙(Heap)을 활용해야 한다.
#  - 힙은 우선순위 큐와 유사
#  - 힙은 그룹 내에서 가장 큰 값 또는 가장 작은 값을 트리의 root에 위치시키는 자료구조이다.

import heapq
import copy

K, N = map(int, input().split())
p_list = [int(i) for i in input().split()]

# lst : heap으로 활용
# ck : 체크한 숫자를 담고 있음 (중복 포함 x; 2 x 2 x 3 = 2 x 3 x 2), set() 대신 dict()도 사용 가능
lst, ck = copy.deepcopy(p_list), set()

heapq.heapify(lst) # lst 를 리스트에서 heap으로 변환
ith = 0 # i번 째 수의 인덱스

while ith < N:
    # mn : heap에 들어 있는 값 중 가장 작은 값
    mn = heapq.heappop(lst)
    if mn in ck: # 해당 최솟값이 ck에 들어 있으면 다음 루프 진행 (중복 체크)
        continue
    # 현재까지 나오지 않은 수 인 경우
    ith += 1
    ck.add(mn)

    # 2 3 5 7
    # - 2 < 2*2
    # - 2 < 2*3
    # - 2 < 2*5
    # - 2 < 2*7
    # 내가 현재 가진 값(2)에 특정 소수(2,3,5,7)를 곱하면 반드시 해당 숫자는 커진다.
    # 2를 체크하기 전에는 2*2, 2*3, 2*5, 2*7 를 고려할 필요가 없다.

    # heap에 들어 있는 값들
    # - 2 3 5 7
    # - 3 5 7 2*2 2*3 2*5 2*7
    # - 5 7 2*2 2*3 2*5 2*7 3*2 3*3 3*5 3*7
    # - 7 2*2 2*3 2*5 2*7 3*2 3*3 3*5 3*7 5*2 5*3 5*5 5*7
    # - ...
    for i in p_list:
        if mn * i< 2**32: # 문제에 주어진 조건을 활용한 시간 복잡도 감소 시키는 로직
            heapq.heappush(lst, mn*i)

print(mn)
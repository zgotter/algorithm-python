# 문제명 : 이름 궁합 테스트
# url : https://www.acmicpc.net/problem/17269

# 직접 풀이 - 성공 (125392 KB, 136 ms)

from collections import deque

strokes = {
    'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 4,
    'F': 3, 'G': 1, 'H': 3, 'I': 1, 'J': 1,
    'K': 3, 'L': 1, 'M': 3, 'N': 2, 'O': 1,
    'P': 2, 'Q': 2, 'R': 2, 'S': 1, 'T': 2,
    'U': 1, 'V': 1, 'W': 1, 'X': 2, 'Y': 2, 'Z': 1
}

N, M = map(int, input().split())
n1, n2 = input().split()
q1, q2 = deque(), deque()


for i in range(N):
    q1.append(n1[i])

for i in range(M):
    q2.append(n2[i])

maxLength = max(N, M)
nameStr = ''

for i in range(maxLength):
    if i < N:
        nameStr += q1.popleft()
    if i < M:
        nameStr += q2.popleft()

array = []
for s in nameStr:
    array.append(strokes[s])

def makeChemistry(arr):
    if len(arr) == 2:
        return arr
    else:
        newArray = []
        for i in range(len(arr)-1):
            newArray.append((arr[i] + arr[i+1]) % 10)
        return makeChemistry(newArray)

result = makeChemistry(array)
if result[0] == 0:
    del result[0]

print(''.join(map(str, result)) + '%')
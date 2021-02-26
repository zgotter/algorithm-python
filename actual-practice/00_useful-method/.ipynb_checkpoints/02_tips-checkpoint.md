# 팁 (Tips)

# 1. 논리 연산자 / 비트 연산자 활용하기

## 1.1 논리 연산자
- `and`
- `or`
- `not`

<br/>

## 1.2 비트 연산자

- `1 << 2` (shift)
- `1 & 1` (and)
- `1 | 1` (or)
- `1 ^ 1` (xor)

<br/>

# 2. 상태를 나타내는 자료 활용하기

## 2.1 소수를 구하는 알고리즘 (한 개의 정수)

```python
N = 71
ck = 0 # False, 상태를 나타내는 자료
for i in range(2, N):
    if N % i == 0:
        print('Not Prime')
        ck = 1 # True
        break

if not ck:
    print('Prime')
```

<br/>

# 3. 나눠서 진행하기

- 특정 로직 함수로 분리하여 진행

<br/>

## 3.1 소수를 구하는 알고리즘 (여러 개의 정수)

```python
def isPrime(N):
    for i in range(2, N):
        if N % i == 0:
            return False
    return True

for N in range(10, 100):
    if isPrime(N):
        print('{} is Prime'.format(N))
    else:
        print('{} is not Prime'.format(N))
```

<br/>

## 3.2 예시 2

- BFS, DFS에서 2차원 배열, 3차원 배열에서 탐색을 하는 경우가 많다.

```python
# 0 ~ N, M 까지의 배열 중에서 a, b가 범위 안에 있는 지 확인
def isRange(a, b, N, M):
    return 0 <= a < N and 0 <= b < M
```

<br/>

# 4. 여러 자료구조와 메서드, 함수 활용하기

## 4.1 Palindrome 구현

### 4.1.1 반복문 활용

```python
S = 'hello'

for idx in S:
    if S[idx] != S[len(S) - idx - 1]:
        print('Not Palindrome')
```

<br/>

### 4.1.2 파이썬 문법 활용

```python
S = 'hello'

if S == S[::-1]:
    print('is Palindrome')
```

<br/>

## 4.2 배열의 원소가 모두 서로 다른 지 확인

```python
def isUnique(lst):
    return len(lst) == len(set(lst))
```

<br/>

# 5. 미리 처리한 케이스와 처리할 케이스 정리하기

<br/>

# 6. 예제, 최소, 최대, 예외, 랜덤 케이스 만들기

- 문제의 조건에 따른 예시를 우선적으로 사용한다.
- 최소 케이스 체크
  -  ex) 0 <= N <= 10000 : N=0 인 경우 체크
  -  체크 안할 시 인덱스 에러, 런타임 에러 등이 발생할 수 있음
- 최대 케이스 체크
  - out of range 에러 발생 체크
- 랜덤 케이스 체크

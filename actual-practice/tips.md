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
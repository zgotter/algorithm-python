# 5. 동적 계획법 (DP, Dynamic Programming)

## 5.1 DP 란?

> 다음 상태를 위해 어떤 상태를 저장하고, 저장한 상태를 계속 불러와서 사용하기

- Memoization : 어떤 상태를 저장하는 것
- DP : Memoization 을 통해 문제를 해결하는 방법

<br>

## 5.2 DP 문제 예시

- 피보나치 수
- Knapsack

<br>

## 5.3 DP 문제 해결 순서

### 5.3.1 상태를 정의

- 2차원 배열을 만들었을 때 `DP[i][j]` 에서 `i` 와 `j` 가 무엇을 의미하는 지 정의
  - ex) `DP[i][j]` : `i` 부터 `j` 까지의 거리의 합
- 초기 상태 정의
  - ex) 피보나치 : 첫 번째, 두 번째 값을 각각 `1`로 정의

<br>

### 5.3.2 점화식을 찾기(구하기)

- 점화식 : 다음 상태를 나타내는 표현식
  - ex) 피보나치 : `F[i] = F[i-1] + F[i-2]`
- 모든 `i`에 대한 점화식이 있을 수도 있고, `i`가 짝수, 홀수 인 경우에 따른 점화식이 존재할 수 도 있다.

<br>

### 5.3.3 시간 복잡도를 계산

- DP로 푸는 문제들은 시간 복잡도가 다양하다.
  - `O(n)` : 1차원 배열 탐색
  - `O(n^2)` : 2차원 배열 탐색
- 보통의 코딩 테스트에서는 3차원 배열 이상은 잘 등장하지 않는다.
- 시간 복잡도를 계산하는 단순한 방법
  - 반복문을 얼만큼 사용했는 가?
    - ex) 이중 반복문 안에서 이진 탐색 수행 -> `O(n^2logn)`
- 파이썬으로 문제를 풀 때 시간 복잡도 계산이 중요하다.
  - 시간 복잡도가 `O(n^2)` 이고 `n=1000` 이면 시간 복잡도는 `1,000,000` 이 된다.
  - 이 때 이 것을 재귀로 풀었을 경우 이 값도 파이썬으로 수행하기 힘들 수 있다.

<br>

### 5.3.4 코딩

<br>

## 5.4 DP 문제 해결 방법

### 5.4.1 Top-Down (재귀)

- 재귀함수를 사용하여 문제를 해결하는 방법
- Java 에서는 해당 방법을 사용하는 것이 좋다.
- 파이썬에서 해당 방법을 이용하여 문제를 풀면 시간 복잡도가 아슬아슬 할 수 있다.

<br>

### 5.4.2 Bottom-Up (반복문)

- 문제를 초기 상태부터 차근차근 쌓아 나아가는 방법
- 점화식대로 반복문을 사용하면 된다.
- 파이썬에서는 해당 방법을 사용하기를 권장한다.
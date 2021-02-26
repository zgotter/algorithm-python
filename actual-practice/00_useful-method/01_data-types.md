# 1. 자료형의 기본 활용과 Tip

## 1.1 기본 자료형

### 1.1.1 single

- 단일 변수를 다루는 자료형

<br>

**1) Integer**
- 파이썬의 Integer 자료형은 overflow가 없다. (즉, 크기의 제한이 없다.)
- 따라서 나머지 연산 시 장점을 갖는다.
- 정수를 문자로 변환하는 방법이 간단하다. (`str(123)`)
- 정수 사이의 나누기 연산을 하면 결과값이 실수형(Float)으로 반환된다.
- 이는 다음 두 가지 방법을 통해 정수형 결과값이 나오게 할 수 있다.
  - `3//3`
  - `divmod(3,3)[0]`

<br>

**2) Float**
- 코딩 테스트에서는 Float 자료형을 연산에 사용하지 않는 것이 좋다.
- 유리수 연산 시에는 될 수 있다면 tuple 등으로 분자/분모를 따로 처리하는 것이 좋다.
  - `1/3` -> `(1,3)`

<br>

**3) String**
- Immutable 변수 : String은 변경이 불가능한 변수이다.
- 문자열 연산(`+`,`*`)을 조심해야 한다. (기본 연산 대신 여러 가지 함수들(ex. `join()`을 활용하는 것이 시간을 단축할 수 있다.)
- `.split()`, `.replace()` 등 다양한 함수들이 활용된다.
- Slicing 을 효율적으로 활용할 수 있어야 한다.
- `chr()`, `ord()` 함수를 다룰 줄 알아야 한다.
  - 단일 문자열 함수 (아스키 코드 관련)


```python
chr(65)
```


    >> 'A'


```python
ord('A')
```


    >> 65

<br>

**4) Boolean**
- `True(1)`, `False(0)`  
  
- Short Circuit : 연산을 최적화해주는 기능

- `and` 연산에서는 앞의 항이 거짓이면 뒤의 항을 무시한다.


```python
if 0 and 1//0:
    print('hello')
```

- `or` 연산에서는 앞의 항이 참이면 뒤의 항을 무시한다.


```python
if 1 or 1//0:
    print('hello')
```

    >> hello


<br>

### 1.1.2 container

- 여러 개의 변수를 다루는 자료형

<br>

**1) List**

- List Comprehension 사용하기
  - `.append()`를 사용하는 것 보다 리스트 컴프리헨션을 사용하는 게 더 빠른 경우가 많다.


```python
list_arr = [i for i in range(10)]
list_arr
```


    >> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



- `sort()`와 `sorted()` 구분하기
  - `list.sort()` : 리스트를 정렬하는 메서드
  - `sorted(list)` : 리스트를 정렬한 객체를 반환하는 함수


```python
lst = [3, 5, 6, 9, 2]
lst
```


    >> [3, 5, 6, 9, 2]


```python
print(sorted(lst))
print(lst)
```

    >> [2, 3, 5, 6, 9]
    >> [3, 5, 6, 9, 2]

```python
lst.sort()
print(lst)
```

    >> [2, 3, 5, 6, 9]


- `len()`, `sum()`, `max()`, `min()` 등의 함수 활용


```python
s = 'abs'
len(s)
```


    >> 3


```python
len(lst)
```


    >> 5


```python
sum(lst)
```


    >> 25


```python
max(lst)
```


    >> 9


```python
min(lst)
```


    >> 2



- Slicing, `[-1]` 등 음수 인덱스 활용


```python
# 리스트의 맨 앞에 원소 추가하는 방법 (1)
lst = [1] + lst
lst
```


    >> [1, 2, 3, 5, 6, 9]




```python
# 리스트의 맨 앞에 원소 추가하는 방법 (2)
lst[0:0] = [0]
lst
```


    >> [0, 1, 2, 3, 5, 6, 9]




```python
# 음수 인덱스 (마지막 원소 반환)
lst[-1]
```


    >> 9



<br>

**2) Tuple**

- 초기 상태 표현 시 코드를 간결하게 해준다.


```python
# 튜플 활용 x
a = 1
b = 2
c = 3
print(a)
print(b)
print(c)
```

    >> 1
    >> 2
    >> 3



```python
# 튜플 활용 o
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)
```

    >> 1
    >> 2
    >> 3


- `map()` 과 함께 사용하여 입력 받기


```python
a, b = map(int, input().split())
print(f'a : {a}')
print(f'b : {b}')
```


    >> a : 3
    >> b : 7


- 동시에 변해야 하는 객체에 효율적 표현 가능


```python
a, b = 3, 7
print(a)
print(b)

a, b = b, a # swap
print(a)
print(b)
```

    >> 3
    >> 7
    >> 7
    >> 3


<br>

**3) Dictionary**

- `keys()`나 `values()`를 사용하여 효율적인 사용 추천


```python
dict_test = {1:2, 2:3, 'abc': 7}
print(dict_test)
```

    >> {1: 2, 2: 3, 'abc': 7}



```python
dict_test.keys()
```


    >> dict_keys([1, 2, 'abc'])




```python
dict_test.values()
```


    >> dict_values([2, 3, 7])



- `collections.Counter` 를 사용할 때 딕셔너리가 활용된다. 

<br>

**4) Set**

- 집합 자료형

- 중복 체크에 활용
  - `set(list)` 사용 (리스트 객체를 `set()` 함수에 넣어주기)


```python
st = set([1,2,3,4,5,1,2,3,4,5])
st
```


    >> {1, 2, 3, 4, 5}




```python
# 리스트 원소 중복 여부 체크 함수 구현
def isCheck(lst):
    return len(lst) == len(set(lst))
   
print(isCheck([1,2,3,2,3]))
print(isCheck([1,2,3]))
```

    >> False
    >> True


- 합집한, 여집합, 차집합 등 집합 연산 가능
  - 시간복잡도가 크므로 사용 시 주의 필요

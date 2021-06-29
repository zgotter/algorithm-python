# 성공
# 다른 사람 풀이 참고

def solution(numbers):
    answer = ''
    numbers = [str(num) for num in numbers]
    numbers.sort(key=lambda x: x*3, reverse=True) # 원소의 길이가 0~1000 이므로 3자리수로 만들어서 비교 정렬
    return str(int(''.join(numbers))) # int -> str : 모든 숫자가 0인 경우(ex. 000)를 처리하기 위해
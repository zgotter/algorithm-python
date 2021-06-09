# 성공
# 다른 사람 풀이 참고
# count() 함수 사용 - lst.count('a') : 문자열 또는 리스트인 lst에서 'a' 의 갯수 반환

def solution(s):
    answer = [0,0]
    while s != '1':
        answer[0] += 1
        num = s.count('1')
        answer[1] += len(s) - num
        s = bin(num)[2:]
    return answer
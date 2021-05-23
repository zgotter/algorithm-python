# 성공
# 조합(Combinations) 이중for문으로 구현

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    answer = list(set(answer))
    answer.sort()
    return answer
# 성공
# 다른 사람 풀이 참고

def solution(name):
    # 상하 조정으로 알파벳 바꾸기
    #  - 각 알파벳 마다 상하 조정 중 min값으로 최소 횟수를 담아두기
    change = [min(ord(i) - ord('A'), ord('Z') - ord(i)+1) for i in name]
    idx = 0
    answer = 0
    while True:
        answer += change[idx] # idx 0번 부터 시작해서 좌우 이동 횟수를 answer에 더해주기
        change[idx] = 0
        # 모든 알파벳이 조정된 경우(sum(change) == 0) 결괏값 반환
        if sum(change) == 0:
            break
        
        # 좌우 이동방향 정하기
        #  - 좌우 방향 전환 시에는 바꿔야하는 알파벳이 나오기까지의 좌우 거리를 구하고
        #    그 중 최소값이 되는 방향으로 전환
        left, right = 1, 1
        while change[idx - left] == 0:
            left += 1
        while change[idx + right] == 0:
            right += 1
        # 위치(인덱스) 조정
        answer += left if left < right else right
        idx += -left if left < right else right
        
    return answer
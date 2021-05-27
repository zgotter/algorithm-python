# 성공
# 다른 사람 풀이 참고
# board의 형태를 잘못 이해했음..

def solution(board, moves):
    answer = 0
    bucket = []
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] > 0:
                bucket.append(board[i][move-1])
                board[i][move-1] = 0
                if len(bucket) > 1 and bucket[-1] == bucket[-2]:
                    answer += 2
                    bucket = bucket[:-2]
                break
    return answer
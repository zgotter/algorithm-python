# 제출 시 실패

def solution(board, moves):
    answer = 0
    bucket = []
    for move in moves:
        move -= 1
        
        # 인형 꺼내기
        line = board[move]
        if len(line) == 0: continue
        doll = line.pop()
        if doll == 0: continue
            
        # 바구니에 넣기
        if len(bucket) == 0:
            bucket.append(doll)
        else:
            last_doll = bucket[-1]
            if last_doll == doll:
                answer += 2
                bucket.pop()
            else:
                bucket.append(doll)
    return answer
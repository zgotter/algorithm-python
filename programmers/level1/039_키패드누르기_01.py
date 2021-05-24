# 성공

pad = [[str(i+j) for i in range(1,4)] for j in range(0,7,3)]
pad.append(['*','0','#'])

def get_pos(a):
    for i in range(4):
        for j in range(3):
            if pad[i][j] == a:
                return (i, j)
            
def get_distance(a, b):
    a_pos = get_pos(a)
    b_pos = get_pos(b)
    return abs(a_pos[0] - b_pos[0]) + abs(a_pos[1] - b_pos[1])
        

def solution(numbers, hand):
    answer = []
    l_pos, r_pos = '*', '#'
    for num in numbers:
        num = str(num)
        if num in ['1','4','7']:
            l_pos = num
            answer.append('L')
        elif num in ['3','6','9']:
            r_pos = num
            answer.append('R')
        else:
            l_dist = get_distance(l_pos, num)
            r_dist = get_distance(r_pos, num)
            if l_dist > r_dist:
                r_pos = num
                answer.append('R')
            elif l_dist < r_dist:
                l_pos = num
                answer.append('L')
            else:
                if hand == 'right':
                    r_pos = num
                    answer.append('R')
                else:
                    l_pos = num
                    answer.append('L')
    return ''.join(answer)
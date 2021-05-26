# 성공
# 복습
# 10진수 -> base진수 : get_data(n, base)
# base진수 -> 10진수 : int(base진수값, base) -> 10진수값 리턴

def get_data(n, base):
    ans = []
    while n > 0:
        n, r = divmod(n, base)
        ans.append(str(r))
    return ''.join(reversed(ans))

def solution(n):
    answer = get_data(n, 3)
    answer = answer[::-1]
    answer = int(answer, 3)
    return answer

print(solution(45))
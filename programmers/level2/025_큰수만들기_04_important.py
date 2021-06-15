# 성공
# 다른 사람 풀이

def solution(number, k):
    stack = []
    for n in number:
        while stack and n > stack[-1]:
            if k > 0:
                stack.pop()
                k -= 1
            else:
                break
        stack.append(n)
    if k > 0:
        for i in range(k):
            stack.pop()
    return ''.join(stack)

print()
#print(solution('1924', 2)) # 94
print(solution('1231234', 3)) # 3234
#print(solution('4177252841', 4)) # 775841
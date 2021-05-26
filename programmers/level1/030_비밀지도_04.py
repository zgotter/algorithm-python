# 성공 (복습)

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        ans = bin(arr1[i]|arr2[i])[2:].rjust(n,'0')
        ans = ans.replace('0',' ')
        ans = ans.replace('1','#')
        answer.append(ans)
    return answer
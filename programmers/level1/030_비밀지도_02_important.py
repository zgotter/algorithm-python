# 다른 사람 풀이
# 성공
# 10진수 -> 2진수 변환

def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        a12 = str(bin(i|j))[2:] # bin() 을 통해 이진수로 변환된 문자의 앞에 두글자(0b)는 제거
        a12 = a12.rjust(n, '0') # 자리수 맞춰 왼쪽에 '0' 채우기 (s12.zfill(n) 이랑 같은 효과)
        a12 = a12.replace('1','#')
        a12 = a12.replace('0',' ')
        answer.append(a12)
    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])) # ["#####","# # #", "### #", "# ##", "#####"]
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10])) # ["######", "### #", "## ##", " #### ", " #####", "### # "]


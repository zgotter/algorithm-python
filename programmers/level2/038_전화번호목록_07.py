# 성공
# 인접해 있는 두 개만 비교하면 될듯..?

def solution(phoneBook):
    phoneBook = sorted(phoneBook)
    for i in range(len(phoneBook)-1):
        if phoneBook[i+1].startswith(phoneBook[i]):
            return False
    return True
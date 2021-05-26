# 성공
# 다른 사람 풀이 참고하여 복습
# 정규 표현식 활용

import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9-_.]*', '', st)
    st = re.sub('[.]+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st
    st = st[:15] if len(st) >= 16 else st
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + ''.join([st[-1] for _ in range(3-len(st))])
    return st
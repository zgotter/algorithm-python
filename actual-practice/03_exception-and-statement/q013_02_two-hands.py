# 문제명 : 두 개의 손
# url : https://www.acmicpc.net/problem/16675

# 해설 (1) - 성공
# - 가위바위보는 moduler 연산과 유사하다.
#  - 0(가위), 1(바위), 2(보)
#  - 1 > 0 : 바위 > 가위
#  - 2 > 1 : 보 > 바위
#  - 0 > 2 : 가위 > 보

# str.index() 와 str.find() 둘 다 사용 가능
ML, MR, TL, TR = ('RSP'.index(i) for i in input().split()) # R S P R -> 1 0 2 1

# (ML+2) % 3
#  - 내가 가위를 가지고 있음 (ML=0)
#  - 상대방이 보를 가지고 있어야 내가 이길 수 있다. ((ML+2)%3 = 2 % 3 = 2)

#  - 내꺼 | 내가 이길 수 있는 거
#  - 0    |    2 (= (0+2) % 3)
#  - 1    |    0 (= (1+2) % 3)
#  - 2    |    1 (= (2+2) % 3)

if ML == MR and (ML+2)%3 in [TL, TR]:
    print('TK')
elif TL == TR and (TL+2)%3 in [ML, MR]:
    print('MS')
else:
    print('?')
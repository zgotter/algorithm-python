# 문제명 : 걸그룹 마스터 준석이
# url : https://www.acmicpc.net/problem/16165

# 직접 풀이 - 성공
#  - 리스트의 인덱스 활용

N, M = map(int, input().split())

teamNameList = []
memberCntList = []
memberNameList = []

for _ in range(N):
    teamNameList.append(input()) # 팀 이름
    memberCnt = int(input())
    memberCntList.append(memberCnt)
    nameList = []
    for _ in range(memberCnt):
        nameList.append(input()) # 맴버 이름
    memberNameList.append(sorted(nameList))

def getMemberName(value):
    idx = teamNameList.index(value)
    for name in memberNameList[idx]:
        print(name)

def getTeamName(value):
    for idx, lst in enumerate(memberNameList):
        if value in lst:
            print(teamNameList[idx])

for _ in range(M):
    value = input()
    quizType = int(input())
    if quizType == 0:
        getMemberName(value)
    else:
        getTeamName(value)


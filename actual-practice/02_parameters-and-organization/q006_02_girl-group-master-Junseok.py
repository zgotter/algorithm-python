# 문제명 : 걸그룹 마스터 준석이
# url : https://www.acmicpc.net/problem/16165

# 해설 (1) - 성공
#  - 딕셔너리와 리스트를 함께 사용

N, M = map(int, input().split())

team_mem, mem_team = {}, {}

for i in range(N):
    team_name, mem_num = input(), int(input())
    team_mem[team_name] = []
    for j in range(mem_num):
        name = input()
        team_mem[team_name].append(name)
        mem_team[name] = team_name

for i in range(M):
    name, q = input(), int(input())
    if q: # q == 1
        print(mem_team[name])
    else: # q == 0
        for mem in sorted(team_mem[name]):
            print(mem)
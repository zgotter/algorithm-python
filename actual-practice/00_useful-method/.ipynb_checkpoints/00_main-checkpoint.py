# ctrl + shift + d : 디버그 창 활성화

# input이 있는 경우
#  - 터미널에 input 값을 직접 입력할 수 있음
#N = int(input())
#print(N)

#  - 'launch.json' 파일의 'configuation'에 다음 내용을 추가하여 'input.txt' 파일 내용을 실행 시킬 수 도 있음
# "args": ["<", "input.txt"]

#  - 위 내용을 다음과 같이 수정하면 출력 결과를 'output.txt' 파일로 저장할 수 있다.
# "args": ["<", "input.txt", ">", "output.txt"]
N = input()
#N = "a"
print(N)


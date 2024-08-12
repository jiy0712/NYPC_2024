from collections import defaultdict
#defultdict 불러와 딕셔너리 쉽게 만들 수 있도록

def count_lines(n, coords): #n을 받아 x,y 동일한 값이 있는 라인의 수 계산하는 함수
    x = defaultdict(int) #기본값 0. x 좌표에 대한 defaultdict 생성
    y = defaultdict(int) #기본값 0. y 좌표에 대한 defaultdict 생성

    for a, b in coords: #좌표에 대한 반복
        x[a] += 1 # x좌표 a에 +1
        y[b] += 1 # y좌표 b에 +1

    #x좌표 중 2개 이상 겹치는지 확인. 해당 값의 개수 계산
    x_count = sum(1 for count in x.values() if count > 1)
    #y좌표 중 2개 이상 겹치는지 확인. 해당 값의 개수 계산
    y_count = sum(1 for count in y.values() if count > 1)

    return x_count + y_count #x좌표 + y좌표 더한 값 반환

n = int(input()) #n에 int형식으로 input받기
coords = [tuple(map(int, input().split())) for _ in range(n)]
# n개의 좌표를 입력받아 튜플의 리스트로 저장

print(count_lines(n, coords))
# count_lines함수를 호출 -> 결과출력

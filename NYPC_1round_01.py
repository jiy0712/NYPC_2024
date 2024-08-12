import sys #sys 불러오기
input = sys.stdin.read #input : 함수(한번에 모두 읽어오는)

def min(PufferCount, SeagrapesCount): #두개의 수로 최소값 계산하는 함수
    if PufferCount > SeagrapesCount: #복어가 바다포도보다 크다면
        PufferCount, SeagrapesCount = SeagrapesCount, PufferCount
        #두개의 값을 변환화며 복어가 더 작도록 유지
    if SeagrapesCount > 3 * PufferCount: #바다포도가 복어*3보다 크다면
        return -1
    return (PufferCount + SeagrapesCount + 3) // 4

def main(): #main함수
    data = input().split() #data : 공백기준 나누어 리스트로 변환
    A = int(data[0]) #1번째 값을 정수로 변환해 A에 저장
    results = [] #빈 리스트
    B = 1
    for _ in range(A): # _ = 아무것도 없이, range(A) data[0] 출력
        PufferCount = int(data[B]) #복어 = int(data[1])
        SeagrapesCount = int(data[B + 1]) #바다보도 int(data[1+1])
        results.append(str(min(PufferCount, SeagrapesCount)))
        #min 함수를 문자열로 변환하여 results에 추가
        B += 2 # B 1+2 ..... B 3+2 .....
    print("\n".join(results)) #결과 한줄씩 출력

if __name__ == "__main__": #이 코드가 직접 실행될때만 main()함수 호출
    main() #main함수 호출하며 프로그램 실행

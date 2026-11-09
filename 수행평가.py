password = "password"  # 정답 비밀번호
count = 0  # 틀린 횟수
max_count = 5  # 최대 시도 횟수

print("로그인 하십시오.")  # 제목 출력

while True:  # 반복 시작
    pw = input("비밀번호를 입력해 주세요: ")  # 비밀번호 입력
    if pw == password:  # 비밀번호가 맞으면
        print("로그인 되었습니다.")  # 로그인 성공
        break  # 반복 종료
    else:  # 비밀번호가 틀리면
        count += 1  # 틀린 횟수 1 증가
        print("비밀번호가 틀렸습니다.")  # 틀렸다고 안내
        if count == max_count:  # 3번 틀렸으면
            print("3번 틀렸습니다.")  # 횟수 초과 안내
            break  # 반복 종료
        else:  # 아직 기회가 남았으면
            print("남은 기회:", max_count - count)  # 남은 기회 출력
            print("다시 입력해 주세요.")  # 다시 입력 안내

print("======================")  # 구분선
print("틀린 횟수:", count)  # 틀린 횟수 출력
print("프로그램을 종료합니다.")  # 종료 안내
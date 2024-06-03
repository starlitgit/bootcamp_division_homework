"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    # 시간 입력 받기
    hour = int(input("시간을 입력하세요 (0부터 23까지): "))

    # 입력된 시간이 12시 이전이면 AM 출력, 그렇지 않으면 PM 출력
    if 0 <= hour < 12:
        print("AM")
    else:
        print("PM")

if __name__ == '__main__':
    main()

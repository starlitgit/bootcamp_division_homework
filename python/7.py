"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
# 연도와 월 입력 받기
    year = int(input("연도를 입력하세요: "))
    month = int(input("월을 입력하세요: "))

    # 입력한 연도가 윤년인지 판단하여 해당하는 달의 날 수 출력
    if month in [4, 6, 9, 11]:
        print("30")
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print("29")
        else:
            print("28")
    else:
        print("31")

if __name__ == '__main__':
    main()

"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():

  # 세 자리 정수 입력 받기
    num = input("세 자리 정수를 입력하세요: ")
    
    # 입력된 정수를 역순으로 출력
    reversed_num = num[::-1]
    print("출력:", reversed_num)

if __name__ == '__main__':
    main()

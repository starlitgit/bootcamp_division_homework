"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    # 나이와 키 입력 받기
    age = int(input("나이를 입력하세요: "))
    height = int(input("키를 입력하세요: "))

    # 놀이방 입장 가능 여부 판단
    if age >= 14 or height >= 160:
        print("X")
    else:
        print("O")

if __name__ == '__main__':
    main()

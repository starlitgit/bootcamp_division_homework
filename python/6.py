"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    # 알파벳 문자 하나 입력 받기
    char = input("알파벳 문자 하나를 입력하세요: ")

    # 입력된 문자가 모음인지 판단하여 출력
    if char in ['a', 'e', 'i', 'o', 'u']:
        print("O")
    else:
        print("X")
        
if __name__ == '__main__':
    main()

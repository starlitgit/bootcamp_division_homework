"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    # 양의 정수 n 입력 받기
    while True:
        n = int(input("양의 정수를 입력하세요: "))
        if n > 0:
            break
        else:
            print("X")

    # 1부터 n까지의 합 계산
    sum_of_integers = sum(range(1, n + 1))

    # 합 출력
    print(sum_of_integers)

if __name__ == '__main__':
    main()

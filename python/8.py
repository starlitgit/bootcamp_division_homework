"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    # 정수 n 입력 받기
    n = int(input("정수를 입력하세요 (12 이하): "))

    # 1부터 n까지의 정수의 합 계산
    sum_of_integers = sum(range(1, n + 1))

    # n! 계산
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    # 결과 출력
    print(sum_of_integers)
    print(factorial)

if __name__ == '__main__':
    main()

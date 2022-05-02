# 알고리즘 복잡도 계산이 필요한 이유

# 1. 하나의 문제를 푸는 알고리즘은 다양할 수 있음

# -> 다양한 알고리즘 중 어느 알고리즘이 더 좋은지 분석하기 위해 복잡도 정의하고 계산한다.

# 2. 알고리즘 복잡도 계산 항목

# -> 시간 복잡도: 알고리즘 실행 속도
# -> 공간 복잡도 : 알고리즘이 사용하는 메모리 사이즈

# 3. 알고리즘 시간 복잡도의 주요 요소
# -> 반복문이 관건입니다.

# 프로그래밍에서 시간 복잡도에 가장 영향을 많이 미치는
# 요소는 반복문

# 입력의 크기가 커지면 커질 수 록 반복문이 알고리즘 수행 시간을 지배한다.

# 알고리즘 성능 표기법
# - Big O 표기법: O(N)
# 알고리즘 최악의 실행 시간을 표기법
# 가장 많이(일반적)으로 사용함
# 아무리 최악의 상황을 가정하라도 이정도는 성능은 보장한다는 의미
# - 오메가 표기법 
# 오메가 표기법은 알고리즘 최상의 실행 시간을 표기
# - 세타 표기법 
# 오메가 표기법은 알고리즘 평균 실행 시간을 표기

# 시간 복잡도 계싼은 반복문이 핵심 요소임을 인지하고, 계산 표기는
# 최상, 평균, 최악 중, 최악의 시간인 Big-O 표기법을 중심으로 익히면 된다.

# 대문자 O 표기법
# 입력 n에 따라 결정되는 시간 복잡도 함수
# 입력 n의 크기에 따라 기하급수적으로 시간 복잡도가 늘어 날 수 있다.

# 단순하게 입력 n에 따라 몇번 실행이 되는지를 계산한다.

# 상수
# n=12
# if n > 10:
#     print(n)

# # n에 따라 n번 n+10번 또는 3n+10번등 실행한다.
# variable = 1
# for num in range(3):
#     for index in range(n):
#         print(index)

# variable =1
# for i in rnage(300):
#     for num in range(n)
#     for index in range(n):
#         print(index)

# O(n)
def sum_all(n):
    total = 0
    for num in range(1, n+1):
        total += num
    return print(total)

sum_all(100)

# O(1)
def sum_all2(n):
    return print(int(n*(n+1)/2))

sum_all2(100)


# 위와 같이 동일한 문제를 푸는 알고리즘은 다양할 수 있음 어느 알고리즘이 보다 좋은지를 객
# 관적으로 비교하기 위해, 빅 오 표기법등의 시간복잡도 계산법을 사용함

# O(n) vs O(1)
# 스택 LIFO 정책   책
# 큐는 FIFO 정책   줄

# 프로그램 실행될 때 
# 프로세스 구조의 함수 동작 방식이 스택

def recursive(data):
    if data < 0:
        print("ended")
    else: 
        print(data)
        recursive(data-1)
        print("returned", data)


recursive(4)        

data_stack = list()

data_stack.append(1)
data_stack.append(2)

print(data_stack)


data_stack.pop()


print(data_stack)



stack_list = list()

def push(data):
    stack_list.append(data)

def pop():
    data = stack_list[-1]
    del stack_list[-1]
    return data



for index in range(10):
    push(index)

pop()    


장점
구조가 단순해서, 구현이 쉽다.
데이터 저장/읽기 속도가 빠르다.

단점
데이터 최대 갯수를 미리 정한ㄷ.(파이썬은 1000번까지만 호출 가능)
저장 공간의 낭비가 발생할 수 있다.(미리최대갯수만큼 저장공간을 확보해야함)
 스택은 단순하고 성능을 위해 사용되므로, 보통 배열 구조를 활용해서 구현하는 것이 일반적임. 이 경우, 위에서 열거한 단점이 있을 수 있다.

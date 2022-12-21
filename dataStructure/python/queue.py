# Queue - FIFO

# 가장 먼저 넣은 값을 가장 먼자 출력하는 자료구조

# Enqueue 큐에 데이터를 넣는 기능
# Dequeue 큐에 데이터를 꺼내는 기능

import queue
# data_queue = queue.Queue()
# data_queue = queue.LifoQueue();
data_queue = queue.PriorityQueue();

# data_queue.put(1);
# data_queue.put(2);
# data_queue.put(3);

# qsz = data_queue.qsize()
# print('queue size',qsz)

# print(data_queue.get())
# print(data_queue.get())
# print(data_queue.get())


data_queue.put((1, "korea"));
data_queue.put((2, "china"));
data_queue.put((3, "usa"));

qsz = data_queue.qsize()
print('queue size',qsz)

print(data_queue.get())
print(data_queue.get())
print(data_queue.get())



# LIFO QUEUE도 있다 - 스택이랑 동일하게 후입선출
# 멀티 태스킹을 위한 프로세스 스케줄링 방식을 구현하기 위해 많이 사용됨
# 큐의 경우에는 장단점 보다는 큐의 활용 예로 프로세스 스케줄링 방식을 함께 이해해두는것이 좋다

queue_list = list()
def enqueue(data):
    queue_list.append(data)

def dequeue():
    data = queue_list[0]    
    del queue_list[0]
    return data

enqueue(1)
enqueue(2)
enqueue(3)
enqueue(4)
print(dequeue())


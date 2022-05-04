class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)
    
    def move_up(self, inserted_idx):

        if inserted_idx <= 1:
            return False
        parent_idx = inserted_idx//2

        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            return True
        else:
            return False

    def insert(self, data):
        if len(self.heap_array)==0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True
        
        self.heap_array.append(data)

        inserted_idx = len(self.heap_array)-1

        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_idx]
            inserted_idx = parent_idx
        return True

# 최대 힙 조건
# 항상 왼쪽부터 노드가 채워진다.(완전 이진 트리)
# 부모노드는 항상 자식 노드보다 크며 최상위 부모느드는 최대 값이다.
# 왼쪽과 오른쪽의 값에 대한 크기 비교는 의미가 없으며 오직 부모와 자식간의 크기가 의미가 있다.(insert 할 때마다 부모와 자식 값만 비교하면 된다.)

# insert 함수는 실직적으로 값을 넣고 특정 조건에 의해 부모와 자식 노드의 크기 나눠 넣는 것이고
# move_up은 insert 함수에서 부모와 자식의 크기를 기준으로 나눠 넣기 위한 기준을 제공하는 곳


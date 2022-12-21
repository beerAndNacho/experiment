# 힙 조건
# 완전 이진 트리(항상 왼쪽부터 채우는 형태)
# 최대 힙은 맨위가 최대값 (항상)
# 최소 힙은 맨위가 최소값 (항상)

class Heap:
    def __init__(self, data):
        self.heap_array =list()
        # 힙의 노드의 idx는 1부터 시작함을 고려해서 배열 첫번 째 값은 None으로 채운다
        self.heap_array.append(None)
        self.heap_array.append(data)

    def move_up(self,inserted_idx):
        if inserted_idx <=1:
            return False
        parent_idx = inserted_idx // 2
        if self.heap_array[inserted_idx]>self.heap_array[parent_idx]:
            return True
        else:
            return False

    def insert(self,data):
        # 힙의 idx가 0일 때 첫 번째 값으로 None을 넣고 그 다음 idx 1번째부터  data를 넣는다.
        if len(self.heap_array)==0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True
        # 무조건 들어오는 data를 배열에 넣는다
        self.heap_array.append(data)
        
        # 일부러 0 idx 넘기고 했기에 -1
        inserted_idx = len(self.heap_array)-1 

        # 다 넣어진 배열을 힙 구조에 맞게 재배치를 시키는 코드
        while self.move_up(inserted_idx):
            parent_idx = inserted_idx //2
            # 스왑하는 형태
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_idx] 
            inserted_idx = parent_idx
        return True
        
# insert 될 때마다 배열과 동시에 부모와 자식간의 값을 비교하여 값의 위치를 바꾼다!
heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)

print(heap.heap_array)

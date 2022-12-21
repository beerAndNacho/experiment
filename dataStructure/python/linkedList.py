# 링크드리스트는 순차적인 연결이 아닌 떨어진 것과의 연결이 가능한 자료구조
# 이전과 다음의 가리키는 포인터를 갖고 있는 노드로 구성되어있다.

# 따라서 하나의 노드를 생성할 때는 이전과 다음값을 담을 수 있는 공간을 항상 생성자로
# 마련해야 한다.
# 다음은 그 노드를 관리하는 형태로서 기본적으로 헤더와 테일부분을 고려한다.


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Nodemgmt:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        node = self.head
        if node == '':
            self.head = Node(data)
        else:
            while node.next:
                node = node.next
            node.next = Node(data)
    
    def desc(self):
        node = self.head
        if node=='':
            return print(None)

        while node:
            print(node.data)
            node = node.next
    
    def insert(self, insertData, findData):
        node = self.head
        if node == '':
            print('findData는 물론 head값도 없어 head에 데이터를 Insert했습니다.')
            node = Node(insertData)
            return
        else:
            while node:
                if node.data == findData:
                    tempNode = node.next
                    newNode = Node(insertData)
                    node.next = newNode
                    newNode.next = tempNode
                    # return 리턴을 안걸어주면 무한히 findData을 갖는 노드 다음값에 노드를 추가하여 무한루프 돈다.
                    return
                else:
                    node = node.next

    def delete(self, deleteData):
        node = self.head
        if node =='':
            print('지울 데이터가 없습니다.(1)')                
        else:
            if node.data == deleteData:
                print(deleteData,'을 삭제하였습니다.')
                del node
                return
            else:
                while node:
                    node_next = node.next
                    if node_next.data == deleteData:
                        print(deleteData,'을 삭제하였습니다.')
                        del node.next
                        node.next = node_next.next
                        return
                    else:
                        node = node.next
                print('지울 데이터가 없습니다.(2)')

linkedList = Nodemgmt(0)
linkedList.desc()

for data in range(1, 10):
    linkedList.add(data)

linkedList.insert(7.5,7)


linkedList.desc()

linkedList.delete(0)

linkedList.desc()






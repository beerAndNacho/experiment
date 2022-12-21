# search_from_head, search_from_tail, insert_before, insert_after

class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
    
    def add_from_head(self, data):
        node = self.head
        if node == "":
            self.head = Node(data)
            self.tail = self.head
        else:
            while node.next:
                node = node.next
            newNode = Node(data)
            node.next = newNode
            newNode.prev = node
            self.tail = newNode

    def add_from_tail(self, data):
        node = self.tail
        print(node.data)
        if node == '':
            self.tail = Node(data)
            self.head = Node(data)
        else:
            while node.prev:
                node = node.prev
            newNode = Node(data)
            node.prev = newNode
            newNode.next = node
            self.head = newNode
    def search_from_head(self, data):
        node = self.head
        if node == '':
            print('search할 값이 없습니다.')
        else:
            while node:
                if node.data == data:
                    print(data, '을 찾았습니다!')
                    return
                else:
                    node = node.next
            print(data, '을 못찾았습니다ㅠ')    
    
    def search_from_tail(self, data):
        node = self.tail
        if node == '':
            print('search할 값이 없습니다.')
        else:
            while node:
                if node.data == data:
                    print(data, '을 찾았습니다!')
                    return
                else:
                    node = node.prev
            print(data, '을 못찾았습니다!')
    
    def insert_after(self, data, after_data):
        node = self.head
        if node == '':
            self.head = Node(data)
            self.tail = self.head
        else:
            while node:
                if node.data == after_data:
                    newNode = Node(data)
                    node_next = node.next

                    if node_next == None:
                        node.next = newNode
                        newNode.prev = node
                        self.tail = newNode
                    else:
                        node.next = newNode
                        newNode.prev = node
                        newNode.next = node_next
                        node_next.prev = newNode
                        if node_next.next == None:
                            self.tail = node_next
                    # return 매우 중요 이게 빠지면 무한 루프 돈다!
                    return
                else:
                    node = node.next

    def insert_before(self, data, before_data):
        node = self.tail
        if node == '':
            self.head = Node(data)
            self.tail = self.head
        else:
            while node:
                if node.data == before_data:
                    newNode = Node(data)
                    node_prev = node.prev

                    if node_prev == None:
                        node.prev = newNode
                        newNode.next = node
                        self.head = newNode
                    else:
                        node.prev = newNode
                        newNode.next = node
                        node_prev.next = newNode
                        newNode.prev = node_prev
                        if node_prev.prev == None:
                            self.head = node_prev
                    return
                else:
                    node = node.prev

    def delete_data(self, data):
        node = self.head
        if node == '':
            print('지울게 없어요ㅠ')
        if node.next == None:
            if node.prev == None:
                del node
                return
        else:
            while node:
                if node.data == data:
                    node_next = node.next
                    node_prev = node.prev

                    if node_prev == None:
                        self.head = node_next
                        del node
                        return
                        
                    if node_next == None:
                        self.tail = node_prev
                        del node
                        return

                    node_prev.next = node_next
                    node_next.prev = node_prev
                    del node
                    return
                else:
                    node = node.next

    def desc(self):
        node = self.head
        while node:
            print('data의 값',node.data)    
            # print('node의 prev', node.prev)
            # print('node의 next', node.next)

            node = node.next
        
linkedList = NodeMgmt(0)

for data in range(1, 10):
    linkedList.add_from_head(data)
# linkedList.desc()

# linkedList.add_from_head(15)
linkedList.add_from_tail(80)

linkedList.desc()

linkedList.search_from_head(81)

linkedList.insert_after(50,80)
linkedList.insert_before(40,50)
linkedList.desc()
linkedList.delete_data(40)
linkedList.desc()
    


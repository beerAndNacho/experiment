class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = None

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
    
    def add(self, data):
        node = self.head
        if node == '':
            node = Node(data)
        else:
            while node.next:
                node = node.next
            newNode = Node(data)
            node.next = newNode
            newNode.prev = node
            self.tail = newNode

    def search(self, findData):
        node = self.head
        if node =='':
            return print('Empty')
        else:
            while node:
                if node.data == findData:
                    return print(node.data,'을 찾았습니다.')
                else:
                    node = node.next
            return print(findData,'는 찾지 못했습니다.')

    def insert(self, data, afterData):
        node = self.head
        if node =='':
            self.head = Node(data)
            self.tail = self.head
        else:
            while node:
                if node.data == afterData:
                    newNode = Node(data)
                    node_next = node.next
                    if node_next == None:
                        node.next = newNode
                        newNode.prev = node
                        self.tail = newNode
                        return
                    if node_next.next == None:
                        node.next = newNode
                        newNode.prev = node
                        node_next.prev = newNode
                        newNode.next = node_next
                        self.tail = node_next
                        return
                    node.next = newNode
                    newNode.prev = node
                    node_next.prev = newNode
                    newNode.next = node_next
                    return
                else:
                    node = node.next
            return print('찾으시는',afterData,'의 값이 없어 insert하지 못했습니다.')

    def desc(self):
        node = self.head
        if node == '':
            return print('Empty')
        else:
            while node:
                print(node.data)
                node = node.next
            


linkedList = NodeMgmt(0)
for data in range(1, 10):
    linkedList.add(data)

linkedList.desc()
linkedList.search(10)
linkedList.insert(6.5,6)
linkedList.desc()
                
                
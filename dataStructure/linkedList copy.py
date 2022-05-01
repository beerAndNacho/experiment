class Node:
    def__init__(self, data, next=None):
    self.data = data
    self.next = next

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
    
    delf add(self, data):
        node = self.head
        if node == '':
            self.head =Node(data)
        
        else:
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self):
        node= self.head
        if node=='':
            return print(None)

        while node:
            print(node.data)
            node = node.next

    def insert(self, insertData, findData):
        node= self.head
        if node == '':
            print('findData는 물론 head값도 없어 head에 데이터를 Insert했습니다.')
            node = Node(insertData)
            return
        else:
            while node:
                if node.data == findData:
                    tempNode = node.next
                    newNode = Node(data)
                    node.next = newNode
                    newNode.next = tempNode
                    return
                else:
                    node = node.node_next

    def delete(self, deleteData):
        node = self.head
        if node=='':
            print('지울 데이터가 없습니다.')
        else:
            if node.data == deleteData:
                print(deleteData,'을 삭제하였습니다.')
                del node
                return
            else:
                while node:
                    node_next = node.next
                    if node_next.data == deleteData:
                        print(deleteData, '을 삭제하였습니다.')
                        del node.next
                        node.next = node_next.next
                        return
                    else:
                        node = node.next
                print('지울 데이터가 없습니다.')
        



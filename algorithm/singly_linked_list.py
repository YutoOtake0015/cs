# 単方向リスト
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList(object):
    def __init__(self, arr):
        self.head = Node(arr[0])

        currentNode = self.head
        for i in range(1, len(arr)):
            currentNode.next = Node(arr[i])
            currentNode = currentNode.next
    
arr = [100, 200, 300, 400, 500]

# 単方向リストを作成
numList = SinglyLinkedList(arr)

# 単方向リストの内容を出力
currentNode = numList.head
while currentNode is not None:
    print(currentNode.data)
    currentNode = currentNode.next

# 単方向リスト
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList(object):
    def __init__(self, node):
        self.head = node

# ノード作成
node1 = Node(100)
node2 = Node(200)
node3 = Node(300)

# 単方向リストの先頭にnode1を設定
numList = SinglyLinkedList(node1)

# ノードを連結
numList.head.next = node2
numList.head.next.next = node3

# 単方向リストの内容を出力
currentNode = numList.head
while currentNode is not None:
    print(currentNode.data)
    currentNode = currentNode.next

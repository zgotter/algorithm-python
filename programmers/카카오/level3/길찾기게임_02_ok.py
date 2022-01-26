# 성공
#  - 테스트 케이스 6, 7 (런타임 에러) sys.setrecursionlimit(10**6) 으로 지정하여 해결
#  - 이진 탐색 트리


import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, head):
        self.head = head
        
    def insert(self, node):
        self.current_node = self.head
        while True:
            if node.x < self.current_node.x:
                if self.current_node.left is not None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = node
                    break
            else:
                if self.current_node.right is not None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = node
                    break

    def get_pre_order_list(self):
        self.pre_order_list = []
        self.pre_order(self.head)
        return self.pre_order_list
    
    def pre_order(self, node):
        self.pre_order_list.append(node.value)
        if node.left is not None:
            self.pre_order(node.left)
        if node.right is not None:
            self.pre_order(node.right)
    
    def get_post_order_list(self):
        self.post_order_list = []
        self.post_order(self.head)
        return self.post_order_list
    
    def post_order(self, node):
        if node.left is not None:
            self.post_order(node.left)
        if node.right is not None:
            self.post_order(node.right)
        self.post_order_list.append(node.value)

def solution(nodeinfo):
    nodeinfo = [[idx+1, x, y] for idx, (x, y) in enumerate(nodeinfo)]
    nodeinfo = sorted(nodeinfo, key=lambda x: -x[2])
    
    head = Node(*nodeinfo.pop(0))
    binary_tree = BinaryTree(head)
    for node in nodeinfo:
        binary_tree.insert(Node(*node))
        
    return [binary_tree.get_pre_order_list(), binary_tree.get_post_order_list()]
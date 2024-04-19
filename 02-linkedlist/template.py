class Node:
    def __init__(self, val, next_node=None) -> None:
        self.val = val
        self.next_node = next_node
    def __str__(self):
        return str(self.val)
    
def remove_the_k_node(k, head):
    dummy = tmp = Node(0, head)
    for _ in range(k - 1):
        tmp = tmp.next_node
    tmp.next_node = tmp.next_node.next_node
    return dummy.next_node

def insert_at_the_k_pos(val, k, nodes):
    dummy = tmp = Node(0, nodes)
    for _ in range(k - 1):
        tmp = tmp.next_node
    new_node = Node(val, tmp.next_node)
    tmp.next_node = new_node
    return dummy.next_node

def get_list(length):
    if length <= 0:
        return None
    dummy = tmp = Node(0)
    for val in range(1, 1 + length):
        tmp.next_node = Node(val)
        tmp = tmp.next_node
    return dummy.next_node

def test_remove_the_k_node():
    nodes = get_list(10)
    print_node(nodes)
    nodes = remove_the_k_node(2, 10)
    print_node(nodes)

def print_node(nodes):
    if not nodes:
        return
    strs = []
    while nodes:
        strs.append(str(nodes.val))
        nodes = nodes.next_node
    print('->'.join(strs))
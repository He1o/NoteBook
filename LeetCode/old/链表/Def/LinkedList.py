class Node():
    ''' 节点 '''
    def __init__(self, val = 0, _next = None):
        self.val = val   #数据
        self.next = _next  #指向下一节点地址

    def to_list(self):
        lis = [self.val]
        temp_head = self.next
        while temp_head != None:
            lis.append(temp_head.val)
            temp_head = temp_head.next
        return lis


def list_to_Linked(lis):
    head = None
    while lis:
        head = Node(lis.pop(), head)
    return head

def linked_to_list(head):
    lis = []
    temp_head = head
    while temp_head != None:
        lis.append(temp_head.val)
        temp_head = temp_head.next
    return lis
            
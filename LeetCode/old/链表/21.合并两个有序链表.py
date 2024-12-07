from Def import LinkedList

class Solution:
    # 迭代
    def mergeTwoLists(self, l1, l2):
        '''
        时间复杂度 O(m + n)
        '''
        dummy = LinkedList.Node(0, None)
        temp = dummy
        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        temp.next = l1 if l1 else l2

        return dummy.next

    # 递归
    def mergeTwoLists3(self, l1, l2):
        if l2 == None:
            return l1
        elif l1 == None:
            return l2

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
'''
递归

想要的操作是将较大的链接在较小的后面，并返回该较小的指针
返回条件就是当一个指针指向None时，则返回另一指针即可
'''

L1 = [1,2,4,6,7]
L2 = [2,3,5,7,8]
L1 = LinkedList.list_to_Linked(L1)
L2 = LinkedList.list_to_Linked(L2)

S = Solution()   
# with timer.timer('time'):
re = LinkedList.linked_to_list(S.mergeTwoLists(L1, L2))
print(re)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, h1: Optional[ListNode], h2: Optional[ListNode]) -> Optional[ListNode]:
        """
        n, m là length của 2 linked list
        C1: dùng 1 array chứa tât cả các node của 2 linked list đó rồi sort, xong rồi tạo 1 sorted linked list mới
        Time: O((m + n)log(m + n))
        Space: O(m + n)
        C2: dùng 2 con trỏ h1, h2. Nếu h1.val < h2.val -> lấy giá trị h1, h1 được trỏ đến node kế tiếp và ngược lại. 

        Ví dụ 1:
        h1 2->4
        h2 3 ->4
        1->1 -> 2 -> 3 -> 4 -> 4
        """
        if not h1 or not h2:
            return h1 or h2
        dummy = tmp = ListNode(-1000000000)
        while h1 and h2:
            if h1.val < h2.val:
                tmp.next = h1
                h1 = h1.next
            else:
                tmp.next = h2
                h2 = h2.next
            tmp = tmp.next
        tmp.next = h1 or h2
        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        return self.v2(head)
    def v2(self, head):

        """

        Giả sử có vòng, gọi node X là node bắt đầu của vòng tính từ head.
        Gọi kc từ head đến X là a, độ dài vòng là b (a nguyên ko âm, b nguyên dương). Rùa đi 1 node/s, thỏ 2 node/s
        sau t s gặp nhau, thỏ đi 2t node, rùa đi t node.
        Trước khi vô vòng, rùa đi đc a node đầu tiên, và t - a bước trong vòng.
        Thỏ thì đi đc a node đầu tiên, và 2t - a bước trong vòng.
        Vì gặp nhau nên toạ độ giống nhau, thì a + (t - a) % b = a + (2t - a) % b => (t - a) % b = (2t - a) % b
        => (t - a) đồng dư với (2t - a) mod b. (x đồng dư y mod z thì (x - y) chia hết cho z)
        => (2t - a - (t - a)) = k * b (tồn tại vô số nguyên duong k) => t = k * b => t tổn tại thật => nếu có vòng thì kiểu gì cũng gặp nhau
        Gặp nhau tại -a + 2t, nếu rùa đi thêm a bước thì sẽ về đến X. Nếu mà có 1 con rùa khác chạy từ head đi thêm a bước nữa, thể nào cũng gặp con rùa hiện tại.
        Time : O(n)
        Space: O(1)
        """

        if not head:
            return False
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def v1(self, head):
        """
        Time: O(n)
        Space: O(n)
        """
        used = set()
        while head:
            if head in used: # Time: O(1)
                return True
            used.add(head)
            head = head.next
        return False


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.v2(head)

    def v2(self, head):
        """
        Duyet từ trài qua phải, tại node x thì ta sẽ bẻ ngược con trỏ, trỏ lại vào các node đã đi qua.
        1->2->3-> NULL
        NULL<-1, 2->3->NULL
        NULL<-1<-2<-3

        Time: O(n)
        Space: O(1)
        """

        if not head:
            return head
        prev = next_node = None
        while head:
            next_node = prev
            prev = head
            head = head.next
            prev.next = next_node
        return prev

    def v1(self, head):
        """
        Time: O(n)
        Space: O(n)
        """
        if not head:
            return head
        node_list = []
        while head:
            node_list.append(head)
            head = head.next
        node_list.reverse()  # O(n), O(1)

        dummy = tmp = ListNode(1)
        for n in node_list:
            tmp.next = n
            tmp = tmp.next
        tmp.next = None
        return dummy.next
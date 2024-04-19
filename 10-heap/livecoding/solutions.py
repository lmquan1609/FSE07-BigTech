class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        n points
        Time: O(n + k log n)
        Space: O(n)
        """
        pool = []
        ans = []
        ori = [0, 0]
        for idx, p in enumerate(points):
            pool.append((self.get_distance_square(p, ori), idx))
        heapify(pool)
        for _ in range(k):
            _, idx = heappop(pool)
            ans.append(points[idx])
        return ans

    def get_distance_square(self, x, y):
        return abs(x[0] - y[0]) * abs(x[0] - y[0])  + abs(x[1] - y[1]) * abs(x[1] - y[1])

    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    class Solution:
        def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
            """
            build 1 min heap chưa k linkedlist.
            Mỗi bước, mình lấy ra từ trong heap thằng head node nào mà có giá trị nhỏ nhất.
            Lấy node đó append vào kết quả và dịch head node đó lên 1 đơn vị và nếu head node mới khác null thì cho
            lại vào trong min heap
            Vi du:
            4->5,
            3->4,
            6

            1-> 1-> 2 -> 3 ...
            k list nodes, mỗi list node có độ dài tối đa là n => có tối đa k * n nodes
            Time: O(k * n * log(k))
            Space: O(k)
            """
            pool = []
            for idx, node in enumerate(lists):
                if not node:
                    continue
                pool.append((node.val, idx))

            heapify(pool)

            dummy = tmp = ListNode(0)

            while pool:
                _, idx = heappop(pool)
                tmp.next = lists[idx]
                tmp = tmp.next
                lists[idx] = lists[idx].next
                if lists[idx]:
                    heappush(pool, (lists[idx].val, idx))

            return dummy.next

    import heapq
    class Solution:
        def findKthLargest(self, pool: List[int], k: int) -> int:
            """
            heapify pool => bien thanh min heap
            the k largest element tuc la phan tu be thu n - k + 1
            Time complex: O(n + (n - k + 1) * log(n))
            Space: O(1)
            """
            heapq.heapify(pool)
            ans = 0
            n = len(pool)
            for _ in range(n - k + 1):
                ans = heapq.heappop(pool)
            return ans


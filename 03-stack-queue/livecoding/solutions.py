MAP_PAIR = {
    "[": "]",
    "{": "}",
    "(": ")"
}


class Solution:
    def isValid(self, s: str) -> bool:
        """
        Sử dụng stack , duyệt từ trái qua phải.
        Với ptu hiện tại là v , v là ngoặc mở thì cho v vào stack
        Nếu đóng thì kiểm tra xem top của stack có phải là 1 ngoặc mở tương ứng ko.
        Nếu ko phải => return False
        Nếu phải , cho nó ra khoỉ stack

        Ví du:
        s = "()[]{}" => []
        Time: O(n)
        Space: O(n)
        """
        st = []
        for v in s:
            if v in MAP_PAIR:  # v co phai la ngoac mo hay khong
                st.append(v)
            else:
                if not st:
                    return False
                if MAP_PAIR[st.pop()] != v:
                    return False
        return len(st) == 0


class MinStack:

    def __init__(self):
        """
        Minh se luu phan tu vao stack theo 2 gia tri (1 pair: phan tu dau tien : la val can insert, phan tu thu 2: la ptu min tinh từ cuối cho đến phần tử top hiện tại)
        khi mà push ptu v hiện tại vào, thì ptu min hiện taị = min(v, phần tử min trước đó của peek)

        Ví du: [(0, 0), (1, 0), (-2, -2), (-3, -3)]

        """
        self.st = []

    def push(self, val: int) -> None:
        cur_min = val
        if self.st:
            cur_min = min(cur_min, self.st[-1][1])
        self.st.append((val, cur_min))

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()



import collections
class RecentCounter:
    MAX_SPAN = 3000
    def __init__(self):
        """
        Cho t vào queue, queue sẽ có thứ tự time tăng dần. Do chỉ cần tính số lượng request trong [t - 3000, t],
        nên queue cần pop tất cả value < t - 3000.
        Time: O(len of queue)
        Space: O(1)
        """
        self.queue = collections.deque()

    def ping(self, t: int) -> int:
        """
        Time: O(length of queue)
        """
        self.queue.append(t)
        while self.queue and self.queue[0] < t - self.MAX_SPAN:
            self.queue.popleft()
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)



class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        """
        Minh có 1 cái queue: q
        Mình duyệt tất cả các ptu của deck từ lớn tới bé.
        Với mỗi ptu val hiện tại đang xét, gọi pe là ptử peek của q
        Cho pe rời hàng , rồi cho pe enqueue vào q. Sau đó thì mới cho val enqueue vào q.


        [7, 17, 5, 11, 3, 13, 2]

        Time: O(nlogn)
        Space: O(n)

        """
        deck.sort(reverse=True) # Time: O(nlogn), n = len(deck)
        q = collections.deque([deck[0]])
        for idx in range(1, len(deck)):
            val = deck[idx]
            pe = q.pop()
            q.appendleft(pe)
            q.appendleft(val)
        ans = []
        while q:
            ans.append(q.pop())
        ans.reverse()
        return ans
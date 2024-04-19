class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        pre_sum
        pre = [0]
        for val in nums:
            pre.append((pre[-1] + val))
        arr = []
        for val in pre:
            arr.append(val % k)
        map_idx = {}
        for idx, val in enumerate(arr):
            if val in map_idx:
                i = map_idx[val]
                if ...
            else:
                map_idx[val] = idx


        sum từ a -> b : pre[b + 1] - pre[a]


        cần tìm index i, và j sao cho j - i + 1  >= 2 , sum[i -> j] = pre[j + 1] - pre[i] mà nó chia hết cho k, tức là pre[j + 1] đồng dư vs pre[i] mod k.
        tức là (pre[j + 1] % k) - (pre[i] % k) == 0 => tức là chỉ cần check arr[j + 1] === arr[i] hay không, thế thôi
        Rõ ràng nếu x chia k thì số dư nằm trong khoảng từ 0, 1, 2, ... k - 1

        Input: nums = [23,2,4,6,7], k = 6
        arr = [0, 5, 1, 5, 1, 2]
        Time: O(n)
        Space: O(n)
        """
        total = 0
        map_idx = {0: -1}
        for j, val in enumerate(nums):
            total = (val + total) % k
            if total in map_idx:
                i = map_idx[total]
                if j - (i + 1) + 1 >= 2:
                    return True
            else:
                map_idx[total] = j
        return False


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return self.v2(strs)

    def v1(self, strs):
        """
        m là độ dài lớn nhất trong tất cả các string strs
        và có n = len(strs)
        Time : O(n * m log(m))
        Space: O(n * m)

        """
        gr = collections.defaultdict(list)
        for s in strs:  # O(n * m log(m))
            key = "".join(sorted(s))
            gr[key].append(s)
        ans = []
        for values in gr.values():  # O(n)
            ans.append(list(values))
        return ans

    def v2(self, strs):
        """
        m là độ dài lớn nhất trong tất cả các string strs
        và có n = len(strs)
        Time : O(n * m )
        Space: O(n * m)

        """
        gr = collections.defaultdict(list)
        for s in strs:  # O(n * m)
            key = self.get_key(s)
            gr[key].append(s)
        ans = []
        for values in gr.values():  # O(n)
            ans.append(list(values))
        return ans

    def get_key(self, s):
        count = [0] * 26
        for v in s:
            idx = ord(v) - ord('a')
            count[idx] += 1
        return tuple(count)

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # counter = collections.Counter(nums)
        """
        n = len(nums)
        Time: O(n)
        Space: O(n)
        """
        counter = Counter()
        for v in nums:
            counter[v] += 1
        ans = 0
        for x in list(counter.keys()):
            k1 = counter[x]
            y = k - x # x + y = k
            if x != y:
                k2 = counter.get(y, 0)
                tmp = min(k1, k2)
                counter[y] -= tmp
                counter[x] -= tmp
                ans += tmp
            else:
                ans += k1 // 2
                counter[x] -= k1
        return ans


class MyHashMap:
    SIZE = 1000

    def __init__(self):
        self.table = [[] for _ in range(self.SIZE)]

    def _get_idx(self, key):
        return (key * 100 + key * key * key - 100000 + 5 * key * key) % self.SIZE
        # return 1

    def _get_bucket(self, key):
        return self.table[self._get_idx(key)]

    def put(self, key: int, value: int) -> None:
        """
        Time avg: O(1)
        """
        bucket = self._get_bucket(key)
        for idx, (k, v) in enumerate(bucket):
            if k == key:
                bucket[idx] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key: int) -> int:
        """
        Time avg: O(1)
        """
        bucket = self._get_bucket(key)
        for k, v in bucket:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        """
        Time avg: O(1)
        """
        bucket = self._get_bucket(key)
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

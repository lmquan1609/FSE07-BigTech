class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        Time: O(m + n)
        Space: O(1)
        """
        a, b = m - 1, n - 1
        c = m + n - 1
        while a >= 0 and b >= 0:
            if nums1[a] >= nums2[b]:
                nums1[c] = nums1[a]
                a -= 1
            else:
                nums1[c] = nums2[b]
                b -= 1
            c -= 1
        while b >= 0:
            nums1[c] = nums2[b]
            b -= 1
            c -= 1


class NumArray:

    def __init__(self, nums: List[int]):
        """
        -A[0] = 0 => A[1] = A[0] + nums[0], A[2] = A[1] + nums[1]
        -A[n] = A[n - 1] + nums[n - 1] (n : 1 -> len(nums))

        suy ra: A[n] = A[n - 1] + nums[n - 1] = A[n - 2] + nums[n - 2] + nums[n - 1] = ... = nums[0] + nums[1] + ... + nums[n - 1]
        => A[right + 1] = nums[right] + nums[right - 1] + ... + nums[0]
        A[left] = nums[left - 1] + ... + nums[0]
        A[right + 1] - A[left] = nums[right] + nums[right - 1] + ... + nums[left]
        TC: O(n) cho hàm init
        SP: O(n) cho hàm init, O(1) cho sumRange

        pool = []
        for val in nums:
            pool.append(pool[-1] + val)

        """
        length_arr = len(nums)
        self.prefix_sum_arr = [0] * (length_arr + 1)
        for idx in range(1, length_arr + 1):
            self.prefix_sum_arr[idx] = self.prefix_sum_arr[idx - 1] + nums[idx - 1]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum_arr[right + 1] - self.prefix_sum_arr[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)




class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        """
        n = len(nums)
        Cách 1: loop qua các ptu của nums, dùng thêm 1 inner loop nữa để check mỗi ptu xem có phải unique hay không,
        nếu phải thì cộng vào kết quả.
        TIme: O(n ** 2)
        Space: O(1)
        https://i.loli.net/2019/05/14/5cdac3209479073662.gif

        """

        return self.v2(nums)

    def v2(self, nums):
        """
        C2: dùng 1 mảng độ dài M + 1 để đếm số lượng phần tử, nêu 1 phần tử unique -> số lần xuất hiên của nó chỉ là 1.
        Tử đây dễ dàng tính. M = max(nums)
        -> Time: O(n + M)
        -> Space: O(M), nếu trong trường hợp ko có đk nums[i] <= M , thì nó sẽ là O(max(nums))
        """
        max_value = max(nums) # run in O(length of nums)
        count_arr = [0] * (max_value + 1)
        ans = 0
        for val in nums:
            count_arr[val] += 1
        for val in nums:
            if count_arr[val] == 1:
                ans += val
        return ans

    def v1(self, nums):
        ans = 0
        for val in nums:
            count = 0
            for v in nums:
                if v == val:
                    count += 1
            if count == 1:
                ans += val
        return ans
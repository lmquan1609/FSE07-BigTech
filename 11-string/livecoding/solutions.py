class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        """
        return self.v2(x)

    def v2(self, x):
        """
        Time: O(log(x))
        Space: O(1)
        """
        if x < 0:
            return False
        original_x = x
        rev_x = 0
        while x > 0:
            rev_x = 10 * rev_x + (x % 10)
            x = x // 10
        return original_x == rev_x

    def v3(self, x):
        if x < 0:
            return False
        s = str(x)
        return s == s[::-1]

    def v1(self, x: int) -> bool:
        """
        Time complexity: O(log(x))
        Space: O(log(x))
        10 ** k <= x <= 10 ** (k + 1)
        """
        if x < 0:
            return False
        s = str(x)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Time: O(len(min_str) * len(strs))
        Space: O(min_str)
        """
        if not strs:
            return ""
        min_str = strs[0]
        for val in strs:
            if len(val) < len(min_str):
                min_str = val
        for idx, ch in enumerate(min_str):
            for s in strs:
                if s[idx] != ch:
                    return min_str[0: idx] # tuc la min_x 0-> idx - 1 moi la ket qua
        return min_str


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        return self.v2(s, words)

    def v1(self, s, words):
        """
        n = len(s)
        m = len(words)
        x la length lon nhat cua cac string trong words

        Time: O(x + 2 * x + ... + m * x = x(1 + 2 + .. m)) = O(x * m * m)
        Space: O(m * x)
        """
        for k in range(1, len(words) + 1):
            prefix = "".join(words[:k])  # time : O()
            if prefix == s:
                return True
            elif len(prefix) > len(s):
                return False
        return False

    def v2(self, s, words):
        """
        Space: O(1)
        Time: O(min(all lengths of words, len(s)))
        """
        cur_idx = w_idx = 0
        # w_idx la index cua array words, cur_idx la index cua string words[w_idx] dang duyet
        for ch in s:
            if w_idx >= len(words):
                return False
            if ch != words[w_idx][cur_idx]:
                return False
            cur_idx += 1
            if cur_idx == len(words[w_idx]):
                cur_idx = 0
                w_idx += 1

        return cur_idx == 0

class Solution:
    def longestPalindrome(self, ss: str) -> str:
        """
        1 palindrome luc nao cung co tâm.
        với độ dài lẻ: là 1 kí tự ở giữa(aba : tâm là index 1: b)
        với độ dài chẵn thì 2 kí tự ở giữa (abba: -> tâm là bb)
        Time: O(n ** 2)
        Space: O(len(str_ket qua))
        """
        if not ss:
            return
        start = end = 0
        n = len(ss)
        for i in range(n):
            s, e = self.expand(ss, i, i)
            #print(s, e)
            if e - s > end - start:
                start, end = s, e
            if i + 1 < n and ss[i + 1] == ss[i]:
                s, e = self.expand(ss, i, i + 1)
             #   print(s, e)
                if e - s > end - start:
                    start, end = s, e
        return ss[start: end + 1]

    def expand(self, s, left, right):
        while 0 <= left <= right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        left += 1
        right -= 1
        return left, right

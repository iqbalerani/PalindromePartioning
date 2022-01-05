s = "aab"

'''Find answer recursively and memory trick can save some time
traverse and check every prefix s[:i] of s
if prefix s[:i] is a palindrome, then process the left suffix s[i:] recursively
since the suffix s[i:] may repeat, the memory trick can save some time'''

class Solution:
    def partition(self, s: str) -> list[list[str]]:
        if not s: return [[]]
        ans = []
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:  # prefix is a palindrome
                for suf in self.partition(s[i:]):  # process suffix recursively
                    ans.append([s[:i]] + suf)
        return ans

print(Solution().partition(s))

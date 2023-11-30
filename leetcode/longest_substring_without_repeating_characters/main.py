class Solution:
    def lengthOfLongestSubstring(self, word: str) -> int:
        _ = 0
        s = ""
        for i in range(len(word)):
            idx = s.find(word[i])
            if idx == len(s) - 1:
                if len(s) > _:
                    _ = len(s)
                s = ""
            if idx > -1 and idx < len(s) - 1:
                if len(s) > _:
                    _ = len(s)
                s = s[idx + 1 :]
            s += word[i]
        if len(s) > _:
            _ = len(s)
        return _

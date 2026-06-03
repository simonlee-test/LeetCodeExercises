def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        l, r = 0, 1
        maxLength = 1
        substring = "" + s[0]

        while r < len(s):
            if s[r] in substring:
                substring = substring[substring.index(s[r]) + 1 :]
                substring += s[r]

            else:
                substring += s[r]
                maxLength = max(maxLength, len(substring))
            r += 1

        return maxLength

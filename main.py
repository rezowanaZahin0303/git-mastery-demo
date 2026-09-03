class Solution:
    def isVowel(self, ch: str) -> bool:
        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
            return True
        return False

    def reverseVowels(self, s: str) -> str:
        vowels = []
        res = []
        i = 0

        # take all the vowels in order it comes
        while i < len(s):
            if self.isVowel(s[i]):
                vowels.append(s[i])
            i = i + 1

        # put all the vowels in reverse order
        j = len(vowels) - 1
        i = 0
        while i < len(s):
            if self.isVowel(s[i]):
                res.append(vowels[j])
                j = j - 1
            else:
                res.append(s[i])
            i = i + 1

        return ''.join(res)


sol = Solution()
print(sol.reverseVowels("leetcode"))


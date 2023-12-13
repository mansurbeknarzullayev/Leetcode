class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        def isVowel(c):
            return c.lower() in ['a', 'e', 'i', 'o', 'u']
        vowels = list(filter(isVowel, s))
        ind = len(vowels) - 1
        for i in range(len(s)):
            if isVowel(s[i]):
                s[i] = vowels[ind]
                ind -= 1
        return '' . join(s)

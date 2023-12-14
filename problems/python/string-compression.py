class Solution:
    def compress(self, chars: List[str]) -> int:
        pos = 0
        char = chars[0]
        cnt = 0
        for c in chars:
            if c == char:
                cnt += 1
            else:
                res = char
                if cnt > 1:
                    res += str(cnt)
                char = c
                cnt = 1
                for w in res:
                    chars[pos] = w
                    pos += 1
        res = char
        if cnt > 1:
            res += str(cnt)
        char = c
        cnt = 1
        for w in res:
            chars[pos] = w
            pos += 1
        while len(chars) > pos:
            chars.pop(-1)

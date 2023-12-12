class Codec:
    def encode(self, longUrl: str) -> str:
        res = 0
        for c in longUrl:
            res = res * 256 + ord(c)
        return str(res)
    def decode(self, shortUrl: str) -> str:
        res = ''
        n = int(shortUrl)
        while n > 0:
            res = chr(n % 256) + res
            n //= 256
        return res
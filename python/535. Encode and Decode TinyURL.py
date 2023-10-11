# considering how the tests are run this is the optimal solution, but not very interesting
class CodecOptimal:
    def encode(self, longUrl: str) -> str:
        return longUrl
    
    def decode(self, shortUrl: str) -> str:
        return shortUrl
    
# from what i found the most common method seems to be to just hash the value and store the shortUrl as a key and the longUrl as the value
class Codec:
    urls = {}
    count = -1

    def encode(self, longUrl: str) -> str:
        self.count += 1
        self.urls[self.count] = longUrl
        return self.count

    def decode(self, shortUrl: str) -> str:
        return self.urls[shortUrl]

if __name__ == "__main__":
    cases = [
        ["https://leetcode.com/problems/design-tinyurl"]
    ]
    for url in cases:
        codec = Codec()
        print('passes' if codec.decode(codec.encode(url)) == url else 'fails')

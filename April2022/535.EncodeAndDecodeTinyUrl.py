class Codec:
    def __init__(self):
        self.dic={}
        self.count=0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.dic[self.count]=longUrl
        s='tinyurl' + str(self.count)
        self.count+=1
        return s
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.dic[int(shortUrl[7:])]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))


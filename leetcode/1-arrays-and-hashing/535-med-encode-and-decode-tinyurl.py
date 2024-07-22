import unittest
from collections import Counter
from typing import List, Optional
from uu import encode


class TestSolution(unittest.TestCase):
    def test_codec_example1(self):
        url = "https://leetcode.com/problems/design-tinyurl"
        codec = Codec()
        tiny = codec.encode(url)
        ans = codec.decode(tiny)
        self.assertEqual(
            url,
            ans,
            f"Failed on Example 1 with original URL {url} not matching decoded URL {ans}",
        )


class Codec:
    encodeMap = {}
    decodeMap = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        if longUrl not in self.encodeMap:
            short = len(self.encodeMap)
            self.encodeMap[longUrl] = short
            self.decodeMap[short] = longUrl
        return self.encodeMap[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        return self.decodeMap[shortUrl]

if __name__ == "__main__":
    unittest.main()

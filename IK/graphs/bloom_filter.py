"""
https://en.wikipedia.org/wiki/Bloom_filter
"""

from bitarray import bitarray
import mmh3

class BloomFilter(object):
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, string):
        """
        set the bit of bit_array hash_count number of times using the output from
        the hash function
        """
        for seed in range(self.hash_count):
            result = mmh3.hash(string, seed) % self.size # to make the index within array range
            self.bit_array[result] = 1

    def lookup(self, string):
        for seed in range(self.hash_count):
            result = mmh3.hash(string, seed) % self.size
            if self.bit_array[result] == 0:
                # It's definitely not present
                return "Not present"
        ## Probably could be present
        return "Probaly present"


if __name__ == "__main__":
    bloom_filter = BloomFilter(500000,7)
    # read the lines from Ubuntu built-in english dictionary
    lines = open("/usr/share/dict/american-english").read().splitlines()
    for line in lines:
        bloom_filter.add(line)

    words = ["Nepal","dog", "test", "ubuntu","hello","sfghgg"]
    for w in words:
        print(w , bloom_filter.lookup(w),sep=" -> ")

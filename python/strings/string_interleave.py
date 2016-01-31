# http://www.geeksforgeeks.org/check-whether-a-given-string-is-an-interleaving-
# of-two-other-given-strings-set-2/
import unittest

def is_interleaved(stra,strb,strc,a,b,c):
    """
    Check if strc is interleaved of stra and strb
    """

    # If stra is empty check remaining of strb and strc are equal
    if a == len(stra):
        return strb[b:] == strc[c:]

    # If strb is empty check remaining of stra and strc are equal
    if b == len(strb):
        return stra[a:] == strc[c:]

    # Check recursively for all the characters,check for stra before strb
    if ((stra[a] == strc[c] and is_interleaved(stra,strb,strc,a+1,b,c+1))
        or (strb[b] == strc[c] and is_interleaved(stra,strb,strc,a,b+1,c+1))):
        return True

    return False

class InterleaveTest(unittest.TestCase):
    def test_is_interleave(self):
        self.assertTrue(is_interleaved("123","123","112233",0,0,0))
        self.assertTrue(is_interleaved("123456","","123456",0,0,0))
        self.assertTrue(is_interleaved("","123456","123456",0,0,0))
        self.assertTrue(is_interleaved("1234","5678","12345678",0,0,0))

    def test_not_interleave(self):
        self.assertFalse(is_interleaved("123","123","1234",0,0,0))
        self.assertFalse(is_interleaved("1233","5678","12345678",0,0,0))
        self.assertFalse(is_interleaved("12","34","4312",0,0,0))


if __name__ == "__main__":
    unittest.main()

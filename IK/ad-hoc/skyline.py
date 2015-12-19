# You are given a set of n rectangles in no particular order. They have varying
# widths and heights, but their bottom edges are collinear, so that they look
# like buildings on a skyline. For each rectangle, you’re given the x position of
# the left edge, the x position of the right edge, and the height. Your task is
# to draw an outline around the set of rectangles so that you can see what the
# skyline would look like when silhouetted at night.
#
# https://briangordon.github.io/2014/08/the-skyline-problem.html
# http://www.geeksforgeeks.org/divide-and-conquer-set-7-the-skyline-problem/
# https://leetcode.com/problems/the-skyline-problem/

class Building(object):
    """
    To represent the rectangular building.
    """
    def __init__(self,left,hi,right):
        self.left = left
        self.hi = hi
        self.right = right

class Strip(object):
    """
    Represent the strip in skyline silhouetted.
    """
    def __init__(self,left,hi):
        self.left = left
        self.hi = hi

    def __str__(self):
        return ("({0},{1})".format(self.left,self.hi))


class Skyline(object):
    """
    Creates the Skyline from Buildings.
    """
    def __init__(self):
        self.silhouette = []
        self.strip_count = 0

    def add_to_silhourette(self,strip):
        # Strip is redundant if it has same height or left as previous
        if self.strip_count > 0 and self.silhouette[-1].hi == strip.hi:
            return
        if self.strip_count > 0 and self.silhouette[-1].left == strip.left:
            self.silhouette[-1].ht = max(self.silhouette[-1].ht, strip.ht)

        self.silhouette.append(strip)
        self.strip_count += 1

    def find_silhoutte(self,building_arr, low, high):
        if (low == high):
            sk = Skyline()
            sk.add_to_silhourette(Strip(building_arr[low][0],building_arr[low][1]))
            sk.add_to_silhourette(Strip(building_arr[low][2],0))
            return sk

        mid = low + (high - low) // 2
        sk_left = self.find_silhoutte(building_arr,low,mid)
        sk_right = self.find_silhoutte(building_arr,mid+1,high)
        return self.merge(sk_left,sk_right)

    def displlay_silhoutte(self):
        for sh in self.silhouette:
            print(sh,end = ",")

        print()

    def merge(self,sk_left, sk_right):
        """
        Merge the two skyline
        """
        h1 , h2 = 0,0
        result = Skyline()
        i = 0
        j = 0
        while i < sk_left.strip_count or j < sk_right.strip_count:
            if i >= sk_left.strip_count:
                result.add_to_silhourette(sk_right.silhouette[j])
                j += 1
            elif j >= sk_right.strip_count:
                result.add_to_silhourette(sk_left.silhouette[i])
                i += 1
            # check for the x-coordinate
            elif sk_left.silhouette[i].left < sk_right.silhouette[j].left:
                h1 = sk_left.silhouette[i].hi
                mx_hi = max(h1,h2)
                result.add_to_silhourette(Strip(sk_left.silhouette[i].left,mx_hi))
                i += 1
            else:
                h2 = sk_right.silhouette[j].hi
                mx_hi = max(h1,h2)
                result.add_to_silhourette(Strip(sk_right.silhouette[j].left,mx_hi))
                j += 1

        return result


if __name__ == "__main__":
    sk = Skyline()
    building_array = [(1,11,5), (2,6,7), (3,13,9), (12,7,16), (14,3,25),
         (19,18,22), (23,13,29), (24,4,28) ]

    sky_line = sk.find_silhoutte(building_array,0, len(building_array) - 1)
    sky_line.displlay_silhoutte()

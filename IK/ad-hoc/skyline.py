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

class Skyline(object):
    """
    Creates the Skyline from Buildings.
    """
    def __init__(self,silhouette = [] ):
        silhouette = silhouette
        strip_count = 0

    def add_to_silhourette(self,strip):
        # Strip is redundant if it has same height or left as previous
        if strip_count > 0 and silhouette[-1].hi == strip.hi:
            return
        if strip_count > 0 and silhouette[-1].left == strip.left:
            silhouette[-1].ht = max(silhouette[-1].ht, strip.ht)

        silhouette.append(strip)
        strip_count += 1

    def find_silhoutte(self,building_arr, low, high):
        if (low == high):
            sk = Skyline()
            sk.append(Strip(building_arr[low][0],building_arr[low][1]))
            sk.append(Strip(building_arr[low][2],0))
            return sk

        mid = low + (low - high) / 2
        sk_left = self.find_silhoutte(building_arr,low,mid)
        sk_right = self.find_silhoutte(building_arr,mid+1,high)
        return self.merge(sk_left,sk_right,low,mid,high)

    def displlay_silhoutte(self):
        for sh in self.silhouette:
            print(sh)
            
    def merge(self,sk_left, sk_right, low,mid,high):
        """
        Merge the two skyline
        """
        hi1 , hi2 = 0
        result = Skyline()
        i = lo
        j = mid + 1
        for k in range(low,high+1):
            if i > mid:
                result.append(sk_right[j])
                j += 1
            elif j > high:
                result.append(sk_left[i])
                i += 1
            # check for the x-coordinate
            elif sk_left[k].left < sk_right[k].left:
                h1 = sk_left[k].hi
                mx_hi = max(h1,h2)
                result.append(Strip(sk_left[k].left,mx_hi))
                i += 1
            else:
                h2 = sk_right[k].hi
                mx_hi = max(h1,h2)
                result.append(Strip(sk_right[k].left,mx_hi))
                j += 1

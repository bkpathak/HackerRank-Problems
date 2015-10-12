"""
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.
"""
def containsDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        # set also can be used instead of dict
        elem_dict = {}
        for n in nums:
            if n in elem_dict:
                return True
            else:
                elem_dict[n] = 1
        return False

print(containsDuplicate([1,2,3,4]))

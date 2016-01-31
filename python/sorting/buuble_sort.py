# Simple bubble sort implementation

def bubble_sort(list_num):
    for i in range(len(list_num)):
        for j in range(len(list_num) - i -1):
            if list_num[j] > list_num[j + 1]:
                list_num[j + 1], list_num[j] = list_num[j], list_num[j+1]
        for i in list_num:
            print(i,end=" ")
        print()

"""
http://www.algolist.net/Algorithms/Sorting/Bubble_sort
Adaptive bubble sort: Check if the elements are being swapped or not.
If no more swapping is occuring then array is sorted.
"""
def bubble_sort_adpt(list_num):
    j = 0
    swap = True
    while(swap):
        swap = False
        j += 1
        for i in range(len(list_num) - j):
            if list_num[i] > list_num[i+1]:
                list_num[i + 1], list_num[i] = list_num[i], list_num[i+1]
                swap = True
        for i in list_num:
            print(i,end=" ")
        print()


bubble_sort_adpt([9,8,7,6,5,4,3,2,1,0])

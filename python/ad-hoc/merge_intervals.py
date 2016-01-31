# Merge overlapping intervals
# Input => {{1,3},{2,4},{5,7},{6,8}}

def partition(intervals,low,high):
    pivot_elem = intervals[low]
    i = low
    j = high + 1

    while True:
        i += 1
        while(i < high and intervals[i][0] < pivot_elem[0]):
            i += 1
        j -= 1
        while j > low and intervals[j][0] > pivot_elem[0]:
            j -= 1
        if i > j:
            break
        intervals[i], intervals[j] = intervals[j], intervals[i]

    intervals[low], intervals[j] = intervals[j], intervals[low]
    return j

def sort_intervals(intervals,low, high):
    if high <= low:
        return

    pivot = partition(intervals,low,high)
    sort_intervals(intervals,low,pivot-1)
    sort_intervals(intervals,pivot+1,high)

def merge(intervals):
    sort_intervals(intervals, 0, len(intervals) - 1)
    merged_intervals = []
    for i in intervals:
        if len(merged_intervals) == 0:
            merged_intervals.append(i)
        elif merged_intervals[-1][1] >= i[0]:
            if merged_intervals[-1][1] >= i[1]:
                right = merged_intervals[-1][1]
            else:
                right = i[1]
            merged_intervals[-1] = (merged_intervals[-1][0],right)

        else:
            merged_intervals.append(i)
    return merged_intervals

if __name__ == "__main__":
    intervals = [(1,3),(2,4),(5,7),(6,8)]
    print("Before Merge: ", intervals)
    merged_intervals = merge(intervals)
    print("After Merge: ", merged_intervals)

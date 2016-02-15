# https://medium.com/@bearsandsharks/i-failed-a-twitter-interview-52062fbb534b#.3aqhczv0y

def calculate_volume(land):
    left_max = right_max = 0
    left  = 0;
    right = len(land) - 1
    volume = 0

    while(left < right):
        if land[left] > left_max:
            left_max = land[left]
        if land[right] > right_max:
            right_max = land[right]
        if left_max >= right_max:
            volume += right_max - land[right]
            right -= 1
        else:
            volume += left_max - land[left]
            left += 1

    return volume

if __name__ == "__main__":
    height = [2, 5, 1, 2, 3, 4, 7, 7, 6]
    print("Volume is ", calculate_volume(height))

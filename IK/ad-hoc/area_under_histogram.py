# Find the max-area under the histogram.

def max_area_hist(histogram):
    stack = []
    max_area = 0
    area_top = 0
    i = 0
    while i < len(histogram):
        # if this bar is higher than the bar on top stack, push to stack
        if len(stack) == 0 or histogram[stack[-1]] <= histogram[i]:
            stack.append(i)
            i += 1
        else:
            top_index = stack.pop()

            # calculate the area with hist[top_index] stack as smallest bar
            area_top = histogram[top_index] * (i if len(stack) == 0 else i - stack[-1] - 1)

            # update max area
            if max_area < area_top:
                max_area = area_top

    # Repeat same for all the ramining bar from the stack

    while len(stack) != 0:
        top_index = stack.pop()

        # calculate the area with hist[top_index] stack as smallest bar
        area_top = histogram[top_index] * (i if len(stack) == 0 else i - stack[-1] - 1)

        # update max area
        if max_area < area_top:
            max_area = area_top

    return max_area

if __name__ == "__main__":
     hist = [6, 2, 5, 4, 5, 1, 6]
     print(max_area_hist(hist))

# FInd the highest product of 3 number from the list

def highest_product_3(num_lists):
    if len(num_lists) < 3:
        raise Exception("Less than 3 items.")

    # Start from the the index 2
    highest = max(num_lists[0], num_lists[1])
    lowest = min(num_lists[0], num_lists[1])

    highest_product_2 = num_lists[0] * num_lists[1]
    lowest_product_2 = num_lists[0] * num_lists[1]

    highest_product_of_3 = num_lists[0] * num_lists[1] * num_lists[2]

    for current in num_lists[2:]:

        highest_product_of_3 = max(highest_product_of_3,
            current * highest_product_2,
            current * lowest_product_2 )

        highest_product_2 = max(highest_product_2,
            current * highest,
            current * lowest)

        lowest_product_2 = min(highest_product_2,
            current * highest,
            current * lowest)

        highest = max(highest, current)
        lowest = min(current, lowest)

    return highest_product_of_3

if __name__ == "__main__":
    num_lists = [-10,-10,1,3,2]
    print("Highest product of 3:", highest_product_3(num_lists))

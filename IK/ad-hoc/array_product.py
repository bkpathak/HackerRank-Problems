# Given the array , return the array product wheere product[i] is product of
# all nums[j] , j != i


def array_product(arr):
    if len(arr) == 0:
        return
    left_product= 1
    result = []

    for i in range(len(arr)):
        result.append(left_product)
        left_product *= arr[i]

    right_product = 1
    for i in range(len(arr)-1,-1,-1):
        result[i] *= right_product
        right_product *= arr[i]

    return result

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    print(array_product(arr))

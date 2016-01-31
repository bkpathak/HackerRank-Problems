# Complete the function below.


def  printTriplets( intArr):
    result = []
    intArr = sorted(intArr)
    for i in range(len(intArr) - 2):
        if (i == 0 or intArr[i] - intArr[i - 1]):
            negate = -intArr[i]
            start = i + 1
            end = len(intArr) - 1
            while(start < end):

                if (intArr[start] + intArr[end] == negate):
                    result.append((intArr[i],intArr[start],intArr[end]))
                    start += 1
                    end -= 1
                    # To aviid duplicates
                    while(start < end and intArr[end] == intArr[end - 1]):
                        end -= 1
                    while(start < end and intArr[start] == intArr[start - 1]):
                        start += 1

                elif (intArr[start] + intArr[end] < negate):
                    start += 1
                else:
                    end -= 1

    res_string = []
    for r in result:
        res_string.append(",".join(map(str,r)))
    return res_string

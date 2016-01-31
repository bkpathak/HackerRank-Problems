def pascal(n):
    arr =[[0 for i in range(n)] for j in range(n)]

    # Iterate through line
    for line in range(n):
        # numbers in each line is equal to line
        for i in range(line):
            if line == i or i == 0:
                arr[line][i] = 1
            else:
                arr[line][i] = arr[line-1][i-1] + arr[line - 1][i]
            print(arr[line][i],end = " ")
        print()

if __name__ == "__main__":
    pascal(10)

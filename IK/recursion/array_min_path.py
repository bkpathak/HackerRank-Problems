# Enter your code here. Read input from STDIN. Print output to STDOUT

def find_low_val_path(matrix,row,col):
    if row == len(matrix) - 1 and col == 0:
        return matrix[row][col]

    if row < len(matrix) - 1 and col > 0:
        return matrix[row][col] + min(find_low_val_path(matrix,row + 1,col),
                                      find_low_val_path(matrix,row,col - 1))
    elif row == len(matrix) - 1:
        return find_low_val_path(matrix,row,col - 1)
    elif col == 0:
        return find_low_val_path(matrix,row - 1,col)
data = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
   ]

print(find_low_val_path(data,0,2))

    

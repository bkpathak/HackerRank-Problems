def dutch_flag(col_string):
    if len(dutch_flag) <= 1:
        return col_string
    lo = 0
    hi = len(col_string) - 1
    mid = 0

    while mid <= hi:
        if col_string[mid] == "R":
            col_string[lo], col_string[mid] = col_string[mid],col_string[lo]
             

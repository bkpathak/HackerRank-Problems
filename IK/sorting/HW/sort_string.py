# Complete the function below.


def  sortCharacters( inString):
    if inString == None:
        return
    asc_arr = [0] * 256
    for c in inString:
        ch_asc = ord(c)
        asc_arr[ch_asc] += 1
    inString = []
    for i in range(256):
        if asc_arr[i] > 0:
            inString.append(chr(i) * asc_arr[i])
    return ''.join(inString)

    

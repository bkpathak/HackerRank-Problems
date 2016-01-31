def permute(string,left,right):
    if(left == right):
        print(string)
    else:
        for i in range(left,right):
            string[i], string[left] = string[left], string[i]
            permute(string,left+1,right)
            string[i], string[left] = string[left], string[i]

permute(list("ABCD"),0,4)

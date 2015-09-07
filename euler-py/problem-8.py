import functools
def find_product(num):
    num_list = list(map(int,num))
    prod = functools.reduce(lambda x,y: x * y,num_list)
    return prod

T = int(input())
for i in range(T):
    n_len,k = map(int,input().split(" "))
    n = input()
    lower_ind = 0
    max = 0
    while k !=n_len:
        k_con = n[lower_ind:k]
        prod = find_product(k_con)
        if prod > max :
            max = prod
        lower_ind += 1
        k += 1
    print(max)

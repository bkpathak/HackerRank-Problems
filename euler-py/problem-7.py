import math
def is_prime(n):
    flag = True
    u_bound = int(math.sqrt(n))
    i = 1
    l_divisor = 6 * i - 1
    u_divisor = 6 * i + 1
    while l_divisor <= u_bound or u_divisor <= u_bound:
        if n % l_divisor == 0 or n % u_divisor == 0:
            flag = False
            break;
        i += 1
        l_divisor = 6 * i - 1
        u_divisor = 6 * i + 1
    return flag


T = int(input())
prime_list = [2,3]
for i in range(T):
    n = int(input())
    if n <= len(prime_list):
        print(prime_list[n-1])
        continue
    count = len(prime_list)
    num = prime_list[-1] + 1
    while count != n:
        if (num % 2 != 0 and num % 3 != 0 ) and is_prime(num):
            prime_list.append(num)
            count += 1
        num += 1
    print(prime_list[-1])

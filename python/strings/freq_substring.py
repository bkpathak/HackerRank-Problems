# Enter your code here. Read input from STDIN. Print output to STDOUT

def most_frequent_substring(input_str,k,l,m):
    freq_occurrence = 0
    sub_string = {}
    current = 0
    for i in range(len(input_str)):
        j = k
        while j <= l and (i + j) <= len(input_str):
            current = input_str[i:j]
            if current in sub_string:
                current_val = sub_string[current] + 1
                sub_string[current] = current_val
            else:
                sub_string[current] = 1
                current_val = 1

            freq_occurrence = current_val if current_val > freq_occurrence else freq_occurrence
            j += 1

    print(freq_occurrence)

# Read value from the input
N = int(input())
k,l,m = list(map(int,input().split(" ")))
input_str = input()
most_frequent_substring(input_str,k,l,m)

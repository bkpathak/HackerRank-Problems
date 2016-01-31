# Given:
# 1. Some text, say T
# 2. An array A of N Strings, all with same length, say K

# Find all the starting points (indices) in T, which has a concatenation of N strings
# e.g.
# T = "dogthecatcatthedog"
# A = {"the", "cat"} N = 2, K = 3
# Answer = {3, 9}
# At Index 3, we have the phrase "thecat" and at index 9, we have the phrase "catthe".
# They are concatenations of two words in A.
# Very Important: Realize that order of concatenation doesn't matter.
# If there is no such combination, then print empty string

# Not a optimal method to do

def is_concatenate(text,word_array,str_size):
    i = 0
    n = 0
    start_index = []
    temp_start = 0
    present = [0] * len(word_array)
    # Set initially all the strings are present in array
    while i < len(text)-3:
        curent_word = text[i:str_size + i]
        if curent_word in array and  not present[word_array.index(curent_word)]:
            # set in dict that text[i:str_size] is already used
            present[word_array.index(curent_word)] = 1
            if temp_start == 0:
                temp_start = i
            n += 1
        if (curent_word in array and not present[word_array.index(curent_word)]) or n == len(word_array):
            if n == len(word_array):
                start_index.append(temp_start)
            temp_start = 0
            n = 0
            for j in range(len(present)):
                present[j] = 0
        i += 3

    return start_index

if __name__ == "__main__":
    array =["cat","the"]
    text = "dogthecatcatthedog"
    print(is_concatenate(text,array,3))

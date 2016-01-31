# http://www.geeksforgeeks.org/dynamic-programming-set-18-word-wrap/

# Greedy approach
# Put as many words in each line
# text is the array containing the length of each words
from collections import defaultdict

def line_justification(text,width):
    word_in_line = defaultdict(list)
    line = 0
    remain_len = width
    for i in range(len(text)):
        remain_len -= len(text[i])
        if remain_len >= 0 :
            word_in_line[line].append(text[i])
        if (i + 1) < len(text) and remain_len < len(text[i])+1:
            line += 1
            remain_len = width

    return word_in_line

def line_justification(words,width):
    # Create cost matrix
    words_len = len(words)
    Cost = [[0] * words_len for i in range(words_len)]

    # Calculate the cost of putting words from
    # i to j in one line. If words don't fit in one line
    # then we put (2^32) - 1
    for i in range(words_len):
        Cost[i][i] = width - len(words[i])
        for j in range(i+1,words_len):
            Cost[i][j] = Cost[i][j-1] - len(words[j]) - 1

    for i in range(words_len):
        for j in range(i,words_len):
            if Cost[i][j] < 0:
                Cost[i][j] = (2 ** 32) -1
            else:
                Cost[i][j] = Cost[i][j] ** 2

    # Find mincost betwwen i to len
    # by trying all the possibilities of j between i to len
    min_cost = [0] * words_len
    result = [0] * words_len
    for i in range(words_len - 1,-1,-1):
        min_cost[i] = Cost[i][words_len-1]
        result[i] = words_len
        for j in range(words_len-1,i,-1):
            if Cost[i][j-1] == (2**32) - 1:
                continue
            if min_cost[i] > min_cost[j] + Cost[i][j-1]:
                min_cost[i] = min_cost[j] + Cost[i][j-1]
                result[i] = j

    result_text = []
    print("The minumum cost is: ",min_cost[0])
    i = 0
    while i < words_len:
        j = result[i]
        for k in range(i,j):
            result_text.append(words[k])
            result_text.append(" ")

        result_text.append("\n")
        i = j

    return "".join(result_text)


if __name__ == "__main__":
    l = ["Eat","sleep","code","repeat","eat","sleep","code","repeat"]
    #words_in_line = line_justification(l,12)
    #for k,v in words_in_line.items():
    #    print(k," ".join(v))

    print(line_justification(l,12))

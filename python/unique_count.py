# Count the number of unique element in string
def unique_count(string):
    string = sorted(string)
    ind = 0
    dict = {string[ind]:1}
    for ind in range(1,len(string)):
        if string[ind] == string[ind -1]:
            dict[string[ind]] += 1
        else:
            dict[string[ind]] = 1
    for k in dict:
        print(k,dict[k],sep="::")
unique_count("ABDDKALLWACBBCC")

def list_subset(input_str,sub_set,left):
    if left == len(input_str):
        print(sub_set)
    else:
        sub_set.append(input_str[left])
        list_subset(input_str,sub_set,left + 1)
        sub_set.pop()
        list_subset(input_str,sub_set,left + 1)

def subset(input_str):
    list_subset(input_str,[],0)

subset("AAA")

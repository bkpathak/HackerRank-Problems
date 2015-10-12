# Find all the group of anagram strings from the string list

def anagram_string_group(string_list):
    if len(string_list) <= 1:
        print("Anagrams not present")
    else:
        group_dict = {}
        for string in string_list:
            sorted_str = ".".join(sorted(string))
            if sorted_str in group_dict:
                group_dict[sorted_str].append(string)
            else:
                group_dict[sorted_str] = [string]
        for key in group_dict:
            if len(group_dict[key]) > 1:
                print(group_dict[key])

anagram_string_group(["CAT","ACT","TAC","DOG","GOD","BAD"])

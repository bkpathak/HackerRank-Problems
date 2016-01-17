# Simpe regex matcher
# Matches the following condition
# (*) matches zero or more of preceding elements.
# (.) matches any single character.
# (^) matches the beginning of the string.
# ($) matches the end of the string.
# http://www.geeksforgeeks.org/wildcard-character-matching/

# This is very simple implementation, better way is to use Auotmata

def match(first, second):
    # If we reach end of the both string , return True
    if len(first) ==0 and len(second) == 0:
        return True

    # Check for the starting
    if len(first) > 2 and first[0] == "^" and len(second) > 1 and first[1] != second[0]:
        return False

    # make sure that the characcters after '*' are present in second string.
    if len(first) > 1 and first[0] == "*" and len(second) == 0:
        return False

    # Check for the end
    if len(first) > 2 and first[-1] == "$" and len(second) > 1 and first[-2] != second[-1]:
        return False


    # Make sure that if first has "^" then it's present in second
    if (len(first) > 2 and first[0] == "^" and len(second) > 1 and first[1] == second[0]):
        return match(first[2:],second[1:])

    # Match the last charater
    if len(first) > 2 and first[-1] == "$" and len(second) > 1 and first[-2] == second[-1]:
        return match(first[:-2],second[:-1])

    # If the first string contains '.', or current character of both string
    # match
    if (len(first) > 1 and  first[0] == ".") or (len(first) != 0 and
            len(second) != 0 and first[0] == second[0]):
        return match(first[1:], second[1:])

    # If there is "*" in first, then
    # we'll consider the current character of second string
    # we'll ignore the current character of second string
    if len(first) != 0 and first[0] == '*':
        return match(first[1:],second) or match(first,second[1:])


def test_regex(first,second):
    if match(first,second):
        print("{0} and {1}: MATCH".format(first,second))
    else:
        print("{0} and {1}: NO MATCH".format(first,second))

if __name__ == "__main__":
    test_regex("^Reg*xT.st$","ReggggxT.st")
    test_regex("G*","GGGGG")
    test_regex("^TEST","TEST")
    test_regex("^Regex","egex")
    test_regex("TEST$","TEST")
    test_regex("Regex$","Rege")
    test_regex("Re*gx","Reeeeeegx")

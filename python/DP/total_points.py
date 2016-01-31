# In American football, a play can lead to 2, 3, or 7 points. Given that a team
# got P points in a game calculate how many different permutations of 2, 3, and
# 7 could make up the score P.

# Input: P.
# Output: Count of combinations of 2,3 and 7, that leads to P. If there are no
# such combinations, then return 0.

# Order matters e.g. for P = 7, 2 + 3 + 2 is not the same as 3 + 2 + 2.
# They are both unique permutations and should be counted as such.
# In your code, you may need to hard-code the total combinations including and
# upto 7.
# Aim for a solution that's based on Dynamic Programming, and is O(N) in time
# and space.

def number_of_permutations(points,total):
    if total == 0:
        return 1
    if total < 0:
        return 0
    result = 0
    for p in points:
        result += number_of_permutations(points,total-p)
    return result

if __name__ == "__main__":
    points = [2,3,7]
    print(number_of_permutations(points,1007))

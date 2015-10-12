"""
Given a string of numbers and operators, return all possible results from computing
all the different possible ways to group numbers and operators. The valid operators
 are +, - and *.

Input: "2-1-1".
((2-1)-1) = 0
(2-(1-1)) = 2

Time complexity of this algorithm is Catalan number.
"""
def way_to_compute(input):
    ans = []
    for i in range(len(input)):
        c = input[i]
        if c in '-*+':
            left = way_to_compute(input[:i])
            right = way_to_compute(input[i+1:])
            if c == "-":
                ans.append( left - right )
            elif c == "+":
                ans.append( left + right )
            elif c == "*":
                ans.append( left * right )
    if not ans:
        ans.append(int(input))
    return ans

print(way_to_compute("2*3-4*5"))

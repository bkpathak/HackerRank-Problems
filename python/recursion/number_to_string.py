"""
Number to string map
0 => None
1 => None
2 => A,B,C
3 => D,E,F
4 => G,H,I
5 => J,K,L
6 => M,N,O
7 => P,Q,R,S
8 => T,U,V
9 => W,X,Y,Z

Map the number to corresponding character.
Example:
23 => AD,AE,AF,BD,BE,BF,CD,CE,CF
"""
num_letter_map = {
    "0":None,
    "1":None,
    "2":"ABC",
    "3":"DEF",
    "4":"GHI",
    "5":"JKL",
    "6":"MNO",
    "7":"PQRS",
    "8":"TUV",
    "9":"WXYZ"
}

def number_to_sting(number_str):
    left = 0 # Keep tracks the position of the number
    result = [] # store the combination
    find_combination(number_str, left, result)

def find_combination(number_str, left, result ):
    if left == len(number_str): # If reached right_end print the combination
        print("".join(map(str,result)))
        return

    # Get the corresponding letters for the number
    letters = num_letter_map[number_str[left]]
    # check if it's empty then add empty in result and call the function
    if letters is None:
        result.append("")
        find_combination(number_str,left+1,result)
        result.pop()
    else:
        for l in letters:
            result.append(l)
            find_combination(number_str,left + 1, result)
            result.pop()

test_input = ["23","12","31","208","345"]

for t_case in test_input:
    number_to_sting(t_case)

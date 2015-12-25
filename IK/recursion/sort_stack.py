"""
Sort the stack using recursion and without extra space.
"""

def sorted_insert(stack,x):
    if len(stack) == 0 or x > stack[-1]:
        stack.append(x)
    else:
        temp = stack.pop()
        sorted_insert(stack,x)
        stack.append(temp)

def sort_stack(stack):
    # Pop out the element till it's empty
    if len(stack) != 0:
        temp = stack.pop()
        sort_stack(stack)
        # push the element in the stack in sorted order
        sorted_insert(stack,temp)


if __name__ == "__main__":
    stack = [5,4,3,2,1]
    print("Before sort")
    print(" ".join(map(str,stack[::-1])))
    sort_stack(stack)
    print("After sort")
    print(" ".join(map(str,stack[::-1])))

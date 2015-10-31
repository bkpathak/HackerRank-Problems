def apply_oper(op,val1,val2):
    if op == '"':
        return val1 * 10 + val2
    elif op == "*":
        return val1 * val2
    else:
        return val1 + val2

# Return true if operator2 has higher or same precedence as op1
def has_precedence(op1,op2):
    if (op1 == '"' or op1 == '*') and (op2 == "+" or op2 == '*'):
        return False
    else:
        return True

def evaluate_expr(expr):
    operand = []
    operator = []
    for ch in expr:
        if ch >= '0' and ch <= '9':
            operand.append(int(ch))
        else:
            while(len(operator) != 0 and has_precedence(ch,operator[-1])):
                val = apply_oper(operator.pop(),operand.pop(),operand.pop())
                operand.append(val)
            operator.append(ch)

    while(len(operator) != 0):
        val = apply_oper(operator.pop(),operand.pop(),operand.pop())
        operand.append(val)

    return operand.pop()

def  expressionCreator( strDigits,  iK):
    expression = " ".join(strDigits)
    # Length of the expr after adding space
    right = len(expression)
    result = []
    expressionCreatorUtil(list(expression),result,1,right,iK)
    return result

def expressionCreatorUtil(expr,result,left,right,target):
    if left >= right:
        res = evaluate_expr(expr)
        if res == target:
            e = "".join(expr) + '=' + str(target)
            final_e = e.replace('"',"")
            result.append(final_e)

    else:
        for oper in ['"','*','+']:
            expr[left] = oper
            expressionCreatorUtil(expr,result,left + 2,right,target)

for i in expressionCreator("222",222):
    print(i)

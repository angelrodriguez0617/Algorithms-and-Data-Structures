import stack
from stack import Stack
from stack import Node
from stack import LinkedList


def in2post(expression):
    """Converts standard expression to a postfix expression"""
    if expression is None:
        raise ValueError()

    expression = " ".join(expression)
    count1 = 0
    count2 = 0
    for ele in expression:
        if (ele == '('):
            count1 = count1 + 1
        if (ele == ')'):
            count2 = count2 + 1
    if count1 != count2:
        raise SyntaxError("Missing parenthesis or necessary parenthesis added")

    prec = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}

    operator_stack = Stack()
    result_list = []
    token_list = expression.split()

    for token in token_list:
        if token.isalpha() or token.isdigit():
            result_list.append(token)
        elif token == '(':
            operator_stack.push(token)
        elif token == ')':
            top_token = operator_stack.pop()
            while top_token != '(':
                result_list.append(top_token)
                top_token = operator_stack.pop()
        else:  # regular operators
            while (not operator_stack.is_empty()) and (prec[operator_stack.top()] >= prec[token]):
                result_list.append(operator_stack.pop())
            operator_stack.push(token)

    while not operator_stack.is_empty():
        result_list.append(operator_stack.pop())

    return " ".join(result_list)


def eval_postfix(expression):
    """Evaluates a postfix expression"""
    if expression is None:
        raise ValueError()

    operand_stack = Stack()
    token_list = expression.split()

    for token in token_list:
        if token.isdigit():
            operand_stack.push(int(token))
        else:
            if operand_stack.is_empty():
                raise SyntaxError()
            rightOperand = operand_stack.pop()
            if operand_stack.is_empty():
                raise SyntaxError()
            leftOperand = operand_stack.pop()
            operand_stack.push(do_math(token, leftOperand, rightOperand))

    return operand_stack.pop()


def do_math(operator, leftoperand, rightoperand):
    """Does math for the postfix evaluation function"""
    if operator == '+':
        return leftoperand + rightoperand
    elif operator == '-':
        return leftoperand - rightoperand
    elif operator == '*':
        return leftoperand * rightoperand
    else:
        return leftoperand / rightoperand


with open("C:\\users\\angel\\downloads\\data.txt", "r") as f:
    lines = f.readlines()
    for l in lines:
        print("infix: ", l, end="")
        print("postfix: ", in2post(l))
        print("answer: ", eval_postfix(in2post(l)))
        print()


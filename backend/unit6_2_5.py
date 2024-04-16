def prefix(input):
    infix_stack = []
    postfix_stack = []

    # Iterate through the prefix expression in reverse order
    for token in reversed(input):
        # If the token is an operand, push it to both stacks
        if token.isalnum():
            infix_stack.append(token)
            postfix_stack.append(token)
        # If the token is an operator
        else:
            # Pop two operands from the infix stack
            operand1 = infix_stack.pop()
            operand2 = infix_stack.pop()
            # Construct the infix expression for this operation
            infix_expression = f"({operand1} {token} {operand2})"
            # Push the infix expression to the infix stack
            infix_stack.append(infix_expression)

            # Pop two operands from the postfix stack
            operand1 = postfix_stack.pop()
            operand2 = postfix_stack.pop()
            # Construct the postfix expression for this operation
            postfix_expression = f"{operand1}{operand2}{token}"
            # Push the postfix expression to the postfix stack
            postfix_stack.append(postfix_expression)

    # The top of both stacks contains the final infix and postfix expressions
    infix_expression = infix_stack.pop()
    postfix_expression = postfix_stack.pop()

    # Return a string holding both infix and postfix expressions
    return f"Infix: {infix_expression}, Postfix: {postfix_expression}"

def infix(input):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    prefix_stack = []
    postfix_stack = []
    operator_stack = []

    # Function to check if the token is an operator
    def is_operator(token):
        return token in precedence.keys()

    # Function to check if the token is an operand
    def is_operand(token):
        return token.isalnum()

    # Function to determine associativity of operators
    def is_left_associative(op):
        return op != '^'

    # Function to compare precedence of operators
    def compare_precedence(op1, op2):
        if precedence[op1] < precedence[op2]:
            return -1
        elif precedence[op1] > precedence[op2]:
            return 1
        else:
            return 0

    # Iterate through the infix expression
    for token in input:
        if is_operand(token):
            # If the token is an operand, append it to both stacks
            prefix_stack.append(token)
            postfix_stack.append(token)
        elif token == '(':
            # If the token is an opening parenthesis, push it to the operator stack
            operator_stack.append(token)
        elif token == ')':
            # If the token is a closing parenthesis, pop operators from the operator stack
            # and append them to the prefix and postfix stacks until an opening parenthesis is found
            while operator_stack[-1] != '(':
                op = operator_stack.pop()
                prefix_stack.append(op)
                postfix_stack.append(op)
            operator_stack.pop()  # Discard the opening parenthesis
        elif is_operator(token):
            # If the token is an operator
            while operator_stack and operator_stack[-1] != '(' and (
                    (is_left_associative(token) and compare_precedence(token, operator_stack[-1]) <= 0) or
                    (not is_left_associative(token) and compare_precedence(token, operator_stack[-1]) < 0)):
                # Pop operators with higher precedence or equal precedence (for left-associative) from the operator stack
                # and append them to the prefix and postfix stacks
                op = operator_stack.pop()
                prefix_stack.append(op)
                postfix_stack.append(op)
            operator_stack.append(token)  # Push the current operator to the operator stack

    # Append any remaining operators from the operator stack to the prefix and postfix stacks
    while operator_stack:
        op = operator_stack.pop()
        prefix_stack.append(op)
        postfix_stack.append(op)

    # Reverse the prefix stack to get the prefix expression
    prefix_expression = ''.join(prefix_stack[::-1])
    # Join the postfix stack to get the postfix expression
    postfix_expression = ''.join(postfix_stack)

    # Return a string containing both prefix and postfix expressions
    return f"Prefix: {prefix_expression}, Postfix: {postfix_expression}"

def postfix(input):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    prefix_stack = []
    infix_stack = []

    # Function to check if the token is an operator
    def is_operator(token):
        return token in precedence.keys()

    # Iterate through the postfix expression
    for token in input:
        if not is_operator(token):
            # If the token is an operand, push it to both stacks
            prefix_stack.append(token)
            infix_stack.append(token)
        else:
            # If the token is an operator, pop two operands from the stack
            operand2 = prefix_stack.pop()
            operand1 = prefix_stack.pop()

            # Combine the operands and operator to form the prefix expression
            prefix_expression = token + operand1 + operand2
            prefix_stack.append(prefix_expression)

            # Combine the operands and operator to form the infix expression
            infix_expression = f"({operand1}{token}{operand2})"
            infix_stack.append(infix_expression)

    # The final element in both stacks will be the prefix and infix expressions
    prefix_expression = prefix_stack.pop()
    infix_expression = infix_stack.pop()

    # Return a string containing both prefix and infix expressions
    return f"Prefix: {prefix_expression}, Infix: {infix_expression}"

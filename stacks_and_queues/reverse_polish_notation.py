# RPN is
# 1) string of numerics prefixed potentially with '-'
# 2) if A, B are valid expressions A B (+, -, *, /) are all valid expressions
def evaluate(RPN_expression):
    intermediate_results = []
    DELIMITER = ','
    OPERATORS = {
            '+': lambda y, x: x + y,
            '-': lambda y, x: x - y,
            '*': lambda y, x: x * y,
            '/': lambda y, x: x // y}

    for token in RPN_expression.split(DELIMITER):
        if token in OPERATORS:
            intermediate_results.append(
                    OPERATORS[token](
                        intermediate_results.pop(),
                        intermediate_results.pop()))
        else:
            intermediate_results.append(int(token))
    return intermediate_results[-1]

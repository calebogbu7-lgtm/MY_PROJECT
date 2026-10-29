import ast
import operator
import math


OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}


def calculate(expression):
    """Evaluate a mathematical expression safely."""

    if not isinstance(expression, str):
        return "Invalid expression"

    expression = expression.strip()
    expression = expression.replace("×", "*").replace("÷", "/")
    expression = expression.replace("x", "*").replace("X", "*")

    if not expression:
        return "Invalid expression"

    if len(expression) > 100:
        return "Expression too long"

    try:
        tree = ast.parse(expression, mode="eval")
        return _evaluate(tree.body)
    
    
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except OverflowError:
        return "Calculation overflow"
    except (SyntaxError, ValueError, TypeError):
        return "Invalid expression"


MAX_RESULT_BITS = 100_000
MAX_EXPONENT = 10_000


def _evaluate(node):
    if isinstance(node, ast.Constant) and type(node.value) in (int, float):
        return node.value

    if isinstance(node, ast.BinOp) and type(node.op) in OPERATORS:
        left = _evaluate(node.left)
        right = _evaluate(node.right)

        if isinstance(node.op, ast.Pow):
            if abs(right) > MAX_EXPONENT:
                raise OverflowError("Calculation overflow")

            if (
                isinstance(left, int)
                and isinstance(right, int)
                and right > 0
                and abs(left) > 1
            ):
                estimated_bits = abs(left).bit_length() * right

                if estimated_bits > MAX_RESULT_BITS:
                    raise OverflowError("Calculation overflow")

        return OPERATORS[type(node.op)](left, right)

    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
        value = _evaluate(node.operand)
        return value if isinstance(node.op, ast.UAdd) else -value

    raise ValueError("Unsupported expression")

def format_result(result):
    if isinstance(result, int):
        if result == 0:
            return "0"

        digits = math.floor(math.log10(abs(result))) + 1

        if digits > 15:
            exponent = digits - 1
            leading_digits = result // (10 ** (exponent - 5))
            mantissa = leading_digits / 100000
            return f"{mantissa:.6g}e+{exponent}"

    if isinstance(result, float):
        if result != 0 and (
            abs(result) >= 1e15 or abs(result) < 1e-6
        ):
            return f"{result:.6e}"

    return str(result)

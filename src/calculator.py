import ast
import operator


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
    try:
        tree = ast.parse(expression, mode="eval")
        return _evaluate(tree.body)
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except (SyntaxError, ValueError, TypeError, OverflowError):
        return "Invalid expression"


def _evaluate(node):
    if isinstance(node, ast.Constant) and type(node.value) in (int, float):
        return node.value

    if isinstance(node, ast.BinOp) and type(node.op) in OPERATORS:
        left = _evaluate(node.left)
        right = _evaluate(node.right)
        return OPERATORS[type(node.op)](left, right)

    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
        value = _evaluate(node.operand)
        return value if isinstance(node.op, ast.UAdd) else -value

    raise ValueError("Unsupported expression")

def calculate(expression):
    """Evaluate a mathematical expression safely."""

    if not isinstance(expression, str):
        return "Invalid expression"

    if len(expression) > 100:
        return "Expression too long"

    try:
        tree = ast.parse(expression, mode="eval")
        return _evaluate(tree.body)
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except (SyntaxError, ValueError, TypeError, OverflowError):
        return "Invalid expression"
if isinstance(node, ast.BinOp) and type(node.op) in OPERATORS:
    left = _evaluate(node.left)
    right = _evaluate(node.right)

    if isinstance(node.op, ast.Pow) and abs(right) > 100:
        raise ValueError("Exponent too large")

    return OPERATORS[type(node.op)](left, right)
from calculator import calculate, format_result


def main():
    print("================================")
    print("         CalebMath")
    print("   Your personal calculator")
    print("================================")
    print("Enter a mathematical expression.")
    print("Examples: 4 + 5, 2 ** 3, (5 + 3) * 2")
    print("Type 'exit' to close the calculator.")

    while True:
        expression = input("\nEnter expression: ").strip()

        if expression.lower().strip() == "exit":
            print("Thank you for using CalebMath!")
            break

        if not expression:
            print("Please enter an expression.")
            continue

        result = calculate(expression)

        if isinstance(result, (int, float)):
            print("Result:", format_result(result))
        else:
            print("Error:", result)


if __name__ == "__main__":
    main()
# CalebMath

CalebMath is a calculator application created by Caleb Ogbu using Python. The goal is to build a reliable, user-friendly calculator that starts as a terminal program and eventually becomes a fully functional Android app.

## Planned Features

- Addition, subtraction, multiplication, and division
- Modulus and exponentiation
- Decimal and negative numbers
- Full mathematical expressions, such as `4 * 7 + 5 - 4`
- Brackets and correct mathematical operator precedence
- Clear (AC) and delete (DEL) buttons
- Error handling for invalid expressions
- Protection against division by zero
- A clean, user-friendly Android interface

## Technologies

- **Python:** Calculator logic and functionality
- **Kivy:** Mobile application framework
- **KV language:** User interface design
- **unittest:** Automated testing
- **Buildozer:** Packaging the application for Android
- **Git and GitHub:** Version control and project hosting

## Project Structure

```text
CalebMath/
├── src/
│   ├── main.py
│   └── calculator.py
├── tests/
│   └── test_calculator.py
├── assets/
│   └── icon.png
├── .gitignore
├── README.md
└── requirements.txt
```

## Development Plan

1. Build the calculator's core logic in Python.
2. Support complete mathematical expressions.
3. Write automated tests to check calculations and errors.
4. Design the mobile interface using Kivy and KV.
5. Connect the interface buttons to the calculator logic.
6. Test the application on a computer.
7. Package the application as an Android APK.
8. Install and test CalebMath on an Android phone.

## Current Status

**In development.**

The current focus is building and testing the calculator logic before moving on to the mobile interface.

## Author

**Caleb Ogbu**

Creator and developer of CalebMath.
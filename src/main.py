from pathlib import Path

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

try:
    from src.calculator import calculate, format_result
except ModuleNotFoundError:
    from calculator import calculate, format_result


Window.size = (360, 600)

Builder.load_file(str(Path(__file__).resolve().with_name("calebmath.kv")))


class CalculatorLayout(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.just_calculated = False
        self.last_was_error = False

    def on_button_press(self, button):
        value = button.text

        if value in {"x", "X"}:
            value = "*"

        if value == "AC":
            self.ids.display.text = ""
            self.just_calculated = False
            self.last_was_error = False
            return

        if value == "DEL":
            self.ids.display.text = self.ids.display.text[:-1]
            self.just_calculated = False
            self.last_was_error = False
            return

        if value == "=":
            expression = self.ids.display.text

            if not expression:
                return

            result = calculate(expression)

            if isinstance(result, (int, float)):
                self.ids.display.text = format_result(result)
                self.last_was_error = False
            else:
                self.ids.display.text = result
                self.last_was_error = True

            self.just_calculated = True
            return

        if self.last_was_error:
            self.ids.display.text = ""
            self.last_was_error = False
            self.just_calculated = False

        if self.just_calculated:
            if value not in {"+", "-", "*", "/", "%", "**"}:
                self.ids.display.text = ""

            self.just_calculated = False

        self.ids.display.text += value


class CalebMathApp(App):

    def build(self):
        self.title = "CalebMath"
        return CalculatorLayout()


if __name__ == "__main__":
    CalebMathApp().run()
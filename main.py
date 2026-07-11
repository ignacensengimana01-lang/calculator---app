from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class Calculator(App):

    def build(self):
        main = GridLayout(cols=1)

        self.display = Label(
            text="0",
            font_size=40,
            size_hint=(1, 0.3)
        )

        self.expression = ""

        buttons = GridLayout(cols=4)

        for text in [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", "=", "+",
            "⌫"
        ]:
            btn = Button(
                text=text,
                font_size=35
            )

            btn.bind(on_press=self.button_pressed)
            buttons.add_widget(btn)

        main.add_widget(self.display)
        main.add_widget(buttons)

        return main

    def button_pressed(self, button):
        text = button.text

        if text == "=":
            try:
                result = eval(self.expression)
                self.display.text = str(result)
                self.expression = str(result)

            except:
                self.display.text = "Error"
                self.expression = ""

        elif text == "C":
            self.expression = ""
            self.display.text = "0"

        elif text == "⌫":
            self.expression = self.expression[:-1]

            if self.expression == "":
                self.display.text = "0"
            else:
                self.display.text = self.expression

        else:
            self.expression += text
            self.display.text = self.expression


Calculator().run()
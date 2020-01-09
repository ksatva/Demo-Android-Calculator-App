# button in MVC (Model-View-Controller) style
# supporting file: button.kv

from kivy.app import App
from kivy.uix.button import Button


class ButtonApp(App):
    def build(self):
        return Button()
        # Absurd??
        # here kivy will automatically look for a 'file that has the same name as the class' in lowercase,
        # without the 'App' part in the class name
        # eg. button.kv

    def on_press_button(self):
        print('You pressed the button!')


if __name__ == '__main__':
    app = ButtonApp()
    app.run()
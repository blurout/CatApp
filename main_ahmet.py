import kivy

kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.button import Button


class TestApp(App):

    def build(self):
        # return a Button() as a root widget
        return Button(text='hello world')


if __name__ == '__main__':
    TestApp().run()

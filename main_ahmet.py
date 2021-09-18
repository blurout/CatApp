import kivy

kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle

class GameWidget(Widget):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        with self.canvas:
            Rectangle(pos=(350,250),size=(100,100))


class TestApp(App):

    def build(self):
        # return a Button() as a root widget
        return GameWidget()


if __name__ == '__main__':
    TestApp().run()

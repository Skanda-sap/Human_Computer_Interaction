from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

class SayHello(App):
    def build(self):
        # Get the screen size
        screen_width, screen_height = Window.size
        print('{0} and {1}'. format(screen_width, screen_height))

        # Set minimum window size for desktop and mobile
        Window.minimum_width = screen_width * 1.0
        Window.minimum_height = screen_height * 1.0

        # returns a window object with all its widgets
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (None, None)  # Disable automatic size_hint
        self.window.width = screen_width * 0.2  # Set an initial width
        self.window.height = screen_height * 0.5  # Set an initial height
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # image widget
        self.window.add_widget(Image(source="logo.png"))

        # label widget
        self.greeting = Label(
            text="What's your name?",
            font_size=18,
            color='#FFA500'
        )
        self.window.add_widget(self.greeting)

        # text input widget
        self.user = TextInput(
            multiline=False,
            size_hint=(1, 0.5)
        )

        self.window.add_widget(self.user)

        # button widget
        self.button = Button(
            text="GREET",
            size_hint=(1, 0.5),
            bold=True,
            background_color='#00FFCE',
        )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, instance):
        # change label text to "Hello + user name!"
        self.greeting.text = "Hello " + self.user.text + "!"

# run Say Hello App Class
if __name__ == "__main__":
    SayHello().run()

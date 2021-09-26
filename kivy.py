from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout ###### надо обновить
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView #пролистывать экран

class ScrButton(Button):
    def __init__(self, screen, direction = 'right', goal = 'main', **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal
    
    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal
    
class MainScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        h = BoxLayout()
        v = BoxLayout(orientation = 'vertical', padding = 5, spacing = 5)
        txt = Label(text = 'Выбери экран')
        v.add_widget(ScrButton(self, direction = 'right', goal = '1', text = '1'))
        v.add_widget(ScrButton(self, direction = 'left', goal = '2', text = '2'))
        v.add_widget(ScrButton(self, direction = 'up', goal = '3', text = '3'))
        v.add_widget(ScrButton(self, direction = 'down', goal = '4', text = '4'))
        h.add_widget(txt)
        h.add_widget(v)
        self.add_widget(v)
    
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScr())
        return sm

app = MyApp()
app.run()

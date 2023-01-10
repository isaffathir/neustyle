from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from neukivy.app import NeuApp

from screens.screens import *

class MyNeu(NeuApp):
    pass


class WindowManager(ScreenManager):
    pass

class NamaProjek(MDApp):
    CLASSES = {
        'Home':'screens.home',
    }
    AUTORELOADER_PATHS = [
        ('.', {'recursive': True})
    ]
    KV_FILES = [
        'kv/home.kv',
    ]
    def build(self):
        a = MyNeu()
        a.use_kivymd = True
        a.theme_manager.bg_color = (0.8, 0.8, 0.85)
        a.theme_manager.light_color = (0.9, 0.9, 0.95, 1)
        a.theme_manager.dark_color = (0.6, 0.6, 0.65, 1)
        a.theme_manager.text_color = (0.5, 0.2, 0.9, 1)

        self.wm = WindowManager()
        screens = [
            Home(name="home"),
        ]
        for screen in screens:
            self.wm.add_widget(screen)
        return self.wm

if __name__ == '__main__':
    NamaProjek().run()

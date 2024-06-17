from app import App

class Terminale (application):
    def __init__(self):
        pass

    def app_lauch (self):
        print("lauchning terminale mode")

    def app_menu (self):
        print("main menu: 1. start app2. quit app")

    def app_quit(self):
        print("closing application")
        exit()

from abc import ABC, abstractmethod
from database import database

class App (ABC):
    pass

    @abstractmethod
    def app_lauch (self):
       print("welcom to the meta-university app")

    @abstractmethod
    def app_menu (self):
        print("main menu:\n\n1) display student info\n2) quit")
        
        user_choise = input()

        match (user_choise):
            case 1:
                print("laoding student database")
            case 2:
                self.app_quit()

    @abstractmethod
    def app_quit(self):
        pass

    
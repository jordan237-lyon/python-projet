from app_terminale import Terminale
from app import App

def main(app_model: int = 0):

    app_instance = app_model

    match (app_instance):
        case 0: #terminale
            pass
        case 1: #panda 3d
            pass
        case _:
            pass
    
    app_instance.app_launch()
    app_instance.app_menu()




if __name__ == "__main__":
    main()
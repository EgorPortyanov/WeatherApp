from modules.app import application
from modules.window import Window

def main():
    try:
        window = Window()
        window.show()
        application.exec()
    except Exception as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()
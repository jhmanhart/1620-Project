from PyQt6.QtWidgets import QMainWindow
from logic import *


def main():
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()

if __name__ == '__main__':
    main()
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My PyQt5 App")

        # x, y, width, height
        self.setGeometry(200, 200, 500, 500)

        self.setStyleSheet("background-color: lightblue;")

        # Optional icon
        self.setWindowIcon(QIcon("icon.png"))


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
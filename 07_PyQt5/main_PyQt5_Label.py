import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My PyQt5 App")
        self.resize(500, 300)

        self.setStyleSheet("background-color: black;")

        label = QLabel("Hello I am Sam", self)

        label.setFont(QFont("Arial", 20))

        label.setStyleSheet("""
            color: white;
            background-color: #182730;
            font-weight: bold;
        """)

     
        label.setGeometry(50, 50, 400, 200)

        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
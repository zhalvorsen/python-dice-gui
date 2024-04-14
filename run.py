from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import QTimer
import sys
from random import randrange

BLANK_IMAGE = "assets/blank.jpg"

class Gui(object):
    def __init__(self, w: QMainWindow):
        # Set the text at the top of the window
        w.setWindowTitle("Die Roller")

        # Set up the main widget
        self.widget = QWidget(w)
        # The layout will be vertical box layout
        self.layout = QVBoxLayout()

        # Set up the picture of the die
        self.label = QLabel(self.widget)
        self.pixmap = QPixmap(BLANK_IMAGE)
        self.label.setPixmap(self.pixmap)

        # Set up the roll button
        self.roll_button = QPushButton(self.widget)
        self.roll_button.setText("Roll")
        # This sets the function to be called when the button is pressed
        self.roll_button.clicked.connect(self._roll_button_pushed)

        # Add the picture and the button to the layout
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.roll_button)
        self.widget.setLayout(self.layout)

        w.setCentralWidget(self.widget)

        # Initialize the die value, this will be overwritten the first time the
        # button is pressed
        self.die_val = 1

    def _roll_button_pushed(self):
        # Get a new random value for the die
        self.die_val = randrange(1, 6)
        # Blank the image
        self._update_image(BLANK_IMAGE)

        # Wait for 1/2 second, then update the image to the correct value
        timer = QTimer()
        timer.singleShot(500, self._change_die_val)

    def _change_die_val(self):
        self._update_image(f"assets/die-{self.die_val}.jpg")

    def _update_image(self, path: str):
        self.pixmap = QPixmap(path)
        self.label.setPixmap(self.pixmap)


if __name__ == "__main__":
    app = QApplication([])
    w = QMainWindow()
    gui = Gui(w)
    w.show()
    sys.exit(app.exec())

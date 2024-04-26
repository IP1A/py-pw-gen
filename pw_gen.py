from pandas import DataFrame as df
from sys import argv
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from string import ascii_letters, digits, punctuation
from random import sample, randint
params = ascii_letters + digits + punctuation

def GeneratePassword(len = 5):
    return "".join(sample(params, len))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Генератор пароля")
        btn = QPushButton(text = "Нажмите чтобы сгенерировать!", parent=self)
        btn.setFixedSize(180, 20)
        btn.move(10, 10)
        btn.clicked.connect(self.click)
        self.btn = btn

    
    def click(self):
        self.btn.setText("Скопировано!")
        password = df([GeneratePassword(len=randint(8, 32))])
        password.to_clipboard(index=False, header=False)


app = QApplication(argv)
app.setStyle('fusion')

window = MainWindow()
window.show()

app.exec()

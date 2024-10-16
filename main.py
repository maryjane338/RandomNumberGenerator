from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QApplication
import random


class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Генератор рандомных чисел')
        self.label1 = QLabel('Нажмите на кнопку для генерации числа')
        self.label2 = QLabel()
        btn = QPushButton('Кнопка')
        main_l = QVBoxLayout()
        main_l.addWidget(self.label1)
        main_l.addWidget(self.label2)
        main_l.addWidget(btn)
        self.setLayout(main_l)
        btn.clicked.connect(self.generate_random_number)

    def generate_random_number(self):
        random_number = random.randint(1, 10001)
        self.label2.setText(f'Рандомное число: {random_number}')
        

def main():
    app = QApplication([])
    win = MainWin()
    win.show()
    app.exec()


if __name__ == '__main__':
    main()

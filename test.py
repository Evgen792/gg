from PyQt6.QtWidgets import QWidget,  QApplication, QMainWindow, QLabel, QHBoxLayout, QLineEdit, QComboBox, QPushButton, QVBoxLayout, QGridLayout, QStackedLayout

class Avtoriz2(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Авторизация")
        self.setFixedSize(500,500)
        
        self.lbl_0 = QLabel("Пройти тест на тему: животных ")
        self.btn_add = QPushButton("Пройти")
        self.btn_exit = QPushButton("вернуться назад")
        layout = QGridLayout()
        widget1 = QWidget()
        widget1.setLayout(layout)
        layout.addWidget(self.lbl_0, 0,0)
        layout.addWidget(self.btn_add, 2,1)
        layout.addWidget(self.btn_exit, 2,0 )
        self.btn_exit.clicked.connect(self.exit_clic)
        widget = QWidget()
        stack = QStackedLayout()
        stack.addWidget(widget1)
        widget.setLayout(stack)
        self.setCentralWidget(widget)
        
    def exit_clic(self):
        self.close()
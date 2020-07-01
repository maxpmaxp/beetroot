import sys
from functools import partial
from PyQt5.QtWidgets import (QApplication,
                             QWidget,
                             QHBoxLayout,
                             QVBoxLayout,
                             QGridLayout,
                             QLineEdit,
                             QMainWindow,
                             QPushButton,
                             QLabel)

class MyWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Calculator 1.0')
        self.setGeometry(300, 0, 500, 200)
        widget = QWidget()
        digitLabel = QLabel('∞-DIGIT')
        self.editArea = QLineEdit('0')

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(digitLabel)
        mainLayout.addWidget(self.editArea)
        buttonLayout = QGridLayout()
        buttons = [
            {
                'name': 'AC',
                'row': 0,
                'col': 0
            },
            {
                'name': 'QR',
                'row': 0,
                'col': 1
            },
            {
                'name': '%',
                'row': 0,
                'col': 2
            },
            {
                'name': '/',
                'row': 0,
                'col': 3
            },
            {
                'name': '7',
                'row': 1,
                'col': 0
            },
            {
                'name': '8',
                'row': 1,
                'col': 1
            },
            {
                'name': '9',
                'row': 1,
                'col': 2
            },
            {
                'name': 'X',
                'row': 1,
                'col': 3
            },
            {
                'name': '4',
                'row': 2,
                'col': 0
            },
            {
                'name': '5',
                'row': 2,
                'col': 1
            },
            {
                'name': '6',
                'row': 2,
                'col': 2
            },
            {
                'name': '-',
                'row': 2,
                'col': 3
            },
            {
                'name': '1',
                'row': 3,
                'col': 0
            },
            {
                'name': '2',
                'row': 3,
                'col': 1
            },
            {
                'name': '3',
                'row': 3,
                'col': 2
            },
            {
                'name': '+',
                'row': 3,
                'col': 3
            },
            {
                'name': '0',
                'row': 4,
                'col': 0,
                'colSpan': 2
            },
            {
                'name': ',',
                'row': 4,
                'col': 2
            },
            {
                'name': '=',
                'row': 4,
                'col': 3
            },

        ]
        self.buttons = {}
        for buttonConfig in buttons:
            name = buttonConfig.get('name', '')
            btn = QPushButton(name)
            self.buttons[name] = btn
            buttonLayout.addWidget(btn,
                                   buttonConfig.get('row'),
                                   buttonConfig.get('col'),
                                   1,
                                   buttonConfig.get('colSpan', 1))

        mainLayout.addLayout(buttonLayout)
        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)

        for buttonName in self.buttons:
            btn = self.buttons[buttonName]
            btn.clicked.connect(partial(self.change_text, buttonName))


    def change_text(self, text):
        self.editArea.setText(self.editArea.text() + text)



'''def main_widget():
    app = QApplication(sys.argv)
    mainWidget = QWidget()
    mainWidget.setWindowTitle('Calculator1.0')
    mainWidget.setGeometry(300, 0, 500, 300)
    #digitLabel = QLabel('12-DIGIT', parent=mainWidget)
    #buttom1 = QPushButton('Buttom', parent=mainWidget)
    mainWidget.show()
    return_code = app.exec()
    sys.exit(return_code)'''

def main_window():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    return_code = app.exec()
    sys.exit(return_code)


if __name__ == '__main__':
    main_window()
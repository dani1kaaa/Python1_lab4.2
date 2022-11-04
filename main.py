#!/usr/bin/env python3
# coding=utf-8

import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('main.ui', self)

        self.setWindowTitle('Работа со строками в Python')

        self.btn_solve.clicked.connect(self.solve)
        self.btn_clear.clicked.connect(self.clear)

    def solve(self):
        self.textEdit_words.clear()
        text = self.textEdit_text.toPlainText().split()

        count = 0
        itog = ""

        for word in text:
            mesto = word.find("$")
            if mesto == -1 and count < 60:
                itog += word + ""
                count += len(word + "")
            else:
                if mesto != -1:
                    word = word[:mesto] + word[mesto+1:]
                itog += word + "\n"
                count = 0

        self.textEdit_words.insertPlainText(itog)

    def clear(self):
        self.textEdit_text.clear()
        self.textEdit_words.clear()


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

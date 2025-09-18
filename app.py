import sys
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import Qt

class MainWindow(QtWidgets.QDialog):

    DEFAULT_SIZE = (300, 325)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task List")
        self.resize(*self.DEFAULT_SIZE)

        self.todo_list = QtWidgets.QListWidget()
        self.item_line = QtWidgets.QLineEdit()
        self.remove_task_button = QtWidgets.QPushButton("Remove selected")

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(self.todo_list)
        main_layout.addWidget(self.item_line)
        main_layout.addWidget(self.remove_task_button)

        self.item_line.returnPressed.connect(self.on_item_line_return_pressed)
        self.remove_task_button.clicked.connect(self.on_remove_task_btn_clicked)

    def on_item_line_return_pressed(self):
        text = self.item_line.text()
        if not text:
            return
        item = QtWidgets.QListWidgetItem(text)
        item.setCheckState(Qt.CheckState.Unchecked)
        self.todo_list.addItem(item)

        self.item_line.clear()

    def on_remove_task_btn_clicked(self):
        for i in range(self.todo_list.count())[::-1]:
            item = self.todo_list.item(i)
            if item.checkState() == Qt.CheckState.Checked:
                self.todo_list.takeItem(i)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
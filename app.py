import sys
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import Qt

class MainWindow(QtWidgets.QDialog):

    DEFAULT_SIZE = (300, 325)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task List")
        self.resize(*self.DEFAULT_SIZE)

        self.tab_bar = QtWidgets.QTabWidget()
        self.list_view = QtWidgets.QWidget()
        self.history_view = QtWidgets.QWidget()

        self.todo_list = QtWidgets.QListWidget()
        self.item_line = QtWidgets.QLineEdit()
        self.remove_task_button = QtWidgets.QPushButton("Remove selected")

        self.history_list = QtWidgets.QListWidget()

        list_view_layout = QtWidgets.QVBoxLayout(self.list_view)
        list_view_layout.addWidget(self.todo_list)
        list_view_layout.addWidget(self.item_line)
        list_view_layout.addWidget(self.remove_task_button)

        history_view_layout = QtWidgets.QVBoxLayout(self.history_view)
        history_view_layout.addWidget(self.history_list)

        self.tab_bar.addTab(self.list_view, "Tasks")
        self.tab_bar.addTab(self.history_view, "History")

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(self.tab_bar)

        self.item_line.returnPressed.connect(self.on_item_line_return_pressed)
        self.remove_task_button.clicked.connect(self.on_remove_task_btn_clicked)
        self.todo_list.itemDoubleClicked.connect(self.on_task_selected)
            
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
                new_item = "- " + item.text()
                self.history_list.addItem(new_item)

    def on_task_selected(self, item):

        for i in range(self.tab_bar.count()):
            if self.tab_bar.tabText(i) == item.text():
                self.tab_bar.removeTab(i)
                return
            
        self.subtask_view = QtWidgets.QWidget()

        self.subtask_list = QtWidgets.QListWidget()

        subtask_view_layout = QtWidgets.QVBoxLayout(self.subtask_view)
        subtask_view_layout.addWidget(self.subtask_list)
        
        self.tab_bar.addTab(self.subtask_view, item.text())      

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
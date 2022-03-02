# cfw
# 2022.3.2
import sys
import os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from ui_savemain import Ui_MainWindow


class MyQLabel(QLabel):
    button_clicked_signal = Signal()

    def __init__(self, parent=None):
        super(MyQLabel, self).__init__(parent)
        self.button_clicked_signal.connect(self.change_map)

    def mouseReleaseEvent(self, QMouseEvent):
        self.button_clicked_signal.emit()

    def change_map(self):
        pic_num, ok = QInputDialog.getInt(
            self, "修改图块", "请输入图块编号：（1-255）", int(self.toolTip())
        )
        if ok:
            image_filename = str(pic_num) + ".png"
            image_path = os.path.join("images", image_filename)
            if os.path.exists(image_path):
                self.setPixmap(QPixmap(image_path))
            else:
                self.setPixmap(QPixmap("images/missing.png"))
            self.setToolTip(str(pic_num))
        else:
            return


class SaveEditor(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup_ui()
        self.calculate_xy()
        self.setup_label()
        self.draw_map(
            "58$92$59$46$10$126$28$46$60$92$54$20$92$92$10$92$126$92$28$92$92$54$60$92$126$126$92$126$126$126$131$92$54$50$92$92$126$92$126$92$126$92$92$54$126$28$126$126$126$126$126$126$126$126$36$92$18$92$18$92$126$92$92$92$126$92$126$28$126$126$126$124$126$126$126$20$126$50$92$92$92$92$126$92$126$92$92$50$59$92$61$18$126$126$126$28$57$92$20$23$92$92$126$92$126$92$46$92$92$60$59$92$61$18$126$126$126$28$56$92$125$"
        )

    def calculate_xy(self):
        xy_offset = 52
        self.xy_list = []
        for i1 in range(11):
            for i2 in range(11):
                y = i1 * 32
                x = i2 * 32
                xy = (x + xy_offset, y + xy_offset)
                self.xy_list.append(xy)

    def setup_label(self):
        self.label_list = []
        for index in range(121):
            object_name = "label_" + str(index)
            map_label = MyQLabel(self)
            map_label.setObjectName(object_name)
            map_label.resize(32, 32)
            x = self.xy_list[index][0]
            y = self.xy_list[index][1]
            map_label.move(x, y)
            self.label_list.append(map_label)

    def setup_ui(self):
        self.label_bg.setPixmap(QPixmap("images/bg.png"))
        self.import_button.clicked.connect(self.import_floor_str)
        self.export_button.clicked.connect(self.export_floor_str)
        self.destroy_button.clicked.connect(self.destroy_wall)
        self.replace_button.clicked.connect(self.replace_map_pic)
        self.about_button.clicked.connect(self.about)

    def import_floor_str(self):
        floor_str, ok = QInputDialog.getText(self, "导入", "请输入存档楼层sol字符串：")
        if ok:
            self.draw_map(floor_str)
        else:
            return

    def export_floor_str(self):
        export_str = ""
        for label_widget in self.label_list:
            text = label_widget.toolTip()
            text = text + "$"
            export_str = export_str + text
        print(export_str)
        return export_str

    def destroy_wall(self):
        for label_widget in self.label_list:
            pic_number = int(label_widget.toolTip())
            if pic_number == 89 or pic_number == 92 or pic_number == 93:
                image_path = os.path.join("images", "126.png")
                label_widget.setPixmap(QPixmap(image_path))
                label_widget.setToolTip("126")

    def replace_map_pic(self):
        src_num, ok = QInputDialog.getInt(self, "替换所有图块", "请输入需要替换的图块编号：")
        if not ok:
            return
        tag_num, ok = QInputDialog.getInt(self, "替换所有图块", "请输入要替换为图块编号：")
        if not ok:
            return
        for label_widget in self.label_list:
            pic_number = int(label_widget.toolTip())
            if pic_number == src_num:
                image_path = os.path.join("images", str(tag_num) + ".png")
                label_widget.setPixmap(QPixmap(image_path))
                label_widget.setToolTip(str(tag_num))

    def draw_map(self, floor_str: str):
        split_floor = floor_str.split("$")
        split_floor = split_floor[0:121]
        for index, text in enumerate(split_floor):
            label_widget = self.label_list[index]
            image_path = os.path.join("images", text + ".png")
            if os.path.exists(image_path):
                label_widget.setPixmap(QPixmap(image_path))
            else:
                label_widget.setPixmap(QPixmap("images/missing.png"))
            label_widget.setToolTip(text)

    def about(self):
        QMessageBox.about(self, "关于...", "新新魔塔存档编辑器 Ver 0.1")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = SaveEditor()
    main_window.show()
    app.exec()

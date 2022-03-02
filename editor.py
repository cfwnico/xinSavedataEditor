# cfw
# 2022.3.2
import sys
import os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from pyamf import sol
from ui_savemain import Ui_MainWindow as MainWindow
from ui_setting import Ui_Dialog as SettingWindow

# pip install Py3AMF


class MyQLabel(QLabel):
    button_clicked_signal = Signal()

    def __init__(self, parent=None):
        super(MyQLabel, self).__init__(parent)
        self.button_clicked_signal.connect(self.change_map)

    def mouseReleaseEvent(self, QMouseEvent):
        self.button_clicked_signal.emit()

    def change_map(self):
        pic_num, ok = QInputDialog.getInt(self, "修改图块", "请输入图块编号：", int(self.toolTip()))
        if ok:
            image_filename = str(pic_num) + ".png"
            image_path = os.path.join("images", image_filename)
            if os.path.exists(image_path):
                self.setPixmap(QPixmap(image_path))
            else:
                self.setPixmap(QPixmap("images/missing.png"))
            self.setToolTip(str(pic_num))


class SaveEditor(QMainWindow, MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup_ui()
        self.calculate_xy()
        self.setup_label()

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
        self.openfile_button.clicked.connect(self.open_sol)
        self.savefile_button.clicked.connect(self.save_sol)
        self.savefloor_button.clicked.connect(self.save_floor)
        self.destroy_button.clicked.connect(self.destroy_wall)
        self.replace_button.clicked.connect(self.replace_map_pic)
        self.about_button.clicked.connect(self.about)
        self.editother_button.clicked.connect(self.edit_other)
        self.floor_widget.itemClicked.connect(self.chage_selectmap)

    def set_floor_name(self):
        self.floor_name_dict = {}
        self.floor_name_list = []
        for i in range(21):
            self.floor_name_dict[f"savefloor1f{i}"] = f"{i}F"
            self.floor_name_list.append(f"savefloor1f{i}")
        for i in range(1, 26):
            self.floor_name_dict[f"savebfloor1f{i}"] = f"B{i}F"
            self.floor_name_list.append(f"savebfloor1f{i}")
        for i in range(1, 11):
            self.floor_name_dict[f"saveofloor1f{i}"] = f"魔塔{i}F"
            self.floor_name_list.append(f"saveofloor1f{i}")

    def set_floor_widget(self):
        for floor_name in self.floor_name_dict:
            item = QListWidgetItem()
            item.setText(self.floor_name_dict[floor_name])
            self.floor_widget.addItem(item)

    def open_sol(self):
        file_name = QFileDialog.getOpenFileName(self, "请选择游戏存档文件...", filter="*.sol")
        if file_name[0] != "":
            self.sol_obj = sol.load(file_name[0])
            f1_str = self.sol_obj["savefloor1f0"]
            self.set_floor_name()
            self.set_floor_widget()
            self.draw_map(f1_str)
            self.destroy_button.setEnabled(True)
            self.replace_button.setEnabled(True)
            self.savefloor_button.setEnabled(True)
            self.editother_button.setEnabled(True)
            self.savefile_button.setEnabled(True)

    def save_sol(self):
        self.save_floor()
        self.sol_obj.save("savedata_edit.sol")

    def export_floor_str(self):
        export_str = ""
        for label_widget in self.label_list:
            text = label_widget.toolTip()
            text = text + "$"
            export_str = export_str + text
        return export_str

    def save_floor(self):
        floor_str = self.export_floor_str()
        selcet_item = self.floor_widget.selectedItems()[0]
        item_index = self.floor_widget.row(selcet_item)
        floor_name = self.floor_name_list[item_index]
        self.sol_obj[floor_name] = floor_str

    def edit_other(self):
        self.setwindow = Setting(self, self.sol_obj)
        self.setwindow.exec()

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

    def chage_selectmap(self):
        selcet_item = self.floor_widget.selectedItems()[0]
        item_index = self.floor_widget.row(selcet_item)
        floor_name = self.floor_name_list[item_index]
        f_str = self.sol_obj[floor_name]
        self.draw_map(f_str)

    def about(self):
        QMessageBox.about(self, "关于...", "新新魔塔存档编辑器 Ver 0.5")


class Setting(QDialog, SettingWindow):
    def __init__(self, parentwindow: QMainWindow, sol_obj: sol.SOL):
        super().__init__(parentwindow)
        self.sol_obj = sol_obj
        self.setupUi(self)
        self.set_item_key()
        self.load_data()

    def set_item_key(self):
        self.item_dict = {
            "save1lv": self.lv_edit,
            "save1hp": self.hp_edit,
            "save1at": self.atk_edit,
            "save1df": self.def_edit,
            "save1miss": self.miss_edit,
            "save1exp": self.exp_edit,
            "save1yellowkey": self.yellow_edit,
            "save1bluekey": self.blue_edit,
            "save1redkey": self.red_edit,
            "save1gold": self.gold_edit,
            "save1fly": self.fly_check,
            "save1ddd": self.ddd_check,
            "save1chor": self.chor_check,
            "save1nod": self.nod_edit,
            "save1nok": self.nok_edit,
            "save1bigchor": self.bigchor_edit,
            "save1ice": self.ice_check,
            "save1betterdf": self.magicdef_check,
            "save1svdata": self.savename_edit,
            "save1currentx": self.x_edit,
            "save1currenty": self.y_edit,
            "save1nowfloor": self.nowfloor_edit,
            "save1tonameofstage": self.toname_edit,
            "save1currentfloor": self.cureenfloor_edit,
        }
        self.item_key_list = []
        for key in self.item_dict:
            self.item_key_list.append(key)

    def load_data(self):
        for key in self.item_key_list:
            widgets = self.item_dict[key]
            value = self.sol_obj[key]
            if isinstance(widgets, QLineEdit):
                value = str(value)
                widgets.setText(value)
            elif isinstance(widgets, QCheckBox):
                if value == 0:
                    widgets.setCheckable(False)
                elif value == 1:
                    widgets.setCheckable(True)
                else:
                    widgets.setCheckable(False)

    def save_data(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = SaveEditor()
    main_window.show()
    app.exec()

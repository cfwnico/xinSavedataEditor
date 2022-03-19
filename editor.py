# cfw
# 2022.3.19
import os
import sys
from glob import glob

from pyamf import amf0  # pyinstaller need this import
from pyamf import sol  # pip install Py3AMF
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from ui_savemain import Ui_MainWindow as MainWindow
from ui_setting import Ui_Dialog as SettingWindow


def error_msg(parent, title, text):
    QMessageBox(QMessageBox.Warning, title, text, QMessageBox.Ok, parent).exec()


class MyQLabel(QLabel):
    button_clicked_signal = Signal()

    def __init__(self, parent=None):
        super(MyQLabel, self).__init__(parent)
        self.button_clicked_signal.connect(self.change_map)

    def mouseReleaseEvent(self, QMouseEvent):
        self.button_clicked_signal.emit()

    def change_map(self):
        try:
            int(self.toolTip())
        except:
            return
        pic_num, ok = QInputDialog.getInt(
            self, "修改图块", "请输入图块编号:(1-137)", int(self.toolTip())
        )
        if ok:
            image_filename = str(pic_num) + ".png"
            image_path = os.path.join("images", image_filename)
            if os.path.exists(image_path):
                self.setPixmap(QPixmap(image_path))
            else:
                self.setPixmap(QPixmap("images/missing.png"))
            self.setToolTip(str(pic_num))

    def clear_all(self):
        self.clear()
        self.setToolTip("")


class SaveEditor(QMainWindow, MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup_ui()
        self.calculate_xy()
        self.setup_label()

    def setup_ui(self):
        self.label_bg.setPixmap(QPixmap("images/bg.png"))
        self.openfile_button.clicked.connect(self.open_sol)
        self.savefile_button.clicked.connect(self.save_sol)
        self.savefloor_button.clicked.connect(self.save_floor)
        self.destroy_button.clicked.connect(self.destroy_wall)
        self.replace_button.clicked.connect(self.replace_map_pic)
        self.editother_button.clicked.connect(self.edit_other)
        self.floor_widget.itemClicked.connect(self.chage_selectmap)
        self.save_combobox.currentIndexChanged.connect(self.update_map)

    def update_map(self):
        self.save_combobox.setEnabled(True)
        save_index = self.save_combobox.currentIndex() + 1
        check_str = f"save{save_index}svdata"
        if not check_str in self.sol_obj:
            for i in self.label_list:
                i.clear_all()
                self.floor_widget.clear()
                self.set_button_enabled(False)
            return
        self.set_floor_name(save_index)
        self.set_floor_listwidget()
        f0_str = self.sol_obj[f"savefloor{save_index}f0"]
        self.draw_map(f0_str)
        self.floor_widget.setCurrentRow(0)
        self.set_button_enabled(True)

    def set_button_enabled(self, bool: bool):
        self.destroy_button.setEnabled(bool)
        self.replace_button.setEnabled(bool)
        self.savefloor_button.setEnabled(bool)
        self.editother_button.setEnabled(bool)
        self.savefile_button.setEnabled(bool)

    def calculate_xy(self):  # 计算lable坐标
        xy_offset = 52
        self.xy_list = []
        for i1 in range(11):
            for i2 in range(11):
                y = i1 * 32
                x = i2 * 32
                xy = (x + xy_offset, y + xy_offset)
                self.xy_list.append(xy)

    def setup_label(self):  # 创建lable
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

    def set_floor_name(self, save_index: int):
        self.floor_name_dict = {}
        self.floor_name_list = []
        for i in range(21):
            self.floor_name_dict[f"savefloor{save_index}f{i}"] = f"{i}F"
            self.floor_name_list.append(f"savefloor{save_index}f{i}")
        for i in range(1, 26):
            self.floor_name_dict[f"savebfloor{save_index}f{i}"] = f"B{i}F"
            self.floor_name_list.append(f"savebfloor{save_index}f{i}")
        for i in range(1, 11):
            self.floor_name_dict[f"saveofloor{save_index}f{i}"] = f"魔塔{i}F"
            self.floor_name_list.append(f"saveofloor{save_index}f{i}")

    def set_floor_listwidget(self):
        self.floor_widget.clear()
        for floor_name in self.floor_name_dict:
            item = QListWidgetItem()
            item.setText(self.floor_name_dict[floor_name])
            self.floor_widget.addItem(item)

    def find_last_edit_sol(self):
        path = r"~\AppData\Roaming\Macromedia\Flash Player\#SharedObjects\**\*.sol"
        path = os.path.expanduser(path)
        sol_file_list = glob(path, recursive=True)
        if len(sol_file_list) == 0:
            return
        edit_times = []
        for file_name in sol_file_list:
            mtime = os.path.getmtime(file_name)
            edit_times.append(mtime)
        max_edit_time = max(edit_times)
        file_name = edit_times.index(max_edit_time)
        last_edit_file = sol_file_list[file_name]
        last_edit_file = os.path.abspath(last_edit_file)
        return last_edit_file

    def open_sol(self):
        file_name_tuple = QFileDialog.getOpenFileName(
            self, "请选择游戏存档文件...", self.find_last_edit_sol(), "*.sol"
        )
        file_name = file_name_tuple[0]
        if file_name != "":
            try:
                self.sol_obj = sol.load(file_name)
            except:
                error_msg(self, "警告", "存档文件读取失败！")
                return
            if len(self.check_sol()) == 0:
                error_msg(self, "警告", "存档文件读取错误！")
                return
            self.update_map()
            self.sol_file_name = file_name

    def check_sol(self):
        check_list = ["save1svdata", "save2svdata", "save3svdata", "save4svdata"]
        exists_list = []
        for index, text in enumerate(check_list):
            if text in self.sol_obj:
                exists_list.append(index)
        return exists_list

    def save_sol(self):
        self.save_floor()
        self.sol_obj.save(self.sol_file_name)

    def export_floor_str(self):
        export_str = ""
        for label_widget in self.label_list:
            text = label_widget.toolTip()
            if text == "":
                return
            text = text + "$"
            export_str = export_str + text
        return export_str

    def save_floor(self):
        floor_str = self.export_floor_str()
        if floor_str is None:
            error_msg(self, "警告！", "保存楼层信息出错，存档未保存！")
            return
        selcet_item = self.floor_widget.selectedItems()[0]
        item_index = self.floor_widget.row(selcet_item)
        floor_name = self.floor_name_list[item_index]
        try:
            self.sol_obj[floor_name] = floor_str
        except:
            error_msg(self, "警告！", "存档保存失败！")

    def edit_other(self):
        save_index = self.save_combobox.currentIndex() + 1
        self.setwindow = Setting(self, self.sol_obj, save_index)
        self.setwindow.exec()

    def destroy_wall(self):
        for label_widget in self.label_list:
            pic_number = int(label_widget.toolTip())
            if pic_number == 89 or pic_number == 92 or pic_number == 93:
                image_path = os.path.join("images", "126.png")
                label_widget.setPixmap(QPixmap(image_path))
                label_widget.setToolTip("126")

    def replace_map_pic(self):
        src_num, ok = QInputDialog.getInt(self, "替换所有图块", "请输入需要替换的图块编号：(1-137)")
        if not ok:
            return
        tag_num, ok = QInputDialog.getInt(self, "替换所有图块", "请输入要替换为图块编号：(1-137)")
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
        split_floor = split_floor[0:121]  # 切片处理防止意外发生
        for index, text in enumerate(split_floor):
            label_widget = self.label_list[index]
            image_path = os.path.join("images", text + ".png")
            if os.path.exists(image_path):
                label_widget.setPixmap(QPixmap(image_path))
            else:  # 如果是未知图块号则显示missing图片来提醒
                label_widget.setPixmap(QPixmap("images/missing.png"))
            label_widget.setToolTip(text)

    def chage_selectmap(self):
        selcet_item = self.floor_widget.selectedItems()[0]
        item_index = self.floor_widget.row(selcet_item)
        floor_name = self.floor_name_list[item_index]
        f_str = self.sol_obj[floor_name]
        self.draw_map(f_str)


class Setting(QDialog, SettingWindow):
    def __init__(self, parentwindow: QMainWindow, sol_obj: sol.SOL, save_index: int):
        super().__init__(parentwindow)
        self.sol_obj = sol_obj
        self.save_index = save_index
        self.setupUi(self)
        self.setup_ui()
        self.set_args()
        self.load_data()

    def setup_ui(self):
        self.save_button.clicked.connect(self.save_and_close)
        self.cancel_button.clicked.connect(lambda: self.close())

    def set_args(self):
        self.key_widgets_default = {
            # =========================================
            # 能力值相关
            # =========================================
            "save1lv": self.lv_edit,
            "save1hp": self.hp_edit,
            "save1at": self.atk_edit,
            "save1df": self.def_edit,
            "save1miss": self.miss_edit,
            "save1exp": self.exp_edit,
            "save1gold": self.gold_edit,
            # =========================================
            # 道具相关
            # =========================================
            "save1yellowkey": self.yellow_edit,
            "save1bluekey": self.blue_edit,
            "save1redkey": self.red_edit,
            "save1nod": self.nod_edit,
            "save1nok": self.nok_edit,
            "save1bigchor": self.bigchor_edit,
            "save1life": self.relive_edit,
            "save1fly": self.fly_check,
            "save1ddd": self.ddd_check,
            "save1ice": self.ice_check,
            "save1betterdf": self.magicdef_check,
            "save1chor": self.chor_check,
            "save1key": self.key_check,
            # =========================================
            # 存档相关
            # =========================================
            "save1currentx": self.x_edit,
            "save1currenty": self.y_edit,
            "save1nowfloor": self.nowfloor_edit,
            "save1currentfloor": self.currenfloor_label,
            "save1svdata": self.savename_edit,
            # =========================================
            # 战斗相关
            # =========================================
            "save1attimes": self.atktimes_edit,
            "save1heavyda": self.baoji_edit,
            "save1nearat": self.atknear_edit,
            "save1neardf": self.defnear_edit,
            # =========================================
            # 杂项相关
            # =========================================
            "save1need1": self.shop3f_edit,
            "save1need2": self.shopb5f_edit,
            "save1maxgou": self.minf_edit,
            "save1maxgoo": self.maxf_edit,
            # =========================================
        }
        self.key_list_now = []
        self.key_widgets_now = {}
        if self.save_index == 1:  # 如果存档槽位为1则不作处理
            self.key_widgets_now = self.key_widgets_default
            for key in self.key_widgets_default:
                self.key_list_now.append(key)
        else:  # 如果存档槽位不为1则对字符串进行替换
            for key in self.key_widgets_default:
                now_key = key.replace("save1", f"save{self.save_index}")
                self.key_widgets_now[now_key] = self.key_widgets_default[key]
                self.key_list_now.append(now_key)
        # 设置攻击动画序号
        self.atkanm_list = [2, 20, 134, 141, 148, 153]

    def load_data(self):
        for key in self.key_list_now:
            widgets = self.key_widgets_now[key]
            value = self.sol_obj[key]
            if isinstance(widgets, QLineEdit):
                widgets.setText(value)
            elif isinstance(widgets, QSpinBox):
                widgets.setValue(value)
            elif isinstance(widgets, QLabel):
                widgets.setText(value)
            elif isinstance(widgets, QCheckBox):
                if value == 1:
                    widgets.setChecked(True)
                else:
                    widgets.setChecked(False)
        # 读取状态
        stats = self.sol_obj[f"save{self.save_index}tostats"]
        self.stat_combobox.setCurrentIndex(stats)
        # 读取攻击动画
        atkanm = self.sol_obj[f"save{self.save_index}attype"]
        self.atkanm_combobox.setCurrentIndex(self.atkanm_list.index(atkanm))

    def save_and_close(self):
        for key in self.key_list_now:
            widgets = self.key_widgets_now[key]
            if isinstance(widgets, QLineEdit):
                text = widgets.text()
                self.sol_obj[key] = text
            elif isinstance(widgets, QSpinBox):
                int_value = widgets.value()
                self.sol_obj[key] = int_value
            elif isinstance(widgets, QCheckBox):
                bool_value = widgets.isChecked()
                if bool_value is True:
                    value = 1
                elif bool_value is False:
                    value = -1
                self.sol_obj[key] = value
        # 单独处理save currentfloor
        nowfloor_value = self.sol_obj[f"save{self.save_index}nowfloor"]
        curfloor_key = f"save{self.save_index}currentfloor"
        if nowfloor_value == 0:
            self.sol_obj[curfloor_key] = "入口"
        elif nowfloor_value >= 100:
            self.sol_obj[curfloor_key] = str(nowfloor_value - 100) + "F"
        else:
            self.sol_obj[curfloor_key] = str(abs(nowfloor_value)) + "F"
        # 设置状态
        stats_value = f"save{self.save_index}tostats"
        self.sol_obj[stats_value] = self.stat_combobox.currentIndex()
        # 设置攻击动画
        atkanm_value = self.atkanm_combobox.currentIndex()
        self.sol_obj[f"save{self.save_index}attype"] = self.atkanm_list[atkanm_value]
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = SaveEditor()
    main_window.show()
    app.exec()

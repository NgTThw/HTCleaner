from UI.ui_main import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QWidget
from PySide6.QtCore import QDateTime, QTime, QTimer, SignalInstance, Signal
from config import Config
from HTG import HTParking
from WindowsTools import SimpleTaskScheduler, ScheduleFrequence, commandline
from thread import SimpleThread
import traceback
import module
import sys
import os


__version__ = '0.0.1'



class Worker(SimpleThread):
    progress = Signal(int, str)
    cleaned = Signal(str)
    def __init__(self, parent, method):
        super().__init__(parent, method)



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("HTParking Cleaner")
        self.label_version.setText("Version " + __version__)
        self.progressBar.hide()
        self.label_log.hide()
        self.dateTimeEdit_in_out.setEnabled(False)
        self.dateTimeEdit_exception.setEnabled(False)
        self.timeEdit_auto.setEnabled(False)
        QWidget.setTabOrder(self.lineEdit_db_name, self.lineEdit_db_host)
        QWidget.setTabOrder(self.lineEdit_db_host, self.spinBox_db_port)
        QWidget.setTabOrder(self.spinBox_db_port, self.lineEdit_db_user)
        QWidget.setTabOrder(self.lineEdit_db_user, self.lineEdit_db_password)
        #connect event
        self.pushButton_setting.pressed.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.pushButton_cancel_setting.pressed.connect(self._on_pushButton_cancel_setting_pressed)
        self.pushButton_save_setting.pressed.connect(self._on_pushButton_save_setting_pressed)
        self.pushButton_save.pressed.connect(self._on_pushButton_save_pressed)
        self.pushButton_postgresql_bin_select.pressed.connect(self._on_pushButton_postgresql_bin_pressed)
        self.pushButton_delete.pressed.connect(self._on_pushButton_delete_pressed)
        self.checkBox_start_time_in_out.toggled.connect(self.dateTimeEdit_in_out.setEnabled)
        self.checkBox_start_time_exception.toggled.connect(self.dateTimeEdit_exception.setEnabled)
        self.checkBox_auto.toggled.connect(self.timeEdit_auto.setEnabled)
        #variable
        self.config = Config("setting")
        self.db_setting = self.config.setup(
            ('postgresql_bin', self.lineEdit_postgresql_bin.text, self.lineEdit_postgresql_bin.setText, 'C:/Program Files/PostgreSQL/11/bin'),
            ('db_name', self.lineEdit_db_name.text, self.lineEdit_db_name.setText, 'lparkingdb'),
            ('db_host', self.lineEdit_db_host.text, self.lineEdit_db_host.setText, 'localhost'),
            ('db_port', self.spinBox_db_port.value, self.spinBox_db_port.setValue, 5432),
            ('username', self.lineEdit_db_user.text, self.lineEdit_db_user.setText, 'lparking'),
            ('password', self.lineEdit_db_password.text, self.lineEdit_db_password.setText, 'Lovad.vn2014')
        )
        self.db_setting.load()
        self.parking = HTParking(
            self.lineEdit_postgresql_bin.text(), 
            self.lineEdit_db_host.text(),
            self.spinBox_db_port.value(),
            self.lineEdit_db_name.text(),
            self.lineEdit_db_user.text(),
            self.lineEdit_db_password.text()
        )
        if self.is_db_setting_valid():
            self.vehicle_types = self.parking.get_vehicle_types()
            if self.parking.error:
                self._error_message(self.parking.error)
        else:
            self.vehicle_types = []
        
        default_date = QDateTime.currentDateTime()
        default_date.setTime(QTime(0, 0))
        self.end_time_in_out = default_date
        self.end_time_except = default_date
        self.vehicle_types_setting = self.config.setup(
            ('vehicle_types', self.comboBox_vehicle_type.checked_item_ids, lambda l: self.comboBox_vehicle_type.set_only_item_id(l, True), [])
        )
        self.main_setting = self.config.setup(
            ('in_out_keep', self.spinBox_in_out_keep.value, self.spinBox_in_out_keep.setValue, 1),
            ('delete_data_in_out', self.checkBox_delete_data_in_out.isChecked, self.checkBox_delete_data_in_out.setChecked, False),
            ('delete_image_in_out', self.checkBox_delete_image_in_out.isChecked, self.checkBox_delete_image_in_out.setChecked, False),
            ('cb_in_out_start_time', self.checkBox_start_time_in_out.isChecked, self.checkBox_start_time_in_out.setChecked, False),
            ('in_out_start_time',
                lambda: self.dateTimeEdit_in_out.dateTime() if self.checkBox_start_time_in_out.isChecked() else '',
                lambda x: self.dateTimeEdit_in_out.setDateTime(x) if x else self.dateTimeEdit_in_out.setDateTime(default_date),
                default_date
            ),
            ('except_keep', self.spinBox_exception_keep.value, self.spinBox_exception_keep.setValue, 1),
            ('delete_data_except', self.checkBox_delete_data_exception.isChecked, self.checkBox_delete_data_exception.setChecked, False),
            ('delete_image_except', self.checkBox_delete_image_exception.isChecked, self.checkBox_delete_image_exception.setChecked, False),
            ('cb_except_start_time', self.checkBox_start_time_exception.isChecked, self.checkBox_start_time_exception.setChecked, False),
            ('except_start_time',
                lambda: self.dateTimeEdit_exception.dateTime() if self.checkBox_start_time_exception.isChecked() else '',
                lambda x: self.dateTimeEdit_exception.setDateTime(x) if x else self.dateTimeEdit_exception.setDateTime(default_date),
                default_date
            ),
            ('cb_auto', self.checkBox_auto.isChecked, self.checkBox_auto.setChecked, False),
            ('auto_time', self.timeEdit_auto.time, self.timeEdit_auto.setTime, QTime(1, 0))
        )
        self.start_time_setting = self.config.setup(
            ('in_out_start_time', 
                lambda: self.end_time_in_out, 
                lambda x: self.dateTimeEdit_in_out.setDateTime(x) if x else self.dateTimeEdit_in_out.setDateTime(default_date)
            ),
            ('except_start_time', 
                lambda: self.end_time_except,
                lambda x: self.dateTimeEdit_exception.setDateTime(x) if x else self.dateTimeEdit_exception.setDateTime(default_date)
            )
        )
        self._create_item_comboBox_vehicle_type()
        self.main_setting.load()
        self.task_auto = SimpleTaskScheduler("HTParkingCleaner", sys.argv[0], ("--hidden",), ScheduleFrequence.DAILY, self.timeEdit_auto.time().toString('HH:mm'))


    def is_db_setting_valid(self) -> bool:
        if not os.path.isfile(self.parking.psql):
            return self._error_message('Không tìm thấy file "' + self.parking.psql + '" vui lòng kiểm tra lại cài đặt')
        return True

    def _on_pushButton_postgresql_bin_pressed(self) -> None:
        folder = QFileDialog.getExistingDirectory(self, "Select PostgreSQL bin folder", 'C:\\')
        if folder:
            self.lineEdit_postgresql_bin.setText(folder)


    def _on_pushButton_save_setting_pressed(self) -> None:
        self._update_parking_value()
        if self.is_db_setting_valid():
            self.vehicle_types = self.parking.get_vehicle_types()
            if self.parking.error:
                return self._error_message(self.parking.error)
            self._create_item_comboBox_vehicle_type()
            self.db_setting.upgrade()
            self.stackedWidget.setCurrentIndex(0)
    

    def _on_pushButton_cancel_setting_pressed(self) -> None:
        self.db_setting.load()
        self._update_parking_value()
        self.stackedWidget.setCurrentIndex(0)


    def _on_pushButton_save_pressed(self) -> None:
        self.vehicle_types_setting.upgrade()
        self.main_setting.upgrade()
        if self.checkBox_auto.isChecked():
            self._create_taskscheduler()
        else:
            self._remove_taskscheduler()
        self.label_log.setText("Saved successfully")
        self.label_log.show()
        QTimer(self).singleShot(1000, self.label_log.hide)

    def _on_pushButton_delete_pressed(self) -> None:
        if not self.is_db_setting_valid():
            return
        self.end_time_in_out = calculator_datetime(self.spinBox_in_out_keep.value())
        self.end_time_except = calculator_datetime(self.spinBox_exception_keep.value())
        self.end_time_in_out.setTime(QTime(0, 0))
        self.end_time_except.setTime(QTime(0, 0))
        self.pushButton_delete.setEnabled(False)
        self.label_log.setText("Starting...")
        self.progressBar.setValue(0)
        self.progressBar.show()
        self.label_log.show()
        self.worker1 = Worker(self, self.__worker1)
        self.worker1.progress.connect(self.__worker1_update_progress)
        self.worker1.cleaned.connect(self.__worker1_cleaned)
        self.worker1.success.connect(self.__worker1_end)
        self.worker1.error.connect(self.__worker1_end)
        self.worker1.start()

    def __worker1(self) -> None:
        clean_data(
            self.parking,
            self.dateTimeEdit_in_out.dateTime().toString('yyyy-MM-dd HH:mm:ss') if self.checkBox_start_time_in_out.isChecked() else '',
            self.end_time_in_out.toString('yyyy-MM-dd 00:00:00'),
            self.comboBox_vehicle_type.checked_item_ids(),
            self.dateTimeEdit_exception.dateTime().toString('yyyy-MM-dd HH:mm:ss') if self.checkBox_start_time_exception.isChecked() else '',
            self.end_time_except.toString('yyyy-MM-dd 00:00:00'),
            self.checkBox_delete_data_in_out.isChecked(),
            self.checkBox_delete_image_in_out.isChecked(),
            self.checkBox_delete_data_exception.isChecked(),
            self.checkBox_delete_image_exception.isChecked(),
            self.worker1,
        )
    
    def __worker1_update_progress(self, total: int, msg: str) -> None:
        if total >= 0:
            self.progressBar.setMaximum(total)
            self.label_log.setText(msg)
        else:
            self.progressBar.setValue(self.progressBar.value() + 1)
            if msg:
                self.label_log.setText(msg)

    def __worker1_cleaned(self, msg: str) -> None:
        self.label_log.setText(msg)
        self._alert(msg)
        QTimer(self).singleShot(3000, self.label_log.hide)
        
    def __worker1_end(self, msg:str = '') -> None:
        if msg:
            self._warning_message(msg)
        else:
            self.start_time_setting.upgrade()
            self.start_time_setting.load()
        self.pushButton_delete.setEnabled(True)
        self.progressBar.hide()
        self.progressBar.setValue(-1)

    def closeEvent(self, event):
        if self.config.is_value_changed():
            if self._question_message("Có cấu hình chưa được lưu, bạn có muốn lưu hay không?") is True:
                self.config.upgrade()
        return super().closeEvent(event)


    Button = QMessageBox.StandardButton
    Icon = QMessageBox.Icon

    def _messagebox(self, icon, title, message, buttons) -> int:
        return QMessageBox(icon, title, message, buttons).exec()

    def _warning_message(self, message) -> bool:
        return self._messagebox(self.Icon.Warning, "Warning", message, self.Button.Ok | self.Button.Cancel) == self.Button.Ok

    def _error_message(self, message) -> bool:
        self._messagebox(self.Icon.Critical, "Error", message, self.Button.Ok | self.Button.Cancel)
        return False

    def _question_message(self, message) -> bool:
        return self._messagebox(self.Icon.Question, "Question", message, self.Button.Yes | self.Button.No) == self.Button.Yes

    def _alert(self, message) -> bool:
        return self._messagebox(self.Icon.Information, "Alert", message, self.Button.Ok | self.Button.Cancel) == self.Button.Ok

    def _update_parking_value(self) -> None:
        self.parking.postgresql_bin = self.lineEdit_postgresql_bin.text()
        self.parking.host = self.lineEdit_db_host.text()
        self.parking.database = self.lineEdit_db_name.text()
        self.parking.port = self.spinBox_db_port.value()
        self.parking.username = self.lineEdit_db_user.text()
        self.parking.password = self.lineEdit_db_password.text()

    def _create_taskscheduler(self) -> None:
        self.task_auto.start_time = self.timeEdit_auto.time().toString('HH:mm')
        self.task_auto.create()
    
    def _remove_taskscheduler(self) -> None:
        self.task_auto.delete()
    
    def _create_item_comboBox_vehicle_type(self) -> None:
        self.comboBox_vehicle_type.clear()
        for vehicle_type in self.vehicle_types:
            self.comboBox_vehicle_type.add_checkable_item(vehicle_type[1], vehicle_type[0], False)
        self.vehicle_types_setting.load()


def calculator_datetime(delta) -> QDateTime:
    current = QDateTime.currentDateTime()
    return current.addDays(-delta)


def delete_images(*args) -> None:
    for img in args:
        if os.path.isfile(img):
            commandline.execute(f'del /F "{img}"')


def clean_data(
        parking: HTParking, 
        in_out_start_time: str, 
        in_out_end_time: str, 
        vehicle_type: list,
        except_start_time: str,
        except_end_time: str,
        is_del_data_in_out: bool,
        is_del_img_in_out: bool,
        is_del_data_except: bool,
        is_del_img_except: bool,
        worker: Worker = None,
    ) -> None:
    in_out_data, except_data = tuple(), tuple()
    if is_del_data_in_out or is_del_img_in_out:
        in_out_data = parking.get_id_image_in_out(
            start_time = in_out_start_time,
            end_time = in_out_end_time,
            vehicle_type = vehicle_type
        )
    if is_del_data_except or is_del_img_except:
        except_data = parking.get_id_image_exception(
            start_time = except_start_time,
            end_time = except_end_time
        )
    if worker:
        total_progress = (6 * len(in_out_data) * int(is_del_img_in_out) + 2 * len(in_out_data) * int(is_del_data_in_out)) + (4 * len(except_data) * int(is_del_img_except) + len(except_data) * int(is_del_data_except))
        worker.progress.emit(total_progress, "Tổng cộng " + str(len(in_out_data) + len(except_data)) + " dòng dữ liệu")
        if is_del_data_in_out and is_del_img_in_out:
            for id_in, id_out, img1, img2, img3, img4, img5, img6 in in_out_data:
                for img in (img1, img2, img3, img4, img5, img6):
                    worker.progress.emit(-1, "Xóa file "+ img) if img else worker.progress.emit(-1, '')
                    delete_images(img)
                worker.progress.emit(-1, "Xóa dữ liệu vào ID "+ id_in)
                parking.delete_parking_in(id_in)
                worker.progress.emit(-1, "Xóa dữ liệu ra ID "+ id_out)
                parking.delete_parking_out(id_out)
        elif is_del_img_in_out:
            for _, _, img1, img2, img3, img4, img5, img6 in in_out_data:
                for img in (img1, img2, img3, img4, img5, img6):
                    worker.progress.emit(-1, "Xóa file "+ img) if img else worker.progress.emit(-1, '')
                    delete_images(img)
        elif is_del_data_in_out:
            for data in in_out_data:
                worker.progress.emit(-1, "Xóa dữ liệu vào ID "+ data[0])
                parking.delete_parking_in(data[0])
                worker.progress.emit(-1, "Xóa dữ liệu ra ID "+ data[1])
                parking.delete_parking_out(data[1])
        if is_del_data_except and is_del_img_except:
            for e_id, img1, img2, img3, img4 in except_data:
                for img in (img1, img2, img3, img4):
                    worker.progress.emit(-1, "Xóa file "+ img) if img else worker.progress.emit(-1, '')
                    delete_images(img)
                worker.progress.emit(-1, "Xóa dữ liệu ngoại lệ ID "+ e_id)
                parking.delete_exception(e_id)
        elif is_del_img_except:
            for _, img1, img2, img3, img4 in except_data:
                for img in (img1, img2, img3, img4):
                    worker.progress.emit(-1, "Xóa file "+ img) if img else worker.progress.emit(-1, '')
                    delete_images(img)
        elif is_del_data_except:
            for data in except_data:
                worker.progress.emit(-1, "Xóa dữ liệu ngoại lệ ID "+ data[0])
                parking.delete_exception(data[0])
        worker.cleaned.emit(f"Hoàn tất xóa {len(in_out_data) + len(except_data)} dòng dữ liệu")
    else:
        if is_del_data_in_out and is_del_img_in_out:
            for id_in, id_out, img1, img2, img3, img4, img5, img6 in in_out_data:
                delete_images(img1, img2, img3, img4, img5, img6)
                parking.delete_parking_in(id_in)
                parking.delete_parking_out(id_out)
        elif is_del_img_in_out:
            for _, _, img1, img2, img3, img4, img5, img6 in in_out_data:
                delete_images(img1, img2, img3, img4, img5, img6)
        elif is_del_data_in_out:
            for data in in_out_data:
                parking.delete_parking_in(data[0])
                parking.delete_parking_out(data[1])
        if is_del_data_except and is_del_img_except:
            for e_id, img1, img2, img3, img4 in except_data:
                delete_images(img1, img2, img3, img4)
                parking.delete_exception(e_id)
        elif is_del_img_except:
            for _, img1, img2, img3, img4 in except_data:
                delete_images(img1, img2, img3, img4)
        elif is_del_data_except:
            for data in except_data:
                parking.delete_exception(data[0])


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--hidden':
        path = module.Path(__file__).app.join("log")
        if not os.path.isdir(path):
            os.mkdir(path)
        try:
            default_date = QDateTime.currentDateTime()
            date = [default_date, default_date]

            def set_in_out_start_time(datetime: QDateTime|str):
                date[0] = datetime
            
            def set_excep_start_time(datetime: QDateTime|str):
                date[1] = datetime

            setting = Config("setting")
            start_time_setting = setting.setup(
                ('in_out_start_time', lambda: date[0], set_in_out_start_time, default_date),
                ('except_start_time', lambda: date[1], set_excep_start_time, default_date)
            )
            config = setting.load()
            parking = HTParking(
                config['postgresql_bin'],
                config['db_host'],
                config['db_port'],
                config['db_name'],
                config['username'],
                config['password']
            )
            date[0] = calculator_datetime(config['in_out_keep'])
            date[1] = calculator_datetime(config['except_keep'])
            date[0].setTime(QTime(0, 0))
            date[1].setTime(QTime(0, 0))
            clean_data(
                parking,
                config['in_out_start_time'].toString('yyyy-MM-dd HH:mm:ss') if config['in_out_start_time'] else '',
                date[0].toString('yyyy-MM-dd HH:mm:ss'),
                config['vehicle_types'],
                config['except_start_time'].toString('yyyy-MM-dd HH:mm:ss') if config['except_start_time'] else '',
                date[1].toString('yyyy-MM-dd HH:mm:ss'),
                config['delete_data_in_out'],
                config['delete_image_in_out'],
                config['delete_data_except'],
                config['delete_image_except']
            )
            start_time_setting.upgrade()
        except Exception:
            log_path = os.path.join(path, QDateTime.currentDateTime().toString('yyyy-MM-dd HH_mm_ss') + ".txt")
            with open(log_path, 'w') as f:
                f.write(traceback.format_exc())
    else:
        app = QApplication(sys.argv)
        win = MainWindow()
        win.show()
        app.exec()

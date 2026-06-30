from PySide6.QtCore import QThread, Signal
import traceback


class SimpleThread(QThread):
    success = Signal()
    error = Signal(str)
    def __init__(self, parent, method: callable):
        super().__init__(parent)
        self.method = method
    
    def run(self):
        try:
            self.method()
        except Exception as e:
            self.error.emit(str(e))
            print(traceback.print_exc())
        else:
            self.success.emit()


class ChainThread(SimpleThread):
    one_success = Signal(int)
    one_error = Signal(int, str)

    def __init__(self, parent, array_thread: list|tuple):
        super().__init__(parent, None)
        self.array_thread = array_thread
    
    def run(self):
        for index, worker in enumerate(self.array_thread):
            worker.success.connect(lambda: self.one_success.emit(index))
            worker.error.connect(lambda e: self.one_error.emit(index, e))
            worker.exec()


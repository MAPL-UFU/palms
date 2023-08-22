from time import sleep

from PyQt5.QtCore import QThread, pyqtSignal
import nest_asyncio
import asyncio
from palms.async_serial_comu import start

nest_asyncio.apply()


class MsgThreadQt(QThread):
    msg_status = pyqtSignal(str, dict, name="msg_status")  # define new Signal

    def __init__(self, serial_ports, parent=None):
        super(MsgThreadQt, self).__init__(parent)
        self.serial_ports = serial_ports
        self.is_running = True
        self.pnrd = dict()
        self.loop = asyncio.get_event_loop()
        self.tasks = list()

    def run(self):
        while True:
            if not self.is_running:
                break
            try:
                for port in self.serial_ports:
                    task = self.loop.create_task(start(self.loop, port))
                    task.add_done_callback(self.got_result)
                    self.tasks.append(task)
                self.loop.run_forever()

            except OSError as error:
                self.msg_status.emit(
                    f"Permission Denied Serial Port and {error}", dict()
                )
                self.loop.stop()

    def got_result(self, future):
        done, _ = future.result()
        for fut in done:
            self.pnrd = fut.result()
        try:
            self.msg_status.emit("Receiving date", self.pnrd)
            print(f"{self.pnrd}")
            sleep(1)
        except Exception:
            self.msg_status.emit("Serial Connection Error", dict())
            print(f"{self.pnrd}")
            sleep(1)
        self.loop.stop()

    def stop(self):
        self.is_running = False
        print("stopping thread...")
        self.loop.stop()
        print("Loop Stoped")
        self.loop.close
        print("Loop Closed")
        self.terminate()
        print("Thread dead")

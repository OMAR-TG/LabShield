from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QMessageBox, QLabel
)
from device_manager import devices, send_command_to_device

class LabShieldAdmin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🛡️ LabShield - لوحة التحكم")
        self.setGeometry(200, 200, 400, 500)

        self.layout = QVBoxLayout()

        self.label = QLabel("🖥️ الأجهزة المتصلة:")
        self.layout.addWidget(self.label)

        self.device_list = QListWidget()
        for name, ip in devices.items():
            self.device_list.addItem(f"{name} ({ip})")
        self.layout.addWidget(self.device_list)

        self.btn_clear = QPushButton("🧹 مسح ملفات الطلاب")
        self.btn_clear.clicked.connect(self.clear_files)
        self.layout.addWidget(self.btn_clear)

        self.setLayout(self.layout)

    def clear_files(self):
        results = []
        for name, ip in devices.items():
            result = send_command_to_device(ip, "CLEAR_FILES")
            results.append(f"{name}: {result}")

        QMessageBox.information(self, "النتائج", "\n".join(results))

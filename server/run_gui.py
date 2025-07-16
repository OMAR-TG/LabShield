import sys
from PyQt5.QtWidgets import QApplication
from gui import LabShieldAdmin

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LabShieldAdmin()
    window.show()
    sys.exit(app.exec_())

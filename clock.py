from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt6.QtCore import QTimer, QTime

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt6 數位時鐘")
        self.setGeometry(100, 100, 250, 100)

        layout = QVBoxLayout()
        self.label = QLabel("00:00:00", self)
        self.label.setStyleSheet("font-size: 40px; color: white; background: black; padding: 10px;")
        layout.addWidget(self.label)

        self.setLayout(layout)

        timer = QTimer(self)
        timer.timeout.connect(self.update_time)
        timer.start(1000)  # 每秒更新一次

        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("HH:mm:ss")
        self.label.setText(current_time)

app = QApplication([])
window = DigitalClock()
window.show()
app.exec()

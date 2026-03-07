from PyQt6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPixmap
import time

class TimeInfo(QFrame):
    def __init__(self):
        QFrame.__init__(self)

        self.setFixedSize(390, 303)
        self.setStyleSheet("""
            background-color: rgba(0, 0, 0, 0.2);
            border-radius: 10px;
        """)

        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.main_layout.setContentsMargins(16, 16, 16, 16)
        self.main_layout.setSpacing(16)
        self.setLayout(self.main_layout)

        self.today_label = QLabel("Сьогодні")
        self.today_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.today_label.setStyleSheet("""
            font-size: 16px;
            font-weight: 500;
            color: white;
            background: transparent;
        """)
        self.main_layout.addWidget(self.today_label)

        self.date_layout = QHBoxLayout()
        self.date_layout.setSpacing(10)

        current_time = time.localtime()
        days = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота", "Неділя"]
        current_day = days[current_time.tm_wday]
        current_date = time.strftime("%d.%m.%Y", current_time)

        self.day_label = QLabel(current_day)
        self.day_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.day_label.setStyleSheet("""
            font-size: 24px;
            font-weight: 500;
            color: white;
            background: transparent;
        """)

        self.date_label = QLabel(current_date)
        self.date_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.date_label.setStyleSheet("""
            font-size: 24px;
            font-weight: 500;
            color: white;
            background: transparent;
        """)

        self.date_layout.addWidget(self.day_label)
        self.date_layout.addWidget(self.date_label)
        self.main_layout.addLayout(self.date_layout)

        self.time_circle = QFrame()
        self.time_circle.setFixedSize(168, 168)
        self.time_circle.setStyleSheet("""
            background-color: rgba(0, 0, 0, 0.2);
            border-radius: 84px;
        """)

        self.image_label = QLabel(self.time_circle)
        self.image_label.setGeometry(0, 0, 168, 168)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.pixmap = QPixmap("images/Ticks.png")
        self.pixmap = self.pixmap.scaled(168, 168)
        self.image_label.setPixmap(self.pixmap)

        current_time_str = time.strftime("%H:%M", current_time)
        self.time_label = QLabel(current_time_str, self.time_circle)
        self.time_label.setGeometry(0, 0, 168, 168)
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_label.setStyleSheet("""
            font-size: 29px;
            font-weight: 500;
            color: white;
            background: transparent;
        """)

        self.main_layout.addWidget(self.time_circle, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
    
    def update_time(self):
        """ОНОВЛЮЄ ЧАС КОЖНУ СЕКУНДУ"""
        current_time = time.localtime()
        current_time_str = time.strftime("%H:%M", current_time)
        self.time_label.setText(current_time_str)
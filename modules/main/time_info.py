# from PyQt6.QtWidgets import QFrame

# class TimeInfo(QFrame):
#     def __init__(self):
#         QFrame.__init__(self)
#         self.setFixedSize(390, 303)
#         self.setStyleSheet("background-color: rgba(0, 0, 0, 0.2)")




from PyQt6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

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

        self.day_label = QLabel("Понеділок")
        self.day_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.day_label.setStyleSheet("""
            font-size: 24px;
            font-weight: 500;
            color: white;
            background: transparent;
        """)

        self.date_label = QLabel("24.03.2025")
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

        self.time_label = QLabel("14:24", self.time_circle)
        self.time_label.setGeometry(0, 0, 168, 168)
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_label.setStyleSheet("""
            font-size: 29px;
            font-weight: 500;
            color: white;
            background: transparent;
        """)

        self.main_layout.addWidget(self.time_circle, alignment=Qt.AlignmentFlag.AlignCenter)

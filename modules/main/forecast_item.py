from PyQt6.QtWidgets import QFrame, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

class ForecastItem(QFrame):
    def __init__(self, time, temp):
        QFrame.__init__(self)
        
        self.setFixedSize(45, 82)
        self.setStyleSheet("background: transparent;")
        
        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.setSpacing(10)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.main_layout)
        
        
        self.time_label = QLabel(time)
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_label.setStyleSheet("""
            font-size: 16px;
            font-weight: 500;
            color: white;
            background: transparent;
        """)
        
       
        self.icon_label = QLabel()
        self.icon_label.setFixedSize(24, 24)
        self.icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.icon_label.setStyleSheet("background: transparent;")
        
       
        pixmap = QPixmap("images/icon_weather.png")
        self.icon_label.setGeometry(0, 0, 24, 24)
        self.icon_label.setPixmap(pixmap)
       
        self.temp_label = QLabel(temp)
        self.temp_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.temp_label.setStyleSheet("""
            font-size: 16px;
            font-weight: 500;
            color: white;
            background: transparent;
        """)
        
        self.main_layout.addWidget(self.time_label)
        self.main_layout.addWidget(self.icon_label)
        self.main_layout.addWidget(self.temp_label)
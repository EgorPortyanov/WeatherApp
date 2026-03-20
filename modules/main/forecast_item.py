from PyQt6.QtWidgets import QFrame, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

class ForecastItem(QFrame):
    def __init__(self, time, temp, icon_code="01d"):
        super().__init__()
        
        self.setFixedWidth(55)
        self.setStyleSheet("background: transparent; border: none;")
        
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.setSpacing(8) 
        self.main_layout.setContentsMargins(0, 5, 0, 5)
        
        self.time_label = QLabel(time)
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_label.setStyleSheet("""
            font-size: 16px; 
            color: white; 
            font-weight: bold;
        """)
        
       
        self.icon_label = QLabel()
        self.icon_label.setFixedSize(32, 32)
        self.icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
       
        icon_path = f"images/dark/{icon_code}.svg"
        pixmap = QPixmap(icon_path)
        
        if pixmap.isNull():
            pixmap = QPixmap("images/dark/02d.svg")
            
        self.icon_label.setPixmap(pixmap.scaled(
            32, 32, 
            Qt.AspectRatioMode.KeepAspectRatio, 
            Qt.TransformationMode.SmoothTransformation
        ))
       
        self.temp_label = QLabel(temp)
        self.temp_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.temp_label.setStyleSheet("""
            font-size: 16px; 
            color: white; 
            font-weight: bold;
        """)
        
        self.main_layout.addWidget(self.time_label)
        self.main_layout.addWidget(self.icon_label)
        self.main_layout.addWidget(self.temp_label)
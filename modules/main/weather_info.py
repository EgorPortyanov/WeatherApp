# from PyQt6.QtWidgets import QFrame

# class WeatherInfo(QFrame):
#     def __init__(self):
#         QFrame.__init__(self)
#         self.setFixedSize(390, 303)
#         self.setStyleSheet("background-color: rgba(0, 0, 0, 0.2)")



from PyQt6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtCore import Qt

class WeatherInfo(QFrame):
    def __init__(self):
        QFrame.__init__(self)
        self.setFixedSize(390, 303)
        self.setStyleSheet("""
            background-color: rgba(0, 0, 0, 0.2);
            border-radius: 10px;
        """)
        
        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.setContentsMargins(16, 16, 16, 16)
        self.main_layout.setSpacing(16)
        self.setLayout(self.main_layout)
        
        self.city_label = QLabel("Ватикан")
        self.city_label.setStyleSheet("""
            font-size: 44px;
            font-weight: 500;
            color: white;
            background: transparent;
        """)
        self.city_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.temp_layout = QHBoxLayout()
        self.temp_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.temp_layout.setSpacing(8)
        
        self.temp_label = QLabel("🌧️14°")
        self.temp_label.setStyleSheet("""
            font-size: 74px;
            font-weight: 500;
            color: white;
            background: transparent;
        """)
        
        self.temp_layout.addWidget(self.temp_label)
        
        self.info_layout = QVBoxLayout()
        self.info_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.info_layout.setSpacing(10)
        
        self.desc_label = QLabel("Дощ")
        self.desc_label.setStyleSheet("""
            font-size: 24px;
            font-weight: 500;
            color: white;
            background: transparent;
        """)
        self.desc_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.range_label = QLabel("Макс.:15°, мін.:1°")
        self.range_label.setStyleSheet("""
            font-size: 16px;
            font-weight: 500;
            color: rgba(255, 255, 255, 0.8);
            background: transparent;
        """)
        self.range_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.info_layout.addWidget(self.desc_label)
        self.info_layout.addWidget(self.range_label)
        
        self.main_layout.addWidget(self.city_label)
        self.main_layout.addLayout(self.temp_layout)
        self.main_layout.addLayout(self.info_layout)
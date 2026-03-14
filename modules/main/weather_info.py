from PyQt6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtCore import Qt
from ..utils.api import get_weather

class WeatherInfo(QFrame):
    def __init__(self):
        QFrame.__init__(self)
        self.setFixedSize(390, 303)
        self.setStyleSheet("""
            background-color: rgba(0, 0, 0, 0.2);
            border-radius: 10px;
        """)
        
        weather_data = get_weather("Dnipro")
        
        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.setContentsMargins(16, 16, 16, 16)
        self.main_layout.setSpacing(16)
        self.setLayout(self.main_layout)
        
        self.city_label = QLabel("Дніпро")
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
        
        if weather_data:
            temp = round(weather_data["main"]["temp"])
            description = weather_data["weather"][0]["description"]
            feels_like = round(weather_data["main"]["feels_like"])
            temp_min = round(weather_data["main"]["temp_min"])
            temp_max = round(weather_data["main"]["temp_max"])
            
            self.temp_label = QLabel(f"{temp}°")
            self.desc_label = QLabel(description)
            self.range_label = QLabel(f"Макс.:{temp_max}°, мін.:{temp_min}°")
        else:
            self.temp_label = QLabel("--°")
            self.desc_label = QLabel("Немає даних")
            self.range_label = QLabel("Макс.:--°, мін.:--°")
        
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
        
        self.desc_label.setStyleSheet("""
            font-size: 24px;
            font-weight: 500;
            color: white;
            background: transparent;
        """)
        self.desc_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
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
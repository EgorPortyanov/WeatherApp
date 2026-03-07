from PyQt6.QtWidgets import QFrame, QScrollArea, QHBoxLayout, QLabel
from PyQt6.QtCore import Qt
from .forecast_item import ForecastItem
from ..utils.api import get_data
import time

class ForecastInfo(QFrame):
    def __init__(self):
        super().__init__()

        self.setFixedHeight(130)
        self.setStyleSheet("""
            background-color: rgba(0, 0, 0, 0.2);
            border-radius: 20px;
        """)

        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(20, 16, 20, 16)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll.setStyleSheet("background: transparent;")

        content = QFrame()
        content.setStyleSheet("background: transparent;")

        items_layout = QHBoxLayout(content)
        items_layout.setSpacing(25)
        items_layout.setContentsMargins(0, 0, 0, 0)
        items_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

      
        forecast_data = get_data("Dnipro")
        
        if forecast_data and "list" in forecast_data:
            forecast_list = forecast_data["list"][:20]
            
            for item in forecast_list:
                timestamp = item["dt"]
                hour = time.strftime("%H", time.localtime(timestamp))
            
                temp = round(item["main"]["temp"])
                
                forecast_item = ForecastItem(hour, f"{temp}°")
                items_layout.addWidget(forecast_item)
        else:   
            hours = ["14","15","16","17","18","19","20","21","22","23","00","01","02","03","04","05","06","07","08","09"]
            temps = ["11°","11°","10°","8°","5°","4°","3°","3°","0°","0°","0°","0°","0°","0°","0°","0°","0°","0°","0°","0°"]
            
            for i in range(20):
                item = ForecastItem(hours[i], temps[i])
                items_layout.addWidget(item)

        scroll.setWidget(content)
        main_layout.addWidget(scroll)
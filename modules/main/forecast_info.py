from PyQt6.QtWidgets import QFrame, QScrollArea, QHBoxLayout
from PyQt6.QtCore import Qt
from .forecast_item import ForecastItem
from ..utils.api import get_forecast
import time

class ForecastInfo(QFrame):
    def __init__(self):
        super().__init__()
        
        self.current_city = "Дніпро"

        self.setFixedHeight(140)
        self.setStyleSheet("""
            background-color: rgba(0, 0, 0, 0.2);
            border-radius: 20px;
            border: none;
        """)

        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(15, 10, 15, 10)

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll.setStyleSheet("background: transparent; border: none;")

        self.content = QFrame()
        self.content.setStyleSheet("background: transparent;")

        self.items_layout = QHBoxLayout(self.content)
        self.items_layout.setSpacing(25)
        self.items_layout.setContentsMargins(0, 0, 0, 0)
        self.items_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.scroll.setWidget(self.content)
        main_layout.addWidget(self.scroll)
        
        self.load_forecast()
    
    def load_forecast(self):
        while self.items_layout.count() > 0:
            item = self.items_layout.takeAt(0)
            if item.widget():
                item.widget().setParent(None)
        
        forecast_data = get_forecast(self.current_city)
        
        if forecast_data and "list" in forecast_data:
            forecast_list = forecast_data["list"][:10]
            
            for item in forecast_list:
                timestamp = item["dt"]
                hour = time.strftime("%H", time.localtime(timestamp))
                temp = round(item["main"]["temp"])
                icon_code = item["weather"][0]["icon"]
                
                forecast_item = ForecastItem(hour, f"{temp}°", icon_code)
                self.items_layout.addWidget(forecast_item)
        else:
            hours = ["14", "15", "16", "17", "18", "19", "20", "21", "22", "23"]
            temps = ["11°", "11°", "10°", "8°", "5°", "4°", "3°", "3°", "0°", "0°"]
            icons = ["02d", "02d", "03d", "03d", "04d", "04d", "02n", "02n", "01n", "01n"]
            
            for i in range(len(hours)):
                item = ForecastItem(hours[i], temps[i], icons[i])
                self.items_layout.addWidget(item)
    
    def update_city(self, city_name):
        self.current_city = city_name
        self.load_forecast()
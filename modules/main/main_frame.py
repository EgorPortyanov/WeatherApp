from PyQt6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout
from .forecast_info import ForecastInfo
from .graphics_info import GraphicsInfo
from .header import Header
from .weather_info import WeatherInfo
from .time_info import TimeInfo
from modules.side_panel import SidePanel

class MainInfo(QFrame):
    def __init__(self, side_panel=None):
        QFrame.__init__(self)
        self.setMinimumSize(790, 733)
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.setStyleSheet("background-color: rgba(0, 0, 0, 0)")

        self.side_panel = side_panel

        self.header = Header(side_panel=self.side_panel)
        self.main_layout.addWidget(self.header)
        
        self.main_container = QFrame()
        self.main_container.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
        self.main_container.setFixedHeight(303)
        self.main_container.setMinimumWidth(790)

        self.horizontal_layout = QHBoxLayout()
        self.horizontal_layout.setContentsMargins(0, 0, 0, 0)
        self.main_container.setLayout(self.horizontal_layout)

        self.weather_info = WeatherInfo()
        self.horizontal_layout.addWidget(self.weather_info)
        self.time_info = TimeInfo()
        self.horizontal_layout.addWidget(self.time_info)

        self.main_layout.addWidget(self.main_container)

        self.forecast_info = ForecastInfo()
        self.main_layout.addWidget(self.forecast_info)

        self.graphics_info = GraphicsInfo()
        self.main_layout.addWidget(self.graphics_info)
    
    def update_city(self, city_name):
        self.weather_info.update_city(city_name)
        self.forecast_info.update_city(city_name)
        self.graphics_info.update_city(city_name)
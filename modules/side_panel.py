from PyQt6.QtWidgets import QFrame, QVBoxLayout, QScrollArea
from PyQt6.QtCore import Qt
from .city import City
from modules.utils.api import get_weather

class SidePanel(QFrame):
    def __init__(self):
        QFrame.__init__(self)

        self.setStyleSheet("""
            background-color: rgba(0, 0, 0, 0.1);
            border: 0
        """)

        self.setFixedSize(370, 800)
        
        self.container = QFrame()
        self.container.setStyleSheet("background: transparent;")
        
        self.vertical_layout = QVBoxLayout(self.container)
        self.vertical_layout.setSpacing(15)
        self.vertical_layout.setContentsMargins(35, 20, 35, 20)
        self.vertical_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        cities = ["Дніпро", "Київ", "Братислава", "Варшава", "Рим"]
        
        for city_name in cities:
            weather_data = get_weather(city_name)
            
            if weather_data:
                temp = round(weather_data["main"]["temp"])
                feels_like = round(weather_data["main"]["feels_like"])
                description = weather_data["weather"][0]["description"]
                
                city_card = City(
                    name=city_name,
                    time="", 
                    temp=f"{temp}°",
                    desc=description,
                    max_temp=f"{temp}°",
                    min_temp=f"{feels_like}°"
                )
            self.vertical_layout.addWidget(city_card)

        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.main_layout)

        self.scroll_element = QScrollArea(self)
        self.scroll_element.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_element.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_element.setWidgetResizable(True)
        self.scroll_element.setStyleSheet("background: transparent; border: none;")
        self.scroll_element.setWidget(self.container)
        
        self.main_layout.addWidget(self.scroll_element)
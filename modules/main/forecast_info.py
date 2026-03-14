from PyQt6.QtWidgets import QFrame, QScrollArea, QHBoxLayout
from PyQt6.QtCore import Qt
from .forecast_item import ForecastItem

class ForecastInfo(QFrame):
    def __init__(self):
        super().__init__()

        self.setFixedHeight(140)
        self.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.1);
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

        content = QFrame()
        content.setStyleSheet("background: transparent;")

        self.items_layout = QHBoxLayout(content)
        self.items_layout.setSpacing(25)
        self.items_layout.setContentsMargins(0, 0, 0, 0)
        self.items_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

       
        hours = ["14", "15", "16", "17", "18", "19", "20", "21", "22", "23"]
        temps = ["11°", "11°", "10°", "8°", "5°", "4°", "3°", "3°", "0°", "0°"]
    
        icons = ["02d", "02d", "03d", "03d", "04d", "04d", "02n", "02n", "01n", "01n"]
        
        for i in range(len(hours)):
            item = ForecastItem(hours[i], temps[i], icons[i]) 
            self.items_layout.addWidget(item)

        self.scroll.setWidget(content)
        main_layout.addWidget(self.scroll)

    def update_forecast(self, city_name):
        pass

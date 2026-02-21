from PyQt6.QtWidgets import QFrame, QScrollArea, QHBoxLayout
from PyQt6.QtCore import Qt
from .forecast_item import ForecastItem


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

        hours = ["14","15","16","17","18","19","20","21","22","23","00","01", "02","03","04","05","06","07","08","09"]
        temps = ["11°","11°","10°","8°","5°","4°","3°","3°","0°","0°","0°","0°", "0°","0°","0°","0°","0°","0°","0°","0°"]

        for i in range(20):
            item = ForecastItem(hours[i], temps[i])
            items_layout.addWidget(item)
        scroll.setWidget(content)
        main_layout.addWidget(scroll)
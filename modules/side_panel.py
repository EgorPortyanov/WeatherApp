from PyQt6.QtWidgets import QFrame, QVBoxLayout, QScrollArea
from PyQt6.QtCore import Qt
from .city import City
from modules.utils.api import get_weather
import json
import os

class SidePanel(QFrame):
    def __init__(self, window):
        super().__init__()
        
        self.window = window
        self.config_file = "config.json"

        self.setStyleSheet("""
            background-color: rgba(0, 0, 0, 0.1);
            border: 0;
        """)
        self.setFixedSize(370, 800)

        self.container = QFrame()
        self.container.setStyleSheet("background: transparent;")

        self.vertical_layout = QVBoxLayout(self.container)
        self.vertical_layout.setSpacing(15)
        self.vertical_layout.setContentsMargins(10, 10, 10, 10)
        self.vertical_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.cities_list = []
        self.current_selected = None

        self.load_cities_from_json()

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
    
    def load_cities_from_json(self):
        loaded_names = []
        
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    loaded_names = data.get("city_list", [])
            except:
                loaded_names = []
        
        for city_name in loaded_names:
            self.add_city_to_panel(city_name)
    
    def add_city_to_panel(self, city_name):
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
                min_temp=f"{feels_like}°",
                panel=self
            )
        else:
            city_card = City(
                name=city_name,
                time="",
                temp="--°",
                desc="Немає даних",
                max_temp="--°",
                min_temp="--°",
                panel=self
            )
        
        self.cities_list.append(city_card)
        self.vertical_layout.addWidget(city_card)
    
    def add_city(self, city_name):
        for city in self.cities_list:
            if city.city_name.lower() == city_name.lower():
                return
        
        self.add_city_to_panel(city_name)
        self.save_cities_to_json()
    
    def save_cities_to_json(self):
        names_to_save = [city.city_name for city in self.cities_list]
        data = {"city_list": names_to_save}
        
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    
    def select_city(self, selected_city):
        if self.current_selected:
            self.current_selected.setStyleSheet("background-color: transparent; border-radius: 6px;")
        
        selected_city.setStyleSheet("background-color: rgba(0, 0, 0, 0.5); border-radius: 6px;")
        
        self.current_selected = selected_city
        self.window.update_main_city(selected_city.city_name)

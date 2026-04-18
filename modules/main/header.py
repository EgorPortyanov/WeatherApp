from PyQt6.QtWidgets import QFrame, QHBoxLayout, QLineEdit, QPushButton, QLabel
from PyQt6.QtCore import Qt

class Header(QFrame):
    def __init__(self, side_panel=None):
        QFrame.__init__(self)
        self.side_panel = side_panel
        

        self.setFixedHeight(36) 
        self.setStyleSheet("background: transparent;")
        
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        
        self.layout.setSpacing(20) 
        
        left_widget = QFrame()
        left_widget.setFixedSize(144, 36)
        left_layout = QHBoxLayout(left_widget)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(10)
        
        settings_button = QPushButton("⚙️")
        settings_button.setFixedSize(36, 36)
        settings_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(0, 0, 0, 0.2);
                border-radius: 4px; border: none; font-size: 18px; color: white;
            }
            QPushButton:hover { background-color: rgba(0, 0, 0, 0.4); }
        """)
        left_layout.addWidget(settings_button)
        
        settings_label = QLabel("Налаштування")
        settings_label.setFixedSize(98, 16)
        settings_label.setStyleSheet("font-family: 'Roboto'; font-weight: 500; font-size: 14px; color: #FFFFFF;")
        left_layout.addWidget(settings_label)
        
        self.layout.addWidget(left_widget)

        self.layout.addStretch()

        right_widget = QFrame()
        right_widget.setFixedSize(380, 36) 
        right_layout = QHBoxLayout(right_widget)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(10)
        
        self.add_button = QPushButton("+")
        self.add_button.setFixedSize(36, 36)
        self.add_button.clicked.connect(self.add_city)
        self.add_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(0, 0, 0, 0.2);
                border-radius: 4px; border: none; font-size: 24px; font-weight: bold; color: white;
            }
            QPushButton:hover { background-color: rgba(0, 0, 0, 0.4); }
        """)
        right_layout.addWidget(self.add_button)
        
        add_label = QLabel("Додати")
        add_label.setFixedSize(58, 22)
        add_label.setStyleSheet("font-family: 'Roboto'; font-weight: 400; font-size: 17px; color: #FFFFFF;")
        right_layout.addWidget(add_label)
        
        self.city_input = QLineEdit()
        self.city_input.setFixedSize(261, 36)
        self.city_input.setPlaceholderText("Назва міста")
        self.city_input.setStyleSheet("""
            QLineEdit {
                background-color: rgba(0, 0, 0, 0.2);
                border: 1px solid #FFFFFF; border-radius: 4px;
                color: #FFFFFF; font-family: 'Roboto'; font-size: 17px; padding: 7px 8px;
            }
        """)
        right_layout.addWidget(self.city_input)
        
        self.layout.addWidget(right_widget)
    
    def add_city(self):
        city_name = self.city_input.text().strip()
        if city_name and self.side_panel:
            self.side_panel.add_city(city_name)
            self.city_input.clear()

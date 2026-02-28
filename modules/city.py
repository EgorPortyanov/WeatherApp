from PyQt6.QtWidgets import QFrame, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt

class City(QFrame):
    def __init__(self, name, time, temp, desc, max_temp, min_temp):
        QFrame.__init__(self)
        
        self.setFixedSize(300, 90)
        
        self.setStyleSheet("""
            background-color: rgba(0, 0, 0, 0.2);
            border-radius: 6px;
        """)
        
        self.city_label = QLabel(name)
        self.time_label = QLabel(time)
        self.temp_label = QLabel(temp)
        self.desc_label = QLabel(desc)
        self.range_label = QLabel("Макс: " + max_temp + ", Мін: " + min_temp)
        
        self.city_label.setStyleSheet("font-size: 18px; font-weight: bold; color: white; background: transparent;")
        self.time_label.setStyleSheet("font-size: 12px; color: rgba(255,255,255,0.8); background: transparent;")
        self.temp_label.setStyleSheet("font-size: 44px; color: rgba(255,255,255,0.8); background: transparent;")
        self.desc_label.setStyleSheet("font-size: 12px; color: rgba(255,255,255,0.8); background: transparent;")
        self.range_label.setStyleSheet("font-size: 12px; color: rgba(255,255,255,0.8); background: transparent;")
        
        self.top_layout = QHBoxLayout()
        
        self.left_layout = QVBoxLayout()
        self.left_layout.addWidget(self.city_label)
        self.left_layout.addWidget(self.time_label)
        
        self.right_layout = QVBoxLayout()
        self.right_layout.addWidget(
            self.temp_label,
            alignment=Qt.AlignmentFlag.AlignRight
        )
        
        self.top_layout.addLayout(self.left_layout)
        self.top_layout.addLayout(self.right_layout)
        
        self.bottom_layout = QHBoxLayout()
        self.bottom_layout.addWidget(self.desc_label)
        self.bottom_layout.addWidget(self.range_label)
        
        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addLayout(self.bottom_layout)
        
        self.main_layout.setContentsMargins(8, 8, 8, 8)
        
        self.setLayout(self.main_layout)
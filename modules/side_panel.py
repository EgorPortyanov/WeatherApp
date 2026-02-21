# from PyQt6.QtWidgets import QFrame, QVBoxLayout, QScrollArea, QWidget
# from PyQt6.QtCore import Qt
# from .city import City


# class SidePanel(QFrame):
#     def __init__(self):
#         QFrame.__init__(self)

#         self.setStyleSheet("""
#             background-color: rgba(0, 0, 0, 0.1);
#             border: 0
#         """)

#         self.setFixedSize(370, 800)
        
        

#         self.container = QFrame()
#         self.vertical_layout = QVBoxLayout(self.container)
#         self.vertical_layout.setSpacing(15)
#         self.vertical_layout.setContentsMargins(35, 20, 35, 20)
#         self.vertical_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        
#         self.city1 = City("Дніпро", "15:24", "11°", "Переважно хмарно", "11°", "0°")
#         self.city2 = City("Київ", "15:24", "14°", "Сонячно", "15°", "0°")
#         self.city3 = City("Братислава", "14:24", "9°", "Подекуди хмарно", "10°", "1°")
#         self.city4 = City("Варшава", "14:24", "15°", "Хмарно", "18°", "7°")
#         self.city5 = City("Рим", "14:24", "24°", "Сонячно", "25°", "16°")

#         self.main_layout = QVBoxLayout()
#         self.setLayout(self.main_layout)

#         self.scroll_element = QScrollArea(self)
#         self.scroll_element.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
#         self.scroll_element.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
#         self.main_layout.addWidget(self.scroll_element)


        
#         self.vertical_layout.addWidget(self.city1)
#         self.vertical_layout.addWidget(self.city2)
#         self.vertical_layout.addWidget(self.city3)
#         self.vertical_layout.addWidget(self.city4)
#         self.vertical_layout.addWidget(self.city5)

#         self.scroll_element.setWidget(self.container)


from PyQt6.QtWidgets import QFrame, QVBoxLayout, QScrollArea
from PyQt6.QtCore import Qt
from .city import City

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
        
        self.city1 = City("Дніпро", "15:24", "11°", "Переважно хмарно", "11°", "0°")
        self.city2 = City("Київ", "15:24", "14°", "Сонячно", "15°", "0°")
        self.city3 = City("Братислава", "14:24", "9°", "Подекуди хмарно", "10°", "1°")
        self.city4 = City("Варшава", "14:24", "15°", "Хмарно", "18°", "7°")
        self.city5 = City("Рим", "14:24", "24°", "Сонячно", "25°", "16°")

        self.vertical_layout.addWidget(self.city1)
        self.vertical_layout.addWidget(self.city2)
        self.vertical_layout.addWidget(self.city3)
        self.vertical_layout.addWidget(self.city4)
        self.vertical_layout.addWidget(self.city5)

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
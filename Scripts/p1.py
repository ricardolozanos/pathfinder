import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QLabel, QTextBrowser, QPushButton, QComboBox, QScrollArea, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from PyQt6.QtCore import Qt, pyqtSignal, QRectF, QRect
from PyQt6.QtGui import QMouseEvent, QPixmap, QPainter, QPen
from PathFinder import PathFinder
import os

#GUI Mapa (Quadrante 0,1)
class MapDisplay(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.rectSize = 400
        self.diff=30
        self.setScene(QGraphicsScene(self))
        self.setSceneRect(0, 0, self.rectSize, self.rectSize)  
        self.map_data = None
        self.path = None
        self.start_pos = None
        self.goal_pos = None
        
    #Refrescar mapa
    def update_map(self, map_data, path, start_pos, goal_pos):
        self.map_data = map_data
        self.path = path
        self.start_pos = start_pos
        self.goal_pos = goal_pos
        self.update()
        self.viewport().update()  

    #Pintar mapa al obtener los datos.        
    def paintEvent(self, event):
        if self.map_data:
            painter = QPainter(self.viewport())
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)


            self.scene().clear()

            # Calcular las dimensiones del cuadro
            num_rows = len(self.map_data)
            num_cols = len(self.map_data[0]) if num_rows > 0 else 0

            
            cell_size = max(min((self.rectSize-self.diff) // num_cols, (self.rectSize-self.diff) // num_rows, 40), 10)
            
            # Calcular las dimensiones de las celdas            
            for i, row in enumerate(self.map_data):
                for j, cell_value in enumerate(row):
                    if cell_value == '#':
                        painter.setBrush(Qt.GlobalColor.black)
                    else:
                        painter.setBrush(Qt.GlobalColor.white)

                        
                    painter.drawRect(j * cell_size, i * cell_size, cell_size, cell_size)

            # Si existe camino pintarlo                    
            if self.path:
                pen = QPen()
                pen.setColor(Qt.GlobalColor.blue)
                pen.setWidth(3)
                painter.setPen(pen)
                for i in range(len(self.path) - 1):
                    x1, y1 = self.path[i][::-1]
                    x2, y2 = self.path[i + 1][::-1]
                    painter.drawLine(x1 * cell_size + cell_size // 2, y1 * cell_size + cell_size // 2,
                                     x2 * cell_size + cell_size // 2, y2 * cell_size + cell_size // 2)

                    
            # Pintar la posicion inicial azul
            if self.start_pos:
                painter.setBrush(Qt.GlobalColor.blue)
                x, y = self.start_pos[::-1]
                painter.drawRect(x * cell_size, y * cell_size, cell_size, cell_size)

            # Pintar posision final rojo o verde
            if self.goal_pos:
                if self.path:
                    painter.setBrush(Qt.GlobalColor.green)
                else:
                    painter.setBrush(Qt.GlobalColor.red)
                x, y = self.goal_pos[::-1]
                painter.drawRect(x * cell_size, y * cell_size, cell_size, cell_size)

                
            for i, row in enumerate(self.map_data):
                for j, cell_value in enumerate(row):
                    text = str(cell_value)
                    text_rect = QRect(j * cell_size, i * cell_size, cell_size, cell_size)
                    painter.drawText(text_rect, Qt.AlignmentFlag.AlignCenter, text)

            painter.end()








#Hacer los mapas que se puedan clickear
class ClickableTextBrowser(QTextBrowser):
    clicked = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

    def mousePressEvent(self, event: QMouseEvent):
        self.clicked.emit()
        super().mousePressEvent(event)
    
    def change_border(self):
        self.setStyleSheet("border: 1px solid blue; padding: 5px;")

    def reset_border(self):
        self.setStyleSheet("border: 1px solid black; padding: 5px;")

class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.labels = {
            'algorithm_label': None,
            'start_pos_label': None,
            'goal_pos_label': None,
            'cost_label': None,
            'nodes_label': None,
            'max_nodes_label': None,
            'runtime_label': None,
            'path_label': None,
        }
        self.showMaximized()  
        



    def init_ui(self):
        
        layout = QGridLayout()
        
        #Seleccionar Mapa
        self.file_section = QVBoxLayout()
        file_label = QLabel("Files in Directory:")

        self.file_section.addWidget(file_label)

        # Seleccionar Algoritmo
        algorithm_section = QVBoxLayout()
        algorithm_label = QLabel("Select Algorithm:")
        self.algorithm_combo = QComboBox()
        algorithms = ["BFS", "IDS", "A*"]
        self.algorithm_combo.addItems(algorithms)
        algorithm_section.addWidget(algorithm_label)
        algorithm_section.addWidget(self.algorithm_combo)

        #  Mostrar Informacion
        info_section = QVBoxLayout()
        info_label = QLabel("Programming Assignment 1\nSearch and Pathfinding\nRicardo Lozano\nIvan Montoya")
        info_section.addWidget(info_label)

        # Mostrar mapa
        map_section = QVBoxLayout()
        self.map_button = QPushButton("Start Map Motion")
        self.map_button.clicked.connect(self.start_map_motion)
        self.map_display = MapDisplay()
        map_section.addWidget(self.map_button)
        map_section.addWidget(self.map_display)

        # Posicionar secciones
        layout.addLayout(self.file_section, 0, 0)
        layout.addLayout(algorithm_section, 1, 0)
        layout.addLayout(info_section, 1, 1)
        layout.addLayout(map_section, 0, 1)

        self.setLayout(layout)
        self.setWindowTitle("Programming Assignment 1")
        self.setGeometry(100, 100, 600, 500)

        
        self.load_txt_files()

        
        self.selected_algorithm = None
        self.selected_map_file = None

    #Files de mapa, (Cambiar color)
    def text_div_clicked(self, txt_file):
        
        for text_div in self.text_divs.values():
            text_div.reset_border()
        
        
        self.text_divs[txt_file].change_border()
        self.selected_map_file = txt_file

        
    #Cargar mapas        
    def load_txt_files(self):
        if not os.path.exists("map"):
            os.makedirs("map")

        map_files = [file for file in os.listdir("map") if file.startswith("map")]

        
        container_widget = QWidget()
        container_layout = QVBoxLayout(container_widget)

        self.text_divs = {}

        for txt_file in map_files:
            # Seccion de mapas scrollable
            scroll_area = QScrollArea()
            scroll_area.setWidgetResizable(True)  
            scroll_area.setFixedSize(400, 200) 

            
            # Crear widget de mapa (No informacion)
            div_widget = QWidget()
            scroll_area.setWidget(div_widget)

            
            div_layout = QVBoxLayout(div_widget)

            
            div = ClickableTextBrowser()  
            div.setOpenExternalLinks(True)  
            div.setReadOnly(True)  
            div.setStyleSheet("border: 1px solid black; padding: 5px;")  

            
            #Leer todos los mapas y empezar a crearlos
            with open(os.path.join("map", txt_file), 'r') as file:
                lines = file.readlines()

            # Extraer info
            map_size = lines[0].strip()
            agent_start_position = lines[1].strip()
            goal_position = lines[2].strip()
            map_data = lines[3:]

            # Pasar info
            div.setPlainText(f"Map Size: {map_size}\n"
                             f"Agent Start Position: {agent_start_position}\n"
                             f"Goal Position: {goal_position}\n"
                             "Map Data:")
            for line in map_data:
                div.append(line.strip())  

            
            div.clicked.connect(lambda txt_file=txt_file: self.text_div_clicked(txt_file))

            
            div_layout.addWidget(div)
            self.text_divs[txt_file] = div

            
            container_layout.addWidget(scroll_area)

        
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)  
        scroll_area.setFixedSize(500, 400)
        scroll_area.setWidget(container_widget)  

        
        self.file_section.addWidget(scroll_area)




        
        






    #Empezar movimiento del mapa
    def start_map_motion(self):
        self.selected_algorithm = self.algorithm_combo.currentText()
        if self.selected_algorithm and self.selected_map_file:
            map_folder = "map"
            full_map_file = os.path.join(map_folder, self.selected_map_file)
            path_finder = PathFinder(full_map_file , self.selected_algorithm)
            data = path_finder.visualize_path(self.selected_algorithm, self)

            self.update_gui_with_path_info(data)

            self.map_display.repaint()
            self.update()
            QApplication.processEvents()
            print("Processed")
        else:
            print("Please select an algorithm and a map file.")

    def update_gui_with_path_info(self, data):
        results = data['results']
        algorithm = data['algorithm']
        start_pos = data['start_pos']
        map_data = data['map']
        goal_pos = data['goal']
        cost_of_path = data['results']['Path Cost']
        nodes_exp = data['results']['Nodes Expanded']
        max_nodes_om = data['results']['Max Nodes in Memory']
        runtime = data['results']['Runtime (ms)']
        path = data['results']['Path']
        #Debug-print("Inside update_gui_with_path_info")  


        # Label de algorithm
        if self.labels['algorithm_label'] is None:
            self.labels['algorithm_label'] = QLabel()
            self.layout().addWidget(self.labels['algorithm_label'])
        self.labels['algorithm_label'].setText(f"Algorithm Used: {algorithm}")

        # Label de posicion
        if self.labels['start_pos_label'] is None:
            self.labels['start_pos_label'] = QLabel()
            self.layout().addWidget(self.labels['start_pos_label'])
        self.labels['start_pos_label'].setText(f"Start Position: {start_pos}")

        # Label de Goal
        if goal_pos is not None:
            if self.labels['goal_pos_label'] is None:
                self.labels['goal_pos_label'] = QLabel()
                self.layout().addWidget(self.labels['goal_pos_label'])
            self.labels['goal_pos_label'].setText(f"Goal Position: {goal_pos}")
        
        #Agregar Label de Costo
        if cost_of_path is not None:
            if self.labels['cost_label'] is None:
                self.labels['cost_label'] = QLabel()
                self.layout().addWidget(self.labels['cost_label'])
            self.labels['cost_label'].setText(f"Cost of the path: {cost_of_path}")
            
        #Agregar Label de # de nodos
        if nodes_exp is not None:
            if self.labels['nodes_label'] is None:
                self.labels['nodes_label'] = QLabel()
                self.layout().addWidget(self.labels['nodes_label'])
            self.labels['nodes_label'].setText(f"Nodes Expanded: {nodes_exp}")
        
        #Agregar label de Max # de nodos
        if max_nodes_om is not None:
            if self.labels['max_nodes_label'] is None:
                self.labels['max_nodes_label'] = QLabel()
                self.layout().addWidget(self.labels['max_nodes_label'])
            self.labels['max_nodes_label'].setText(f"Max nodes on memory: {max_nodes_om}")
        
        #Agregar Label de Runtime
        if runtime is not None:
            if self.labels['runtime_label'] is None:
                self.labels['runtime_label'] = QLabel()
                self.layout().addWidget(self.labels['runtime_label'])
            self.labels['runtime_label'].setText(f"Runtime on milliseconds: {runtime}")
        
        #Agregar Label de Path
        if path is not None:
            if self.labels['path_label'] is None:
                self.labels['path_label'] = QLabel()
                self.layout().addWidget(self.labels['path_label'])
            if len(path)>15:
                path_label_string=''
                for i in range(len(path)):
                    if i%15 != 0:
                        path_label_string+=str(path[i])
                        path_label_string+= ' '
                    else:
                        path_label_string+='\n'
                        path_label_string+=str(path[i])
            else:
                path_label_string=''
                for i in range(len(path)):
                    path_label_string+=str(path[i])
                    path_label_string+= ' '
            self.labels['path_label'].setText(f"Path Taken: {path_label_string}")
        

        
        self.map_display.update_map(map_data, path,start_pos, goal_pos)

        self.update()

        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec())

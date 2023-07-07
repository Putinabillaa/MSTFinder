''' 
This file contains the main application. 
It is responsible for creating the main window and
handling user input. 
'''
import sys
import networkx as nx
import Style as s
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from Kruskal import kruskal
from Prim import prim


class MainWindow(QMainWindow):
    '''main application window'''
    def __init__(self):
        '''initialize main window'''
        super().__init__()
        self.adj_matrix = []
        self.algo_choice = "Prim"
        self.create_graph()

        # Set windows
        self.wdw = None
        self.setWindowTitle('MST Finder')
        self.setStyleSheet(s.bg_color)
        self.resize(500, 700)

        # Create the main widget
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        # Create the main layout
        main_layout = QVBoxLayout(main_widget)
        main_layout.setContentsMargins(50, 50, 50, 50)

        # Create the stretchable container
        stretchable_container = QWidget()
        stretchable_layout = QVBoxLayout(stretchable_container)

        # Create the fixed-width container
        fixed_width_container = QWidget()
        fixed_width_container.setFixedWidth(400)
        fixed_width_layout = QVBoxLayout(fixed_width_container)

        # Create the centered alignment layout
        center_layout = QHBoxLayout()
        center_layout.addWidget(fixed_width_container)

        # Add the containers and center layout to the main layout
        main_layout.addWidget(stretchable_container)
        main_layout.addLayout(center_layout)     

        self.total_weight_label = QLabel()
        self.total_weight_label.setStyleSheet(s.label_style)

        # Create button for file selection
        file_button = QPushButton('Select File')
        file_button.setStyleSheet(s.button_style4)
        file_button.setMaximumWidth(100)
        file_button.clicked.connect(self.file_button_clicked)
        
        # Create visualize button
        self.visualize_button = QPushButton('Visualize')
        self.visualize_button.setIcon(QIcon("asset/eye.png"))
        self.visualize_button.setStyleSheet(s.button_style1)
        self.visualize_button.clicked.connect(self.visualize_button_clicked)
        if(self.adj_matrix == []):
            self.visualize_button.setEnabled(False)
        
        # Create QHBoxLayout for file and visualize buttons
        file_visualize_hlayout = QHBoxLayout()
        file_visualize_hlayout.addWidget(file_button)
        file_visualize_hlayout.addWidget(self.visualize_button)

        # Create add node button
        add_node_label = QLabel('Add Node:')
        add_node_button = QPushButton('+')
        add_node_button.setStyleSheet(s.button_style2)
        add_node_button.clicked.connect(self.add_node_button_clicked)

        # Create QLineEdit widget for entering the node number
        self.node_number_textfield = QLineEdit()
        self.node_number_textfield.setStyleSheet(s.line_edit_style)
        
        # Create delete node button
        delete_node_label = QLabel('Delete Node (Enter Number):')
        delete_node_button = QPushButton('-')
        delete_node_button.setStyleSheet(s.button_style3)
        delete_node_button.clicked.connect(self.delete_node_button_clicked)

        # Create QHBoxLayout for edit node buttons
        edit_node_hlayout = QHBoxLayout()
        edit_node_hlayout.addWidget(add_node_label)
        edit_node_hlayout.addWidget(add_node_button)
        edit_node_hlayout.addWidget(delete_node_label)
        edit_node_hlayout.addWidget(self.node_number_textfield)
        edit_node_hlayout.addWidget(delete_node_button)
        
        # Create QLineEdit widgets for entering the edge source and destination
        add_edgesrc_label = QLabel('From:')
        add_edgesrc_label.setStyleSheet(s.label_style)
        add_edgedest_label = QLabel('To:')
        add_edgedest_label.setStyleSheet(s.label_style)
        add_edgeweight_label = QLabel('Weight:')
        add_edgeweight_label.setStyleSheet(s.label_style)
        self.add_edgesrc_textfield = QLineEdit()
        self.add_edgesrc_textfield.setStyleSheet(s.line_edit_style)
        self.add_edgedest_textfield = QLineEdit()
        self.add_edgedest_textfield.setStyleSheet(s.line_edit_style)
        self.add_edgeweight_textfield = QLineEdit()
        self.add_edgeweight_textfield.setStyleSheet(s.line_edit_style)

        # Create add edge button
        add_edge_label = QLabel('Add Edge:')
        add_edge_label.setStyleSheet(s.label_style)
        add_edge_button = QPushButton('+')
        add_edge_button.setStyleSheet(s.button_style2)
        add_edge_button.clicked.connect(self.add_edge_button_clicked)

        # Create QHBoxLayout for add edge buttons
        add_edge_hlayout = QHBoxLayout()
        add_edge_hlayout.addWidget(add_edge_label)
        add_edge_hlayout.addWidget(add_edgesrc_label)
        add_edge_hlayout.addWidget(self.add_edgesrc_textfield)
        add_edge_hlayout.addWidget(add_edgedest_label)
        add_edge_hlayout.addWidget(self.add_edgedest_textfield)
        add_edge_hlayout.addWidget(add_edgeweight_label)
        add_edge_hlayout.addWidget(self.add_edgeweight_textfield)
        add_edge_hlayout.addWidget(add_edge_button)

        # Create QLineEdit widgets for entering the edge source and destination
        del_edgesrc_label = QLabel('From:')
        del_edgesrc_label.setStyleSheet(s.label_style)
        del_edgedest_label = QLabel('To:')
        del_edgedest_label.setStyleSheet(s.label_style)
        self.del_edgesrc_textfield = QLineEdit()
        self.del_edgesrc_textfield.setStyleSheet(s.line_edit_style)
        self.del_edgedest_textfield = QLineEdit()
        self.del_edgedest_textfield.setStyleSheet(s.line_edit_style)

        # Create delete edge button
        del_edge_label = QLabel('Delete Edge:')
        del_edge_label.setStyleSheet(s.label_style)
        del_edge_button = QPushButton('-')
        del_edge_button.setStyleSheet(s.button_style3)
        del_edge_button.clicked.connect(self.del_edge_button_clicked)

        # Create QHBoxLayout for delete edge buttons
        del_edge_hlayout = QHBoxLayout()
        del_edge_hlayout.addWidget(del_edge_label)
        del_edge_hlayout.addWidget(del_edgesrc_label)
        del_edge_hlayout.addWidget(self.del_edgesrc_textfield)
        del_edge_hlayout.addWidget(del_edgedest_label)
        del_edge_hlayout.addWidget(self.del_edgedest_textfield)
        del_edge_hlayout.addWidget(del_edge_button)

        # Create radio button for algorithm options
        algo_label = QLabel('Algorithm:')
        algo_label.setStyleSheet(s.label_style)
        button_group = QButtonGroup()
        rad_button1 = QRadioButton('Prim')
        rad_button1.setStyleSheet(s.radio_button_style)
        rad_button2 = QRadioButton('Kruskal')
        rad_button2.setStyleSheet(s.radio_button_style)
        button_group.addButton(rad_button1)
        button_group.addButton(rad_button2)
        rad_button1.setChecked(True)
        rad_button1.clicked.connect(self.radio_button_clicked)
        rad_button2.clicked.connect(self.radio_button_clicked)

        # Create QHBoxLayout for algorithm radio buttons
        algo_hlayout = QHBoxLayout()
        algo_hlayout.addWidget(algo_label)
        algo_hlayout.addWidget(rad_button1)
        algo_hlayout.addWidget(rad_button2)

        # Create solve button
        self.solve_button = QPushButton('Solve')
        self.solve_button.setIcon(QIcon("asset/right-arrow.png"))
        self.solve_button.setStyleSheet(s.button_style4)
        self.solve_button.setMaximumWidth(400)
        if len(self.graph.nodes()) == 0:
            self.solve_button.setEnabled(False)            
        self.solve_button.clicked.connect(self.solve_button_clicked)

        # Create canvas for graph visualization
        self.figure = Figure(facecolor=s.canvas_face_color)
        self.canvas = FigureCanvas(self.figure)

        # Add widgets to layout
        stretchable_layout.addWidget(self.canvas)
        fixed_width_layout.addWidget(self.total_weight_label)
        fixed_width_layout.addWidget(self.total_weight_label)   
        fixed_width_layout.addLayout(file_visualize_hlayout)
        fixed_width_layout.addLayout(edit_node_hlayout)
        fixed_width_layout.addLayout(add_edge_hlayout)
        fixed_width_layout.addLayout(del_edge_hlayout)
        fixed_width_layout.addLayout(algo_hlayout)
        fixed_width_layout.addWidget(self.solve_button)
    
    def draw_graph(self, nc, ec):
        if len(self.graph.nodes()) != 0: 
            self.solve_button.setEnabled(True)
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        pos = nx.fruchterman_reingold_layout(self.graph, k=39)
        edge_labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx(self.graph, pos, with_labels=True, node_color=nc, edge_color=ec, font_weight='bold', ax=ax, font_color=s.node_font_color)
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels, ax=ax, 
                                     bbox=dict(facecolor=s.edge_label_face_color), font_color=s.edge_label_font_color)
        ax.set_axis_off()
        self.canvas.draw()

    def radio_button_clicked(self):
        '''handle radio button clicks'''
        self.algo_choice = self.sender().text()

    def file_button_clicked(self):
        '''handle file button clicks'''
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, 'Select File')
        if file_path:
            self.read_graph(file_path)
            if(self.adj_matrix != []):
                self.visualize_button.setEnabled(True)
            try:
                self.create_graph()
            except IndexError:
                self.show_error_message("Input format error")

    def visualize_button_clicked(self):
        '''handle visualize button clicks'''
        self.visualize_button.setEnabled(False)
        self.draw_graph(s.node_color1, s.edge_color1)
        self.visualize_button.setEnabled(True)

    def solve_button_clicked(self):
        '''handle solve button clicks'''
        self.solve_button.setEnabled(False)
        if self.algo_choice == 'Prim':
            mst_edges, total_weight = prim(self.graph)

        elif self.algo_choice == 'Kruskal':
            mst_edges, total_weight = kruskal(self.graph)

        edge_colors = [s.edge_color2 if edge in mst_edges else s.edge_color1 for edge in self.graph.edges()]
        self.draw_graph(s.node_color2, edge_colors)
        self.total_weight_label.setText('Total weight: ' + str(total_weight))
        self.solve_button.setEnabled(True)

    def add_node_button_clicked(self):
        '''handle add node button clicks'''
        try:
            self.graph.add_node(max(self.graph.nodes()) + 1)
        except ValueError:
            self.graph.add_node(0)
        self.draw_graph(s.node_color1, s.edge_color1)
    
    def delete_node_button_clicked(self):
        '''handle delete node button clicks'''
        try:
            node_number = int(self.node_number_textfield.text())
        except ValueError:
            self.show_error_message("Invalid input, please input an integer.")
            return
        try:
            self.graph.remove_node(node_number)
        except nx.NetworkXError as e:
            self.show_error_message('Node does not exist.')
        self.draw_graph(s.node_color1, s.edge_color1)

    def add_edge_button_clicked(self):
        '''handle add edge button clicks'''
        try:
            src = int(self.add_edgesrc_textfield.text())
            dest = int(self.add_edgedest_textfield.text())
            weight = int(self.add_edgeweight_textfield.text())
        except ValueError:
            self.show_error_message("Invalid input, please input an integer.")
            return
        self.graph.add_edge(src, dest, weight=weight)
        self.draw_graph(s.node_color1, s.edge_color1)
    
    def del_edge_button_clicked(self):
        '''handle delete edge button clicks'''
        try:
            src = int(self.del_edgesrc_textfield.text())
            dest = int(self.del_edgedest_textfield.text())
        except ValueError:
            self.show_error_message("Invalid input, please input an integer.")
            return
        try:
            self.graph.remove_edge(src, dest)
        except nx.NetworkXError:
            try:
                self.graph.remove_edge(dest, src)
            except nx.NetworkXError:
                self.show_error_message("Edge does not exist.")
        self.draw_graph(s.node_color1, s.edge_color1)

    def show_error_message(self, message):
        error_box = QMessageBox()
        error_box.setWindowTitle("Error")
        icon = QIcon("asset/error.png")
        error_box.setIconPixmap(icon.pixmap(32, 32)) 
        error_box.setText(message)
        error_box.setStyleSheet(s.error_style)
        error_box.exec_()

    def read_graph(self, file_path):
        self.adj_matrix = []
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    row = [int(weight) for weight in line.strip().split()]
                    self.adj_matrix.append(row)
        except IOError:
            self.show_error_message("Error reading file")
            return None
        except ValueError:
            self.show_error_message("Input format error")
            return None
        return self.adj_matrix

    def create_graph(self):
        self.graph = nx.Graph()
        num_nodes = len(self.adj_matrix)
        for i in range(num_nodes):
            for j in range(num_nodes):
                weight = self.adj_matrix[i][j]
                if weight > 0:
                    self.graph.add_edge(i, j, weight=weight)
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("asset/icon.png"))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

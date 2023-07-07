''' This file contains the style of the GUI. '''
node_color1 = '#414443'
node_color2 = '#4672F6'
node_font_color = '#FFFFFF'
edge_color1 = '#414443'
edge_color2 = '#4672F6'
edge_label_face_color = '#000000'
edge_label_font_color = '#FFFFFF'
canvas_face_color = '#000000'
cluster_colors = ['#4BA488', '#4672F6', '#D96C84', '#D9A06C', '#7E46F6', '#DD46F6']

bg_color = """QMainWindow{
  background-color: #000000;
}"""

button_style1 = """QPushButton{
  background-color: #4672F6;
  color: #FFFFFF;
  max-width: 300px;
  height: 30px;
  border-radius: 6px;
  font: inter;
}
QPushButton:disabled{
  background-color: #27314F;
  color: #9BA5C2;
}
QPushButton:hover{
  background-color: #3759C1;
  color: #FFFFFF;
}
"""

button_style2 = """QPushButton{
  background-color: #4BA488;
  color: #FFFFFF;
  width: 30px;
  height: 30px;
  border-radius: 15px;
  font: inter;
}
QPushButton:hover{
  background-color: #357D67;
  color: #FFFFFF;
}
"""

button_style3 = """QPushButton{
  background-color: #D96C84;
  color: #FFFFFF;
  width: 30px;
  height: 30px;
  border-radius: 15px;
  font: inter;
}
QPushButton:hover{
  background-color: #994A5B;
  color: #FFFFFF;
}
"""

button_style4 = """QPushButton{
  background-color: #4672F6;
  color: #FFFFFF;
  height: 30px;
  border-radius: 6px;
  font: inter;
}
QPushButton:disabled{
  background-color: #27314F;
  color: #9BA5C2;
}
QPushButton:hover{
  background-color: #3759C1;
  color: #FFFFFF;
}
"""

button_style5 = """QPushButton{
  background-color: #4BA488;
  color: #FFFFFF;
  height: 30px;
  width: 200px;
  border-radius: 6px;
  font: inter;
}
QPushButton:disabled{
  background-color: #265E4C;
  color: #9BA5C2;
}
QPushButton:hover{
  background-color: #357D67;
  color: #FFFFFF;
}
"""

label_style = """QLabel{
  background-color: #000000;
  color: #FFFFFF;
  font: inter;
}"""

line_edit_style = """QLineEdit{
  background-color: #1A1A1A;
  color: #FFFFFF;
  height: 30px;
  border-radius: 6px;
  font: inter;
}

QLineEdit:focus{
    background-color: #1A1A1A;
    color: #FFFFFF;
    border-radius: 6px;
    border: 1px solid #FFFFFF;
    font: inter;
}
QLineEdit:hover{
    background-color: #2E2E2E;
    color: #FFFFFF;
}
"""

error_style = """QMessageBox{
  background-color: #000000;
  color: #FFFFFF;
  font: inter;
}"""

radio_button_style = """QRadioButton{
  background-color: #000000;
  color: #FFFFFF;
  font: inter;
}
QRadioButton::hover{
  background-color: #000000;
  color: #C1C1C1;
}
"""

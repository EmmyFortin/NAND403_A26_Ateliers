import random
from maya import cmds
from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QLabel,
    QGridLayout
)

# CODE FOURNI PAR PROF
class RandomGenerator(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Atelier 4-5")
        self.setMinimumWidth(400)
        self.build_ui()
    
    def build_ui(self):
        layout = QVBoxLayout(self)

        # Mon code

        # Grid layout
        grid_layout = QGridLayout()

        # Labels
        # vertical horizontal

        # Coin supérieur gauche = 0 0
        grid_layout.addWidget(QLabel("Number of objects"),0,0)

        # Premiere colonne à droite
        grid_layout.addWidget(QLabel("Min"),1,1)

        # Deuxième colonne à droite
        grid_layout.addWidget(QLabel("Max"),1,2)

        # 2ieme rangé 
        grid_layout.addWidget(QLabel("Position X"),2,0)

        # 3ieme rangé
        grid_layout.addWidget(QLabel("Position Y"), 3,0)

        # 4ieme rangé 
        grid_layout.addWidget(QLabel("Position Z"),4,0)

        # 5ieme rangé 
        grid_layout.addWidget(QLabel("Scale"),5,0)

        # Inputs

        # Nombre objets
        self.number_objects_field = QLineEdit("20")
        grid_layout.addWidget(self.number_objects_field,0,1)

        # X Min et max
        self.min_x = QLineEdit("-10")
        self.max_x = QLineEdit("10")

        grid_layout.addWidget(self.min_x, 2, 1)
        grid_layout.addWidget(self.max_x, 2, 2)

        # Y Min et max
        self.min_y = QLineEdit("-10")
        self.max_y = QLineEdit("10")

        grid_layout.addWidget(self.min_y, 3, 1)
        grid_layout.addWidget(self.max_y, 3, 2)

        # Z Min et max
        self.min_z = QLineEdit("-10")
        self.max_z = QLineEdit("10")

        grid_layout.addWidget(self.min_z, 4, 1)
        grid_layout.addWidget(self.max_z, 4, 2)

        # Scale Min et max
        self.min_scale = QLineEdit("0.5")
        self.max_scale = QLineEdit("2")

        grid_layout.addWidget(self.min_scale, 5, 1)
        grid_layout.addWidget(self.max_scale, 5, 2)


        
        # Ajouter les layouts au layout principal

        layout.addLayout(grid_layout)
        
        
        
        
        
                
        
        # Mon code fin

        self.create_button = QPushButton("Create")
        self.create_button.clicked.connect(self.create_object)
        layout.addWidget(self.create_button)

    

    def create_object(self):
        forme = random.choice(["cube", "cylindre", "sphere"])

        if forme == "cube":
            objet = cmds.polyCube()[0]
        elif forme == "cylindre":
            objet = cmds.polyCylinder()[0]
        else:
            objet = cmds.polySphere()[0]

        random_value = random.uniform(-10, 10)
        cmds.move(random_value, random_value, random_value, objet)


def main():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = RandomGenerator()
    tool_window.show()

main()
# CODE FOURNI FIN
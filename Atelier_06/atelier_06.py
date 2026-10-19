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


class FenceGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fence Generator")
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
        grid_layout.addWidget(QLabel("Fence Length"),0,0)

        # Premiere colonne à droite
        grid_layout.addWidget(QLabel("X"),1,1)

        # Deuxième colonne à droite
        grid_layout.addWidget(QLabel("Y"),1,2)

        grid_layout.addWidget(QLabel("Z"),1,3)

        # 2ieme rangé 
        grid_layout.addWidget(QLabel("Position"),2,0)

        # 5ieme rangé 
        grid_layout.addWidget(QLabel("Scale"),5,0)

        # Inputs

        # Nombre objets
        self.number_objects_field = QLineEdit("20")
        grid_layout.addWidget(self.number_objects_field,0,1)

        # X Min et max
        self.position_x = QLineEdit("0")


        grid_layout.addWidget(self.position_x, 2, 1)


        # Y Min et max
        self.position_y = QLineEdit("0")


        grid_layout.addWidget(self.position_y, 2, 2)

        # Z Min et max
        self.position_z = QLineEdit("0")

        grid_layout.addWidget(self.position_z, 2, 3)

        # Scale Min et max
        self.x_scale = QLineEdit("0.5")
        self.y_scale = QLineEdit("2")
        self.z_scale = QLineEdit("2")

        grid_layout.addWidget(self.x_scale, 5, 1)
        grid_layout.addWidget(self.y_scale, 5, 2)
        grid_layout.addWidget(self.z_scale, 5, 3)

        # Ajouter les layouts au layout principal
        layout.addLayout(grid_layout)
        
        # Mon code fin

        self.create_button = QPushButton("Create")
        self.create_button.clicked.connect(self.create_object)
        layout.addWidget(self.create_button)

    def create_object(self):
    
            # MON CODE
    
            # Récupere nombre d'objet
            number_objects = int(self.number_objects_field.text())
    
            # Récupère les valeurs des positions
            x_value = float(self.position_x.text())

    
            y_value = float(self.position_y.text())

    
            z_value = float(self.position_z.text())
    
            # Récupère scale
            x_scale_value = float(self.x_scale.text())
            y_scale_value = float(self.y_scale.text())
            z_scale_value = float(self.z_scale.text())
    
    
            # Boucle pour créer les objets selon le nombre rentré
            for elements in range(number_objects):
    
            # MON CODE FIN
    
                # forme = random.choice(["cube", "cylindre", "sphere"])
    
                # if forme == "cube":
                #     objet = cmds.polyCube()[0]
                # elif forme == "cylindre":
                #     objet = cmds.polyCylinder()[0]
                # else:
                #     objet = cmds.polySphere()[0]

                #forme = fence

                objet_vertical = cmds.polyCube()[0]

                objet_horizontal = cmds.polyCube()[0]
    
                cmds.move(self.position_x, self.position_y, self.position_z, objet_vertical)
    
                #random_scale = random.uniform(min_scale_value, max_scale_value)
    
                cmds.scale(x_scale_value, y_scale_value, z_scale_value, objet_vertical)
                # MON CODE FIN
    
                # random_value = random.uniform(-10, 10)




def main():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = FenceGenerator()
    tool_window.show()

main()
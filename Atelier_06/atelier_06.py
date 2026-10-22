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

        # Général 
        grid_layout.addWidget(QLabel("Number of fences"),0,0)

        # Position
        # Premiere colonne à droite
        grid_layout.addWidget(QLabel("X"),2,1)

        # Deuxième colonne à droite
        grid_layout.addWidget(QLabel("Y"),2,2)

        grid_layout.addWidget(QLabel("Z"),2,3)

        # 2ieme rangé 
        grid_layout.addWidget(QLabel("Position"),3,0)


        # Dimension poteau vertical
        # 5ieme rangé 
        grid_layout.addWidget(QLabel("Vertical Fence Post Dimensions"),6,0)

        grid_layout.addWidget(QLabel("Width"),5,1)

        # Deuxième colonne à droite
        grid_layout.addWidget(QLabel("Height"),5,2)

        grid_layout.addWidget(QLabel("Depth"),5,3)

        grid_layout.addWidget(QLabel("Horizontal Fence Post Dimensions"),7,0)

        grid_layout.addWidget(QLabel("Space Between Horizontal Posts"),8,0)

        grid_layout.addWidget(QLabel("Horizontal Fence Post Position Y"),9,0)

        # Inputs

        # Nombre objets
        self.number_objects_field = QLineEdit("1")
        grid_layout.addWidget(self.number_objects_field,0,1)

        # X Min et max
        self.position_x = QLineEdit("0")
        grid_layout.addWidget(self.position_x, 3, 1)

        # Y Min et max
        self.position_y = QLineEdit("0")


        grid_layout.addWidget(self.position_y, 3, 2)

        # Z Min et max
        self.position_z = QLineEdit("0")

        grid_layout.addWidget(self.position_z, 3, 3)

        # Scale Min et max
        self.x_scale = QLineEdit("0.5")
        self.y_scale = QLineEdit("2")
        self.z_scale = QLineEdit("0.5")

        grid_layout.addWidget(self.x_scale, 6, 1)
        grid_layout.addWidget(self.y_scale, 6, 2)
        grid_layout.addWidget(self.z_scale, 6, 3)

        self.x_scale_horizontal = QLineEdit("4")
        self.y_scale_horizontal = QLineEdit("0.5")
        self.z_scale_horizontal = QLineEdit("0.2")

        grid_layout.addWidget(self.x_scale_horizontal, 7, 1)
        grid_layout.addWidget(self.y_scale_horizontal, 7, 2)
        grid_layout.addWidget(self.z_scale_horizontal, 7, 3)

        # Distance between horizontal post fences
        self.distance_between_horizontal_fences_post_field = QLineEdit("0.5")
        grid_layout.addWidget(self.distance_between_horizontal_fences_post_field,8,1)

        self.position_y_horizontal_fences_post = QLineEdit("1")
        grid_layout.addWidget(self.position_y_horizontal_fences_post, 9, 1)

        # Ajouter les layouts au layout principal
        layout.addLayout(grid_layout)
        
        # Mon code fin

        self.create_button = QPushButton("Create")
        self.create_button.clicked.connect(self.create_object)
        layout.addWidget(self.create_button)

    def create_object(self):
    
        # Récupere nombre d'objet
        number_objects = int(self.number_objects_field.text())

        if number_objects < 1:
            return

        # Récupère les valeurs des positions
        x_value = float(self.position_x.text())
        y_value = float(self.position_y.text())
        z_value = float(self.position_z.text())

        # Scale poteaux verticaux
        x_scale_value = float(self.x_scale.text())
        y_scale_value = float(self.y_scale.text())
        z_scale_value = float(self.z_scale.text())

        # Scale poteaux horizontaux
        x_scale_value_horizontal = float(self.x_scale_horizontal.text())
        y_scale_value_horizontal = float(self.y_scale_horizontal.text())
        z_scale_value_horizontal = float(self.z_scale_horizontal.text())
           
        # Calcul espacement entre les poteaux horizontaux
        distance_horizontal = float(self.distance_between_horizontal_fences_post_field.text())
        
        # Espacement égal en haut et en bas
        espacement = (y_scale_value - (2* y_scale_value_horizontal) - distance_horizontal)/2
        
        # position premier poteau horizontal (en bas)
        y_horizontal_p = (y_value +  espacement + y_scale_value_horizontal/2)
        
        # position deuxieme poteau horizontal (en haut)
        y_horizontal_p2 = (y_horizontal_p + y_scale_value_horizontal + distance_horizontal)

        # Distance entre les centres des poteaux verticaux
        fence_length = (x_scale_value_horizontal + x_scale_value)
        
        y_value_horizontal = float(self.position_y_horizontal_fences_post.text())

        # Groupe de cloture
        fence_group = cmds.group(empty = True, name = "GRP_Fence")

        # Boucle pour créer les objets selon le nombre rentré
        for elements in range(number_objects):

            # Position en x de la cloture actuelle
            x_position_actuelle = (x_value + elements * fence_length)

            # Premier poteau vertical
            objet_vertical = cmds.polyCube(name = "Vertical_Post_01")[0]

            # Applique la scale
            cmds.scale(x_scale_value, y_scale_value, z_scale_value, objet_vertical)

            # Placer pivot du poteau vertical à un coin inférieur 
            cmds.xform(
                objet_vertical,
                pivots=(0, -0.5, 0),
                objectSpace=True
            )

            # Move
            cmds.move(x_position_actuelle, y_value, z_value, objet_vertical, absolute=True, worldSpace=True, rotatePivotRelative=True)

            # Position des poteaux horizontaux
            x_horizontal = (x_position_actuelle + x_scale_value / 2 + x_scale_value_horizontal / 2)

            # Poteau horizontal
            objet_horizontal = cmds.polyCube(name = "Horizontal_Post_01")[0]
            
            # Applique la scale
            cmds.scale(x_scale_value_horizontal, y_scale_value_horizontal, z_scale_value_horizontal, objet_horizontal)

            # Move
            cmds.move(x_horizontal, y_horizontal_p, z_value, objet_horizontal, absolute=True, worldSpace=True)

            # Poteau horizontal 2
            objet_horizontal_2 = cmds.polyCube(name = "Horizontal_Post_02")[0]
            
            # Applique la scale
            cmds.scale(x_scale_value_horizontal, y_scale_value_horizontal, z_scale_value_horizontal, objet_horizontal_2)

            # Move
            cmds.move(x_horizontal, y_horizontal_p2, z_value, objet_horizontal_2, absolute=True, worldSpace=True)

            cmds.parent(
                objet_vertical,
                objet_horizontal,
                objet_horizontal_2,
                objet_vertical_2,
                fence_group
            )

        # Objet vertical 2
        objet_vertical_2 = cmds.polyCube(name = "Vertical_Post_02")[0]

        # Applique la scale
        cmds.scale(x_scale_value, y_scale_value, z_scale_value, objet_vertical_2)
        
        # Placer pivot du poteau vertical à un coin inférieur 
        cmds.xform(
            objet_vertical_2,
            pivots=(0, -0.5, 0),
            objectSpace=True
        )
        
        # Move
        cmds.move(x_value + number_objects * fence_length, y_value, z_value, objet_vertical_2, absolute=True, worldSpace=True, rotatePivotRelative=True)


def main():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = FenceGenerator()
    tool_window.show()

main()
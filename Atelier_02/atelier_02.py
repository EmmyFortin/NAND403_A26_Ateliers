import sys
import json

from PySide6.QtCore import QMargins, Qt, QFileInfo
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QMessageBox,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QLineEdit,
)





        # Donne un nom à mon objet MainWindow
    



      
json_file = sys.argv[1]
print(json_file)

try: 
    # Chargement des données du fichier .json reçu en paramètre
    file = open(json_file)
    data = json.load(file)
    print(type(data))
except:
    print(f"Could not load data from {json_file}")
     
for i in data:
    for k in i.values():
        print(f"     - {k}")



# Début de l'application
# Fonction main qui démarre l'application



# app = QApplication(sys.argv)

# window = MainWindow()

#     # Affichage de ma fenêtre principale car elle est cachée par défaut.
# window.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()
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
          
json_file = sys.argv[1]
print(json_file)

try: 
    # Chargement des données du fichier .json reçu en paramètre

    file = open(json_file)
    data = json.load(file)
    print(type(data))
except Exception as error:
    print(f"Could not load data from {json_file}")

     
for i in data:
    print("Keys\n")
    for k in i.keys():
        print(f"        - {k}")



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
          



# Création de la fenêtre qui va contenir la grille

class MainWindow(QMainWindow):


    def __init__(self):
        super().__init__()

        self.setWindowTitle("Menu Drinks")

        # Appelle la fonction qui crée le tableau
        self.create_spreadsheet()

    def create_spreadsheet(self):

        # Crée le tableau dans MainWindow
        self.my_spreadsheet = QTableWidget()

        # Création du layout pour placer le tableau dans le centre de la fenêtre
        layout = QVBoxLayout()
        layout.addWidget(self.my_spreadsheet)

        # Widget parent
        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

        # Appelle la fonction qui load les data
        self.load_data()

    def load_data(self):
        json_file = sys.argv[1]

        try: 
            # Chargement des données du fichier .json reçu en paramètre

            file = open(json_file)
            data = json.load(file)

        except Exception as error:
            print(f"Could not load data from {json_file}")


        # Liste des propriétés des objets
        column_names = []

        # Boucle qui parcout tout les objets dans data et qui fait une autre boucle pour trouver toute les propriété des objets (keys)
        for object in data:
            for property in object.keys():
                if property not in column_names:
                    column_names.append(property)
                else: 
                    break

        # Appelle la fonction pour remplir le tableau avec la valeur des objets et le nom des colonnes
        self.fill_spreadsheet(data, column_names)

    def fill_spreadsheet(self, data, column_names):

        # Donne le nombre de rangées pour la quantité d'objet
        self.my_spreadsheet.setRowCount(len(data))

        # Donne le nombre de colonnes par rapport au nombre de colonnes
        self.my_spreadsheet.setColumnCount(len(column_names))

        # Affiche le noms des colonnes dans le tableau
        self.my_spreadsheet.setHorizontalHeaderLabels(column_names)


        # Afficher les données dans le tableau
        for row in range((len(data))):
            for column in range((len(column_names))):
                cell_value = data[row][column_names[column]]
                spreadsheet_item = QTableWidgetItem(str(cell_value))

                self.my_spreadsheet.setItem(
                    row,
                    column,
                    spreadsheet_item
                )


def main(): 

    # Création de l'application en passant en paramètres les arguments
    app = QApplication(sys.argv)

    # Création de ma fenêtre principale et appel de son constructeur
    window = MainWindow()

    # Afficher la fenêtre principale car elle est caché par défaut
    window.show()

    # Boucle d'exécution de l'app
    sys.exit(app.exec())


# Vérification de si le fichier est en standalone
if __name__ == "__main__":
    main()



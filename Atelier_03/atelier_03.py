from PySide6.QtWidgets import QWidget,QLabel,QVBoxLayout, QTextEdit, QPushButton
 
class MessageBoard(QWidget):
    def __init__(self):  # Constructeur
        super().__init__() # Constructeur QWidget (Parent)
        self.setWindowTitle("Message board")
        self.create_ui()

    def create_ui(self):
        print("create UI")
        layout = QVBoxLayout(self)
        label = QLabel("Message Board")
        layout.addWidget(label)

        #QEditTexte
        #QPushButton

    def on_click(self):
        print("on click call")
        #QMessageBox


        
 
def main():
    global widget
    try:
        widget.close()
    except Exception:
        pass
    widget = MessageBoard()
    widget.show()
 
main()


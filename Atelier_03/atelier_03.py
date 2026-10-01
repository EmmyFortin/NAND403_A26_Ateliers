from PySide6.QtWidgets import QWidget,QLabel,QVBoxLayout, QTextEdit, QPushButton, QMessageBox
 
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

        global text_box
        text_box = QTextEdit(self)
        layout.addWidget(text_box)

        button_send = QPushButton("Send", self)
        layout.addWidget(button_send)
        button_send.clicked.connect(self.on_click)
  

    def on_click(self):
        print("on click call")
        message_box = QMessageBox.information(self, "Alerte", text_box.toPlainText() )
        
        


        
 
def main():
    global widget
    try:
        widget.close()
    except Exception:
        pass
    widget = MessageBoard()
    widget.show()
 
main()


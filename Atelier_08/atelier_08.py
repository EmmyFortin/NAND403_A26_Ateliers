from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QLabel,
    QGridLayout,
    QTextEdit,
    QMessageBox
)

class RandomAnim(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Atelier 08")
        self.setMinimumWidth(400)
        self.create_ui()

    def create_ui(self):
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


    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = RandomAnim()
    tool_window.show()

main()
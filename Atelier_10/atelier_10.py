import random
from maya import cmds
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QFormLayout,
    QSpinBox,
    QDoubleSpinBox,
    QPushButton,
    QMessageBox
)


from PySide6.QtCore import Qt
import maya.OpenMayaUI as omui
from shiboken6 import wrapInstance

# Pour que la fenêtre du tool always on top
def maya_main_window():
    pointer = omui.MQtUtil.mainWindow()
    return wrapInstance(int(pointer), QWidget)


class Scatter(QWidget):

    def __init__(self):
        super().__init__(maya_main_window())
        self.setWindowFlags(Qt.Window)
        self.source = None

        self.setWindowTitle("Scatter")
        self.setMinimumWidth(250)
        self.build_ui()

    def build_ui(self):
        self.layout = QVBoxLayout(self)
        self.form = QFormLayout()
        self.layout.addLayout(self.form)
        self.create_spinboxes()

    def create_spinboxes(self):

        self.count_spin = QSpinBox()
        self.count_spin.setRange(1, 100)
        self.count_spin.setValue(10)
        self.form.addRow("Copies", self.count_spin)

        self.radius_spin = QDoubleSpinBox()
        self.radius_spin.setRange(1.0, 50.0)
        self.radius_spin.setValue(10.0)
        self.form.addRow("Radius", self.radius_spin)

        self.seed_spin = QSpinBox()
        self.seed_spin.setRange(0, 9999)
        self.form.addRow("Seed", self.seed_spin)

        # Pour update live
        self.count_spin.valueChanged.connect(self.scatter)
        self.radius_spin.valueChanged.connect(self.scatter)
        self.seed_spin.valueChanged.connect(self.scatter)

    def scatter(self):
        # Récupérer une fois car sinon crash
        if self.source is None:
            selection = cmds.ls(selection=True, transforms=True)

            if not selection:
                QMessageBox.warning(self, "Scatter", "Select an object first.")
                return
            self.source = selection[0]

        cmds.undoInfo(openChunk=True)
        try:
            random.seed(self.seed_spin.value())
            radius = self.radius_spin.value()

            # Pour ne pas créer un deuxième groupe à chaque fois que la valeur est changée
            if cmds.objExists("scatter_grp"):
                cmds.delete("scatter_grp")
            group = cmds.group(empty=True, name="scatter_grp")

            for i in range(self.count_spin.value()):
                copy = cmds.duplicate(self.source)[0]
                copy = cmds.parent(copy, group)[0]
                x = random.uniform(-radius, radius)
                z = random.uniform(-radius, radius)
                cmds.move(x, 0, z, copy, relative=True)

            # Pour garder la selection
            cmds.select(self.source, replace=True)
        finally:
            cmds.undoInfo(closeChunk=True)



def show_tool():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = Scatter()
    tool_window.show()

show_tool()

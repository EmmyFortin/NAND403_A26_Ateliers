import os
import sys

absolute_file_path = os.path.abspath(__file__)
absolute_folder_path = os.path.dirname(absolute_file_path)
print(absolute_folder_path)

# Ici on vient ajouter absolute_folder_path au path de python pour qu'il puisse trouver ui_atelier.py
sys.path.append(absolute_folder_path)

# refresh des fichiers
import importlib

import ui_atelier

# Version sans double import
importlib.reload(ui_atelier)
# si sa fonctionne pas mettre comme ca dans variable MyClass = importlib.reload(ui_atelier).RandomAnim et juste besoin de call la variable (ligne 33)
# Version double import
#from ui_atelier import RandomAnim



def main():
    absolute_path = os.path.abspath(os.path.curdir)
    print(absolute_path)

    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = ui_atelier.RandomAnim()
    tool_window.show()

main()



import random
from maya import cmds

class CreateAnimation () :
    # Création cube
    objet = cmds.polyCube()[0]

    cmds.scale(5, 5, 5, objet)

    # Ajout premier Keyframe 
    cmds.setKeyframe(objet, attribute= "translateX", value=0, time=0)
    cmds.setKeyframe(objet, attribute= "translateX", value=50, time=25)
    cmds.setKeyframe(objet, attribute= "translateX", value=100, time=50)
    cmds.setKeyframe(objet, attribute= "translateX", value=150, time=100)

    # Plage d'animation
    cmds.playbackOptions(min=0, max=100)
    
    # Durée
    cmds.currentTime(0)

    # Joue anim
    cmds.play(forward = True)


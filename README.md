# Layer View Set

layerviewset.py

A gui for saving, loading view sets as well as interacting with a stack of view sets for changing which layers are viewed within KiCad.

**Because of a bug in KiCad, you must currently switch views from and back
to OpenGL to see the effect of layerviewset on the layers.**


## INSTALLATION

LayerViewSet is a ActionPlugin and is installed similarly to other Action Plugins:
1) Place the layerviewset.py and layerviewset_gui.py files in 
C:\Program Files\KiCad\share\kicad\scripting\plugins
Or the equivalent in MacOS or Linux
(*there may be a user-level directory for such files, but I am not aware of it at the moment.*)
2) Within KiCad pcbnew, select the Tools > External Plugins > Refresh Plugins

LayerViewSet dialog box is shown when the Tools > External Plugins > LayerViewSet menu item is selected.


## USE

Selecting the menu item brings up the window allowing you to control
a *View Set* Stack. You can push to the top of the stack one of three sets:
1) **Layers** - only pushes Layers onto the stack
2) **-v-** - pushes both Layers and Renders onto the stack
3) **Renders** - only pushes Renders onto the stack

Popping the stack (**^**) pulls the top item on the stack and sets the corresponding
check boxes, affecting either the Layers, Renders, or both depending on what
button was used to push that *View Set* onto the stack.

You can also select any item on the stack directly. This will set the visibility
as appropriate, but not change the stack at all.

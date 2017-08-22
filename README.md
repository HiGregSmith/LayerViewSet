# Layer View Set

**layerviewset.py** and **layerviewset_gui.py**

*[Please report any bugs found](https://github.com/HiGregSmith/LayerViewSet/issues)*

A gui for saving and loading ViewSets and interacting
with a stack of ViewSets for quickly changing the currently visible
layers and renders within KiCad.

**Because of a [bug in KiCad](https://bugs.launchpad.net/kicad/+bug/1712233), you must currently switch views from and back
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

Selecting the menu item brings up the window allowing you to control a
*Named ViewSet List* on the left and a *ViewSet Stack* on the right. 
The buttons at the top allow you to control the stack. While right clicking
for the context menu on a button allow you to name view sets and delete them.

Within the *Layer Manager*, the *layers* are listed in the *Layer* tab and
the *renders* are listed in the *Render* tab. **LayerViewSet** allows you to
save either or both of these lists in memory (on the *ViewSet Stack*) or on disk
(on the *Named ViewSet List*). Both the stack and the list are available
in their entirety to load any of the *ViewSets* into the *Layer Manager*, affecting
the visibility of the currently viewed PCB.

### ViewSet Stack
You can push the currently visible layers and or renders to the top of the 
stack as one of three types of *ViewSet*:
1) **Layers** - only pushes Layers onto the stack. When popped or selected, only the layers' visibilities are modified.
2) **-v-** - pushes both Layers and Renders onto the stack.  When popped or selected, both the renders' and the layers' visibilities are modified.
3) **Renders** - only pushes Renders onto the stack. When popped or selected, only the renders' visibilities are modified.

Each type of *ViewSet* appears on the stack with a slightly different label.
When view sets are pushed onto the stack, they get the label "[number of layers]/[number of renders]".

Here is a little guide on the stack label format:
- 3/5 - 3 layers are visible and 5 renders are visible
- 2/  - 2 layers are visible and renders will be unchanged
- /4  - layers will be unchanged and 4 renders are visible
- 0/3 - 0 layers are visible and 3 renders are visible

Note the subtle distinction between "/4" and "0/3".

Popping the stack (**--^--**) pulls the top item from the stack and
sets the corresponding check boxes, affecting either the
Layers, Renders, or both depending on the type of *ViewSet*.

You can also select any item on the stack directly. This will set the visibility
as appropriate, but not change the stack at all.

### Named / Saved ViewSet

All Named ViewSets are persisted in *~/kicad/viewsets*. And none of the stack
ViewSets are persisted. For this reason, there is not a separate
"load" or "save" button or menu item.

Right clicking any button brings up the option to either "Name" or "Delete" the
ViewSet. If you name a set on the stack, it is added to the list on the left
and persists between KiCad runs (in ~/kicad/viewsets).
If you name an already named stack, it is renamed.

### Deleting a ViewSet
Deleting a view set removes it from the list or stack and deletes the
persistent file, if any.

## Example of use

Because the expected interaction with this control is low, there is not a
need to complicate the user interface. The actions have been chosen
carefully to allow full flexibility with a minimum of available actions.
Here is an example of how you would save the currently visible layers to disk:

- Select the "Layers" button to push the current layer visibility on the stack.
- Right click on the new button at the top of the stack.
- Select "Name" to save the named view set.
- Right click on the top of the stack again and
- Select "Delete" to remove the view set from the stack.
- The view set remains on the named list and will persist to future
runs of KiCad.

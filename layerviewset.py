# Layer View Set.py
#
# A gui for saving, loading view sets as well as interacting with a stack
# of view sets for changing which layers are viewed within KiCad.

import time
import pcbnew
import wx
import layerviewset_gui

#######
## GUI Definition
#######

class gui (layerviewset_gui.layerviewset_frame):
    """Inherits from the layerviewset_gui form wxFormBuilder. Supplies
       functions that tie the gui to the layerviewset class below."""
    _lvset_instance = None
    def __init__(self, lvset_instance, parent_frame,
        *args, **kw):
        self._lvset_instance = lvset_instance
        super(gui,self).__init__(parent_frame, *args, **kw)

    def load(self,e):
        wx.MessageDialog(self,"load Not Implemented",style=wx.OK).ShowModal()
        return
        openFileDialog = wx.FileDialog(self, "Open DRU File", "", "", 
                              "DRU File (*.dru)|*.dru|All Files|*.*", 
                               wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
 
        openFileDialog.ShowModal()
        textcontrol = self.FindWindowByName('filetabtext')
        filetoload = openFileDialog.GetPath()
        openFileDialog.Destroy()
        textcontrol.AppendText("%s\n\n\n"%filetoload)
        with open(filetoload) as f:
            for line in f:
                textcontrol.AppendText("%s"%line)

    def save(self,e):
        wx.MessageDialog(self,"save Not Implemented",style=wx.OK).ShowModal()
    def loadset(self,e):
        self._lvset_instance.loadset(e)
        #wx.MessageDialog(self,"loadset Not Implemented "+str(e),style=wx.OK).ShowModal()
    def push(self,e):
        self._lvset_instance.push()
        
    def pop(self,e):
        self._lvset_instance.pop()
#######
## End GUI Definition
#######

# Not sure how to enable Action Script without creating a class that
# inherits from ActionPlugin class

class layerviewset(pcbnew.ActionPlugin):
    """The main class for layerview set, supplies the functions for a creating,
       loading, and saving viewsets, instantiates the gui, and creates the
       stack of viewsets displayed in the gui."""
    _lvset_frame = None
    """The top level frame of the layerviewset gui instantiation."""
    _linkparent = None
    """The window containing the stack elements."""
    _message = None
    """The control containing a message (error, information, etc)."""
    

    #######
    ## ActionPlugin
    #######
    def defaults( self ):
        """Support for ActionPlugins, though it doesn't work in 4.0.6 nightly and later"""
        self.name = "Layer ViewSet"
        self.category = "Layers"
        self.description = "Save and restore layer view settings."
        
    def Run(self):
        """Necessary for ActionPlugin, shows the gui and sets up some class
        variables for use within the functions."""
        # Instantiate and Show the gui, giving it
        # the current instance (for calling functions) and
        # the parent frame (Pcbnew)
        
        # Find the main "Pcbnew" wx window.
        _pcbnew_frame = \
            filter(lambda w: w.GetTitle().startswith('Pcbnew'), 
                   wx.GetTopLevelWindows()
            )[0]

        self._lvset_frame=gui(self,_pcbnew_frame)        
        self._lvset_frame.Show()
        
        # Set the class variable for the window that will contain the stack.
        self._linkparent = self._lvset_frame.FindWindowByName('linkwindow')
        self._message = self._lvset_frame.FindWindowByName('message_label')
        self._message.SetLabel("Click on any label:")
        # Destroy sample links
        self._linkparent.DestroyChildren()
        
        # Set the layersetstack first item to the current visible layers.
        self._lvset_frame.push(None)
    #######
    ## End ActionPlugin
    #######


    # _layersetstack elements are tuples (LSET *,widget,name)
    _layersetstack = []
    _count = 1
    
    def loadset(self,e):
        """Load a viewset based on the object (e) clicked."""
        # The widget is the object that was clicked.
        widget = e.GetEventObject()
        
        # Find that widget in the layersetstack.
        element = filter (lambda x: x[1],self._layersetstack)[0]
        
        # The the visible layers according to that element in the stack.
        pcbnew.GetBoard().SetVisibleLayers(element[0])
    
    def push(self):
        """Push the current view set onto the stack, create the text widget,
           and add the widget to the display."""
        board = pcbnew.GetBoard()
        
        # Nested list comprehensions to retrieve the names of the currently
        # visible layers.
        names = ','.join([
            board.GetLayerName(num) for num in 
            [x for x in board.GetVisibleLayers().Seq()]])
        
        # Create the staticText widget in the stack, that when clicked will
        # set the visible layers to that element.
        
        widget = wx.StaticText(
            self._linkparent,
            wx.ID_ANY,
            names,
            wx.DefaultPosition,
            wx.DefaultSize,
            0 )
        widget.Wrap( -1 )
        widget.Bind( wx.EVT_LEFT_UP, self._lvset_frame.loadset )

        self._count += 1
        element = (pcbnew.GetBoard().GetVisibleLayers(),widget)
        self._layersetstack.append(element)
        
        # Insert this widget as the first element on the stack,
        # i.e. the top of the list.        
        self._linkparent.GetSizer().Insert(0,widget,0,wx.ALL,5)

        # Try a whole bunch of things to get the wxWindow to refresh.
        self._linkparent.Layout()
        self._linkparent.Refresh()

        
    def pop(self):
        """Pop the top of the layersetstack and set the visible layers to
           those indicated in the element popped."""
           
        # Only do this if there are elements within the layersetstack.
        if len(self._layersetstack) > 0:
            # pop the element
            element = self._layersetstack.pop()
            
            # Set the layers
            pcbnew.GetBoard().SetVisibleLayers(element[0])
            
            # Try a few things to get the window to refresh.
            # Perhaps the only thing necessary here is "Destroy"
            p = element[1].GetParent()
            p.GetSizer().Remove(0)
            element[1].Destroy()
            p.GetSizer().Layout()
            p.Refresh()
            p.Parent().Layout()
            p.Parent().Refresh()
            self._linkparent.Layout()
            self._linkparent.Refresh()


# Instantiate and register the ActionPlugin class when imported.
_lvset = layerviewset()
_lvset.register()
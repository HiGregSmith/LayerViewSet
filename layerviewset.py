# Layer View Set.py
#
# A gui for saving, loading view sets as well as interacting with a stack
# of view sets for changing which layers are viewed within KiCad.
#
# Because of a bug in KiCad, you must currently switch views from and back
# to OpenGL to see the effect of layerviewset on the checkboxes and layers.
#
#
# INSTALLATION
#
# LayerViewSet is a ActionPlugin and is installed similar to other Action Plugins.
# Place the layerviewset.py file in 
# C:\Program Files\KiCad\share\kicad\scripting\plugins
# Or the equivalent in MacOS or Linux
# (there may be a user-level directory for such files, but I am not aware of it at the moment.)
# Within KiCad pcbnew, select the Tools > External Plugins > Refresh Plugins
#
# LayerViewSet dialog box is shown when the LayerViewSet menu item is selected.
# 

import time
import pcbnew
import wx
import wx.aui
import layerviewset_gui


#######
## GUI Definition
#######

class gui (layerviewset_gui.layerviewset_panel2):
    """Inherits from the layerviewset_gui form wxFormBuilder. Supplies
       functions that tie the gui to the layerviewset class below."""
    _lvset_instance = None
    interior_panel = None
    def __init__(self, lvset_instance, parent_frame,
        *args, **kw):
        self._lvset_instance = lvset_instance
        super(gui,self).__init__(parent_frame)#, *args, **kw)
        #self.makedock(self.GetChildren()[1])#.interior_panel)
        

    def makedock(self,panel=None):
        managed_window,manager = get_parent_panel()
        print panel
        if panel is not None:
            panel = wx.Panel( managed_window, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
        panel.Reparent(managed_window)
        manager.AddPane( panel, wx.aui.AuiPaneInfo() .Center() .Caption( u"ViewSet" ).PinButton( True ).Float().FloatingPosition( wx.Point( 346,268 ) ).Resizable().FloatingSize( wx.Size( 60,300 ) ).Layer( 0 ) )    
        panel.Show()
        panel.Enable()
        panel.Raise()
        manager.Update()


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
        self._lvset_instance.loadset()
        #wx.MessageDialog(self,"loadset Not Implemented "+str(e),style=wx.OK).ShowModal()
    def push(self,e):
        self._lvset_instance.push()
    def pushlayers(self,e):
        self._lvset_instance.pushlayers()
    def pushrenders(self,e):
        self._lvset_instance.pushrenders()
        
    def pop(self,e):
        self._lvset_instance.pop()
    def dock(self,e):
        return
        
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
        self.description = "Save and restore view settings for layers and renders."

        
    #######
    ## Application Specific KiCad window manipulation
    #######
    def GetLayerManager(self):
        """Find the layer_manager panel and its AUI manager"""
        # find the top-level auimanager
        win = wx.FindWindowByLabel('F.Cu')
        am = [wx.aui.AuiManager.GetManager(win)]
        # an attempt to get the AuiManager from one of the parents.
        # (an earlier test showed maybe 2-3 different AuiManagers among the ancestors)
        # The dock doesn't seem to work regardless of which AuiManagers.
        # It does appear to dock, but the LayerManager tabs don't move out
        # of the way to reveal the new window behind them (when I manually dock).
        while True:
            win=win.GetParent()
            newam = wx.aui.AuiManager.GetManager(win)
            if str(am[-1]) != str(newam):
                am.append(newam)
                if len(am) >= 2: # This sets how many generations of different managers to go back
                    break
        managed_window = am[-1].GetManagedWindow()
        return managed_window,am[-1]
        
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

        parent, manager = self.GetLayerManager()
        self._lvset_frame=gui(self,parent)        
        self._lvset_frame.Show()
        
        manager.AddPane( self._lvset_frame, wx.aui.AuiPaneInfo().Caption( u"ViewSet" ) .Center().Float().FloatingPosition( wx.Point( 346,268 ) ).Resizable().FloatingSize( wx.Size( 60,300 ) ).Layer( 0 ) )
        #  .Caption( u"ViewSet" )
        manager.Update()
        
        #wx.aui.AuiManager.GetManager(self._lvset_frame).Update()
        
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


    # _layersetstack elements are tuples (layer LSET *,render int *,widget,name)
    _layersetstack = []
    _count = 1
    
    def loadset(self,e):
        """Load a viewset based on the object (e) clicked."""
        # The widget is the object that was clicked.
        widget = e.GetEventObject()
        
        # Find that widget in the layersetstack.
        element = filter (lambda x: x[2],self._layersetstack)[0]
        
        # The the visible layers according to that element in the stack.        
        if element[0] is not None:
            pcbnew.GetBoard().SetVisibleLayers(element[0])
        if element[1] is not None:
            pcbnew.GetBoard().SetVisibleElements(element[1])
        self._message.SetLabel("Change Canvas to view")


    def push(self):
        self._push(pcbnew.GetBoard().GetVisibleLayers(),pcbnew.GetBoard().GetVisibleElements())
    
    def pushlayers(self):
        self._push(pcbnew.GetBoard().GetVisibleLayers(),None)
    
    def pushrenders(self):
        self._push(None,pcbnew.GetBoard().GetVisibleElements())
    
    def _push(self,layers,renders):
        """Push the current view set onto the stack, create the text widget,
           and add the widget to the display."""
        board = pcbnew.GetBoard()
        layercb,rendercb = self.GetCheckboxes()
        
        # Nested list comprehensions to retrieve the names of the currently
        # visible layers.
        if layers is not None:
            names = ', '.join([
                board.GetLayerName(num) for num in 
                [x for x in layers.Seq()]])
        else:
            names = ''
        if renders is not None:
            if layers is not None:
                names += ", "
            names += "Renders"
            
        if renders is not None:
            rendercount = len(filter(lambda x: x.Value,rendercb.values()))
            
        if layers is not None:
            layercount = len([x for x in layers.Seq()])
            
        if layers is not None:
            if renders is not None:
                label = "%d Layers; %d Renders"%(layercount,rendercount)
            else:
                label = "%d Layers"%layercount
        else:
            label = "%d Renders"%rendercount
            
        # Create the staticText widget in the stack, that when clicked will
        # set the visible layers to that element.
        # self.m_staticText3 = wx.StaticText( 
            # self.m_scrollwindow, 
            # wx.ID_ANY, 
            # u"My Set", 
            # wx.DefaultPosition, 
            # wx.DefaultSize, 
            # 0|wx.RAISED_BORDER )
		# self.m_staticText3.Wrap( -1 )

        widget = wx.StaticText(
            self._linkparent,
            wx.ID_ANY,
            label,
            wx.DefaultPosition,
            wx.DefaultSize,
            0|wx.RAISED_BORDER )
        widget.SetToolTip(wx.ToolTip(names))
        widget.Wrap( -1 )
        widget.Bind( wx.EVT_LEFT_UP, self._lvset_frame.loadset )
        widget.Bind( wx.EVT_SIZE, self.sizelabel )

        self._count += 1
        element = (layers,renders,widget)
        self._layersetstack.append(element)
        
        # Insert this widget as the first element on the stack,
        # i.e. the top of the list.        
        self._linkparent.GetSizer().Insert(0,widget,0,wx.ALL,5)

        # Try a whole bunch of things to get the wxWindow to refresh.
        self._linkparent.Layout()
        self._linkparent.Refresh()

    def sizelabel(self,e):
        """Called when a label is resized. This simply resets the wrapping
           width of the label."""
        widget = e.GetEventObject()
        widget.Wrap( widget.GetClientSize().GetWidth() )
        
        
    def GetCheckboxes(self):
        layercb=None
        rendercb=None
        board = pcbnew.GetBoard()
        fcu = wx.FindWindowByLabel('F.Cu')
        wins = [sc.GetWindow() for sc in fcu.GetParent().GetSizer().GetChildren()]
        wins = filter(lambda x: isinstance(x,wx._controls.StaticText) or isinstance(x,wx._controls.CheckBox),wins)
        # split into length 2 chunks:
        # Assume that the controls are in order (that's why we use the Sizer children)
        layercb = {board.GetLayerID(label.GetLabel()):cb for cb,label in zip(*[iter(wins)]*2)}
        
        # for rendercb, get the checkbox and that checkbox's label
        rendercb = {label2elementnum[x.GetLabel()]:x for x in filter(lambda x: isinstance(x,wx._controls.CheckBox),
                map(lambda x: x.GetWindow(),
                    fcu.GetParent().
                    GetParent().GetParent().
                    FindWindowByLabel('Grid').
                    GetParent().
                    GetSizer().GetChildren())
            )}
        
        return layercb,rendercb
    def pop(self):
        """Pop the top of the layersetstack and set the visible layers to
           those indicated in the element popped."""
        board = pcbnew.GetBoard()
        layercb,rendercb = self.GetCheckboxes()
           
        # Only do this if there are elements within the layersetstack.
        if len(self._layersetstack) > 0:
            # pop the element
            self._message.SetLabel("Change Canvas to view")
            element = self._layersetstack.pop()
            
            # Set the layers
            if element[0] is not None:
                board.SetVisibleLayers(element[0])
            if element[1] is not None:
                board.SetVisibleElements(element[1])
                
            for layer,cb in layercb.iteritems():
                cb.Value = board.IsLayerVisible(layer)
            for r,cb in rendercb.iteritems():
                cb.Value = board.IsElementVisible(r)
            
            
            # Try a few things to get the window to refresh.
            # Perhaps the only thing necessary here is "Destroy"
            p = element[2].GetParent()
            p.GetSizer().Remove(0)
            element[2].Destroy()
            p.GetSizer().Layout()
            p.Refresh()
            p.GetParent().Layout()
            p.GetParent().Refresh()
            self._linkparent.Layout()
            self._linkparent.Refresh()
        else:
            self._message.SetLabel("Nothing to pop")

# en=filter(lambda x: x.startswith('LAYER') != -1,dir(pcbnew))
# en=map(lambda x: (x,getattr(pcbnew,x)),en)
# en=filter(lambda x:isinstance(x[1],int),en)
# en=sorted(en,key=lambda x:x[1])
# i=1
# while (en[i][1]-en[i-1][1]<10):
    # i=i+1
# en=en[0:i]

# Instantiate and register the ActionPlugin class when imported.
_lvset = layerviewset()
_lvset.register()



# Derived rom KiCad source code, near the top of pcbnew/class_pcb_layer_widget.cpp
label2elementnum = {
     "Through Via" : pcbnew.LAYER_VIA_THROUGH ,
     "Bl/Buried Via" : pcbnew.LAYER_VIA_BBLIND , 
     "Micro Via" : pcbnew.LAYER_VIA_MICROVIA , 
     "Non Plated Holes" : pcbnew.LAYER_NON_PLATED ,
     "Ratsnest" : pcbnew.LAYER_RATSNEST ,
     "Pads Front" : pcbnew.LAYER_PAD_FR ,
     "Pads Back" : pcbnew.LAYER_PAD_BK , 
     "Text Front" : pcbnew.LAYER_MOD_TEXT_FR ,
     "Text Back" : pcbnew.LAYER_MOD_TEXT_BK , 
     "Hidden Text" : pcbnew.LAYER_MOD_TEXT_INVISIBLE ,
     "Anchors" : pcbnew.LAYER_ANCHOR ,
     "Grid" : pcbnew.LAYER_GRID , 
     "No-Connects" : pcbnew.LAYER_NO_CONNECTS , 
     "Footprints Front" : pcbnew.LAYER_MOD_FR , 
     "Footprints Back" : pcbnew.LAYER_MOD_BK ,
     "Values" : pcbnew.LAYER_MOD_VALUES , 
     "References" : pcbnew.LAYER_MOD_REFERENCES , 
     "Worksheet" : pcbnew.LAYER_WORKSHEET , 
     "Cursor" : pcbnew.LAYER_CURSOR , 
     "Aux items" : pcbnew.LAYER_AUX_ITEMS , 
     "Background" : pcbnew.LAYER_PCB_BACKGROUND ,
}
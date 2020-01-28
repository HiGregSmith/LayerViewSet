# Layer View Set.py
# https://github.com/HiGregSmith/LayerViewSet
# https://github.com/HiGregSmith/LayerViewSet/blob/master/README.md
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

import os
import time
import pcbnew
import wx
import wx.aui
import layerviewset_gui
import collections

# collections.namedtuple(typename, field_names[, verbose=False][, rename=False])

Element = collections.namedtuple('Element','layers items widget name filepath')

savepath = os.path.join(os.path.expanduser('~'),'kicad','viewsets')

#######
## GUI Definition
#######
# Modifications to wxFormBuilder
# Frame.SizeHints -> SizeHintsSz
# Menu.Append -> Menu.AppendItem

    
class gui (layerviewset_gui.layerviewset_panel):
    """Inherits from the layerviewset_gui form wxFormBuilder. Supplies
       functions that tie the gui to the layerviewset class below."""
    _lvset_instance = None
    interior_panel = None
    def __init__(self, lvset_instance, parent_frame, pane=None, *args, **kw):
        
        self._lvset_instance = lvset_instance
        if pane is not None:
            manager.AddPane( self, pane)
        super(gui,self).__init__(parent_frame)#, *args, **kw)
        #self.makedock(self.GetChildren()[1])#.interior_panel)
        #print self.linkpanel

    # def makedock(self,panel=None):
        # managed_window,manager = get_parent_panel()
        # print panel
        # if panel is not None:
            # panel = wx.Panel( managed_window, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
        # panel.Reparent(managed_window)
        # manager.AddPane( panel, wx.aui.AuiPaneInfo() .Center() .Caption( u"ViewSet" ).PinButton( True ).Float().FloatingPosition( wx.Point( 346,268 ) ).Resizable().FloatingSize( wx.Size( 60,300 ) ).Layer( 0 ) )    
        # panel.Show()
        # panel.Enable()
        # panel.Raise()
        # manager.Update()


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
    def pushlayers(self,e):
        self._lvset_instance.pushlayers()
    def pushitems(self,e):
        self._lvset_instance.pushitems()
        
    def pop(self,e):
        self._lvset_instance.pop()
    def dock(self,e):
        return
    def nameset(self,e):
        #self._lvset_instance._message.SetLabel("name")
        self._lvset_instance.nameset(e)
        return
    def deleteset(self,e):
        #self._lvset_instance._message.SetLabel("delete")
        self._lvset_instance.deleteset(e)
    def linkbuttonOnContextMenu( self, event ):
        #self._message.SetLabel("override")
        self.context_object = event.GetEventObject()
        self.linkpanel.PopupMenu( self.m_menu3, self.linkpanel.ScreenToClient(event.GetPosition()) )
    context_object = None
    
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
    def findwidget(self,widget):
        """Find the widget either with the saved sets or the stack sets."""
        self._message.SetLabel("1 Finding...")
        found = filter(lambda x:x[2] == widget,self._layersetstack)
        self._message.SetLabel("2 Finding...")
        
        if not found:
            self._message.SetLabel("3 Finding...")
            found = filter(lambda x:x[2] == widget,self._layersetsaved)
            self._message.SetLabel("4 Finding...")
        if not found:
            self._message.SetLabel("5 Finding...")
            return None
            
        self._message.SetLabel("6 Finding...")
        return found[0]
    def loadsetsfromfolder(self):
        board = pcbnew.GetBoard()
        f = []
        for (dirpath, dirnames, filenames) in os.walk(savepath):
            f.extend(filenames)
            break
        for filename in f:
            layerarray = []
            rendervalue = None
            with open(os.path.join(dirpath,filename),'r') as f:
                for line in f:
                    line=line.strip()
                    if line.startswith('#'):
                        continue
                    # line here is 3 values separated by commas
                    (type,name,visible) = map(str.strip,line.split(','))
                    if type=='layer':
                        id = board.GetLayerID(name)
                        layerarray.append((id,visible))
                    elif type=='render':
                        rendervalue = int(name, 2)
                    else:
                        pass
                        # type is unrecognized
                # Generate the lset and the render values, and assign them to an element
                # element is (layerset,rendervalue,widget,name,file)
                if layerarray:
                    layerset = pcbnew.LSET()
                    for layer,visible in layerarray:
                        layerset.addLayer(layer)
                else:
                    layerset = None
            widget = self.get_viewset_widget(
              self._nameparent,
              filename,
              self.get_tool_tip(layerset,rendervalue))

            #Element = collections.namedtuple('Element','layers items widget name filepath')

            element = Element(layerset,rendervalue,widget,filename,os.path.join(dirpath,filename))
            self._layersetsaved.append(element)
            
    def get_tool_tip(self, layers, items):
        #board = pcbnew.GetBoard()
        #renderlabel = ""
        #layerlabel = ""
           
        # Nested list comprehensions to retrieve the names of the currently
        # visible layers.
        if layers is not None:
            tooltip = ', '.join(self.getnamefromlayers(layers))
            #layerlabel = str(len([x for x in layers.Seq()]))
        else:
            tooltip = ''
            
        if items is not None:
            if layers is not None:
                tooltip += "; "
            num2name = {v:k for k,v in label2elementnum.items()}
            # evisible = filter(lambda x: board.IsElementVisible(x),
                                # label2elementnum.values()
                             # )
            # tooltip += ", ".join([num2name[e] for e in evisible])
            tooltip += "Items"
            
            #layercb,rendercb = self.GetCheckboxes()
            #rendercount = len(filter(lambda x: x.Value,rendercb.values()))
            # This gets the "raw" count including all "behind the scenes" items:
            # renderlabel = str(bin(items).count("1"))
            
            # This gets the items selected by the user,
            # assuming label2elementnum is uptodate
            #renderlabel = str(len(evisible))
            
        #label = layerlabel + '/' + renderlabel
        return tooltip
        
    def nameset(self,e):
        widget = self._lvset_frame.context_object
        self._message.SetLabel(widget.GetLabel())
        
        try:
            tooltip = widget.GetToolTip().GetTip()
        except:
            tooltip = ""
        
        try:
            found = self.findwidget(widget)
        except:
            self._message.SetLabel("error during find")
            
        if found is None:
            self._message.SetLabel("ERROR: set not found")
            return
        else:
            self._message.SetLabel("set found %d"%len(self._layersetsaved))
        # Ask user for set name
        initname = "Hello"
        if found[3:4][0] is not None:
            self._message.SetLabel("1")
            initname = found[3:4][0]
            self._message.SetLabel("2")
        else:
            self._message.SetLabel("3")
            count = 1
            while os.path.exists(os.path.join(savepath,"ViewSet "+str(count))):
                count += 1
            self._message.SetLabel("4")
            initname = "ViewSet "+str(count)
        self._message.SetLabel("5")
        try:
            dlg = wx.TextEntryDialog(self._lvset_frame, "Enter new set name", defaultValue=initname)
            result = dlg.ShowModal()
        except Exception as e:
            self._message.SetLabel("E! "+str(initname))
            result = None
            return
        
        # self._message.SetLabel("6")
        # self._message.SetLabel("7")
        if result != wx.ID_OK:
            self._message.SetLabel("Cancelled (%s)"%str(result))
            return
        self._message.SetLabel("8")
        new_name = dlg.GetValue()
        if filter(lambda x:x.name==new_name,self._layersetsaved):
            self._message.SetLabel("Already exists")
            return
        dlg.Destroy()

        try:
            if found[3:4][0] is None: # test to see if there's a fourth element (i.e. name)
            #if not found[3:4]: # test to see if there's a fourth element (i.e. name)
                # this is a stack, so save and name it.
                #new_name = str(len(self._layersetsaved))
                self._message.SetLabel("new name %s"%new_name)
                if not os.path.exists(savepath):
                    os.makedirs(savepath)
                    self._message.SetLabel('created ~/kicad/viewsets')
                self._message.SetLabel("saving to %s"%new_name)
                new_path = os.path.join(savepath, new_name)
                with open(new_path,'w') as f:
                    #print(dir(found))
                    layers=found.layers
                    self._message.SetLabel("L %s"%new_name)
                    items=found.items
                    self._message.SetLabel("I %s"%new_name)
                    if layers is not None:
                        self._message.SetLabel("writing %s, %s"%(new_name,str(layers)))
                        for layer in self.getnamefromlayers(layers):
                            f.write('layer,%s,%d\n'%(layer,1))
                        self._message.SetLabel("wrote layers")
                    if items is not None:
                        rname = "{0:b}".format(items)
                        f.write('render,%s,%d\n'%(rname,1))
                        self._message.SetLabel("wrote items")

                new_widget = self.get_viewset_widget(self._nameparent,new_name,tooltip) # names
                new_element = Element(found.layers,found.items,new_widget,new_name,new_path)
                self._message.SetLabel("created element")

                self._layersetsaved.append(new_element)    
                self._message.SetLabel("appended")
            else:
                self._message.SetLabel("new name %s"%new_name)
                # found contains the element to rename
                widget = found.widget
                old_name = found.name
                old_filepath = found.filepath
                new_filepath = os.path.join(savepath,new_name)
                
                # rename the file
                os.rename(old_filepath,new_filepath)
                # rename the widget
                widget.SetLabel(new_name)
                # replace the element in the Named ViewSet List
                i = self._layersetsaved.index(found)
                self._layersetsaved[i] = (found.layers,found.items,widget,new_name,new_filepath)
            self._message.SetLabel("Saved %s"%new_name)
        except Exception as e:
            self._message.SetLabel("ERROR "+self._message.GetLabel())
            etext = str(e)
            wx.MessageDialog(widget,etext,style=wx.OK).ShowModal()


    def deleteset(self,widget):
        self._message.SetLabel("deleteset")
        widget = self._lvset_frame.context_object
        self._message.SetLabel(widget.GetLabel())
        found = self.findwidget(widget)
        if found is None:
            self._message.SetLabel("set not found")
            return
        else:
            self._message.SetLabel("set found %d"%len(self._layersetsaved))
        try:
            self._layersetstack.remove(found)
        except:
            pass
        try:
            self._layersetsaved.remove(found)
        except:
            pass
        parent = found.widget.GetParent()
        sizer=parent.GetSizer()
        found[2].Destroy()
        try:
            filename = found[4:5]
            if filename and os.path.exists(filename[0]):
                self._message.SetLabel("removing")
                os.remove(found[4])
                self._message.SetLabel("removed")
        except:
            pass
        sizer.Layout()
                
    #######
    ## ActionPlugin
    #######
    def defaults( self ):
        """Support for ActionPlugins, though it doesn't work in 4.0.6 nightly and later"""
        self.name = "Layer ViewSet"
        self.category = "Layers"
        self.description = "Save and restore view settings for layers and items."

        
    #######
    ## Application Specific KiCad window manipulation
    #######
    def GetLayerManager(self):
        """Find the layer_manager panel and its AUI manager"""
        # find the top-level auimanager
        win = wx.FindWindowByLabel(pcbnew.GetBoard().GetLayerName( pcbnew.F_Cu ))
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
                if len(am) >= 1: # This sets how many generations of different managers to go back
                    break
        managed_window = am[-1].GetManagedWindow()
        return managed_window,am[-1]
        
    def Run(self):
        """Necessary for ActionPlugin, shows the gui and sets up some class
        variables for use within the functions."""
        self._layersetstack = []
        self._layersetsaved = []
        # Instantiate and Show the gui, giving it
        # the current instance (for calling functions) and
        # the parent frame (Pcbnew)
        #import wx
        # Find the main "Pcbnew" wx window.
        _pcbnew_frame = \
            filter(lambda w: w.GetTitle().startswith('Pcbnew'), 
                   wx.GetTopLevelWindows()
            )[0]
        _pcbnew_manager = wx.aui.AuiManager.GetManager(_pcbnew_frame)
        parent = _pcbnew_frame
        manager = _pcbnew_manager
        #parent, manager = self.GetLayerManager()
        #print parent.GetTitle(),parent.GetLabel()
        pane = wx.aui.AuiPaneInfo()                       \
                 .Caption( u"ViewSet" )                   \
                 .Center()                                \
                 .Float()                                 \
                 .FloatingPosition( wx.Point( 346,268 ) ) \
                 .Resizable()                             \
                 .FloatingSize( wx.Size( 60,300 ) )       \
                 .Layer( 0 )                                 
        self._lvset_frame=gui(self,parent)
        #  .Caption( u"ViewSet" )
        #self._lvset_frame.Show()
        manager.AddPane( self._lvset_frame, pane )
        #self._lvset_frame.Reparent(parent)
        manager.Update()
        
        #wx.aui.AuiManager.GetManager(self._lvset_frame).Update()
        
        # Set the class variable for the window that will contain the stack.
        self._linkparent = self._lvset_frame.FindWindowByName('linkwindow')
        self._nameparent = self._lvset_frame.FindWindowByName('namewindow')
        self._message = self._lvset_frame.FindWindowByName('message_label')
        self._message.SetLabel("Click on any label:")
        # Destroy sample links
        self._linkparent.DestroyChildren()
        self._nameparent.DestroyChildren()
        
        # Set the layersetstack first item to the current visible layers.
        self._lvset_frame.push(None)
        
        # initialize named layer sets
        self.loadsetsfromfolder()
    #######
    ## End ActionPlugin
    #######    

    # _layersetstack elements are tuples (layer LSET *,render int *,widget,name)
    _layersetstack = []
    _layersetsaved = []
    _count = 1
    
    def loadset(self,e):
        """Load a viewset based on the object (e) clicked."""
        # self._message.SetLabel("m1")
        # return
        # The widget is the object that was clicked.
        widget = e.GetEventObject()
        #wx.MessageDialog(widget,widget.GetLabel(),style=wx.OK).ShowModal()
        # Find that widget in the layersetstack.
        element = filter (lambda x: x[2]==widget,self._layersetstack)
        if not element:
            element = filter (lambda x: x[2]==widget,self._layersetsaved)
        element = element[0]
        # The the visible layers according to that element in the stack.        
        if element[0] is not None:
            pcbnew.GetBoard().SetVisibleLayers(element[0])
        if element[1] is not None:
            pcbnew.GetBoard().SetVisibleElements(element[1])
        try:
            pcbnew.UpdateUserInterface()
            self._message.SetLabel(element[2].GetLabel())
        except:
            self._message.SetLabel("Change Canvas to view")

    def push(self):
        self._push(pcbnew.GetBoard().GetVisibleLayers(),pcbnew.GetBoard().GetVisibleElements())
    
    def pushlayers(self):
        self._push(pcbnew.GetBoard().GetVisibleLayers(),None)
    
    def pushitems(self):
        self._push(None,pcbnew.GetBoard().GetVisibleElements())
    def getnamefromlayers(self,layers):
        return [pcbnew.GetBoard().GetLayerName(num) for num in 
                [x for x in layers.Seq()]]
    def getnamefromitems(self,items):
        return name
    
    d = {}
    ## Attempt to implement the following:
    # MouseDown: capture the object, object position, and mouse position
    # MouseMove: only if the mouse has moved further than half the height of the object,
    # then begin object movement.
    # If object is moving:
    #    Check mouse position over other objects in the same panel
    #    if moving object is below the current object,
    #    else if moving object is above the current object,
    
    
    def MouseDown(e):
        o           = e.GetEventObject()
        sx,sy       = panel.ScreenToClient(o.GetPositionTuple())
        dx,dy       = panel.ScreenToClient(wx.GetMousePosition())
        o._x,o._y   = (sx-dx, sy-dy)
        self.d['d'] = o

    def MouseMove(e):
        try:
            if 'd' in self.d:
                o = self.d['d']
                x, y = wx.GetMousePosition()
                o.SetPosition(wx.Point(x+o._x,y+o._y))
        except: pass

    def MouseUp(e):
        try:
            if 'd' in self.d: del d['d']
        except: pass
        
    def get_viewset_widget(self,parent,label,tooltip=None):
        widget = wx.StaticText(
            parent,
            wx.ID_ANY,
            label,
            wx.DefaultPosition,
            wx.DefaultSize,
            0|wx.RAISED_BORDER )
        widget.SetToolTip(wx.ToolTip(tooltip))
        #widget.Wrap( -1 )
        #widget.Bind(wx.EVT_BUTTON, self._lvset_frame.loadset)
        widget.Bind( wx.EVT_CONTEXT_MENU, self._lvset_frame.linkbuttonOnContextMenu )
        widget.Bind( wx.EVT_LEFT_UP, self._lvset_frame.loadset )
        
        #widget.Bind( wx.EVT_CONTEXT_MENU, self._lvset_frame.m_button3OnContextMenu )
        #self._lvset_frame.Bind( wx.EVT_CONTEXT_MENU, self._lvset_frame.m_button3OnContextMenu, widget)
        
        #self.get_button_context(widget)
        #widget.Bind( wx.EVT_RIGHT_UP, self._lvset_frame.stacksetcontext )

        #widget.Bind( wx.EVT_SIZE, self.sizelabel )
        
        # Insert this widget as the first element on the stack widget,
        # i.e. the top of the list.        
        parent.GetSizer().Insert(0,widget,0,wx.ALL,5)

        # Try a whole bunch of things to get the wxWindow to refresh.
        parent.Layout()
        parent.Refresh()

        return widget
    def switchfirst(self):
        '''Get the first two buttons in the named set, and switch their places'''
        #w0 = self._layersetsaved[0][2]
        #w1 = self._layersetsaved[1][2]
        p = self._layersetsaved[0][2].GetParent()
        s = p.GetSizer()
        flags = []
        for e in self._layersetsaved:
            w = e[2]
            flags.append(s.GetItem(w).GetFlag()) # Get Flags from SizerItem
            s.Detach(w)
            p.RemoveChild(w)
        self._layersetsaved = self._layersetsaved[::-1] # reverse, shallow copy
        
        for i,e in enumerate(self._layersetsaved):
            w = e[2]
            p.AddChild(w)           
            #s.Add(w,wx.ALL)#flags[i])
            s.Insert(0,w,0,wx.ALL,5)
        #bsizer = w0.GetParent().GetSizer()
        # sizer_item0 = bsizer.GetItem(w0)
        # sizer_item1 = bsizer.GetItem(w1)
        #bsizer.Detach(w1)
        #bsizer.Insert(0,w1)
        #children = w0.GetParent().GetChildren()
        
        
        s.Layout()
        
    def _push(self,layers,items):
        """Push the current view set onto the stack, create the text widget,
           and add the widget to the display."""

        board = pcbnew.GetBoard()
        renderlabel = ""
        layerlabel = ""
           
        # Nested list comprehensions to retrieve the names of the currently
        # visible layers.
        if layers is not None:
            names = ', '.join(self.getnamefromlayers(layers))
            layerlabel = str(len([x for x in layers.Seq()]))
        else:
            names = ''
            
        if items is not None:
            if layers is not None:
                names += "; "
            num2name = {v:k for k,v in label2elementnum.items()}
            evisible = filter(lambda x: board.IsElementVisible(x),
                                label2elementnum.values()
                             )
            # names += "Items"
            names += ", ".join([num2name[e] for e in evisible])
            
            #layercb,rendercb = self.GetCheckboxes()
            #rendercount = len(filter(lambda x: x.Value,rendercb.values()))
            # This gets the "raw" count including all "behind the scenes" items:
            # renderlabel = str(bin(items).count("1"))
            
            # This gets the items selected by the user,
            # assuming label2elementnum is uptodate
            renderlabel = str(len(evisible))
            
        label = layerlabel + '/' + renderlabel
            
        # Create the staticText widget in the stack, that when clicked will
        # set the visible layers to that element.
        widget = self.get_viewset_widget(self._linkparent,label,names)

        self._count += 1

        element = Element(layers,items,widget,None,None)
        self._layersetstack.append(element)
        self._message.SetLabel("done")


    def sizelabel(self,e):
        """Called when a label is resized. This simply resets the wrapping
           width of the label."""
        widget = e.GetEventObject()
        widget.Wrap( widget.GetClientSize().GetWidth() )
        
        
    # def GetCheckboxes(self):
        # layercb=None
        # rendercb=None
        # board = pcbnew.GetBoard()
        # fcu = wx.FindWindowByLabel(board.GetLayerName( pcbnew.F_Cu ))
        # wins = [sc.GetWindow() for sc in fcu.GetParent().GetSizer().GetChildren()]
        # wins = filter(lambda x: isinstance(x,wx._controls.StaticText) or isinstance(x,wx._controls.CheckBox),wins)
        # # split into length 2 chunks:
        # # Assume that the controls are in order (that's why we use the Sizer children)
        # layercb = {board.GetLayerID(label.GetLabel()):cb for cb,label in zip(*[iter(wins)]*2)}
        
        # # for rendercb, get the checkbox and that checkbox's label
        # rendercb = {label2elementnum[x.GetLabel()]:x for x in filter(lambda x: isinstance(x,wx._controls.CheckBox),
                # map(lambda x: x.GetWindow(),
                    # fcu.GetParent().
                    # GetParent().GetParent().
                    # FindWindowByLabel('Grid'). # wx.GetTranslation('Grid')
                    # GetParent().
                    # GetSizer().GetChildren())
            # )}
        
        # return layercb,rendercb
    def pop(self):
        """Pop the top of the layersetstack and set the visible layers to
           those indicated in the element popped."""
        board = pcbnew.GetBoard()
        #layercb,rendercb = self.GetCheckboxes()
           
        # Only do this if there are elements within the layersetstack.
        if len(self._layersetstack) > 0:
            # pop the element
            self._message.SetLabel("Change Canvas to view")
            element = self._layersetstack.pop()
            
            # Set the layers
            if element[0] is not None:
                # for num in range(board.PCB_LAYER_ID_COUNT):
                    # board.GetDesignSettings().SetLayerVisibility(num,False)
                board.SetVisibleLayers(element[0])
            if element[1] is not None:
                board.SetVisibleElements(element[1])
                
            #for layer,cb in layercb.iteritems():
            #    cb.Value = board.IsLayerVisible(layer)
            #for r,cb in rendercb.iteritems():
            #    cb.Value = board.IsElementVisible(r)
            
            
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
            try:
                pcbnew.UpdateUserInterface()
            except:
                self._message.SetLabel("Change Canvas to view")
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

# Derived from KiCad source code, near the top of pcbnew/class_pcb_layer_widget.cpp
try:
    label2elementnum = {
        
        "Through Via"      : pcbnew.     VIA_THROUGH_VISIBLE,    
        "Bl/Buried Via"    : pcbnew.   VIA_BBLIND_VISIBLE,       
        "Micro Via"        : pcbnew.       VIA_MICROVIA_VISIBLE, 
        "Non Plated"       : pcbnew.      NON_PLATED_VISIBLE,    
        "Ratsnest"         : pcbnew.        RATSNEST_VISIBLE,    
                            
        "Pads Front"       : pcbnew.      PAD_FR_VISIBLE,        
        "Pads Back"        : pcbnew.       PAD_BK_VISIBLE,       
                            
        "Text Front"       : pcbnew.      MOD_TEXT_FR_VISIBLE,   
        "Text Back"        : pcbnew.       MOD_TEXT_BK_VISIBLE,  
        "Hidden Text"      : pcbnew.     MOD_TEXT_INVISIBLE,     
                            
        "Anchors"          : pcbnew.      ANCHOR_VISIBLE,        
        "Grid"             : pcbnew.            GRID_VISIBLE,    
        "No-Connects"      : pcbnew.     NO_CONNECTS_VISIBLE,    
        "Footprints Front" : pcbnew.   MOD_FR_VISIBLE,           
        "Footprints Back"  : pcbnew.    MOD_BK_VISIBLE,          
        "Values"           : pcbnew.          MOD_VALUES_VISIBLE,
        "References"       : pcbnew.      MOD_REFERENCES_VISIBLE,
    }
except:
    label2elementnum = {
         "Through Via" : pcbnew.LAYER_VIA_THROUGH ,
         "Bl/Buried Via" : pcbnew.LAYER_VIA_BBLIND , 
         "Micro Via" : pcbnew.LAYER_VIA_MICROVIA , 
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
    try:
        label2elementnum["Non Plated Holes"] = pcbnew.LAYER_NON_PLATED 
    except:
        label2elementnum["Non Plated Holes"] = pcbnew.LAYER_NON_PLATEDHOLES

# Instantiate and register the ActionPlugin class when imported.
_lvset = layerviewset()
_lvset.register()
#_lvset.Run()



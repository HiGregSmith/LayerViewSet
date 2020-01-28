# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 28 2017)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.aui

###########################################################################
## Class layerviewset_panel
###########################################################################

class layerviewset_panel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 217,285 ), style = wx.TAB_TRAVERSAL )
		
		self.Hide()
		self.m_mgr = wx.aui.AuiManager()
		self.m_mgr.SetManagedWindow( self )
		self.m_mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT)
		
		self.interior_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_mgr.AddPane( self.interior_panel, wx.aui.AuiPaneInfo() .Center() .CaptionVisible( False ).CloseButton( False ).Dock().Resizable().FloatingSize( wx.DefaultSize ).DockFixed( True ).Row( 1 ) )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_splitter1 = wx.SplitterWindow( self.interior_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter1.SetSashGravity( 1 )
		self.m_splitter1.Bind( wx.EVT_IDLE, self.m_splitter1OnIdle )
		self.m_splitter1.SetMinimumPaneSize( 10 )
		
		self.namepanel = wx.Panel( self.m_splitter1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL, u"namewindow" )
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText19 = wx.StaticText( self.namepanel, wx.ID_ANY, u"This is a named set", wx.DefaultPosition, wx.DefaultSize, 0|wx.RAISED_BORDER )
		self.m_staticText19.Wrap( -1 )
		bSizer7.Add( self.m_staticText19, 0, wx.ALL, 5 )
		
		self.namepanel.SetSizer( bSizer7 )
		self.namepanel.Layout()
		bSizer7.Fit( self.namepanel )
		self.linkpanel = wx.Panel( self.m_splitter1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL, u"linkwindow" )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText3 = wx.StaticText( self.linkpanel, wx.ID_ANY, u"88/88", wx.DefaultPosition, wx.DefaultSize, 0|wx.RAISED_BORDER )
		self.m_staticText3.Wrap( -1 )
		bSizer3.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.m_button3 = wx.Button( self.linkpanel, wx.ID_ANY, u"99/99", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT|wx.NO_BORDER )
        
		self.m_menu3 = wx.Menu()
		#self.m_menuItem5 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Name", wx.EmptyString, wx.ITEM_NORMAL )
		#self.m_menu3.Append( self.m_menuItem5)
		#self.m_menuItem5 = self.m_menu3.Append(self.m_menu3,wx.ID_ANY, item=u"Name", helpString=wx.EmptyString, kind=wx.ITEM_NORMAL)
		
		# It's a fairly consistent battle to get this Append or AppendItem to work. This works for now.
		self.m_menuItem5 = self.m_menu3.Append(wx.ID_ANY, text=u"Name", help=wx.EmptyString, kind=wx.ITEM_NORMAL)
        
		#self.m_menuItem6 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Delete", wx.EmptyString, wx.ITEM_NORMAL )
		#self.m_menu3.Append( self.m_menuItem6)
		self.m_menuItem6 = self.m_menu3.Append( wx.ID_ANY, u"Delete", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_button3.Bind( wx.EVT_RIGHT_DOWN, self.m_button3OnContextMenu ) 
		
		bSizer3.Add( self.m_button3, 0, wx.LEFT|wx.RIGHT|wx.SHAPED, 4 )
		
		
		self.linkpanel.SetSizer( bSizer3 )
		self.linkpanel.Layout()
		bSizer3.Fit( self.linkpanel )
		self.m_splitter1.SplitVertically( self.namepanel, self.linkpanel, 143 )
		gbSizer1.Add( self.m_splitter1, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 3 ), wx.EXPAND, 5 )
		
		self.toppanel = wx.Panel( self.interior_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText4 = wx.StaticText( self.toppanel, wx.ID_ANY, u"Layers", wx.DefaultPosition, wx.DefaultSize, 0|wx.RAISED_BORDER )
		self.m_staticText4.Wrap( -1 )
		self.m_staticText4.SetToolTipString( u"Push visible Layers onto stack." )
		
		gbSizer2.Add( self.m_staticText4, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.m_staticText41 = wx.StaticText( self.toppanel, wx.ID_ANY, u"Items", wx.DefaultPosition, wx.DefaultSize, 0|wx.RAISED_BORDER )
		self.m_staticText41.Wrap( -1 )
		self.m_staticText41.SetToolTipString( u"Push visible Items onto stack." )
		
		gbSizer2.Add( self.m_staticText41, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALIGN_LEFT|wx.ALL, 5 )
		
		self.m_staticText42 = wx.StaticText( self.toppanel, wx.ID_ANY, u"-v-", wx.DefaultPosition, wx.DefaultSize, 0|wx.RAISED_BORDER )
		self.m_staticText42.Wrap( -1 )
		self.m_staticText42.SetToolTipString( u"Push visible Layers and Items onto stack." )
		
		gbSizer2.Add( self.m_staticText42, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticText5 = wx.StaticText( self.toppanel, wx.ID_ANY, u"--^--", wx.DefaultPosition, wx.DefaultSize, 0|wx.RAISED_BORDER )
		self.m_staticText5.Wrap( -1 )
		self.m_staticText5.SetToolTipString( u"Pop stack and assign visible layers and/or items." )
		
		gbSizer2.Add( self.m_staticText5, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.LEFT|wx.TOP, 5 )
		
		self._message = wx.StaticText( self.toppanel, wx.ID_ANY, u"Click below", wx.DefaultPosition, wx.DefaultSize, 0, u"message_label" )
		self._message.Wrap( -1 )
		gbSizer2.Add( self._message, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 2 ), wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT|wx.EXPAND|wx.TOP, 5 )
		
		
		self.toppanel.SetSizer( gbSizer2 )
		self.toppanel.Layout()
		gbSizer2.Fit( self.toppanel )
		gbSizer1.Add( self.toppanel, wx.GBPosition( 0, 0 ), wx.GBSpan( 2, 3 ), wx.EXPAND |wx.ALL, 5 )
		
		
		gbSizer1.AddGrowableCol( 0 )
		gbSizer1.AddGrowableRow( 2 )
		
		self.interior_panel.SetSizer( gbSizer1 )
		self.interior_panel.Layout()
		gbSizer1.Fit( self.interior_panel )
		
		self.m_mgr.Update()
		
		# Connect Events
		self.m_staticText3.Bind( wx.EVT_SIZE, self.sizelabel )
		self.Bind( wx.EVT_MENU, self.nameset, id = self.m_menuItem5.GetId() )
		self.Bind( wx.EVT_MENU, self.deleteset, id = self.m_menuItem6.GetId() )
		self.m_staticText4.Bind( wx.EVT_LEFT_UP, self.pushlayers )
		self.m_staticText41.Bind( wx.EVT_LEFT_UP, self.pushrenders )
		self.m_staticText42.Bind( wx.EVT_LEFT_UP, self.push )
		self.m_staticText5.Bind( wx.EVT_LEFT_UP, self.pop )
	
	def __del__( self ):
		self.m_mgr.UnInit()
		
	
	
	# Virtual event handlers, overide them in your derived class
	def sizelabel( self, event ):
		event.Skip()
	
	def nameset( self, event ):
		event.Skip()
	
	def deleteset( self, event ):
		event.Skip()
	
	def pushlayers( self, event ):
		event.Skip()
	
	def pushrenders( self, event ):
		event.Skip()
	
	def push( self, event ):
		event.Skip()
	
	def pop( self, event ):
		event.Skip()
	
	def m_splitter1OnIdle( self, event ):
		self.m_splitter1.SetSashPosition( 143 )
		self.m_splitter1.Unbind( wx.EVT_IDLE )
	
	def m_button3OnContextMenu( self, event ):
		self.m_button3.PopupMenu( self.m_menu3, event.GetPosition() )
		


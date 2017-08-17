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
## Class layerviewset_frame2
###########################################################################

class layerviewset_frame2 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.layerviewset_p2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5.Add( self.layerviewset_p2, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer5 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 368,371 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.m_mgr = wx.aui.AuiManager()
		self.m_mgr.SetManagedWindow( self )
		self.m_mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT)
		
		self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		self.m_mgr.AddPane( self.m_panel6, wx.aui.AuiPaneInfo() .Center() .Caption( u"who are you" ).PinButton( True ).Gripper().Hide().Float().FloatingPosition( wx.Point( 871,407 ) ).Resizable().FloatingSize( wx.Size( 474,245 ) ).Row( 1 ).Layer( 1 ) )
		
		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText11 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		gbSizer2.Add( self.m_staticText11, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		gbSizer2.Add( self.m_staticText12, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText13 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		gbSizer2.Add( self.m_staticText13, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText14 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		gbSizer2.Add( self.m_staticText14, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText15 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		gbSizer2.Add( self.m_staticText15, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText16 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		gbSizer2.Add( self.m_staticText16, wx.GBPosition( 0, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_panel7 = wx.Panel( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText17 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		bSizer7.Add( self.m_staticText17, 0, wx.ALL, 5 )
		
		
		self.m_panel7.SetSizer( bSizer7 )
		self.m_panel7.Layout()
		bSizer7.Fit( self.m_panel7 )
		gbSizer2.Add( self.m_panel7, wx.GBPosition( 0, 6 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		
		gbSizer2.AddGrowableCol( 0 )
		gbSizer2.AddGrowableRow( 0 )
		
		self.m_panel6.SetSizer( gbSizer2 )
		self.m_panel6.Layout()
		gbSizer2.Fit( self.m_panel6 )
		
		self.m_mgr.Update()
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		self.m_mgr.UnInit()
		
	

###########################################################################
## Class docktop
###########################################################################

class docktop ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 191,585 ), style = wx.TAB_TRAVERSAL, name = u"docktop" )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.splitter = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_LIVE_UPDATE|wx.SIMPLE_BORDER )
		self.splitter.SetSashGravity( 0.8 )
		self.splitter.SetSashSize( 20 )
		self.splitter.Bind( wx.EVT_IDLE, self.splitterOnIdle )
		self.splitter.SetMinimumPaneSize( 50 )
		
		self.m_panel2 = wx.Panel( self.splitter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button6 = wx.Button( self.m_panel2, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button6, 0, wx.ALL, 5 )
		
		
		self.m_panel2.SetSizer( bSizer3 )
		self.m_panel2.Layout()
		bSizer3.Fit( self.m_panel2 )
		self.viewsettop = wx.Panel( self.splitter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL, u"viewsettop" )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button7 = wx.Button( self.viewsettop, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0|wx.SIMPLE_BORDER )
		bSizer4.Add( self.m_button7, 0, wx.ALL, 5 )
		
		
		self.viewsettop.SetSizer( bSizer4 )
		self.viewsettop.Layout()
		bSizer4.Fit( self.viewsettop )
		self.splitter.SplitHorizontally( self.m_panel2, self.viewsettop, 443 )
		bSizer2.Add( self.splitter, 1, wx.EXPAND, 20 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
	
	def __del__( self ):
		pass
	
	def splitterOnIdle( self, event ):
		self.splitter.SetSashPosition( 443 )
		self.splitter.Unbind( wx.EVT_IDLE )
	

###########################################################################
## Class MyPanel2
###########################################################################

class MyPanel2 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
		self.m_mgr = wx.aui.AuiManager()
		self.m_mgr.SetManagedWindow( self )
		self.m_mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT)
		
		
		self.m_mgr.Update()
	
	def __del__( self ):
		self.m_mgr.UnInit()
		
	

###########################################################################
## Class layerviewset_panel2
###########################################################################

class layerviewset_panel2 ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
		
		self.m_mgr = wx.aui.AuiManager()
		self.m_mgr.SetManagedWindow( self )
		self.m_mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT)
		
		self.interior_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_mgr.AddPane( self.interior_panel, wx.aui.AuiPaneInfo() .Center() .CaptionVisible( False ).CloseButton( False ).Dock().Resizable().FloatingSize( wx.DefaultSize ).DockFixed( True ).Row( 1 ) )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText4 = wx.StaticText( self.interior_panel, wx.ID_ANY, u"Layers", wx.DefaultPosition, wx.DefaultSize, 0|wx.RAISED_BORDER )
		self.m_staticText4.Wrap( -1 )
		self.m_staticText4.SetToolTipString( u"Push visible Layers onto stack." )
		
		gbSizer1.Add( self.m_staticText4, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.m_staticText41 = wx.StaticText( self.interior_panel, wx.ID_ANY, u"Renders", wx.DefaultPosition, wx.DefaultSize, 0|wx.RAISED_BORDER )
		self.m_staticText41.Wrap( -1 )
		self.m_staticText41.SetToolTipString( u"Push visible Renders onto stack." )
		
		gbSizer1.Add( self.m_staticText41, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALIGN_LEFT|wx.ALL, 5 )
		
		self.m_staticText42 = wx.StaticText( self.interior_panel, wx.ID_ANY, u"-v-", wx.DefaultPosition, wx.DefaultSize, 0|wx.RAISED_BORDER )
		self.m_staticText42.Wrap( -1 )
		self.m_staticText42.SetToolTipString( u"Push visible Layers and Renders onto stack." )
		
		gbSizer1.Add( self.m_staticText42, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticText5 = wx.StaticText( self.interior_panel, wx.ID_ANY, u"--^--", wx.DefaultPosition, wx.DefaultSize, 0|wx.RAISED_BORDER )
		self.m_staticText5.Wrap( -1 )
		self.m_staticText5.SetToolTipString( u"Pop stack and assign visible layers and/or renders." )
		
		gbSizer1.Add( self.m_staticText5, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.LEFT|wx.TOP, 5 )
		
		self._message = wx.StaticText( self.interior_panel, wx.ID_ANY, u"Click below", wx.DefaultPosition, wx.DefaultSize, 0, u"message_label" )
		self._message.Wrap( -1 )
		gbSizer1.Add( self._message, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 2 ), wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT|wx.EXPAND|wx.TOP, 5 )
		
		self.m_panel1 = wx.Panel( self.interior_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL, u"linkwindow" )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText3 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"My Set", wx.DefaultPosition, wx.DefaultSize, 0|wx.RAISED_BORDER )
		self.m_staticText3.Wrap( -1 )
		bSizer3.Add( self.m_staticText3, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel1.SetSizer( bSizer3 )
		self.m_panel1.Layout()
		bSizer3.Fit( self.m_panel1 )
		gbSizer1.Add( self.m_panel1, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 3 ), wx.EXPAND, 5 )
		
		
		gbSizer1.AddGrowableCol( 2 )
		gbSizer1.AddGrowableRow( 2 )
		
		self.interior_panel.SetSizer( gbSizer1 )
		self.interior_panel.Layout()
		gbSizer1.Fit( self.interior_panel )
		
		self.m_mgr.Update()
		
		# Connect Events
		self.m_staticText4.Bind( wx.EVT_LEFT_UP, self.pushlayers )
		self.m_staticText41.Bind( wx.EVT_LEFT_UP, self.pushrenders )
		self.m_staticText42.Bind( wx.EVT_LEFT_UP, self.push )
		self.m_staticText5.Bind( wx.EVT_LEFT_UP, self.pop )
		self.m_staticText3.Bind( wx.EVT_SIZE, self.sizelabel )
	
	def __del__( self ):
		self.m_mgr.UnInit()
		
	
	
	# Virtual event handlers, overide them in your derived class
	def pushlayers( self, event ):
		event.Skip()
	
	def pushrenders( self, event ):
		event.Skip()
	
	def push( self, event ):
		event.Skip()
	
	def pop( self, event ):
		event.Skip()
	
	def sizelabel( self, event ):
		event.Skip()
	

###########################################################################
## Class layerviewset_frame
###########################################################################

class layerviewset_frame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.m_mgr = wx.aui.AuiManager()
		self.m_mgr.SetManagedWindow( self )
		self.m_mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT)
		
		self.interior_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_mgr.AddPane( self.interior_panel, wx.aui.AuiPaneInfo() .Center() .PinButton( True ).Dock().Resizable().FloatingSize( wx.DefaultSize ) )
		
		gbSizer6 = wx.GridBagSizer( 0, 0 )
		gbSizer6.SetFlexibleDirection( wx.BOTH )
		gbSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self._message = wx.StaticText( self.interior_panel, wx.ID_ANY, u"Click item below.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self._message.Wrap( -1 )
		gbSizer6.Add( self._message, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 4 ), wx.ALL, 5 )
		
		self.m_staticText16 = wx.StaticText( self.interior_panel, wx.ID_ANY, u"push L", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		gbSizer6.Add( self.m_staticText16, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText17 = wx.StaticText( self.interior_panel, wx.ID_ANY, u"push R", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		gbSizer6.Add( self.m_staticText17, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText18 = wx.StaticText( self.interior_panel, wx.ID_ANY, u"push A", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )
		gbSizer6.Add( self.m_staticText18, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText19 = wx.StaticText( self.interior_panel, wx.ID_ANY, u"pop", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		gbSizer6.Add( self.m_staticText19, wx.GBPosition( 1, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_panel9 = wx.Panel( self.interior_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gbSizer6.Add( self.m_panel9, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 5 ), wx.EXPAND |wx.ALL, 5 )
		
		
		gbSizer6.AddGrowableCol( 4 )
		gbSizer6.AddGrowableRow( 3 )
		
		self.interior_panel.SetSizer( gbSizer6 )
		self.interior_panel.Layout()
		gbSizer6.Fit( self.interior_panel )
		
		self.m_mgr.Update()
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		self.m_mgr.UnInit()
		
	


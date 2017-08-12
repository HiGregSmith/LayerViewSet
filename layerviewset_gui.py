# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 28 2017)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class layerviewset_frame
###########################################################################

class layerviewset_frame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Layer ViewSet", pos = wx.DefaultPosition, size = wx.Size( 504,397 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Push -v-", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button1.SetDefault() 
		gbSizer1.Add( self.m_button1, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.SHAPED, 5 )
		
		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Load...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button5.Enable( False )
		
		gbSizer1.Add( self.m_button5, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button6 = wx.Button( self, wx.ID_ANY, u"Save...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button6.Enable( False )
		
		gbSizer1.Add( self.m_button6, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Pop -^-", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.m_button2, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.SHAPED, 5 )
		
		self.m_button51 = wx.Button( self, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		self.m_button51.Enable( False )
		self.m_button51.SetToolTipString( u"Dock" )
		
		gbSizer1.Add( self.m_button51, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER, 0 )
		
		self.m_scrollwindow = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL, u"linkwindow" )
		self.m_scrollwindow.SetScrollRate( 5, 5 )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		
		self.m_scrollwindow.SetSizer( bSizer3 )
		self.m_scrollwindow.Layout()
		bSizer3.Fit( self.m_scrollwindow )
		gbSizer1.Add( self.m_scrollwindow, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 4 ), wx.ALL|wx.EXPAND, 0 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, u"message_label" )
		self.m_staticText2.Wrap( -1 )
		gbSizer1.Add( self.m_staticText2, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 4 ), wx.ALL|wx.EXPAND, 5 )
		
		
		gbSizer1.AddGrowableCol( 3 )
		gbSizer1.AddGrowableRow( 3 )
		
		self.SetSizer( gbSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.push )
		self.m_button5.Bind( wx.EVT_BUTTON, self.load )
		self.m_button6.Bind( wx.EVT_BUTTON, self.save )
		self.m_button2.Bind( wx.EVT_BUTTON, self.pop )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def push( self, event ):
		event.Skip()
	
	def load( self, event ):
		event.Skip()
	
	def save( self, event ):
		event.Skip()
	
	def pop( self, event ):
		event.Skip()
	


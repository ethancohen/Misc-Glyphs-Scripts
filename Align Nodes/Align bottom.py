#MenuTitle: Align bottom
# -*- coding: utf-8 -*-
__doc__="""
Align selected nodes to the bottom
"""

import GlyphsApp

f = Glyphs.font
m = Font.selectedFontMaster
l = Font.selectedLayers[0]
selection = l.selection

if selection:
	ymin = min((node.y for node in selection))
	
	for node in selection:
		node.y = ymin
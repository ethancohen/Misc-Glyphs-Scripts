#MenuTitle: Align right
# -*- coding: utf-8 -*-
__doc__="""
Align selected nodes to the right
"""

import GlyphsApp

f = Glyphs.font
m = Font.selectedFontMaster
l = Font.selectedLayers[0]
selection = l.selection

if selection:
	xmax = max((node.x for node in selection))
	
	for node in selection:
		node.x = xmax
#MenuTitle: Align top
# -*- coding: utf-8 -*-
__doc__="""
Align selected nodes to the top
"""

import GlyphsApp

f = Glyphs.font
m = Font.selectedFontMaster
l = Font.selectedLayers[0]
selection = l.selection

if selection:
	ymax = max((node.y for node in selection))
	
	for node in selection:
		node.y = ymax
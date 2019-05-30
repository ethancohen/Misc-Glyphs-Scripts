#MenuTitle: Align left
# -*- coding: utf-8 -*-
__doc__="""
Align selected nodes to the left
"""

import GlyphsApp

f = Glyphs.font
m = Font.selectedFontMaster
l = Font.selectedLayers[0]
selection = l.selection

if selection:
	xmin = min((node.x for node in selection))
	
	for node in selection:
		node.x = xmin
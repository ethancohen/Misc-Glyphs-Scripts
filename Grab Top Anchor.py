#MenuTitle: Grab Top Anchor
# -*- coding: utf-8 -*-
__doc__ = """
Select the anchor called 'top' if it exists.
"""

import GlyphsApp

l = Font.selectedLayers[0]

l.clearSelection()

if l.anchors['top']:
	l.addSelection_(l.anchors['top'])
#MenuTitle: Grab Anchors
# -*- coding: utf-8 -*-
__doc__ = """
Select all anchors in the current glyph/layer.
"""

import GlyphsApp

l = Font.selectedLayers[0]

l.clearSelection()

for anchor in l.anchors:
	l.addSelection_(anchor)
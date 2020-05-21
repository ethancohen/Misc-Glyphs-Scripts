#MenuTitle: Copy components to other masters
# -*- coding: utf-8 -*-
__doc__="""
Propagate selected components to all other masters.
"""

# Ethan Cohen. Updated 5/21/2020.

import GlyphsApp
import copy
from random import shuffle

f = Glyphs.font
l = Font.selectedLayers[0]
g = l.parent

for layer in g.layers:
	for c in l.components:
		if c.selected and c.name not in [x.name for x in layer.components]:
			layer.components.append(c.copy())

Glyphs.redraw()
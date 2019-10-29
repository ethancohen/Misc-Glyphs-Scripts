#MenuTitle: Duplicate UC as components in LC
# -*- coding: utf-8 -*-
__doc__="""
Make lower case versions of selected glyphs and insert the selected glyphs as components. Useful for creating a LC that is identical to the UC in all caps fonts.
"""

import GlyphsApp

f = Glyphs.font

LC = list(g.name.lower() for g in f.selection)

for glyph in LC:
	f.glyphs.append(GSGlyph(glyph))
	for layer in f.glyphs[glyph].layers:
		layer.components.append(GSComponent(glyph.upper()))
#MenuTitle: Copy active glyphs to clipboard
# -*- coding: utf-8 -*-
__doc__="""
Copy glyphs which have unicode values and contain outlines and/or components to clipboard for use in Generate Spacing Strings script.
"""

import GlyphsApp
from AppKit import NSPasteboard, NSArray

def clipboard(text):
    p = NSPasteboard.generalPasteboard()
    p.clearContents()
    a = NSArray.arrayWithObject_(text)
    p.writeObjects_(a)

f = Glyphs.font

selection = ""
for g in f.glyphs:
	inclusion = False
	for layer in range(len(g.layers)):
		if g.layers[layer].components or g.layers[layer].paths:
			inclusion = True
	if g.unicode and inclusion == True:
		selection += g.string

clipboard(selection)
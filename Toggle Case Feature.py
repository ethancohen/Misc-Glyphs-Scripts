#MenuTitle: Toggle Case Feature
# -*- coding: utf-8 -*-
__doc__="""
Toggle .case feature in edit view.
"""

import GlyphsApp

f = Glyphs.font
feats = f.currentTab.features

if 'case' in feats:
	feats.remove('case')
else:
	feats.append('case')